import duckdb
import pandas as pd

import init_db_case_when as cw
import init_db_cross_join as cj
import init_db_full_outer_join as fj
import init_db_group_by as gb
import init_db_grouping_sets as gs
import init_db_inner_join as ij
import init_db_left_join as lj
import init_db_self_join as sj
import init_db_window_function as wf

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# ------------------------------------------------------------
# EXERCISES LIST
# ------------------------------------------------------------
memory_state_cj = cj.get_memory_state_cross_join()
memory_state_ij = ij.get_memory_state_inner_join()
memory_state_lj = lj.get_memory_state_left_join()
memory_state_fj = fj.get_memory_state_full_outer_join()
memory_state_sj = sj.get_memory_state_self_join()
memory_state_gb = gb.get_memory_state_group_by()
memory_state_gs = gs.get_memory_state_grouping_sets()
memory_state_cw = cw.get_memory_state_case_when()
memory_state_wf = wf.get_memory_state_window_function()
memory_state_df = pd.concat(
    [
        memory_state_cj,
        memory_state_ij,
        memory_state_lj,
        memory_state_fj,
        memory_state_sj,
        memory_state_gb,
        memory_state_gs,
        memory_state_cw,
        memory_state_wf,
    ]
)

con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ------------------------------------------------------------
# CROSS JOIN TABLES
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
# INNER JOIN and LEFT JOIN TABLES
# ------------------------------------------------------------

salaries, seniority = ij.get_salaries_and_seniority()
con.execute("CREATE TABLE IF NOT EXISTS salaries AS SELECT * FROM salaries")
con.execute("CREATE TABLE IF NOT EXISTS seniority AS SELECT * FROM seniority")

orders, order_details = ij.get_orders_and_details()
con.execute("CREATE TABLE IF NOT EXISTS orders AS SELECT * FROM orders")
con.execute("CREATE TABLE IF NOT EXISTS order_details AS SELECT * FROM order_details")

customers = ij.get_customers_data()
con.execute("CREATE TABLE IF NOT EXISTS customers AS SELECT * FROM customers")

products = ij.get_products_data()
con.execute("CREATE TABLE IF NOT EXISTS products AS SELECT * FROM products")

real_products, product_category, universe_category, sales = (
    lj.get_real_life_data_left_join()
)
con.execute("CREATE TABLE IF NOT EXISTS real_products AS SELECT * FROM real_products")
con.execute(
    "CREATE TABLE IF NOT EXISTS product_category AS SELECT * FROM product_category"
)
con.execute(
    "CREATE TABLE IF NOT EXISTS universe_category AS SELECT * FROM universe_category"
)
con.execute("CREATE TABLE IF NOT EXISTS sales AS SELECT * FROM sales")

# ------------------------------------------------------------
# FULL OUTER JOIN TABLES
# ------------------------------------------------------------

full_customers = fj.get_customers()
con.execute("CREATE TABLE IF NOT EXISTS full_customers AS SELECT * FROM full_customers")

full_stores = fj.get_stores()
con.execute("CREATE TABLE IF NOT EXISTS full_stores AS SELECT * FROM full_stores")

full_store_products = fj.get_store_products()
con.execute(
    "CREATE TABLE IF NOT EXISTS full_store_products AS SELECT * FROM full_store_products"
)

full_products = fj.get_products()
con.execute("CREATE TABLE IF NOT EXISTS full_products AS SELECT * FROM full_products")

# ------------------------------------------------------------
# SELF JOIN TABLES
# ------------------------------------------------------------

self_sales = sj.get_sales()
con.execute("CREATE TABLE IF NOT EXISTS self_sales AS SELECT * FROM self_sales")

meetings = sj.get_meetings()
con.execute("CREATE TABLE IF NOT EXISTS meetings AS SELECT * FROM meetings")

# ------------------------------------------------------------
# GROUP BY, HAVING and CTE TABLES
# ------------------------------------------------------------

gb_sales = gb.get_sales()
con.execute("CREATE TABLE IF NOT EXISTS gb_sales AS SELECT * FROM gb_sales")

# ------------------------------------------------------------
# GROUPING SETS, ROLLUP and CUBE
# ------------------------------------------------------------

health_care = gs.get_health_care()
con.execute("CREATE TABLE IF NOT EXISTS health_care AS SELECT * FROM health_care")

# ------------------------------------------------------------
# CASE WHEN
# ------------------------------------------------------------

cw_orders = cw.get_cw_orders()
con.execute("CREATE TABLE IF NOT EXISTS cw_orders AS SELECT * FROM cw_orders")

wages = cw.get_wages()
con.execute("CREATE TABLE IF NOT EXISTS wages AS SELECT * FROM wages")

redbull = cw.get_redbull()
con.execute("CREATE TABLE IF NOT EXISTS redbull AS SELECT * FROM redbull")

# ------------------------------------------------------------
# WINDOW FUNCTION
# ------------------------------------------------------------

furniture = wf.get_furniture()
con.execute("CREATE TABLE IF NOT EXISTS furniture AS SELECT * FROM furniture")

wf_sales = wf.get_sales()
con.execute("CREATE TABLE IF NOT EXISTS wf_sales AS SELECT * FROM wf_sales")

con.close()
