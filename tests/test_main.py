"""Tests pour le point d'entrée de l'API."""

from fastapi.testclient import TestClient

from talentflow.main import app

client = TestClient(app)


def test_root():
    """Vérifie que la racine de l'API répond correctement (Statut 200 et JSON)."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "talentflow"}