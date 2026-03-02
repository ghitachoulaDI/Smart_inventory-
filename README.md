SMART INVENTORY MANAGEMENT SYSTEM

Description

Smart Inventory est une application web développée avec Python et Django permettant de gérer les produits, les clients et les commandes.

L’objectif du projet est de simuler un système réel de gestion d’inventaire utilisé dans une entreprise, avec mise à jour automatique du stock et validation des données.

⸻

Fonctionnalités
	1.	Dashboard

	•	Nombre total de produits
	•	Nombre total de clients
	•	Nombre total de commandes
	•	Valeur totale du stock
	•	Revenu total

	2.	Gestion des Produits (CRUD)

	•	Ajouter un produit
	•	Modifier un produit
	•	Supprimer un produit
	•	Suivre la quantité en stock

	3.	Gestion des Clients (CRUD)

	•	Ajouter un client
	•	Modifier un client
	•	Supprimer un client
	•	Validation du format email
	•	Vérification d’unicité de l’email

	4.	Gestion des Commandes

	•	Création de commande avec plusieurs produits
	•	Déduction automatique du stock
	•	Vérification du stock disponible
	•	Blocage de la commande en cas de stock insuffisant

⸻

Logique du système

Lorsqu’une commande est créée :
	•	Le système vérifie si la quantité demandée est disponible
	•	Si le stock est insuffisant, la commande est annulée
	•	Si le stock est suffisant, la commande est enregistrée
	•	Le stock est automatiquement mis à jour

Cela garantit l’intégrité des données et empêche la vente de produits non disponibles.

⸻

Technologies utilisées
	•	Python 3
	•	Django
	•	MySQL
	•	HTML / CSS
	•	Bootstrap

⸻

Base de données

Base de données : smart_inventory

Tables principales :
	•	inventory_product
	•	inventory_customer
	•	inventory_order
	•	inventory_orderitem

⸻

Installation
	1.	Cloner le projet
	2.	Créer un environnement virtuel
	3.	Installer les dépendances
	4.	Configurer la base de données MySQL
	5.	Appliquer les migrations
	6.	Lancer le serveur avec :

python manage.py runserver

Puis accéder à :
http://127.0.0.1:8000/

⸻

Objectif académique

Ce projet démontre :
	•	L’utilisation du framework Django
	•	Les opérations CRUD complètes
	•	L’intégration avec une base de données relationnelle
	•	L’implémentation d’une logique métier
	•	La validation côté backend
