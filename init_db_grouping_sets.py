import random

import numpy as np
import pandas as pd


def get_memory_state_grouping_sets() -> pd.DataFrame:
    """
    Returns metadata for SQL exercises related to Grouping Sets, Rollup, and Cube.

    This metadata includes the theme, names of the exercises, the relevant tables used in each,
    and the date each was last reviewed.

    :return: A Pandas DataFrame with columns: 'theme', 'exercise_name', 'tables', and 'last_reviewed'.
    """
    data = {
        "theme": [
            "Grouping sets, Rollup & Cube",
            "Grouping sets, Rollup & Cube",
            "Grouping sets, Rollup & Cube",
            "Grouping sets, Rollup & Cube",
        ],
        "exercise_name": [
            "Union contract and procedure type",
            "Contract, procedure and subdivision",
            "Ice cube",
            "Heads will roll",
        ],
        "tables": [
            ["health_care"],
            ["health_care"],
            ["health_care"],
            ["health_care"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01", "1970-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_health_care(num_samples: int = 1000) -> pd.DataFrame:
    """
    Generates a synthetic healthcare dataset used for exercises involving grouping sets, rollup, and cube operations.

    This dataset simulates healthcare reimbursements based on different contract types, procedure types,
    sex, age groups, and years. Random data is generated to mimic realistic distributions for training purposes.

    :param num_samples: The number of records (rows) to generate. Default is 1000.
    :return: A Pandas DataFrame with the following columns:
             - 'contract_type': Type of health insurance contract (e.g., senior, famille).
             - 'sex': Gender of the individual (homme, femme).
             - 'procedure_type': Type of medical procedure (e.g., pharmacie, hospitalisation).
             - 'age_group': Age group of the individual.
             - 'years': Year of the procedure.
             - 'reimbursement_amount': Simulated cost of the procedure.
    """
    contrats = ["senior", "jeunes", "expat", "famille", "salarié"]
    sexe = ["homme", "femme"]
    type_acte = {
        "pharmacie": 15,
        "consultation_generaliste": 25,
        "hospitalisation": 2800,
        "biologie": 150,
        "radio": 1300,
        "maternite": 1700,
    }
    groupe_age = ["18-25", "25-45", "45-65", "65+"]
    annee = [2017, 2018, 2019]

    contrats_data = []
    sexe_data = []
    type_acte_data = []
    groupe_age_data = []
    annee_data = []
    cost_data = []

    for _ in range(num_samples):
        selected_sexe = random.choice(sexe)
        selected_contract = random.choice(contrats)

        if selected_sexe == "femme":
            procedure_type = random.choice(list(type_acte.keys()))
        else:
            procedure_type = random.choice([k for k in type_acte if k != "maternite"])

        mean_cost = type_acte[procedure_type]
        cost = np.random.normal(mean_cost, mean_cost / 3.5)

        contrats_data.append(selected_contract)
        sexe_data.append(selected_sexe)
        type_acte_data.append(procedure_type)
        groupe_age_data.append(random.choice(groupe_age))
        annee_data.append(random.choice(annee))
        cost_data.append(cost)

    return pd.DataFrame(
        {
            "contract_type": contrats_data,
            "sex": sexe_data,
            "procedure_type": type_acte_data,
            "age_group": groupe_age_data,
            "years": annee_data,
            "reimbursement_amount": cost_data,
        }
    )
