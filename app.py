import logging
import os
import subprocess
import sys
from datetime import date, timedelta

import duckdb
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


def create_database():
    """
    Ensures the 'data' directory and DuckDB database file exist.

    Creates the 'data' folder if missing and runs 'init_db.py' to initialize
    the 'exercises_sql_tables.duckdb' database if it's not found.
    """
    if "data" not in os.listdir():
        logging.error(os.listdir())
        logging.error("creating folder data")
        os.mkdir("data")
    if "exercises_sql_tables.duckdb" not in os.listdir("data"):
        subprocess.run([sys.executable, "init_db.py"])


def check_users_solution(user_query: str) -> None:
    """
    Validates a user's SQL query result against a predefined solution DataFrame.

    Args:
        user_query (str): A valid SQL query string written by the user.
            Example: "SELECT name FROM customers WHERE age > 30"

    Returns:
        None: Outputs feedback directly to the Streamlit interface.
    """
    result = con.execute(user_query).df()
    st.dataframe(result)
    try:
        if result.compare(solution_df).shape == (0, 0):
            st.write("Correct !")
            st.balloons()
    except ValueError:
        n_columns_difference = result.shape[1] - solution_df.shape[1]
        n_lines_difference = result.shape[0] - solution_df.shape[0]
        if n_columns_difference != 0 and n_lines_difference != 0:
            st.write(
                f"Result has a {n_columns_difference} columns and a {n_lines_difference} lines difference with the solution."
            )
        elif n_lines_difference != 0:
            st.write(
                f"Result has a {n_lines_difference} lines difference with the solution."
            )
        elif n_columns_difference != 0:
            st.write(
                f"Result has a {n_columns_difference} columns difference with the solution."
            )


def get_exercise(user_theme: str) -> pd.DataFrame:
    """
    Retrieves exercises matching the given theme, sorted by last reviewed date.

    Args:
        user_theme (str): Theme of the exercise (e.g. 'joins', 'group by').
            If empty, retrieves all exercises.

    Returns:
        pd.DataFrame: A DataFrame of exercises sorted by 'last_reviewed'.
    """
    if user_theme:
        select_exercise_query = (
            f"SELECT * FROM memory_state WHERE theme = '{user_theme}'"
        )
    else:
        select_exercise_query = "SELECT * FROM memory_state"
    user_exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    return user_exercise


def create_srs_button(list_d: list[int], user_exercise: str) -> None:
    """
    Creates Streamlit buttons to schedule or reset the review date of an exercise.

    Args:
        list_d (list[int]): A list of integers representing delay durations in days.
            Example: [1, 3, 7, 14]
        user_exercise (str): The name of the exercise to update.
            Must match the 'exercise_name' field in the database.

    Returns:
        None: Updates the database and triggers a rerun in the Streamlit app.
    """
    for n_days, col in zip(list_d, st.columns(len(list_d))):
        if col.button(f"Review in {n_days} days", use_container_width=True):
            next_review = date.today() + timedelta(days=n_days)
            con.execute(
                f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercise_name = '{user_exercise}'"
            )
            st.rerun()

    if st.button("Reset"):
        con.execute("UPDATE memory_state SET last_reviewed = '1970-01-01'")
        st.rerun()


# Creation of the database
create_database()

# Connection to the database
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

# Change the name of the web page
st.set_page_config(
    page_title="SQL SRS",
    layout="centered",
    # initial_sidebar_state=st.session_state.get('sidebar_state', 'expanded'),
)

# Title of the page

st.markdown(
    "<h1 style='text-align: center; color: black;'>SQL SRS </h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h3 style='text-align: center; color: black;'>Spaced Repetition System SQL practice </h3>",
    unsafe_allow_html=True,
)

# Creation of the sidebar
with st.sidebar:
    _, exp_col, _ = st.columns([1, 2, 1])
    with exp_col:
        st.image("logo/SQL_SRS_logo.png", width=225)
        # st.markdown("####")
    available_themes_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = option_menu(
        "What would you like to review ?",
        [
            "Cross join",
            "Inner join",
            "Left join",
            "Full outer join",
            "Self join",
            "Group by, CTE & Having",
            "Grouping sets, Rollup & Cube",
            "Case when",
            "Window function",
        ],
        menu_icon="intersect",
        default_index=0,
    )

    exercise = get_exercise(theme)
    st.write(exercise[["exercise_name", "tables", "last_reviewed"]])
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"questions/{exercise_name}.txt", "r") as q:
        question = q.read()
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(f"Current exercise: {exercise_name}")
    # Retrieve solution dataframe
    solution_df = con.execute(answer).df()

    # Create area for tables and solution in the sidebar
    tab2, tab3 = st.tabs(["Tables", "Solutions"])
    with tab2:
        exercise_tables = exercise.loc[0, "tables"]
        for table in exercise_tables:
            st.write(f"Table: {table}")
            df_table = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(df_table)
    with tab3:
        st.text(answer)

# Create the text area for SQL query
st.markdown("######")
st.text(f"{question}")
form = st.form("my_form")
query = form.text_area(
    label="Here your SQL code",
    key="user_input",
    label_visibility="collapsed",
    height=200,
)
form.form_submit_button("Submit")

if query:
    check_users_solution(query)

# Create the three buttons for SRS
create_srs_button([2, 7, 21], exercise_name)
