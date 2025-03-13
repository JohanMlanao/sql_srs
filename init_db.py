import io

import duckdb
import pandas as pd

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

data = {
    "theme": ["cross_joins", "cross_joins", "cross_joins", "cross_joins"],
    "exercise_name": [
        "beverages_and_food",
        "sizes_and_trademarks",
        "hours_and_quarters",
        "real_life_case"
    ],
    "tables": [
        ["beverages", "food_items"],
        ["sizes", "trademarks"],
        ["hours", "minutes"],
        ["stores", "months", "days", "markets", "quarters"]
    ],
    "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")


# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
beverages = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(beverages))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

food_items = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(food_items))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

trademarks = """
trademark
Nike
Asphalt
Abercrombie
Lewis
"""
trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

hours = """
hour
8
9
10
11
12
"""
hours = pd.read_csv(io.StringIO(hours))
con.execute("CREATE TABLE IF NOT EXISTS hours AS SELECT * FROM hours")

minutes = """
minute
0
15
30
45
"""
minutes = pd.read_csv(io.StringIO(minutes))
con.execute("CREATE TABLE IF NOT EXISTS minutes AS SELECT * FROM minutes")

unique_stores = ['Bordeaux', 'London', 'Madrid', 'Paris', 'Whatever']
unique_months = list(range(1,13))
unique_days = list(range(1,8))
unique_markets = ['fruits and vegetables', 'home products', 'charcuterie', 'snacks', 'video games']
quarters = (['08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45',
       '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30',
       '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15',
       '13:30', '08:30', '13:45', '14:00', '14:15', '14:30', '14:45',
       '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30',
       '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15',
       '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00'])

stores = pd.DataFrame(unique_stores, columns=["store_id"])
con.execute("CREATE TABLE IF NOT EXISTS stores AS SELECT * FROM stores")

months = pd.DataFrame(unique_months, columns=["month"])
con.execute("CREATE TABLE IF NOT EXISTS months AS SELECT * FROM months")

days = pd.DataFrame(unique_days, columns=["day_of_week"])
con.execute("CREATE TABLE IF NOT EXISTS days AS SELECT * FROM days")

markets = pd.DataFrame(unique_markets, columns=["market_type"])
con.execute("CREATE TABLE IF NOT EXISTS markets AS SELECT * FROM markets")

quarters = pd.DataFrame(quarters, columns=["quarter_hour"])
con.execute("CREATE TABLE IF NOT EXISTS quarters AS SELECT * FROM quarters")

con.close()
