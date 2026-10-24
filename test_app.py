from fastapi import FastAPI
from fastapi.testclient import TestClient
from app import app

testClient = TestClient(app)

def test_criar_estacao():
    data = {"id": 1, "nome": "Estação Cacatua"}

    response = testClient.post(
        "/estacoes",
        json=data
    )

    assert response.status_code == 201
    assert response.json() == data