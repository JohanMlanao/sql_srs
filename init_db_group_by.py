import pandas as pd


def get_memory_state_group_by() -> pd.DataFrame:
    """
    Returns a DataFrame containing metadata for 'Group by, CTE & Having' exercises.

    This includes the theme, exercise names, associated tables, and last reviewed dates
    for a series of SQL exercises that focus on group by operations, common table expressions, and HAVING clauses.

    :return: A Pandas DataFrame with columns: 'theme', 'exercise_name', 'tables', and 'last_reviewed'.
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


def get_sales() -> pd.DataFrame:
    """
    Returns a DataFrame simulating client sales data.

    This method generates a mock dataset where each row represents a sale made by a client.
    The data is structured to include duplicate entries to simulate multiple purchases per client.

    :return: A Pandas DataFrame with columns: 'amount' (float) and 'client' (str).
    """
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
    sales = pd.DataFrame(sales, columns=["amount"])
    sales["client"] = (
        clients * 3
    )  # Replicates the client names to match the length of sales
    return sales
