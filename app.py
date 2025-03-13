import logging
import os
import subprocess
import sys
from datetime import date, timedelta

import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    # Méthode "hacky" : exec(open("init_db.py").read())
    subprocess.run([sys.executable, "init_db.py"])

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


def check_users_solution(user_query: str) -> None:
    """
    Checks that user SQL query is correct by:
    1: checking the columns
    2: checking the values
    :param user_query: a string containing the query inserted by the user
    """
    result = con.execute(user_query).df()
    st.dataframe(result)
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
        if result.compare(solution_df).shape == (0, 0):
            st.write("Correct !")
            st.balloons()
    except KeyError:
        st.write("Some columns are missing.")
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"Result has a {n_lines_difference} lines difference with the solution."
        )


def get_exercise(user_theme: str):
    if user_theme:
        st.write(f"You selected: {user_theme}")
        select_exercise_query = (
            f"SELECT * FROM memory_state WHERE theme = '{user_theme}'"
        )
    else:
        select_exercise_query = f"SELECT * FROM memory_state "
    user_exercise = (
        con.execute(select_exercise_query)
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    return user_exercise


st.set_page_config(
    page_title="SQL SRS",
    layout="centered",
    # initial_sidebar_state=st.session_state.get('sidebar_state', 'expanded'),
)
st.write(
    """
    # SQL SRS
    Spaced Repetition System SQL practice
    """
)


with st.sidebar:
    _, exp_col, _ = st.columns([1, 3, 1])
    with exp_col:
        st.image("logo/SQL_SRS_logo.png")

    available_themes_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review ?",
        available_themes_df["theme"].unique(),
        index=None,
        placeholder="Select a theme...",
    )
    exercise = get_exercise(theme)
    st.write(exercise[["theme", "exercise_name", "last_reviewed"]])
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"questions/{exercise_name}.txt", "r") as q:
        question = q.read()
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()
st.text(f"Exercice: {question}")
query = st.text_area(
    label="Here your SQL code", key="user_input", label_visibility="collapsed"
)

if query:
    check_users_solution(query)

list_days = [2, 7, 21]

for n_days, col in zip(list_days, st.columns(len(list_days))):
    if col.button(f"Review in {n_days} days", use_container_width=True):
        next_review = date.today() + timedelta(days=n_days)
        con.execute(
            f"UPDATE memory_state SET last_reviewed = '{next_review}' WHERE exercise_name = '{exercise_name}'"
        )
        st.rerun()


if st.button("Reset"):
    con.execute(f"UPDATE memory_state SET last_reviewed = '1970-01-01'")
    st.rerun()

tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"Table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    st.text(answer)
