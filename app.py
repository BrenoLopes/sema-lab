from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient

app = FastAPI()

class Estacao(BaseModel):
    id: int = Field(gt=0)
    nome: str = Field(min_length=3)

estacoes: dict[int, Estacao] = {}

@app.get("/health")
def health():
    return { "status": "ok" }

@app.post("/estacoes", status_code=201)
def criar_estacao(estacao: Estacao):
    if estacao.id in estacoes:
        raise HTTPException(409, "Estação já cadastrada!")

    estacoes[estacao.id] = estacao
    return estacao

@app.get("/estacoes")
def listar_estacoes():
    return list(estacoes.values())

@app.get("/estacao/{estacao_id}")
def find_estacao(estacao_id: int):
    if not (estacao_id in estacoes):
        raise HTTPException(404, "Estação não encontrada!")
    return estacoes[estacao_id]
