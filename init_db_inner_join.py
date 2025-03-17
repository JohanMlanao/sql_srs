import io
import random
from datetime import datetime, timedelta

import pandas as pd


def get_memory_state_inner_join():
    """
    Create and return a pandas DataFrame containing all the basic information for all inner join exercises
    """
    data = {
        "theme": ["Inner join", "Inner join", "Inner join", "Inner join", "Inner join"],
        "exercise_name": [
            "Salaries and seniority",
            "Orders and details",
            "Detailed orders and customers",
            "Detailed orders with customers and products",
            "Real life inner-join"
        ],
        "tables": [
            ["salaries", "seniority"],
            ["orders", "order_details"],
            ["orders", "order_details", "customers"],
            ["orders", "order_details", "customers", "products"],
            ["real_products", "product_category", "universe_category", "sales"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1969-01-01"],
    }
    return pd.DataFrame(data)


def get_salaries_and_seniority():
    """
    Create and return salaries and seniority tables as pandas DataFrames
    """
    salaries = """
salary,employee_id
2000,1
2500,2
2200,3
"""
    salaries = pd.read_csv(io.StringIO(salaries))
    seniority = """
employee_id,seniority
1,2ans
2,4ans
"""
    seniority = pd.read_csv(io.StringIO(seniority))
    return salaries, seniority


def get_orders_and_details():
    """
    Create and return orders and details tables as pandas DataFrames
    :return:
    """
    orders_data = {
        "order_id": [1, 2, 3, 4, 5],
        "customer_id": [101, 102, 103, 104, 105],
    }
    orders = pd.DataFrame(orders_data)
    order_details_data = {
        "order_id": [1, 2, 3, 4, 5],
        "product_id": [102, 104, 101, 103, 105],
        "quantity": [2, 1, 3, 2, 1],
    }

    order_details = pd.DataFrame(order_details_data)
    return orders, order_details


def get_customers_data():
    """
    Create and return customers table as pandas DataFrame
    :return:
    """
    customers_data = {
        "customer_id": [101, 102, 103, 104, 105, 106],
        "customer_name": [
            "Toufik",
            "Daniel",
            "Tancrède",
            "Kaouter",
            "Jean-Nicolas",
            "David",
        ],
    }
    return pd.DataFrame(customers_data)


def get_products_data():
    """
    Create and return products table as pandas DataFrame
    :return:
    """
    p_names = ["Laptop", "Ipad", "Livre", "Petitos"]
    products_data = {
        "product_id": [101, 103, 104, 105],
        "product_name": p_names,
        "product_price": [800, 400, 30, 2],
    }
    return pd.DataFrame(products_data)


def get_real_life_data_inner_join():
    """
    Create and return 4 pandas DataFrames: products,product_category, universe_category, sales
    :return:
    """
    universe = ["Électronique", "Mode", "Maison"]
    categories_par_univers = {
        "Électronique": ["Téléphones", "Ordinateurs"],
        "Mode": ["Vêtements", "Accessoires"],
        "Maison": ["Meubles", "Décoration"],
    }
    noms_produits = {
        "Téléphones": [
            "iPhone 13",
            "Samsung Galaxy S21",
            "Google Pixel 6",
            "OnePlus 9",
            "Xiaomi Mi 11",
            "Sony Xperia 5 III",
            "Huawei P40 Pro",
            "LG Velvet",
            "Motorola Edge",
            "Nokia 8.3",
        ],
        "Ordinateurs": [
            "MacBook Pro",
            "Dell XPS 15",
            "HP Spectre x360",
            "Lenovo ThinkPad",
            "Asus ROG Zephyrus",
            "Microsoft Surface Laptop",
            "Acer Predator Helios",
            "Razer Blade",
            "MSI Prestige",
            "LG Gram",
        ],
        "Vêtements": [
            "Chemise en lin",
            "Robe d'été",
            "Jeans slim",
            "Veste en cuir",
            "Pull en laine",
            "Pantalon chino",
            "T-shirt graphique",
            "Blouse à volants",
            "Blazer ajusté",
            "Short en denim",
        ],
        "Accessoires": [
            "Montre élégante",
            "Sac à dos moderne",
            "Lunettes de soleil",
            "Ceinture en cuir",
            "Écharpe en soie",
            "Boucles d'oreilles",
            "Chapeau en feutre",
            "Bracelet en métal",
            "Cravate en soie",
            "Portefeuille en cuir",
        ],
        "Meubles": [
            "Canapé modulaire",
            "Table à manger en bois",
            "Lit king-size",
            "Chaise ergonomique",
            "Bureau en verre",
            "Étagère murale",
            "Buffet en bois",
            "Fauteuil inclinable",
            "Table basse moderne",
            "Commode à tiroirs",
        ],
        "Décoration": [
            "Vase en céramique",
            "Tableau abstrait",
            "Bougie parfumée",
            "Coussins décoratifs",
            "Horloge murale",
            "Plante d'intérieur",
            "Suspension lumineuse",
            "Miroir encadré",
            "Tapis tissé",
            "Statuette en bronze",
        ],
    }
    donnees = []
    product_id_counter = 1
    category_id = 0
    for universe_id, universe_name in enumerate(universe):
        for categorie in categories_par_univers[universe_name]:
            category_id += 1
            for _ in range(15):  # Créer 15 exemples de produits par catégorie
                produit = {
                    "product_id": product_id_counter,
                    "universe_id": universe_id,
                    "universe_name": universe_name,
                    "category_name": categorie,
                    "category_id": category_id,
                    "nom": random.choice(noms_produits[categorie]),
                    "prix_unitaire": round(random.uniform(10, 1000), 2),
                }
                donnees.append(produit)
                product_id_counter += 1
    df = pd.DataFrame(donnees)
    products = df[["product_id", "prix_unitaire", "nom"]]
    product_category = df[["category_id", "category_name", "product_id"]]
    universe_category = df[
        ["universe_id", "universe_name", "category_id"]
    ].drop_duplicates()
    # Un mois de ventes:
    date_debut = datetime(2023, 7, 1)
    date_fin = datetime(2023, 7, 31)
    jours_dans_le_mois = (date_fin - date_debut).days + 1
    ventes = []
    for jour in range(jours_dans_le_mois):
        date_vente = date_debut + timedelta(days=jour)
        n_sales_that_day = range(1, random.randint(10, 300))
        for vente in n_sales_that_day:
            products_in_that_sale = products.sample(random.randint(1, 36))
            for _, row in products_in_that_sale.iterrows():
                quantite_vendue = random.randint(1, 10)
                montant_total = row["prix_unitaire"] * quantite_vendue
                ventes.append(
                    {
                        "date": date_vente,
                        "product_id": row["product_id"],
                        "sold_quantity": quantite_vendue,
                        "price_unit": row["prix_unitaire"],
                        "total_amount": montant_total,
                    }
                )
    # Créer une DataFrame Pandas pour les ventes
    sales = pd.DataFrame(ventes)

    return products, product_category, universe_category, sales
