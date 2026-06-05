"""Point d'entrée de l'API TalentFlow."""

from fastapi import FastAPI

app = FastAPI(
    title="TalentFlow",
    description="Plateforme IA de recrutement et onboarding RH",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Endpoint de santé : permet de vérifier que l'API tourne."""
    return {"status": "ok", "service": "talentflow"}