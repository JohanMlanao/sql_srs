import random
from datetime import datetime, timedelta

import pandas as pd


def get_memory_state_left_join():
    """
    Create and return a pandas DataFrame containing all the basic information for all inner join exercises
    """
    data = {
        "theme": ["Left join", "Left join", "Left join", "Left join"],
        "exercise_name": [
            "Orders with details",
            "Customers with detailed orders",
            "Customers with detailed orders and products",
            "Real life left-join",
        ],
        "tables": [
            ["orders", "order_details"],
            ["orders", "order_details", "customers"],
            ["orders", "order_details", "customers", "products"],
            [
                "real_products_custom",
                "product_category_custom",
                "universe_category_custom",
                "sales_custom",
            ],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1969-01-01"],
    }
    return pd.DataFrame(data)


def get_real_life_data_left_join():
    """
    Create and return 4 pandas DataFrames: products,product_category, universe_category, sales
    :return:
    """
    universe = ["Électronique", "Mode", "Maison", "Retail_magasin"]
    categories_par_univers = {
        "Électronique": ["Téléphones", "Ordinateurs"],
        "Mode": ["Vêtements", "Accessoires"],
        "Maison": ["Meubles", "Décoration"],
        "Retail_magasin": ["custom"],
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
        "custom": ["produit_local", "fournisseur_local", "circuit_court"],
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
                    "name": random.choice(noms_produits[categorie]),
                    "price_unit": round(random.uniform(10, 1000), 2),
                }
                donnees.append(produit)
                product_id_counter += 1
    df = pd.DataFrame(donnees)
    products = df[["product_id", "price_unit", "name"]]
    product_category = df[["category_id", "category_name", "product_id"]]
    universe_category = (
        df[["universe_id", "universe_name", "category_id"]].drop_duplicates().drop(90)
    )
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
                montant_total = row["price_unit"] * quantite_vendue
                ventes.append(
                    {
                        "date": date_vente,
                        "product_id": row["product_id"],
                        "sold_quantity": quantite_vendue,
                        "price_unit": row["price_unit"],
                        "total_amount": montant_total,
                    }
                )
    # Créer une DataFrame Pandas pour les ventes
    sales = pd.DataFrame(ventes)

    return products, product_category, universe_category, sales
