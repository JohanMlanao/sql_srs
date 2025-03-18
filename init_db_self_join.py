import random

import pandas as pd


def get_memory_state_self_join():
    """
    Create and return a pandas DataFrame containing all the basic information for all self join exercises
    """
    data = {
        "theme": ["Self join", "Self join"],
        "exercise_name": ["Two days in a row", "The meeting"],
        "tables": [["self_sales"], ["meetings"]],
        "last_reviewed": ["1980-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_sales():
    sales = {
        "order_id": list(range(1110, 1198)),
        "customer_id": random.choices([11, 12, 13, 14, 15, 11, 12, 13, 14], k=88),
    }
    df_sales = pd.DataFrame(sales)
    df_sales["date"] = [d // 3 + 1 for d in range(1, 89)]
    return df_sales


def get_meetings():
    person_names = ["Benjamin", "Florian", "Tarik", "Bob", "Sirine", "Alice"]
    meetings_data = []
    for meeting_id in range(150):
        persons_in_meet = random.sample(person_names, random.randint(1, 5))
        for person_name in persons_in_meet:
            meetings_data.append((meeting_id, person_name))
    meetings_df = pd.DataFrame(meetings_data, columns=["meeting_id", "person_name"])
    meeting_durations = []
    for meeting_id in meetings_df["meeting_id"].unique():
        duration = random.randint(10, 60)  # You can adjust the range as needed
        meeting_durations.append((meeting_id, duration))
    durations_df = pd.DataFrame(
        meeting_durations, columns=["meeting_id", "duration_minutes"]
    )
    average_duration = durations_df["duration_minutes"].mean()
    meetings_with_flo = meetings_df[meetings_df["person_name"] == "Florian"][
        "meeting_id"
    ].unique()
    # meetings_with_ben = meetings_df[meetings_df["person_name"] == "Benjamin"]["meeting_id"].unique()
    # s=set(meetings_with_ben) & set(meetings_with_flo)
    for _, row in durations_df.iterrows():
        if row["meeting_id"] in meetings_with_flo:
            row["duration_minutes"] += random.randint(
                50, 55
            )  # Add extra minutes to meet the condition
    merged_df = meetings_df.merge(durations_df, on="meeting_id")
    return merged_df
