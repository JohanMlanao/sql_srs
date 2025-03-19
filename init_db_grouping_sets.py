import random
import pandas as pd
import numpy as np


def get_memory_state_grouping_sets():
    """
    Create and returns a pandas DataFrame containing all the basic information for all exercises
    """
    data = {
        "theme": ["Grouping sets, Rollup & Cube", "Grouping sets, Rollup & Cube"],
        "exercise_name": [
            "Union contract and procedure type",
            "Contract, procedure and subdivision"
        ],
        "tables": [
            ["health_care"],
            ["health_care"],
        ],
        "last_reviewed": ["1980-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_health_care():
    num_samples = 1000
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
    # Initialize empty lists to store the data
    contrats_data = []
    sexe_data = []
    type_acte_data = []
    groupe_age_data = []
    annee_data = []
    cost_data = []
    # Generate random data for each category
    for _ in range(num_samples):
        contrats_data.append(random.choice(contrats))
        sexe_data.append(random.choice(sexe))
        if sexe_data == "femme":
            type_acte_choice = random.choice(list(type_acte.keys()))
        else:
            type_acte_options = list(type_acte.keys())
            type_acte_options.remove("maternite")
            type_acte_choice = random.choice(type_acte_options)

        type_acte_data.append(type_acte_choice)
        cost_mean = type_acte[type_acte_choice]
        cost_data.append(
            np.random.normal(cost_mean, cost_mean // 3.5)
        )  # Assuming a standard deviation of 50 for costs
        groupe_age_data.append(random.choice(groupe_age))
        annee_data.append(random.choice(annee))

    return pd.DataFrame(
        {
            "contract_type": contrats_data,
            "sex": sexe_data,
            "procedure_type": type_acte_data,
            "age_group": groupe_age_data,
            "year": annee_data,
            "reimbursement_amount": cost_data,
        }
    )
