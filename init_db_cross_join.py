import io

import pandas as pd


def get_memory_state_cross_join():
    """
    Create and returns a pandas DataFrame containing all the basic information for all exercises
    """
    data = {
        "theme": ["cross_joins", "cross_joins", "cross_joins", "cross_joins"],
        "exercise_name": [
            "beverages_and_food",
            "sizes_and_trademarks",
            "hours_and_minutes",
            "real_life_case",
        ],
        "tables": [
            ["beverages", "food_items"],
            ["sizes", "trademarks"],
            ["hours", "minutes"],
            ["stores", "months", "days", "markets", "quarters"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_beverages_and_food_items():
    """
    Creates and returns beverages and food_items tables as pandas DataFrames
    """
    beverages = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
    beverages = pd.read_csv(io.StringIO(beverages))
    food_items = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
    food_items = pd.read_csv(io.StringIO(food_items))
    return beverages, food_items


def get_sizes_and_trademarks():
    """
    Creates and returns sizes and trademarks tables as pandas DataFrames
    """
    sizes = """
size
XS
M
L
XL
"""
    sizes = pd.read_csv(io.StringIO(sizes))
    trademarks = """
trademark
Nike
Asphalt
Abercrombie
Lewis
"""
    trademarks = pd.read_csv(io.StringIO(trademarks))
    return sizes, trademarks


def get_hours_and_minutes():
    """
    Creates and returns hours and minutes tables as pandas DataFrames
    """
    hours = """
hour
8
9
10
11
12
"""
    hours = pd.read_csv(io.StringIO(hours))
    minutes = """
minute
0
15
30
45
"""
    minutes = pd.read_csv(io.StringIO(minutes))
    return hours, minutes


def get_real_life_data():
    """
    Creates and returns tables as pandas DataFrames
    """
    unique_stores = ["Bordeaux", "London", "Madrid", "Paris", "Whatever"]
    stores = pd.DataFrame(unique_stores, columns=["store_id"])
    unique_months = list(range(1, 13))
    months = pd.DataFrame(unique_months, columns=["month"])
    unique_days = list(range(1, 8))
    days = pd.DataFrame(unique_days, columns=["day_of_week"])
    unique_markets = [
        "fruits and vegetables",
        "home products",
        "charcuterie",
        "snacks",
        "video games",
    ]
    markets = pd.DataFrame(unique_markets, columns=["market_type"])
    quarters = [
        "08:00",
        "08:15",
        "08:30",
        "08:45",
        "09:00",
        "09:15",
        "09:30",
        "09:45",
        "10:00",
        "10:15",
        "10:30",
        "10:45",
        "11:00",
        "11:15",
        "11:30",
        "11:45",
        "12:00",
        "12:15",
        "12:30",
        "12:45",
        "13:00",
        "13:15",
        "13:30",
        "08:30",
        "13:45",
        "14:00",
        "14:15",
        "14:30",
        "14:45",
        "15:00",
        "15:15",
        "15:30",
        "15:45",
        "16:00",
        "16:15",
        "16:30",
        "16:45",
        "17:00",
        "17:15",
        "17:30",
        "17:45",
        "18:00",
        "18:15",
        "18:30",
        "18:45",
        "19:00",
        "19:15",
        "19:30",
        "19:45",
        "20:00",
    ]
    quarters = pd.DataFrame(quarters, columns=["quarter_hour"])
    return stores, months, days, markets, quarters
