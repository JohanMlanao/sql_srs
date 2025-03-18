import pandas as pd


def get_memory_state_full_outer_join():
    """
    Create and return a pandas DataFrame containing all the basic information for all full outer join exercises
    """
    data = {
        "theme": ["Full outer join"],
        "exercise_name": ["Customer, stores, products with details"],
        "tables": [
            ["full_customers", "full_stores", "full_store_products", "full_products"]
        ],
        "last_reviewed": ["1980-01-01"],
    }
    return pd.DataFrame(data)


def get_customers():
    customers_data = {
        "customer_id": [11, 12, 13, 14, 15],
        "customer_name": ["Zeinaba", "Tancrède", "Israel", "Kaouter", "Alan"],
    }
    return pd.DataFrame(customers_data)


def get_stores():
    stores_data = {"store_id": [1, 2, 3, 4], "customer_id": [11, 12, 13, 15]}
    return pd.DataFrame(stores_data)


def get_store_products():
    store_products_data = {
        "store_id": [1, 1, 1, 2, 2, 3, 4],
        "product_id": [101, 103, 105, 101, 103, 104, 105],
    }
    return pd.DataFrame(store_products_data)


def get_products():
    p_names = [
        "Cherry coke",
        "Laptop",
        "Ipad",
        "Livre",
    ]
    products_data = {
        "product_id": [100, 101, 103, 104],
        "product_name": p_names,
        "product_price": [3, 800, 400, 30],
    }
    return pd.DataFrame(products_data)
