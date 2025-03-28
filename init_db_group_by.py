import pandas as pd


def get_memory_state_group_by():
    """
    Create and returns a pandas DataFrame containing all the basic information for all exercises
    """
    data = {
        "theme": [
            "Group by, CTE & Having",
            "Group by, CTE & Having",
            "Group by, CTE & Having",
            "Group by, CTE & Having",
        ],
        "exercise_name": [
            "Average purchase",
            "Above average purchase",
            "Average sum of sales",
            "More meetings",
        ],
        "tables": [["gb_sales"], ["gb_sales"], ["gb_sales"], ["meetings"]],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_sales():
    clients = [
        "Oussama",
        "Julie",
        "Chris",
        "Tom",
        "Jean-Nicolas",
        "Aline",
        "Ben",
        "Toufik",
        "Sylvie",
        "David",
    ]
    sales = [110, 49, 65, 23, 24, 3.99, 29, 48.77, 44, 10, 60, 12, 62, 19, 75] * 2
    sales = pd.DataFrame(sales)
    sales.columns = ["amount"]
    sales["client"] = clients * 3
    return sales
