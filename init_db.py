import os
import subprocess
import sys

import duckdb

import init_db_cross_join as cj

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------

memory_state_df = cj.get_memory_state_cross_join()

con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------
beverages, food_items = cj.get_beverages_and_food_items()
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

sizes, trademarks = cj.get_sizes_and_trademarks()
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

hours, minutes = cj.get_hours_and_minutes()
con.execute("CREATE TABLE IF NOT EXISTS hours AS SELECT * FROM hours")
con.execute("CREATE TABLE IF NOT EXISTS minutes AS SELECT * FROM minutes")

stores, months, days, markets, quarters = cj.get_real_life_data()
con.execute("CREATE TABLE IF NOT EXISTS stores AS SELECT * FROM stores")
con.execute("CREATE TABLE IF NOT EXISTS months AS SELECT * FROM months")
con.execute("CREATE TABLE IF NOT EXISTS days AS SELECT * FROM days")
con.execute("CREATE TABLE IF NOT EXISTS markets AS SELECT * FROM markets")
con.execute("CREATE TABLE IF NOT EXISTS quarters AS SELECT * FROM quarters")

# ------------------------------------------------------------
# CROSS JOIN EXERCISES
# ------------------------------------------------------------

con.close()
