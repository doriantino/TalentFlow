# Conventions de Branches Git - TalentFlow

---

## Branche principale

- **`main`** : branche principale, toujours stable. Représente l'état de production. **Aucun commit direct sur `main` après le Sprint 0** - passage obligatoire par une branche dédiée.

## Branches de travail

Le nommage des branches suit le format : `<type>/TF-XX-description-courte`

| Type | Pour |
|------|------|
| `feat/` | Une nouvelle fonctionnalité |
| `fix/` | Une correction de bug |
| `docs/` | Une mise à jour de documentation seule |
| `refactor/` | Une réorganisation de code |
| `chore/` | De la maintenance |

## Exemples
feat/TF-29-authentification-recruteur
fix/TF-38-correction-scoring-soft-skills
docs/TF-44-charte-gouvernance-v2
chore/TF-22-initialisation-projet

## Cycle de vie d'une branche

1. **Créer** la branche à partir de `main` au démarrage du travail sur un ticket.
2. **Commiter** régulièrement sur cette branche (commits propres, conventionnels).
3. **Pousser** la branche vers GitHub.
4. **Ouvrir une Pull Request** vers `main` quand le travail est prêt (voir `pull_requests.md` à venir).
5. **Merger** dans `main` une fois la Definition of Done satisfaite.
6. **Supprimer** la branche après merge.

## Cas particulier : pendant le Sprint 0

Pendant le Sprint 0 (cadrage), les commits directs sur `main` sont tolérés pour les fichiers de documentation et de configuration initiale. À partir du Sprint 1, la règle « pas de commit direct sur main » s'applique strictement.
