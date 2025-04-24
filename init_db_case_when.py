import pandas as pd


def get_memory_state_case_when() -> pd.DataFrame:
    """
    Returns a DataFrame representing the memory state for 'Case when' exercises.

    This method provides mock data for SQL exercises related to the "Case when" SQL concept.

    :return: A Pandas DataFrame with columns: 'theme', 'exercise_name', 'tables', and 'last_reviewed'.
    """
    data = {
        "theme": ["Case when", "Case when", "Case when", "Case when"],
        "exercise_name": ["Sizes", "The rise", "Wings", "Income by category"],
        "tables": [["cw_orders"], ["wages"], ["redbull"], ["wages"]],
        "last_reviewed": ["1970-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_cw_orders() -> pd.DataFrame:
    """
    Returns a DataFrame with sample order data for 'cw_orders' table.

    This method provides mock data simulating order records in a table used for SQL exercises.

    :return: A Pandas DataFrame with columns: 'order_id', 'order_date', and 'order_amount'.
    """
    data = {
        "order_id": [1, 2, 3, 4, 5],
        "order_date": [
            "2023-01-15",
            "2023-02-20",
            "2023-03-05",
            "2023-04-10",
            "2023-05-18",
        ],
        "order_amount": [120, 450, 800, 60, 1500],
    }
    # Create a Pandas DataFrame
    return pd.DataFrame(data)


def get_wages() -> pd.DataFrame:
    """
    Returns a DataFrame with sample wage data for 'wages' table.

    This method provides mock data simulating wage records for employees in various departments.

    :return: A Pandas DataFrame with columns: 'name', 'wage', 'department', and 'sex'.
    """
    data = {
        "name": [
            "Toufik",
            "Jean-Nicolas",
            "Daniel",
            "Kaouter",
            "Sylvie",
            "Sebastien",
            "Diane",
            "Romain",
            "François",
            "Anna",
            "Zeinaba",
            "Gregory",
            "Karima",
            "Arthur",
            "Benjamin",
        ],
        "wage": [
            60000,
            75000,
            55000,
            80000,
            70000,
            90000,
            65000,
            72000,
            68000,
            85000,
            100000,
            120000,
            95000,
            83000,
            110000,
        ],
        "department": [
            "IT",
            "HR",
            "SALES",
            "IT",
            "IT",
            "HR",
            "SALES",
            "IT",
            "HR",
            "SALES",
            "IT",
            "IT",
            "HR",
            "SALES",
            "CEO",
        ],
        "sex": [
            "H",
            "H",
            "H",
            "F",
            "F",
            "H",
            "F",
            "H",
            "H",
            "F",
            "F",
            "H",
            "F",
            "H",
            "H",
        ],
    }
    return pd.DataFrame(data)


def get_redbull() -> pd.DataFrame:
    """
    Returns a DataFrame with sample sales data for 'redbull' products.

    This method provides mock data simulating sales records for a product in different store locations.

    :return: A Pandas DataFrame with columns: 'store_id', 'product_name', and 'amount'.
    """
    data = {
        "store_id": [
            "Armentieres",
            "Armentieres",
            "Armentieres",
            "Armentieres",
            "Lille",
            "Lille",
            "Lille",
            "Lille",
            "Douai",
            "Douai",
            "Douai",
            "Douai",
        ],
        "product_name": [
            "redbull",
            "chips",
            "wine",
            "redbull",
            "redbull",
            "chips",
            "wine",
            "icecream",
            "redbull",
            "chips",
            "wine",
            "icecream",
        ],
        "amount": [45, 60, 60, 45, 100, 140, 190, 170, 55, 70, 20, 45],
    }
    return pd.DataFrame(data)
