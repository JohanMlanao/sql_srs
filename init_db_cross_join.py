import io

import pandas as pd


def get_memory_state_cross_join() -> pd.DataFrame:
    """
    Returns a DataFrame containing basic information for all 'Cross join' exercises.

    This method creates a DataFrame that includes themes, exercise names, associated tables,
    and the last reviewed dates for 'Cross join' exercises.

    :return: A Pandas DataFrame with columns: 'theme', 'exercise_name', 'tables', and 'last_reviewed'.
    """
    data = {
        "theme": ["Cross join", "Cross join", "Cross join", "Cross join"],
        "exercise_name": [
            "Beverages and food",
            "Sizes and trademarks",
            "Hours and minutes",
            "Real life cross-join",
        ],
        "tables": [
            ["beverages", "food_items"],
            ["sizes", "trademarks"],
            ["hours", "minutes"],
            ["stores", "markets", "months", "days", "quarters"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_beverages_and_food_items() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Creates and returns the 'beverages' and 'food_items' tables as Pandas DataFrames.

    This method provides mock data for beverages and food items, returning two DataFrames:
    one for beverages and one for food items.

    :return: A tuple containing two Pandas DataFrames:
             - beverages DataFrame with columns: 'beverage' and 'price'
             - food_items DataFrame with columns: 'food_item' and 'food_price'
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


def get_sizes_and_trademarks() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Creates and returns the 'sizes' and 'trademarks' tables as Pandas DataFrames.

    This method provides mock data for sizes and trademarks, returning two DataFrames:
    one for sizes and one for trademarks.

    :return: A tuple containing two Pandas DataFrames:
             - sizes DataFrame with a single column: 'size'
             - trademarks DataFrame with a single column: 'trademark'
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


def get_hours_and_minutes() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Creates and returns the 'hours' and 'minutes' tables as Pandas DataFrames.

    This method provides mock data for hours and minutes, returning two DataFrames:
    one for hours and one for minutes.

    :return: A tuple containing two Pandas DataFrames:
             - hours DataFrame with a single column: 'hour'
             - minutes DataFrame with a single column: 'minute'
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


def get_real_life_data() -> (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
):
    """
    Creates and returns tables for stores, months, days, markets, and quarters as Pandas DataFrames.

    This method provides mock data for different types of real-life data, returning
    five DataFrames: one for stores, one for months, one for days of the week, one for markets,
    and one for quarter-hour time slots.

    :return: A tuple containing five Pandas DataFrames:
             - stores DataFrame with a single column: 'store_id'
             - months DataFrame with a single column: 'month'
             - days DataFrame with a single column: 'day_of_week'
             - markets DataFrame with a single column: 'market_type'
             - quarters DataFrame with a single column: 'quarter_hour'
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
