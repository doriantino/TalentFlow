# GOV-07 - Registre des Décisions de Gouvernance

**Version :** V0.1 (squelette)
**Statut :** Document vivant, à enrichir à chaque décision
**Responsable :** Awa

---

## Vocation

Journal chronologique des **décisions importantes prises sur la gouvernance elle-même** : modification d'une règle, ajout d'un rôle, changement d'une politique, exception accordée, veto exercé.

Chaque décision est datée, justifiée, et signée. C'est la **traçabilité de la gouvernance** appliquée à elle-même.

## Format d'une entrée

| Date | Décision | Justification | Décideur | Référence |
|------|----------|---------------|----------|-----------|
| AAAA-MM-JJ | *Décision prise* | *Pourquoi* | *Qui* | *Ticket/Doc* |

## Premières entrées (à créer au Sprint 1)

| Date | Décision | Justification | Décideur | Référence |
|------|----------|---------------|----------|-----------|
| 2026-06-01 | Intégration de Moïse Dikoume comme Apprenti Développeur | Formation par le projet, accompagnement Sprint 1, transmission de compétences (Git, GitHub, Jira, Python) | Dorian Dikoume | SPRINT1-ONBOARDING |
| 2026-06-01 | Permissions GitHub : rôle "Write" sur le dépôt TalentFlow | Principe du moindre privilège — peut pousser des branches et ouvrir des PR, ne peut pas merger sur main protégé | Dorian Dikoume | GOV-02.2 (SOD) |
| 2026-06-01 | Permissions Jira : rôle "Membre" sur l'espace TalentFlow | Peut consulter et modifier ses tickets, ne peut pas reconfigurer le projet | Dorian Dikoume | GOV-02.1 (Accès) |
| 2026-06-01 | Mise en place de la protection de la branche main (PR obligatoire, 1 approbation, pas de force push) | Garantir l'intégrité du code et tracer toute modification | Dorian Dikoume | GOV-02.4 (Journalisation) |
| 2026-06-02 | Assouplissement temporaire de la règle d'approbation sur les PR : passage de 1 à 0 approbation requise | Phase de bootstrap où le projet n'a qu'un seul codeur opérationnel ; aucune review pair n'est possible. La règle sera réinstaurée (1 approbation) dès que Moïse aura terminé son onboarding et sera capable de reviewer les PR de gouvernance. | Dorian Dikoume | GOV-02.4, Branch ruleset GitHub |

---

*Squelette V0.1 — chaque décision majeure prise par Awa y sera consignée.*
