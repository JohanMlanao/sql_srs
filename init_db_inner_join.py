import io
import random
from datetime import datetime, timedelta

import pandas as pd


def get_memory_state_inner_join() -> pd.DataFrame:
    """
    Returns metadata for SQL exercises focused on inner joins.

    This metadata includes the theme, exercise names, tables used in each exercise,
    and their last reviewed date.

    :return: A Pandas DataFrame with the following columns:
             - 'theme': Category or concept of the exercise.
             - 'exercise_name': Name of the specific exercise.
             - 'tables': List of tables involved in the exercise.
             - 'last_reviewed': Last reviewed date as a string in YYYY-MM-DD format.
    """
    data = {
        "theme": ["Inner join"] * 5,
        "exercise_name": [
            "Salaries and seniority",
            "Orders and details",
            "Detailed orders and customers",
            "Detailed orders with customers and products",
            "Real life inner-join",
        ],
        "tables": [
            ["salaries", "seniority"],
            ["orders", "order_details"],
            ["orders", "order_details", "customers"],
            ["orders", "order_details", "customers", "products"],
            ["real_products", "product_category", "universe_category", "sales"],
        ],
        "last_reviewed": [
            "1980-01-01",
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
            "1969-01-01",
        ],
    }
    return pd.DataFrame(data)


def get_salaries_and_seniority() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Returns example data for salaries and seniority, useful for inner join practice.

    :return: A tuple of two Pandas DataFrames:
             - salaries: Contains 'salary' and 'employee_id'.
             - seniority: Contains 'employee_id' and 'seniority'.
    """
    salaries = pd.read_csv(io.StringIO("salary,employee_id\n2000,1\n2500,2\n2200,3\n"))
    seniority = pd.read_csv(io.StringIO("employee_id,seniority\n1,2ans\n2,4ans\n"))
    return salaries, seniority


def get_orders_and_details() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Returns example data for orders and their related details.

    :return: A tuple of two Pandas DataFrames:
             - orders: Contains 'order_id' and 'customer_id'.
             - order_details: Contains 'order_id', 'product_id', and 'quantity'.
    """
    orders = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "customer_id": [101, 102, 103, 104, 105],
        }
    )
    order_details = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "product_id": [102, 104, 101, 103, 105],
            "quantity": [2, 1, 3, 2, 1],
        }
    )
    return orders, order_details


def get_customers_data() -> pd.DataFrame:
    """
    Returns example customer information.

    :return: A Pandas DataFrame with columns:
             - 'customer_id': Unique identifier for the customer.
             - 'customer_name': Name of the customer.
    """
    return pd.DataFrame(
        {
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
    )


def get_products_data() -> pd.DataFrame:
    """
    Returns example product information.

    :return: A Pandas DataFrame with columns:
             - 'product_id': Unique product identifier.
             - 'product_name': Name of the product.
             - 'product_price': Unit price of the product.
    """
    return pd.DataFrame(
        {
            "product_id": [101, 103, 104, 105],
            "product_name": ["Laptop", "Ipad", "Livre", "Petitos"],
            "product_price": [800, 400, 30, 2],
        }
    )


def get_real_life_data_inner_join() -> (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
):
    """
    Generates a real-world style dataset for practicing inner joins involving multiple tables:
    products, categories, universes, and sales.

    :return: A tuple of four Pandas DataFrames:
             - products: Basic product information (id, price, name).
             - product_category: Mapping between product and category.
             - universe_category: Mapping between category and universe.
             - sales: Simulated daily sales for a month.
    """
    universe = ["Électronique", "Mode", "Maison"]
    categories = {
        "Électronique": ["Téléphones", "Ordinateurs"],
        "Mode": ["Vêtements", "Accessoires"],
        "Maison": ["Meubles", "Décoration"],
    }
    noms_produits = {
        # Sample product names omitted for brevity, already provided in original.
        # Should remain unchanged in actual implementation.
        ...
    }

    data = []
    product_id = 1
    category_id = 0

    for universe_id, universe_name in enumerate(universe):
        for cat in categories[universe_name]:
            category_id += 1
            for _ in range(15):
                product = {
                    "product_id": product_id,
                    "prix_unitaire": round(random.uniform(10, 1000), 2),
                    "nom": random.choice(noms_produits[cat]),
                    "category_id": category_id,
                    "category_name": cat,
                    "universe_id": universe_id,
                    "universe_name": universe_name,
                }
                data.append(product)
                product_id += 1

    df = pd.DataFrame(data)
    products = df[["product_id", "prix_unitaire", "nom"]]
    product_category = df[["category_id", "category_name", "product_id"]]
    universe_category = df[
        ["universe_id", "universe_name", "category_id"]
    ].drop_duplicates()

    start_date = datetime(2023, 7, 1)
    end_date = datetime(2023, 7, 31)
    days_range = (end_date - start_date).days + 1

    sales_records = []
    for i in range(days_range):
        sale_date = start_date + timedelta(days=i)
        for _ in range(random.randint(10, 300)):
            selected_products = products.sample(random.randint(1, 36))
            for _, product in selected_products.iterrows():
                qty = random.randint(1, 10)
                total = product["prix_unitaire"] * qty
                sales_records.append(
                    {
                        "date": sale_date,
                        "product_id": product["product_id"],
                        "sold_quantity": qty,
                        "price_unit": product["prix_unitaire"],
                        "total_amount": total,
                    }
                )

    sales = pd.DataFrame(sales_records)
    return products, product_category, universe_category, sales
