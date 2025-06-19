from fastapi import FastAPI
from app.routes import animal_routes, rebanho_routes, fazenda_routes, raca_routes, usuario_routes, funcionario_routes, doenca_routes, medicamento_routes, manejo_routes, movimentacao_routes, ocorrencia_routes, parasita_routes, vacinacao_routes, acasalamento_routes, simulacao_ga_routes, auth_routes
from app.db.session import Base, engine

# Importar os modelos para que o SQLAlchemy crie as tabelas
import app.models 
from fastapi.middleware.cors import CORSMiddleware
origins = ["http://localhost:3000"]  # URL do seu front


Base.metadata.drop_all(bind=engine)   # ⚠️ apaga tudo

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Instanciar a aplicação FastAPI
app = FastAPI(
    title="CAPRIOVI API",
    description="API para controle zootécnico, genético e acasalamentos em caprinos e ovinos.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(animal_routes.router)
app.include_router(rebanho_routes.router)
app.include_router(fazenda_routes.router)
app.include_router(raca_routes.router)
app.include_router(usuario_routes.router)
app.include_router(funcionario_routes.router)
app.include_router(doenca_routes.router)
app.include_router(medicamento_routes.router)
app.include_router(manejo_routes.router)
app.include_router(movimentacao_routes.router)
app.include_router(ocorrencia_routes.router)
app.include_router(parasita_routes.router)
app.include_router(vacinacao_routes.router)
app.include_router(acasalamento_routes.router)
app.include_router(simulacao_ga_routes.router)
app.include_router(auth_routes.router)