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
            "Real life left-join"
        ],
        "tables": [
            ["orders", "order_details"],
            ["orders", "order_details", "customers"],
            ["orders", "order_details", "customers", "products"],
            ["real_products", "product_category", "universe_category", "sales"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01", "1969-01-01"],
    }
    return pd.DataFrame(data)