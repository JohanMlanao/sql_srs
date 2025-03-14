import io

import pandas as pd

data = {
        "theme": ["inner_joins", "inner_joins", "inner_joins", "inner_joins"],
        "exercise_name": [
            "salaries_and_seniority",
            "sizes_and_trademarks",
            "hours_and_minutes",
            "real_life_case",
        ],
        "tables": [
            ["salaries", "seniority"],
            ["sizes", "trademarks"],
            ["hours", "minutes"],
            ["stores", "months", "days", "markets", "quarters"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    }
pd.DataFrame(data)

salaries = '''
salary,employee_id
2000,1
2500,2
2200,3
'''
salaries = pd.read_csv(io.StringIO(salaries))

seniority = '''
employee_id,seniority
1,2ans
2,4ans
'''
seniority = pd.read_csv(io.StringIO(seniority))