import io

import pandas as pd


def get_memory_state_inner_join():
    """
    Create and return a pandas DataFrame containing all the basic information for all inner join exercises
    """
    data = {
        "theme": ["Inner join", "Inner join", "Inner join"],
        "exercise_name": ["Salaries and seniority", "Orders and details", "Detailed orders and customers"],
        "tables": [["salaries", "seniority"], ["orders", "order_details"], ["orders", "order_details", "customers"]],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01"],
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
        'customer_id': [101, 102, 103, 104, 105, 106],
        'customer_name': ["Toufik", "Daniel", "Tancrède", "Kaouter", "Jean-Nicolas", "David"]
    }
    return pd.DataFrame(customers_data)


def get_products_data():
    """
    Create and return products table as pandas DataFrame
    :return:
    """
    p_names = ["Laptop", "Ipad", "Livre", "Petitos"]
    products_data = {
        'product_id': [101, 103, 104, 105],
        'product_name': p_names,
        'product_price': [800, 400, 30, 2]
    }
    return pd.DataFrame(products_data)


