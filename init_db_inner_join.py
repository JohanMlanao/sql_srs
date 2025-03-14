import io

import pandas as pd


def get_memory_state_inner_join():
    """
    Create and return a pandas DataFrame containing all the basic information for all inner join exercises
    """
    data = {
        "theme": ["inner_joins"],
        "exercise_name": ["salaries_and_seniority"],
        "tables": [["salaries", "seniority"]],
        "last_reviewed": ["1980-01-01"],
    }
    return pd.DataFrame(data)


def get_salaries_and_seniority():
    """
    Create and return salaries and seniority tables as pandas DataFrames
    """
    salaries = """
salary,employee_id
2000,1
2500,2
2200,3
"""
    salaries = pd.read_csv(io.StringIO(salaries))
    seniority = """
employee_id,seniority
1,2ans
2,4ans
"""
    seniority = pd.read_csv(io.StringIO(seniority))
    return salaries, seniority
