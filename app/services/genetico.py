import random
from statistics import mean
from typing import List, Dict
from sqlalchemy.orm import Session
from deap import base, creator, tools
from app.models.animal import Animal
from typing import Optional
# ───────────────────────────────────────────────
def _load_pop(db: Session, rebanho_id: Optional[int]):
    query = db.query(Animal)
    if rebanho_id:
        query = query.filter(Animal.rebanho_id == rebanho_id)
    matrizes = query.filter(Animal.genero == "F").all()
    reprodutores = query.filter(Animal.genero == "M").all()
    return matrizes, reprodutores

# ───────────────────────────────────────────────
def _fitness(individuo, matrizes, reprodutores, peso_endogamia):
    ganhos, endogs = [], []
    for matriz_idx, rep_idx in enumerate(individuo):
        f = matrizes[matriz_idx]
        m = reprodutores[rep_idx]
        ganho = (f.indice_genetico + m.indice_genetico) / 2
        endog = random.uniform(0, 10)          # placeholder
        ganhos.append(ganho)
        endogs.append(endog)
    media_ganho = mean(ganhos)
    media_endog = mean(endogs)
    escore = media_ganho - peso_endogamia * media_endog
    return (escore,)

# ───────────────────────────────────────────────
def executar_ga(
        db: Session,
        rebanho_id: Optional[int] = None,
        peso_endogamia: float = 2.0,
        geracoes: int = 50,
        pop_size: int = 30,
        top: int = 10) -> List[Dict]:

    matrizes, reprodutores = _load_pop(db, rebanho_id)
    if not matrizes or not reprodutores:
        return []

    # Criar espaço GA
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    # Gene = índice do reprodutor
    toolbox.register("gene", random.randrange, len(reprodutores))
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.gene, n=len(matrizes))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Avaliação
    toolbox.register("evaluate",
                     _fitness, matrizes=matrizes,
                     reprodutores=reprodutores,
                     peso_endogamia=peso_endogamia)

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt,
                     low=0, up=len(reprodutores)-1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=pop_size)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(geracoes):
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < 0.8:
                toolbox.mate(child1, child2)
                del child1.fitness.values, child2.fitness.values

        for mutant in offspring:
            if random.random() < 0.2:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid = [ind for ind in offspring if not ind.fitness.valid]
        for ind in invalid:
            ind.fitness.values = toolbox.evaluate(ind)

        pop[:] = tools.selBest(pop + offspring, pop_size)

    # ─────────── montar ranking
    melhores = tools.selBest(pop, k=min(top, len(pop)))
    sugestoes = []
    for ind in melhores:
        pares = []
        ganhos, endogs = [], []
        for matriz_idx, rep_idx in enumerate(ind):
            f = matrizes[matriz_idx]
            m = reprodutores[rep_idx]
            ganho = (f.indice_genetico + m.indice_genetico) / 2
            endog = random.uniform(0, 10)
            ganhos.append(ganho)
            endogs.append(endog)
            pares.append({
                "matriz_id": f.id,
                "reprodutor_id": m.id,
                "indice_progênie": round(ganho, 2),
                "endogamia_prevista": round(endog, 2)
            })

        sugestoes.append({
            "fitness": round(ind.fitness.values[0], 2),
            "media_ganho": round(mean(ganhos), 2),
            "media_endogamia": round(mean(endogs), 2),
            "pares": pares
        })
    return sugestoes