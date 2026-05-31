# Definition of Done - TalentFlow

**Version :** V1
**Statut :** Document de référence du projet
**Inscrite dans la doctrine fondatrice : « L'IA pour l'IA n'est que ruine de l'âme. »**

---

## Principe général

Aucune fonctionnalité, aucun sprint, n'est considéré comme terminé tant que **toutes** les conditions ci-dessous ne sont pas remplies. Cette Definition of Done est non-négociable : c'est elle qui garantit que la qualité, la traçabilité et l'équité ne sont jamais sacrifiées au profit de la vitesse.

---

## 1. Sur la fonctionnalité elle-même

- [ ] Le code est écrit, testé, et fonctionne dans les conditions définies par les critères d'acceptation de la user story.
- [ ] Le code est versionné dans GitHub.
- [ ] Le message de commit référence le ticket Jira correspondant (ex : `TF-22 feat: initialisation du projet`).
- [ ] La documentation technique correspondante est mise à jour dans `docs/architecture/`.
- [ ] Les tests éventuels passent.

## 2. Sur la gouvernance (volet ajouté à la demande du Product Owner)

- [ ] Chaque fonctionnalité livrée a satisfait son **exigence de gouvernance** : règle documentée, action tracée, donnée protégée.
- [ ] Tous les **livrables de gouvernance** (GOV-01 à GOV-07) ont été passés en revue par Awa durant le sprint. Ils sont soit mis à jour (nouvelle version V2, V3...), soit confirmés inchangés avec mention explicite et justification.
- [ ] À la **démo de sprint**, Awa présente l'évolution de la documentation de gouvernance : ce qui a été ajouté, modifié, ou consciemment laissé inchangé. Cette présentation est un point d'agenda obligatoire de la démo.

## 3. Sur le droit de veto

- [ ] Awa dispose d'un **droit de veto gouvernance** : toute fonctionnalité dont les exigences de gouvernance ne sont pas remplies est suspendue, quel que soit son avancement technique. Ce veto incarne le principe fondateur de TalentFlow.

---

## Conséquence opérationnelle

Une story qui passe toutes les conditions ci-dessus peut passer de la colonne **Testing** à **Done** dans Jira.

Une story qui n'en remplit qu'une partie reste en **Testing**, avec le détail de ce qui manque indiqué en commentaire dans le ticket Jira.

---

*Document V1 - sera révisé à chaque rétrospective si une condition s'avère mal calibrée.*
