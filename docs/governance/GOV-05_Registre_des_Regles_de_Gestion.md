# GOV-05 - Registre des Règles de Gestion

**Version :** V0.1 (squelette)
**Statut :** À démarrer au Sprint 1
**Responsable :** Awa

---

## Vocation

Liste explicite et versionnée de toutes les **règles métier** (business rules) du système. Chaque règle est documentée, justifiée, et peut être auditée.

## Format d'une règle

| Code | Énoncé | Justification | Version |
|------|--------|---------------|---------|
| RG-XX | *Règle...* | *Pourquoi...* | V1 |

## Règles pressenties (à formaliser sprint par sprint)

| Code | Énoncé | Sprint |
|------|--------|--------|
| RG-01 | Tout utilisateur possède exactement un rôle parmi {Recruteur, Gouvernance, Administrateur}. Les cumuls sont interdits. | Sprint 1 |
| RG-02 | Un candidat ne peut postuler qu'une seule fois à la même offre. | Sprint 2 |
| RG-03 | Le score d'adéquation se calcule selon la formule : 60% compétences + 25% expérience + 15% soft skills. | Sprint 3 |
| RG-04 | Un candidat avec un score < 40/100 est automatiquement classé en "non retenu". | Sprint 3 |
| RG-05 | Un CV de candidat non retenu est supprimé après X mois (durée à préciser dans GOV-02.3). | Sprint 2 |

---

*Squelette V0.1 — règles à formaliser au fur et à mesure de leur implémentation.*
