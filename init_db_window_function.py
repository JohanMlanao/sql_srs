import random
from datetime import datetime, timedelta

import pandas as pd


def get_memory_state_window_function():
    """
    Create and returns a pandas DataFrame containing all the basic information for all exercises
    """
    data = {
        "theme": ["Window function", "Window function"],
        "exercise_name": ["Its over", "Move it"],
        "tables": [["furniture"], ["wf_sales"]],
        "last_reviewed": ["1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_furniture():
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
    # Create a pandas DataFrame from the predefined data
    return pd.DataFrame(furniture_data, columns=["category", "item", "weight"])


def get_sales():
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2023, 9, 30)
    date_range = [
        start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)
    ]
    sales_data = [random.randint(1, 7) * 1000 for _ in range(len(date_range))]
    return pd.DataFrame({"date": date_range, "daily_sales": sales_data})
