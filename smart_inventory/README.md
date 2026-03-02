# Smart Inventory

Smart Inventory est une application complète de gestion de stock et de commandes développée en Python.  
Le projet combine logique métier, base de données relationnelle, application web Django et analyse de données avec Pandas.

---

##  Fonctionnalités

- Gestion des produits (CRUD)
- Gestion des clients avec validation email
- Gestion des commandes avec plusieurs articles
- Déduction automatique du stock
- Dashboard avec indicateurs (KPI)
- Analyse des ventes avec Pandas
- Tests unitaires pour la logique métier

---

##  Architecture du Projet

Le projet est structuré en 4 couches principales :

###  Core (Logique Métier)
Contient les classes principales :
- `Product`
- `Customer`
- `Order`
- `OrderItem`

Inclut des exceptions personnalisées :
- OutOfStockException
- InvalidEmailException
- InvalidQuantityException

---

###  Database (MySQL + DAO)

- `schema.sql` : création des tables
- `populate.sql` : insertion de données
- DAO : gestion du CRUD et des transactions

Tables principales :
- products
- customers
- orders
- order_items

---

###  Web (Django)

Application Django avec :
- CRUD Produits
- CRUD Clients
- Gestion des commandes
- Dashboard avec KPI

---

### Analytics

- Export des données vers CSV
- Notebook Pandas (`analysis.ipynb`)
- Analyse : revenu total, top produits, valeur du stock

---

## Installation

### 1. Cloner le projet
```bash
git clone <repo_url>
cd smart_inventory