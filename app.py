# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice
"""
)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)

    exercise = (
        con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'")
        .df()
        .sort_values("last_reviewed")
        .reset_index(drop=True)
    )
    st.write(exercise)

    try:
        exercise_name = exercise.loc[0, "exercise_name"]
        with open(f"answers/{exercise_name}.sql", "r") as f:
            answer = f.read()

        solution_df = con.execute(answer).df()
    except KeyError as e:
        pass

st.header("Enter your code:")
query = st.text_area(label="Here your SQL code", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))

    except KeyError as e:
        st.write("Some columns are missing")
    except NameError as n:
        pass
    try:
        n_lines_difference = result.shape[0] - solution_df.shape[0]
        if n_lines_difference != 0:
            st.write(
                f"result has a {n_lines_difference} lines difference with the solution"
            )
    except NameError as n:
        pass


tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    try:
        exercise_tables = exercise.loc[0, "tables"]
        for table in exercise_tables:
            st.write(f"table: {table}")
            df_table = con.execute(f"SELECT * FROM {table}").df()
            st.dataframe(df_table)
    except KeyError as e:
        pass

with tab3:
    try:
        st.write(answer)
    except NameError as n:
        pass
