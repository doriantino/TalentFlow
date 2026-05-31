# TalentFlow — Document Projet

**Version :** V1 — Sortie de phase de cadrage
**Statut :** Validé pour démarrage du Sprint 0
**Auteur :** Product Owner du projet
**Méthode de travail :** Scrum (sprints de 2 semaines), tableau Kanban pour le suivi quotidien
**Outils :** Jira Cloud (gestion de projet) · GitHub (code et documentation)

---

## Sommaire

1. Convictions fondatrices
2. Vision produit
3. Business problem
4. Objectifs du produit
5. Personas
6. Parcours utilisateurs
7. Fonctionnalités par domaines
8. Périmètre du MVP
9. Architecture simplifiée (vue de haut)
10. Cadre de gouvernance
11. Structure Agile du projet
12. Backlog initial — Epic E6 (Socle Technique)
13. Definition of Done
14. Conclusion et suite du travail

---

## 1. Convictions fondatrices

TalentFlow est construit autour de deux convictions qui orientent chaque décision du projet.

> *« L'IA pour l'IA n'est que ruine de l'âme. »*

Une intelligence artificielle puissante mais non gouvernée n'est pas un progrès, c'est un risque. Toute capacité IA ajoutée à TalentFlow doit être encadrée par des règles explicites, traçables et défendables. Sans gouvernance, l'IA calcule mais ne mérite pas confiance.

> *« Dans un système data-driven, la personne qui garantit la qualité, l'équité et la traçabilité de la donnée est la personne la plus stratégique de l'entreprise. »*

Awa, notre Data & Governance Officer, est l'employée la mieux payée de NovaTech. Cette inversion volontaire de hiérarchie traduit une philosophie produit : la gouvernance n'est pas un coût subi, c'est l'actif le plus précieux d'un système qui prend des décisions sur de vraies personnes.

Ces deux phrases ne sont pas décoratives. Elles sont opérationnalisées dans le projet par un mécanisme concret : la **Definition of Done** (section 13) et le **droit de veto d'Awa** sur toute fonctionnalité livrée.

---

## 2. Vision produit

Pour les équipes de recrutement qui croulent sous les candidatures et manquent de temps pour évaluer chaque talent en profondeur et équitablement, **TalentFlow** est une plateforme de recrutement et d'onboarding augmentée par l'intelligence artificielle.

Là où les outils classiques se contentent de filtrer et de scorer les CV, TalentFlow va plus loin. Pour chaque candidat, il génère une évaluation sur mesure — test technique ciblé et trame d'entretien personnalisée — calibrée sur trois dimensions croisées : le profil réel extrait du CV, les exigences techniques du poste, et les soft skills attendus par l'organisation. Il met en lumière les écarts précis de chaque profil et prépare un plan d'onboarding personnalisé pour le candidat retenu.

Le résultat : un processus **rapide, équitable, traçable et profondément personnalisé**, où l'IA ne remplace pas le jugement humain mais l'arme des bonnes informations, au bon moment — de la première candidature jusqu'aux premières semaines dans l'entreprise.

---

## 3. Business problem

Lorsqu'une entreprise publie une offre attractive, elle reçoit des centaines de candidatures en quelques jours. Les équipes RH font alors face à trois douleurs majeures, qui définissent le problème que TalentFlow vient résoudre.

**Lenteur.** Trier manuellement chaque CV prend un temps considérable. Faute de temps, les recruteurs n'accordent que quelques secondes à chaque candidature au premier tri — et de bons profils passent à la trappe.

**Subjectivité.** Deux recruteurs (ou le même, fatigué un vendredi soir) n'évaluent pas un CV de la même manière. Les critères sont appliqués de façon inégale, ce qui ouvre la porte aux biais et aux décisions injustes.

**Opacité.** Quand on demande *« pourquoi ce candidat a-t-il été écarté ? »*, il est souvent impossible de répondre précisément. Les analyses sont éparpillées dans des e-mails et des têtes ; rien n'est centralisé, tracé, ni réutilisable — alors même que les entreprises doivent de plus en plus pouvoir justifier leurs décisions, pour des raisons légales et éthiques.

La réponse de TalentFlow transforme chacune de ces douleurs en promesse, terme pour terme :

| La douleur (le problème) | → | La promesse (la solution) |
|---|---|---|
| **Lenteur** | → | **Rapide** : analyse et scoring automatiques dès la réception du CV |
| **Subjectivité** | → | **Équitable** : mêmes critères appliqués à tous, de façon cohérente |
| **Opacité** | → | **Traçable** : chaque analyse et chaque action sont historisées et justifiables |

En une phrase : **TalentFlow remplace un tri lent, subjectif et opaque par un processus rapide, équitable et traçable.**

---

## 4. Objectifs du produit

### 4.1 Objectifs métier

Réduire drastiquement le temps de tri des candidatures, en faisant passer le recruteur d'un tri manuel de plusieurs heures à une shortlist prête en quelques minutes.

Garantir une évaluation cohérente et équitable, en appliquant les mêmes critères de scoring à tous les candidats d'une même offre, de façon automatique et reproductible.

Assurer la traçabilité complète du processus, en historisant chaque analyse et chaque action pour pouvoir justifier toute décision à tout moment.

Aider le recruteur à mieux décider, en lui fournissant non pas un simple score, mais un résumé clair, les forces et écarts du candidat, et des questions d'entretien prêtes à l'emploi.

### 4.2 Objectifs techniques et d'apprentissage

Construire une architecture réaliste qui simule de façon crédible un flux d'entreprise complet — publication d'offre, candidature, traitement IA, dashboard — sans dépendre des vrais systèmes LinkedIn ou Workday.

Mettre en place un pipeline de traitement automatique déclenché à chaque nouveau CV : analyse, extraction des compétences, scoring, génération de résumé et de questions d'entretien.

**Appliquer une véritable gouvernance des données, traitée comme un fil rouge présent à chaque étape du projet, et non comme un document final isolé.** Cela inclut la production progressive de livrables de gouvernance professionnels : charte, politique générale de gouvernance et ses articles d'application (accès, SOD, conservation, journalisation, secrets), glossaire / dictionnaire de données, démarche MDM (Master Data Management), registre des règles de gestion, procédures opérationnelles, et registre des décisions de gouvernance. À chaque fonctionnalité construite correspondra le livrable de gouvernance qu'elle exige.

Démontrer la traçabilité de bout en bout : audit logs, horodatage, historique des analyses et suivi de toutes les actions.

Livrer un produit présentable et entièrement documenté, prêt à être démontré en vidéo et raconté sur LinkedIn.

---

## 5. Personas

TalentFlow met en scène trois utilisateurs distincts, qui couvrent l'ensemble des interactions avec le produit.

### Karim — Recruteur (NovaTech)

Côté métier RH. Il a deux casquettes dans le produit : il *crée et configure* les offres d'emploi, et il *exploite* ensuite le dashboard pour analyser, comparer et décider. C'est l'utilisateur principal au quotidien — celui à qui le produit fait gagner du temps et de la fiabilité.

### Sarah — Candidate

Côté postulant. Son parcours est volontairement simple : découvrir une offre, postuler, déposer son CV, recevoir une confirmation. Elle n'a pas accès au système interne ; elle alimente le flux sans même le savoir.

### Awa — Data & Governance Officer

Garante de l'équité, de la traçabilité et de la conformité. Définit les règles de gestion, veille sur les audit logs, valide les changements, répond de toute décision. **Persona de premier plan, présente à chaque étape du projet** : aucune fonctionnalité n'est considérée comme terminée sans satisfaire ses exigences de gouvernance. Dispose d'un **droit de veto gouvernance** : toute fonctionnalité dont les exigences de gouvernance ne sont pas remplies est suspendue, quel que soit son avancement technique. Ce veto incarne le principe fondateur de TalentFlow.

---

## 6. Parcours utilisateurs

### Parcours 1 — Karim crée et publie l'offre

Karim est recruteur chez NovaTech. Son équipe a besoin d'un Data Analyst. Il se connecte à son espace recruteur. Il clique sur « Créer une offre ». Un formulaire s'ouvre : il saisit l'intitulé du poste, rédige la description des missions, indique le type de contrat et le niveau d'expérience attendu, et configure les compétences requises (par exemple : SQL, Python, visualisation de données, esprit d'analyse). Il relit, puis clique sur « Publier ». L'offre apparaît immédiatement sur une page publique, à l'apparence familière d'une annonce LinkedIn. Karim copie le lien et le partage.

### Parcours 2 — Sarah découvre l'offre et postule

Sarah cherche un poste de Data Analyst. Elle tombe sur l'annonce de NovaTech via le lien partagé. La page ressemble à s'y méprendre à une offre LinkedIn : logo de l'entreprise, intitulé, description des missions, compétences attendues. Intéressée, elle clique sur « Postuler ». Elle est alors redirigée vers le portail de candidature, dont l'apparence rappelle Workday. Là, elle renseigne ses informations et dépose son CV au format PDF. Elle vérifie, puis clique sur « Submit ». Une page de confirmation s'affiche : *« Votre candidature a bien été enregistrée. »* Pour Sarah, c'est terminé. Mais c'est précisément à cet instant, invisible pour elle, que TalentFlow se met en marche.

### Parcours 3 — Karim exploite les résultats

Quelques minutes plus tard, Karim ouvre son dashboard TalentFlow. Sans qu'il ait rien fait, plusieurs candidatures sont déjà là, analysées et classées automatiquement. En haut, une shortlist des meilleurs profils ; en dessous, le classement complet par score d'adéquation. Karim clique sur Sarah, en tête de liste avec 87/100. Il découvre son résumé RH en quelques lignes, les compétences détectées, les écarts repérés, et une liste de questions d'entretien déjà prêtes, adaptées à son profil. En un coup d'œil, Karim sait qui contacter en priorité et avec quelles questions. Et s'il se demande *« pourquoi ce score ? »*, l'historique et le journal d'audit lui montrent ce qui a été analysé, quand, et selon quelles règles. Il prend sa décision — éclairé par l'IA, mais c'est bien lui qui décide.

### Parcours 4 — Awa veille

Awa ouvre l'espace gouvernance de TalentFlow. Elle consulte le journal d'audit : chaque CV reçu, chaque analyse lancée, chaque score attribué y figure, horodaté. Elle ouvre le dossier d'un candidat écarté et vérifie pourquoi : quelles compétences ont été détectées, selon quelles règles le score a été calculé — tout est traçable, rien n'est une boîte noire. Elle vérifie qu'aucune donnée n'est conservée au-delà de la durée autorisée. Si une règle de scoring doit changer, c'est elle qui en valide la nouvelle version, et le changement est lui-même tracé. À tout moment, si on lui demande *« cette décision de recrutement est-elle justifiable et conforme ? »*, Awa peut répondre **oui, preuve à l'appui.**

---

## 7. Fonctionnalités par domaines

Le produit complet — au-delà du MVP — se déploie sur six domaines.

### Domaine 1 — Expérience LinkedIn simulée (publication & candidature)

Côté recruteur : une page d'administration façon espace recruteur LinkedIn où le RH crée et configure une offre d'emploi. Côté candidat : une page d'offre publique fidèle à l'expérience LinkedIn avec un bouton « Postuler » qui redirige vers l'espace de candidature.

### Domaine 2 — Espace de candidature & réception, façon Workday

Portail de candidature fidèle à l'expérience Workday. Le candidat dépose son CV au format PDF puis clique sur « Submit ». À ce moment précis, la candidature atterrit dans le système de réception centralisé et déclenche automatiquement le traitement IA.

### Domaine 3 — Moteur d'analyse IA

Extraction automatique des informations du CV. Identification des compétences et rapprochement avec un référentiel unique (MDM). Comparaison avec la description du poste. Calcul d'un score d'adéquation selon des règles de gestion explicites. Génération d'un résumé RH, de questions d'entretien adaptées, détection des écarts. En vision élargie : génération d'un test technique sur mesure et d'un plan d'onboarding personnalisé.

### Domaine 4 — Dashboard recruteur

Vue d'ensemble des candidatures d'une offre. Classement dynamique par score. Shortlist. Détail par candidat (score, compétences, résumé, écarts, questions). Mise à jour en quasi temps réel. Analytics.

### Domaine 5 — Gouvernance & traçabilité

Audit logs, historique des analyses, traçabilité des décisions. Livrables documentaires (charte, politiques, glossaire, MDM, règles de gestion, procédures) produits progressivement à chaque sprint.

### Domaine 6 — Socle technique

Stockage des données, authentification, gestion des comptes et rôles utilisateurs avec permissions séparées (mise en œuvre de la Séparation des tâches — SOD), configuration générale de sécurité, organisation du projet et documentation technique.

---

## 8. Périmètre du MVP

Le MVP (Minimum Viable Product) est défini comme **le plus petit chemin complet qui prouve déjà la valeur du produit**.

> Une offre est visible, un candidat dépose son CV, l'IA en extrait les compétences, les compare à l'offre, calcule un score et rédige un résumé ; le recruteur voit la liste des candidats classés et le détail de chacun ; chaque étape est tracée dans un journal d'audit, avec un glossaire et la règle de scoring documentés.

**Sont reportés après le MVP** (sans être oubliés) : la création d'offre côté recruteur via une interface dédiée (l'offre est pré-créée dans le MVP), la génération de questions d'entretien sur mesure, le test technique généré, le plan d'onboarding personnalisé, les analytics avancés, le MDM compétences complet, les politiques avancées.

---

## 9. Architecture simplifiée (vue de haut)

L'architecture détaillée sera produite en Sprint 0. À ce stade de cadrage, on retient les briques suivantes :

Une **interface web** (front-end) qui expose les pages côté candidat (page d'offre, portail de candidature) et côté recruteur (dashboard).

Un **back-end applicatif** qui gère la logique métier, les utilisateurs, les permissions, les candidatures.

Une **base de données** qui stocke les offres, candidats, candidatures, analyses et audit logs.

Un **module d'analyse IA** qui s'active à chaque nouvelle candidature reçue, lit le CV, en extrait les compétences, calcule le score et génère le résumé.

Un **stockage de fichiers** pour les CV PDF, séparé de la base de données.

Un **module d'audit** qui trace toute action sensible avec horodatage.

Une **gestion des secrets** qui isole les mots de passe d'application et clés d'API hors du code versionné.

---

## 10. Cadre de gouvernance

La gouvernance n'est pas un document final isolé : elle se construit sprint après sprint. Sa bibliothèque officielle compte sept documents (plus les articles d'application de la politique générale), tous versionnés indépendamment et tous passés en revue à chaque sprint par Awa.

### Bibliothèque officielle des documents de gouvernance

**GOV-01 — Charte de Gouvernance.** Document fondateur. Principes (équité, traçabilité, IA au service de l'humain), rôles et responsabilités, droit de veto d'Awa, vocation du projet.

**GOV-02 — Politique Générale de Gouvernance des Données.** Document de référence qui chapeaute toutes les politiques d'application. Énonce le cadre global et liste les politiques détaillées ci-dessous, présentées comme articles d'application.

- **GOV-02.1 — Politique d'Accès & Authentification** *(article)*
- **GOV-02.2 — Politique de Séparation des Tâches — SOD** *(article)*
- **GOV-02.3 — Politique de Conservation & Confidentialité** *(article)*
- **GOV-02.4 — Politique de Journalisation & Audit** *(article)*
- **GOV-02.5 — Politique de Gestion des Secrets** *(article)*

**GOV-03 — Glossaire / Dictionnaire de Données.** Liste officielle de tous les termes métier et techniques du projet, avec une définition unique partagée par tous.

**GOV-04 — Référentiel MDM (Master Data Management).** Données de référence du projet : référentiel unique de compétences, référentiel des rôles utilisateurs, référentiel des statuts de candidature. Source unique de vérité.

**GOV-05 — Registre des Règles de Gestion.** Liste explicite et versionnée de toutes les règles métier du système (scoring, classement, unicité, suppression…).

**GOV-06 — Procédures Opérationnelles.** Modes d'emploi des politiques (comment supprimer un CV expiré, comment changer une règle de scoring, comment revoir la matrice SOD…).

**GOV-07 — Registre des Décisions de Gouvernance.** Journal des décisions importantes prises par Awa, daté et signé.

### Règle de fonctionnement

Tous les documents de gouvernance sont **passés en revue à chaque sprint**. Ils sont soit mis à jour (nouvelle version : V2, V3…), soit confirmés inchangés avec justification explicite. Cette revue est présentée par Awa lors de chaque démo de sprint, en point d'agenda obligatoire.

---

## 11. Structure Agile du projet

### Méthode : Scrum, sprints de 2 semaines

Le projet adopte la méthode Scrum avec des sprints de deux semaines. Chaque sprint est jalonné de quatre cérémonies : planification (au début), point quotidien (chaque jour), revue/démo (à la fin), rétrospective (juste après la démo). Le suivi visuel quotidien s'appuie sur un tableau de type Kanban (colonnes *À faire / En cours / Terminé*) dans Jira.

### Six Epics du projet

| Code | Epic | MoSCoW | Ordre de construction |
|------|------|--------|----------------------|
| E6 | Socle Technique | Must | 1 |
| E2 | Workday Simulé | Must | 2 |
| E3 | Moteur d'Analyse IA | Must | 3 |
| E4 | Dashboard Recruteur | Must | 4 |
| E5 | Gouvernance & Traçabilité | Must (dosé) | En parallèle de tout |
| E1 | LinkedIn Simulé | Should | 5 (après MVP) |

**E5 — Gouvernance** n'a pas un ordre séquentiel : il accompagne *chaque* sprint des autres Epics, conformément à la doctrine de gouvernance vivante. À chaque sprint, les livrables de gouvernance correspondants sont produits ou mis à jour.

### Roadmap initiale (haute volée)

- **Sprint 0** — Cadrage final : outils, architecture détaillée, backlog complet, conventions, organisation GitHub, stratégie portfolio.
- **Sprint 1** — Début de E6 (Socle Technique) : initialisation du projet, stockage, comptes/rôles avec SOD.
- **Sprint 2** — Fin de E6 et démarrage de E2 (Workday simulé) : authentification, audit log, dépôt de CV.
- **Sprint 3** — E3 (Moteur IA) phase 1 : extraction des compétences, scoring de base, résumé RH.
- **Sprint 4** — E4 (Dashboard) : classement, vue détail candidat.
- **Sprint 5** — Consolidation MVP, démo de fin de MVP.
- **Sprints suivants** — E1 (LinkedIn simulé, interface de création d'offre), puis fonctionnalités élargies de la vision (questions d'entretien sur mesure, test technique, onboarding personnalisé, analytics avancés).

*Cette roadmap est indicative et sera affinée en Sprint 0.*

---

## 12. Backlog initial — Epic E6 (Socle Technique)

Le backlog initial du projet contient les six user stories et tâches techniques de l'Epic E6, qui sera construit en premier. Le détail complet (au format à 8 sections : en-tête, narration, contexte, détail fonctionnel, critères d'acceptation, note de gouvernance par document, dépendances, estimation) est saisi dans Jira. Vue synthétique ici.

**US-E6-01 — Initialisation du projet et organisation du dépôt**
Mise en place de l'arborescence du dépôt Git, du README, des conventions, du fichier d'ignorance des fichiers sensibles.
*Documents enrichis :* GOV-01 (charte v1), GOV-02.5 (politique gestion des secrets v1).

**US-E6-02 — Mise en place du stockage des données**
Base de données et entités principales (Offre, Candidat, Candidature, Analyse, AuditLog). Stockage séparé des CV PDF.
*Documents enrichis :* GOV-03 (glossaire v1), GOV-04 (référentiel MDM v1, premières briques).

**US-E6-03 — Création des comptes et rôles utilisateurs (SOD)** *(story de référence, format détaillé)*
Mise en œuvre technique de la Séparation des Tâches : trois rôles (Recruteur, Gouvernance, Administrateur), matrice des permissions, mécanisme de vérification du rôle à chaque action sensible, comptes de démonstration.
*Documents enrichis :* GOV-02.2 (politique SOD v1), GOV-03 (glossaire — nouveaux termes), GOV-04 (MDM — rôles comme donnée de référence), GOV-05 (registre des règles de gestion — règle sur l'unicité du rôle).

**US-E6-04 — Authentification sécurisée du recruteur**
Connexion, déconnexion, stockage chiffré des mots de passe, refus d'accès aux non-connectés.
*Documents enrichis :* GOV-02.1 (politique d'accès & authentification v1).

**US-E6-05 — Mise en place du journal d'audit (Audit Log)**
Entité AuditLog, traçage horodaté des actions sensibles, première action de test tracée.
*Documents enrichis :* GOV-02.4 (politique de journalisation & audit v1).

**US-E6-06 — Documentation technique initiale du projet**
Dossier `docs/`, page d'accueil avec schéma d'architecture, conventions de nommage.
*Documents enrichis :* tous les documents GOV trouvent leur emplacement officiel dans `docs/governance/`.

---

## 13. Definition of Done

Aucune fonctionnalité, aucun sprint, n'est considéré comme terminé tant que les conditions suivantes ne sont pas remplies.

**Sur la fonctionnalité elle-même.**

- Le code est écrit, testé, fonctionne dans les conditions définies par les critères d'acceptation de la user story.
- Le code est versionné dans GitHub, lié à son ticket Jira via le numéro du ticket dans le message de commit.
- La documentation technique correspondante est mise à jour.

**Sur la gouvernance** *(volet ajouté à la demande du Product Owner)*.

- Chaque fonctionnalité livrée a satisfait son exigence de gouvernance : règle documentée, action tracée, donnée protégée.
- Tous les livrables de gouvernance (GOV-01 à GOV-07) ont été passés en revue par Awa. Ils sont soit mis à jour (nouvelle version), soit confirmés inchangés avec mention explicite et justification.
- À la démo de sprint, Awa présente l'évolution de la documentation de gouvernance : ce qui a été ajouté, modifié, ou consciemment laissé inchangé. Cette présentation est un point d'agenda obligatoire de la démo.

**Sur le droit de veto.**

- Awa dispose d'un droit de veto gouvernance : toute fonctionnalité dont les exigences de gouvernance ne sont pas remplies est suspendue, quel que soit son avancement technique.

---

## 14. Conclusion et suite du travail

Ce document constitue la **V1 du cadrage** du projet TalentFlow. Il fige la vision, le problème, les objectifs, les utilisateurs, les parcours, le périmètre, le MVP, le cadre de gouvernance et la structure Agile. Il sera enrichi et raffiné au fil des sprints (les documents Agile sont des documents vivants — pas des monuments figés).

**Suite immédiate du travail (Sprint 0) :**

1. Configuration de Jira Cloud et de GitHub avec leur intégration.
2. Production de l'architecture détaillée (schémas).
3. Production de la roadmap finale.
4. Production du backlog complet des cinq autres Epics (E1, E2, E3, E4, E5) au format à 8 sections.
5. Définition des conventions GitHub (commits, branches, pull requests).
6. Production de la **V1 des documents de gouvernance** (GOV-01 squelette, GOV-03 glossaire de démarrage, GOV-02 politique générale dans son ossature).
7. Définition de la stratégie portfolio (vidéo de démo, publication LinkedIn, narration projet).

Une fois le Sprint 0 terminé, le **Sprint 1** entrera dans la construction réelle de l'Epic E6.

---

*Document V1 — sera versionné dans `docs/projet/` du dépôt GitHub de TalentFlow.*
