import pandas as pd


def get_memory_state_case_when():
    """
    Create and returns a pandas DataFrame containing all the basic information for all exercises
    """
    data = {
        "theme": ["Case when"],
        "exercise_name": [
            "Sizes",
        ],
        "tables": [["cw_orders"]],
        "last_reviewed": ["1970-01-01"],
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
