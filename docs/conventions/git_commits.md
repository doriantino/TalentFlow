# Conventions de Commits Git - TalentFlow

**Norme suivie :** [Conventional Commits](https://www.conventionalcommits.org/)

---

## Format d'un message de commit
<type>(<scope>): <description courte>
[corps optionnel, plus détaillé]
[pied optionnel : référence ticket, etc.]

## Types autorisés

| Type | Quand l'utiliser |
|------|------------------|
| `feat` | Nouvelle fonctionnalité utilisateur |
| `fix` | Correction de bug |
| `docs` | Documentation uniquement |
| `refactor` | Refonte de code sans changement fonctionnel |
| `test` | Ajout ou modification de tests |
| `chore` | Maintenance, configuration, dépendances |
| `style` | Mise en forme (espaces, indentation) — pas de logique modifiée |

## Scopes courants pour TalentFlow

- `projet`, `methode`, `governance`, `backlog`, `conventions`, `architecture` (pour la doc)
- `auth`, `audit`, `scoring`, `dashboard`, `workday`, `linkedin` (pour le code)

## Référencement obligatoire des tickets Jira

**Tout commit qui implémente une partie d'un ticket Jira DOIT mentionner le code du ticket** (`TF-XX`) dans le message. Cela permet l'**intégration automatique Jira ↔ GitHub** : le commit apparaît sur le ticket Jira correspondant.

## Exemples

✅ Bons exemples :
feat(auth): TF-29 implémentation de l'authentification recruteur
fix(scoring): TF-38 correction du calcul du score sur les soft skills
docs(governance): TF-44 V2 de la Charte de Gouvernance après revue d'Awa
chore: mise à jour des dépendances

❌ Mauvais exemples :
update                     (pas de type, pas de description claire)
fix bug                    (pas de scope, pas de description précise, pas de ticket)
WIP                        (work in progress — interdit sur main)

## Lien avec la Definition of Done
Le respect de ces conventions fait partie de la **Definition of Done** (section 1) : un commit qui ne respecte pas ces règles peut être refusé en revue.
