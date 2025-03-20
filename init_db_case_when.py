import pandas as pd


def get_memory_state_case_when():
    """
    Create and returns a pandas DataFrame containing all the basic information for all exercises
    """
    data = {
        "theme": ["Case when", "Case when"],
        "exercise_name": [
            "Sizes",
            "The rise",
        ],
        "tables": [["cw_orders"], ["wages"]],
        "last_reviewed": ["1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_cw_orders():
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


def get_wages():
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
    }
    return pd.DataFrame(data)
