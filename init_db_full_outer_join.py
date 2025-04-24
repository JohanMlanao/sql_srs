import pandas as pd


def get_memory_state_full_outer_join() -> pd.DataFrame:
    """
    Returns a DataFrame containing basic information for all 'Full outer join' exercises.

    This method creates a DataFrame that includes the theme, exercise name, associated tables,
    and the last reviewed date for 'Full outer join' exercises.

    :return: A Pandas DataFrame with columns: 'theme', 'exercise_name', 'tables', and 'last_reviewed'.
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


def get_customers() -> pd.DataFrame:
    """
    Returns a DataFrame containing customer data.

    This method creates and returns a DataFrame with customer IDs and customer names.

    :return: A Pandas DataFrame with columns: 'customer_id' and 'customer_name'.
    """
    customers_data = {
        "customer_id": [11, 12, 13, 14, 15],
        "customer_name": ["Zeinaba", "Tancrède", "Israel", "Kaouter", "Alan"],
    }
    return pd.DataFrame(customers_data)


def get_stores() -> pd.DataFrame:
    """
    Returns a DataFrame containing store data with associated customer IDs.

    This method creates and returns a DataFrame that links stores to customer IDs.

    :return: A Pandas DataFrame with columns: 'store_id' and 'customer_id'.
    """
    stores_data = {"store_id": [1, 2, 3, 4], "customer_id": [11, 12, 13, 15]}
    return pd.DataFrame(stores_data)


def get_store_products() -> pd.DataFrame:
    """
    Returns a DataFrame containing store-product relationships.

    This method creates and returns a DataFrame that links stores with products via their IDs.

    :return: A Pandas DataFrame with columns: 'store_id' and 'product_id'.
    """
    store_products_data = {
        "store_id": [1, 1, 1, 2, 2, 3, 4],
        "product_id": [101, 103, 105, 101, 103, 104, 105],
    }
    return pd.DataFrame(store_products_data)


def get_products() -> pd.DataFrame:
    """
    Returns a DataFrame containing product data.

    This method creates and returns a DataFrame with product IDs, names, and prices.

    :return: A Pandas DataFrame with columns: 'product_id', 'product_name', and 'product_price'.
    """
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
