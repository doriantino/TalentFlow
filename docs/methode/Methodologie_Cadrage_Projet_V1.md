# Guide de Méthode — Cadrer un projet IA/produit de bout en bout

**Version :** V1
**Statut :** Document méthodologique réutilisable
**Vocation :** Servir de référence pour cadrer professionnellement tout nouveau projet IA ou produit numérique, du nom jusqu'au premier sprint de construction.

---

## Avant-propos — Pourquoi ce guide existe

Ce guide n'est pas un manuel théorique. Il est l'extraction, sous forme générique, de la méthode pratiquée pas à pas lors du cadrage du projet TalentFlow. Chaque section décrit *une étape réutilisable* et la *règle de pro* qui la sous-tend, accompagnée d'une question d'or à se poser pour ne pas se tromper.

La règle d'or qui chapeaute tout :

> **Une heure de cadrage économise dix heures de galère plus tard.**
> Construire sans avoir réfléchi en amont, c'est poser des briques sans plan. On finit toujours par tout casser et recommencer.

---

## Sommaire

1. Préparer le terrain mental
2. Étape 1 — Nommer le projet
3. Étape 2 — Écrire la vision produit
4. Étape 3 — Écrire le business problem
5. Étape 4 — Définir les objectifs
6. Étape 5 — Identifier les personas
7. Étape 6 — Écrire les parcours utilisateurs
8. Étape 7 — Lister les fonctionnalités par domaines
9. Étape 8 — Définir le MVP
10. Étape 9 — Instaurer une gouvernance vivante
11. Étape 10 — Mettre en place la structure Agile
12. Étape 11 — Rédiger les user stories au format pro
13. Étape 12 — Choisir et configurer les outils
14. Étape 13 — Préparer la sortie de phase (V1 des documents)
15. Annexe — Glossaire des termes professionnels

---

## 1. Préparer le terrain mental

Avant de poser quoi que ce soit, deux dispositions mentales sont essentielles.

**Distinguer le « pourquoi », le « quoi » et le « comment ».** Le cadrage répond au pourquoi (raison d'être) et au quoi (périmètre). Le comment (technologies, code) vient *après*. La plupart des erreurs viennent de gens qui sautent directement au comment.

**Accepter l'itération.** Un cadrage propre n'est jamais parfait du premier coup. On affine par allers-retours : on précise, on corrige, on reformule. C'est la méthode, pas un signe d'échec.

**Question d'or :** *« Sais-je expliquer en deux phrases pourquoi ce projet existe ? »* Si non, on cadre. Si oui, on peut envisager d'avancer.

---

## 2. Étape 1 — Nommer le projet

Le nom n'est pas cosmétique. Un bon nom rend le projet *racontable* avec fierté en entretien et sur LinkedIn, et donne tout de suite une impression de « produit réel » plutôt que d'exercice scolaire.

**Trois styles à explorer :**

- **Moderne / startup tech** : court, mémorable, évocateur. Bon pour un produit grand public ou un portfolio.
- **Corporate / B2B sérieux** : rassurant pour les grandes entreprises, explicite.
- **Clin d'œil au domaine** : nom métaphorique qui raconte une histoire.

**Bonnes pratiques.** Vérifier sommairement que le nom ne crée pas de confusion juridique évidente (pour un projet personnel, pas besoin d'aller plus loin). Choisir un nom qu'on aime *prononcer*.

**Question d'or :** *« Suis-je content de dire ce nom à voix haute ? »*

---

## 3. Étape 2 — Écrire la vision produit

La vision est l'**étoile polaire** du projet. Une ou deux phrases qui décrivent le monde idéal que le produit veut créer. Ce n'est pas une liste de fonctionnalités, c'est une direction.

**Modèle de phrase à utiliser :**

> Pour **[qui]**, qui **[a tel problème]**, **[nom du produit]** est **[quel type de produit]** qui **[bénéfice clé]**. Contrairement à **[la situation actuelle]**, notre produit **[ce qui le rend différent]**.

**Règle de pro : la vision doit montrer la différenciation, pas se limiter à ce que tout le monde fait déjà.** Une vision qui ne dit que « ce qu'on connaît » ne donne aucune raison de te choisir toi plutôt qu'un concurrent. Il faut au moins un élément « waouh » qui sort de l'ordinaire.

**Important : vision ≠ MVP.** La vision est ambitieuse — c'est la destination. Le MVP (étape 8) est le premier pas vers cette destination. Une bonne vision est volontairement plus large que ce qu'on construira d'abord.

**Question d'or :** *« Si quelqu'un lisait uniquement ma vision, comprendrait-il pourquoi mon produit mérite d'exister et ce qui le rend différent ? »*

---

## 4. Étape 3 — Écrire le business problem

Le business problem est la **douleur réelle** que vivent de vraies personnes et qui justifie l'existence du produit. C'est le « pourquoi on fait ça ». C'est la section la plus importante du document projet, parce qu'un produit qui ne résout pas un vrai problème ne sert à rien.

**Bonne pratique : décrire le problème avec des faits concrets**, pas avec « c'est compliqué ». Plusieurs douleurs distinctes valent mieux qu'une seule formulation vague.

### La technique des trois mots d'or en miroir

C'est l'une des techniques les plus puissantes du cadrage. Elle consiste à résumer :

- **Trois mots qui décrivent le problème** (les douleurs)
- **Trois mots qui décrivent la solution** (les promesses)
- En miroir, mot pour mot.

**Exemple TalentFlow :**

| Problème | → | Solution |
|---|---|---|
| Lenteur | → | Rapide |
| Subjectivité | → | Équitable |
| Opacité | → | Traçable |

Tu obtiens deux trios qui se répondent et que tu peux mobiliser à l'oral : *« mon produit résout la lenteur, la subjectivité et l'opacité — il est rapide, équitable et traçable. »*

**Question d'or :** *« Quels trois mots résument le problème ? Quels trois mots leur répondent ? »*

---

## 5. Étape 4 — Définir les objectifs

Un objectif est **orienté résultat** (pas « faire un dashboard » mais « permettre au recruteur de décider vite ») et idéalement **mesurable** (on peut dire si on l'a atteint).

**Mémo SMART** (vague mais utile) : Spécifique, Mesurable, Atteignable, Réaliste, Temporellement défini.

**Bonne pratique : séparer les objectifs en deux familles.**

- **Objectifs métier** : la valeur pour l'entreprise et les utilisateurs.
- **Objectifs techniques / d'apprentissage** : ce qu'on veut réussir techniquement, et ce qu'on veut apprendre dans le cas d'un projet de portfolio.

### Le trio à ne plus jamais confondre

| | Objectif | Fonctionnalité | User Story |
|---|---|---|---|
| **C'est quoi ?** | Pourquoi on construit et ce qu'on veut atteindre | Une capacité concrète du produit | Le même besoin vu par un utilisateur précis |
| **Image** | La direction du voyage | Un équipement de la voiture (frein, GPS…) | « Sarah veut des phares pour voir la nuit » |
| **Niveau** | Le plus haut, le plus abstrait | Niveau intermédiaire | Niveau concret, prêt à construire |

Cascade : **un objectif** se réalise grâce à **plusieurs fonctionnalités**, et chaque fonctionnalité se découpe en **plusieurs user stories**.

**Question d'or :** *« Si ma fonctionnalité réussit techniquement mais que mon objectif n'est pas atteint, ai-je vraiment réussi ? »* Si la réponse est non, l'objectif est mal défini ou la fonctionnalité ne sert pas l'objectif.

---

## 6. Étape 5 — Identifier les personas

Une persona est **un utilisateur-type incarné** : pas « l'utilisateur » (froid, abstrait) mais « Karim, recruteur de 35 ans chez NovaTech ». Lui donner un nom, un rôle, un contexte transforme la conception.

**Règle de pro découverte au fil du cadrage TalentFlow : identifier les personas en amont, mais accepter qu'elles s'affinent en écrivant les parcours.** Les deux étapes se nourrissent l'une l'autre.

**Règle de pro essentielle : un enjeu transverse (gouvernance, sécurité, accessibilité…) ne reste vivant que si on l'incarne dans une persona dédiée ET qu'on l'inscrit dans la Definition of Done.** Sans persona, l'enjeu se dilue. Sans Definition of Done, la persona n'a aucun pouvoir réel.

**Question d'or :** *« Ai-je au moins une persona par enjeu critique du produit, y compris les enjeux transverses ? »*

---

## 7. Étape 6 — Écrire les parcours utilisateurs

Un **parcours utilisateur** (*user journey*) est l'histoire complète, du début à la fin, de ce que vit une persona quand elle utilise le produit. C'est un **récit chronologique** — un film, pas une photo.

**Trois règles pour bien écrire un parcours :**

- **Donner un nom et un rôle** à la personne (la persona).
- **Raconter au présent, dans l'ordre chronologique**, étape par étape.
- **S'en tenir au ressenti et à l'action visible** — pas de technique interne.

**Distinction cruciale à ancrer définitivement :**

| | Parcours utilisateur | User story |
|---|---|---|
| **Image** | Un film | Une photo extraite du film |
| **Forme** | Récit chronologique | Phrase « En tant que… je veux… afin de… » |
| **Sert à** | Vue d'ensemble dans l'ordre | Brique concrète à construire |
| **Ordre** | D'abord | Ensuite (en découpant le parcours) |

**Bonne pratique :** écrire **un parcours par persona** (au moins). Pour un produit comme TalentFlow, on a écrit quatre parcours (Karim publie, Sarah postule, Karim exploite, Awa veille).

**Question d'or :** *« Si je raconte ce parcours à voix haute à quelqu'un, comprend-il en 30 secondes ce que fait mon produit ? »*

---

## 8. Étape 7 — Lister les fonctionnalités par domaines

Plutôt que d'éparpiller les fonctionnalités, les **regrouper par grands domaines cohérents**. Chaque domaine deviendra plus tard un **Epic** dans la structure Agile.

**Bonne pratique : organiser les domaines en suivant le parcours naturel du produit** (côté client, côté interne, etc.), puis les domaines transverses (gouvernance, socle technique) à la fin.

**Pour chaque domaine, indiquer à quel objectif il répond.** C'est le fil rouge : aucun domaine ne doit exister sans servir un objectif.

**Question d'or :** *« Pour chaque domaine listé, à quel objectif sert-il ? Si je ne sais pas répondre, il est peut-être de trop. »*

---

## 9. Étape 8 — Définir le MVP

Le **MVP** (Minimum Viable Product) est *le plus petit produit qui marche et rend déjà un vrai service*.

### Image cruciale à retenir

> Un MVP n'est pas une partie de voiture (un châssis tout seul, inutilisable). Un MVP est une **trottinette** : c'est petit, c'est simple, mais ça *roule déjà*. Ensuite tu feras un vélo, puis une moto, puis la voiture complète.

**Erreur classique à éviter :** croire qu'un MVP est « le produit en plus petit ». Il n'est pas une réduction proportionnelle ; il est **le chemin le plus court qui prouve la valeur**.

### La question d'or du MVP

> *« Quel est le plus petit chemin complet qui prouve déjà la valeur du produit ? »*

« Complet » est le mot clé. Le MVP doit raconter l'histoire **du début à la fin**, même de façon simple.

### Outil de priorisation : MoSCoW

Pour trier ce qui entre dans le MVP de ce qui est reporté, utiliser **MoSCoW** :

- **M — Must have** : indispensable, sans ça le produit ne fonctionne pas.
- **S — Should have** : important, mais le produit peut tenir sans pendant un temps.
- **C — Could have** : sympathique, optionnel.
- **W — Won't have (this time)** : volontairement reporté à plus tard.

Force à dire « non » proprement et à rendre les choix transparents.

**Règle de pro :** dire *« ça, plus tard »* à de bonnes idées — sans les jeter — est l'art du Product Owner. Tout ce qui ne sert pas à prouver la valeur est reporté, **même si c'est beau, même si c'est dans la vision**.

---

## 10. Étape 9 — Instaurer une gouvernance vivante

Cette étape est *optionnelle* pour des projets sans enjeu de données — mais pour tout projet IA, data ou traitant de données personnelles, elle est **non négociable**.

### Comprendre la gouvernance des données

La gouvernance des données, c'est **l'ensemble des règles, rôles, documents et procédures qui garantissent que les données sont fiables, protégées, bien définies et utilisées correctement**.

**Hiérarchie logique :**

> **Charte** (la constitution) → **Politiques** (les grandes lois) → **Procédures** (les modes d'emploi) → **Règles de gestion** (le comportement métier précis) → **Glossaire & MDM** (le langage et les données de référence communs).

Du plus général au plus concret.

### Termes clés

- **Charte de gouvernance** : document de haut niveau, pourquoi on gouverne, qui est responsable, grands principes.
- **Politique de données** : règles à respecter sur un sujet précis (accès, conservation, etc.).
- **Procédures** : le mode d'emploi des politiques, étape par étape.
- **Règles de gestion** *(business rules)* : décisions logiques explicites du système.
- **Glossaire / dictionnaire de données** : liste officielle des termes avec une définition unique partagée.
- **MDM** *(Master Data Management)* : discipline qui garantit qu'il existe **une seule version vraie et unique** des données de référence (compétences, rôles, statuts…).

### Règles de pro pour une gouvernance vivante

1. **Fixer une bibliothèque officielle de documents de gouvernance dès le début**, avec un code et un rôle clair pour chacun. Sans cette liste figée, les notes de gouvernance restent floues.

2. **Versionner les livrables non techniques comme on versionne le code.** Charte V1, V2, V3… Glossaire V1, V2, V3… La gouvernance elle-même devient auditée et historisée.

3. **Revue systématique à chaque sprint, mise à jour seulement quand c'est justifié.** Protège contre la « gouvernance théâtrale » (ajouter des paragraphes vides pour faire bien).

4. **Présentation obligatoire à chaque démo de sprint.** Un acteur dédié (la persona gouvernance) présente ce qui a évolué dans les documents — ou ce qui est consciemment resté inchangé.

5. **Droit de veto réel pour la persona gouvernance.** Une fonctionnalité dont les exigences de gouvernance ne sont pas remplies est suspendue, quel que soit son avancement technique. Sans pouvoir réel, la gouvernance reste décorative.

### Cadre éthique pour les projets IA

Pour tout projet IA touchant des décisions sur des personnes : poser explicitement le principe que **l'IA aide mais ne décide jamais seule**. L'humain garde la décision finale. C'est à la fois un garde-fou éthique, une exigence légale croissante, et un signal fort de maturité.

---

## 11. Étape 10 — Mettre en place la structure Agile

### Agile, en une phrase

> On ne sait jamais vraiment ce qu'on veut tant qu'on ne l'a pas vu fonctionner. Donc plutôt que tout planifier d'avance, on construit par petits morceaux livrables, on les montre, on apprend, on ajuste.

**Agile = philosophie. Scrum = recette pratique pour l'appliquer.**

### Scrum, l'essentiel

- **Rôles :** Product Owner (décide quoi et dans quel ordre), Scrum Master (gardien de la méthode), Équipe de développement.
- **Artefacts :** Product Backlog (tout ce qu'il faut faire un jour, classé par priorité), Sprint Backlog (sous-ensemble pris pour le sprint), Incrément (ce qui est livré à la fin du sprint).
- **Sprint :** période courte (souvent 2 semaines) pendant laquelle l'équipe livre un incrément.
- **Cérémonies :** Sprint Planning (au début), Daily Stand-up (chaque jour, 10-15 min), Sprint Review/Démo (à la fin), Rétrospective (juste après la démo).

### Hiérarchie du travail

> **Epic** (chapitre du livre) → **User Story** (page du livre) → **Tâche technique** (ligne dans la page)

**Chaque grand domaine de fonctionnalités identifié à l'étape 7 devient un Epic.** Coder les Epics (E1, E2…) facilite la traçabilité.

### Sprint 0 : la phase de préparation

Avant le premier vrai sprint de construction, un **Sprint 0** est utile pour : configurer les outils, créer les dépôts, finaliser le backlog, dessiner l'architecture, écrire la roadmap, définir les conventions. **On ne livre pas encore de fonctionnalité, mais on rend possible tous les sprints qui viennent.**

### Roadmap

Vue d'avion qui montre **quelle famille de fonctionnalités arrive à quel sprint**. C'est la carte temporelle du projet. Indicative et révisable.

### Kanban

Approche complémentaire à Scrum, basée sur un **tableau visuel** (colonnes *À faire / En cours / Terminé*). Beaucoup d'équipes combinent : Scrum pour le rythme (sprints + cérémonies), tableau Kanban pour le suivi quotidien.

---

## 12. Étape 11 — Rédiger les user stories au format pro

### Format d'une user story professionnelle (8 sections)

1. **En-tête** : code (ex. US-E6-03), type (User Story ou Tâche technique), titre court, Epic de rattachement, priorité MoSCoW, estimation indicative.

2. **Description narrative** : *« En tant que [qui], je veux [quoi], afin de [pourquoi] »* — ou description claire si c'est une tâche technique.

3. **Contexte** : pourquoi cette story existe, à quoi elle sert dans le tableau d'ensemble.

4. **Détail fonctionnel** : ce qu'il faut concrètement construire, étape par étape, **avec assez de précision pour qu'un profane comprenne l'action à mener**.

5. **Critères d'acceptation** : 3 à 6 conditions vérifiables qui prouvent que la story est réussie.

6. **Note de gouvernance** : pour chaque document de gouvernance enrichi, préciser quel document, quelle version, et ce qui est ajouté.

7. **Dépendances** : ce qui doit être fait avant.

8. **Estimation indicative** : Petit / Moyen / Grand (à raffiner en *story points* plus tard).

### Règles de pro

- Sans **critères d'acceptation**, on ne sait jamais quand s'arrêter. Toujours les écrire.
- Un Epic « Socle Technique » contient surtout des **tâches techniques**, pas des user stories au format « En tant que ». Ne pas forcer le format : suivre la nature du travail.
- Une user story doit pouvoir être **lue par un profane** et lui dire exactement quoi faire.

---

## 13. Étape 12 — Choisir et configurer les outils

### Recommandation par défaut (équilibre apprentissage / réalisme professionnel)

- **Gestion de projet :** Jira Cloud (plan Free, gratuit jusqu'à 10 utilisateurs). C'est l'outil de référence du marché.
- **Code et documentation :** GitHub (gratuit pour dépôts publics et privés).
- **Intégration :** GitHub for Jira (gratuite). Lie les commits aux tickets.

### Alternative open source

- **Gestion de projet :** Taiga (taiga.io, version hébergée gratuite).
- **Code :** GitHub.

### Critère de choix

**Si l'objectif est l'employabilité dans des entreprises traditionnelles** → privilégier Jira (l'outil que les recruteurs reconnaissent).

**Si la conviction open source est prioritaire** → Taiga, parfaitement valable méthodologiquement.

**Règle de pro :** un outil unifié (genre GitHub Projects seul) simplifie la vie mais ne reproduit pas l'expérience réelle des grandes entreprises où la gestion projet et le code vivent dans des outils séparés. Choisir en conscience.

---

## 14. Étape 13 — Préparer la sortie de phase (V1 des documents)

À la fin du cadrage, **produire deux documents distincts** :

- **Le document projet** (la « recette ») : spécifique au projet, contient vision, problème, objectifs, fonctionnalités, etc. C'est le PRD (*Product Requirements Document*).

- **Le guide de méthode** (la « méthode de travail ») : générique et réutilisable, décrit la démarche elle-même. Permet de gagner un temps fou sur le prochain projet.

**Règle de pro distinctive :** un consultant ne vend pas qu'un résultat ; il vend une méthode reproductible. Distinguer livrable-projet et livrable-méthode est la marque d'un profil sénior.

**Format :** Markdown pour les deux. Lisible sur GitHub, versionnable comme le code, exportable en Word ou PDF si besoin.

**Statut :** ces documents sont des **V1**, pas des versions définitives. Ils seront mis à jour au fil des sprints. *Rien n'est figé éternellement en Agile.*

---

## 15. Annexe — Glossaire des termes professionnels

**Agile.** Philosophie de développement par petits morceaux livrables, avec adaptation continue.

**Audit log.** Journal qui enregistre chaque action sensible du système, avec horodatage et auteur. Pierre angulaire de la traçabilité.

**Backlog (Product Backlog).** Liste de tout ce qu'il faut un jour construire, classée par priorité. Vivante : on y ajoute, on en retire, on réordonne.

**Business problem.** Douleur réelle des utilisateurs que le produit vient résoudre. Justifie l'existence du produit.

**Cérémonies Scrum.** Sprint Planning, Daily Stand-up, Sprint Review (démo), Rétrospective.

**Critères d'acceptation.** Conditions vérifiables qui prouvent qu'une user story est terminée et réussie.

**Definition of Done.** Liste des conditions pour qu'une tâche soit considérée comme *vraiment* finie. Inclut souvent : tests passés, code revu, documentation à jour, exigences transverses (gouvernance, sécurité) satisfaites.

**Epic.** Gros bloc de travail cohérent, regroupant plusieurs user stories autour d'un même thème. Chapitre du livre projet.

**Just-in-time learning.** Apprentissage juste-à-temps : apprendre un concept au moment précis où on s'en sert, pas en théorie à froid.

**Kanban.** Approche basée sur un tableau visuel à colonnes (À faire / En cours / Terminé). Souvent combinée à Scrum pour le suivi quotidien.

**MDM (Master Data Management).** Discipline qui garantit qu'il existe une seule version vraie et unique des données de référence (la « source unique de vérité »).

**MoSCoW.** Outil de priorisation : Must / Should / Could / Won't.

**MVP (Minimum Viable Product).** Le plus petit chemin complet qui prouve déjà la valeur du produit. Pas une réduction proportionnelle, mais le cœur essentiel.

**Persona.** Utilisateur-type incarné avec un nom, un rôle, un contexte. Permet de concevoir pour quelqu'un de précis plutôt que pour un « utilisateur » abstrait.

**PRD (Product Requirements Document).** Document de référence d'un projet produit. Contient vision, problème, objectifs, périmètre.

**Product Owner (PO).** Personne qui décide *quoi* construire et *dans quel ordre*. Parle aux utilisateurs, maintient le backlog.

**Règles de gestion** *(business rules)*. Décisions logiques explicites du système (formule de scoring, seuils, conditions). Doivent être documentées et versionnées.

**Roadmap.** Carte temporelle qui montre quelle famille de fonctionnalités arrive à quel moment.

**Scrum.** Recette pratique pour appliquer Agile. Sprints courts, rôles définis, cérémonies régulières.

**Scrum Master.** Personne qui garantit que la méthode est bien appliquée et débloque les obstacles.

**SOD (Segregation of Duties).** Séparation des Tâches. Principe : aucune personne ne doit pouvoir, à elle seule, accomplir un acte sensible de bout en bout. Qui configure n'exécute pas, qui exécute n'audite pas.

**Sprint.** Période courte (souvent 2 semaines) pendant laquelle l'équipe construit un incrément démontrable.

**Sprint 0.** Phase de préparation avant le premier sprint de construction : outils, backlog, architecture, conventions.

**Story points.** Unité d'estimation relative de l'effort d'une user story. (À introduire plus tard dans le projet.)

**User journey (parcours utilisateur).** Récit chronologique complet de l'expérience d'une persona avec le produit. Un film.

**User story.** Besoin précis exprimé du point de vue de l'utilisateur. Format : *« En tant que [qui], je veux [quoi], afin de [pourquoi] »*. Une photo extraite du film du parcours.

**Vision produit.** Phrase qui décrit le monde idéal que le produit veut créer. Étoile polaire du projet.

**Waterfall.** Méthode classique en cascade (tout planifier puis tout construire puis livrer). Opposée d'Agile.

---

*Ce guide est une V1. Il s'enrichira avec l'expérience des projets futurs. Chaque projet est une occasion d'affiner la méthode.*
