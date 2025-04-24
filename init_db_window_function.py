import random
from datetime import datetime, timedelta

import pandas as pd


def get_memory_state_window_function() -> pd.DataFrame:
    """
    Returns a DataFrame containing metadata about window function exercises.

    The dataset includes:
    - `theme`: The overarching category of the exercise.
    - `exercise_name`: The name of each exercise related to window functions.
    - `tables`: The tables involved in each exercise.
    - `last_reviewed`: The date when the exercise was last reviewed.

    :return: A Pandas DataFrame containing details of window function exercises.
    """
    data = {
        "theme": [
            "Window function",
            "Window function",
            "Window function",
            "Window function",
            "Window function",
            "Window function",
            "Window function",
            "Window function",
        ],
        "exercise_name": [
            "Its over",
            "Move it",
            "Bi-twin",
            "Before and after",
            "A music score",
            "A second music score",
            "Ranking",
            "Qualification",
        ],
        "tables": [
            ["furniture"],
            ["wf_sales"],
            ["wf_sales"],
            ["wf_sales"],
            ["wages"],
            ["wages"],
            ["wages"],
            ["wages"],
        ],
        "last_reviewed": [
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
            "1970-01-01",
        ],
    }
    return pd.DataFrame(data)


def get_furniture() -> pd.DataFrame:
    """
    Generates and returns a Pandas DataFrame representing furniture inventory.

    The dataset includes:
    - `category`: The category of the furniture item (e.g., Chairs, Sofas, Tables).
    - `item`: The specific name of the furniture item.
    - `weight`: The weight of the item in kilograms.

    :return: A Pandas DataFrame containing furniture information.
    """
    furniture_data = [
        ("Chairs", "Chair 1", 5.2),
        ("Chairs", "Chair 2", 4.5),
        ("Chairs", "Chair 3", 6.8),
        ("Sofas", "Sofa 1", 25.5),
        ("Sofas", "Sofa 2", 20.3),
        ("Sofas", "Sofa 3", 30.0),
        ("Tables", "Table 1", 15.0),
        ("Tables", "Table 2", 12.5),
        ("Tables", "Table 3", 18.2),
    ]
    return pd.DataFrame(furniture_data, columns=["category", "item", "weight"])


def get_sales() -> pd.DataFrame:
    """
    Generates and returns a Pandas DataFrame representing sales data for a month.

    The dataset includes:
    - `date`: The specific date of sales transactions.
    - `daily_sales`: The total sales amount for each day in units of 1000.

    The sales values are randomly generated between 1000 and 7000 per day.

    :return: A Pandas DataFrame containing daily sales amounts.
    """
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2023, 9, 30)
    date_range = [
        start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)
    ]
    sales_data = [random.randint(1, 7) * 1000 for _ in range(len(date_range))]
    return pd.DataFrame({"date": date_range, "daily_sales": sales_data})
