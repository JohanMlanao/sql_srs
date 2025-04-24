import random

import pandas as pd


def get_memory_state_self_join() -> pd.DataFrame:
    """
    Returns a DataFrame containing metadata about self join exercises.

    :return: A Pandas DataFrame containing the theme, exercise names, involved tables, and last reviewed dates.
    """
    data = {
        "theme": ["Self join", "Self join"],
        "exercise_name": ["Two days in a row", "The meeting"],
        "tables": [["self_sales"], ["meetings"]],
        "last_reviewed": ["1980-01-01", "1970-01-01"],
    }
    return pd.DataFrame(data)


def get_sales() -> pd.DataFrame:
    """
    Generates and returns a Pandas DataFrame representing sales data.

    The dataset includes:
    - `order_id`: Unique order identifiers.
    - `customer_id`: Randomly assigned customer IDs associated with each order.
    - `date`: Artificial day index representing when the order was placed.

    :return: A Pandas DataFrame containing sales data.
    """
    sales = {
        "order_id": list(range(1110, 1198)),
        "customer_id": random.choices([11, 12, 13, 14, 15, 11, 12, 13, 14], k=88),
    }
    df_sales = pd.DataFrame(sales)
    df_sales["date"] = [d // 3 + 1 for d in range(1, 89)]
    return df_sales


def get_meetings() -> pd.DataFrame:
    """
    Generates and returns a Pandas DataFrame containing meeting data.

    The dataset includes:
    - `meeting_id`: Unique identifiers for meetings.
    - `person_name`: Names of participants in each meeting.
    - `duration_minutes`: The duration of each meeting in minutes.

    Meetings that include "Florian" receive a randomly increased duration.

    :return: A Pandas DataFrame containing meeting details with participant names and durations.
    """
    person_names = ["Benjamin", "Florian", "Tarik", "Bob", "Sirine", "Alice"]
    meetings_data = []

    # Generate random meeting participants
    for meeting_id in range(150):
        persons_in_meet = random.sample(person_names, random.randint(1, 5))
        for person_name in persons_in_meet:
            meetings_data.append((meeting_id, person_name))

    meetings_df = pd.DataFrame(meetings_data, columns=["meeting_id", "person_name"])

    # Generate random meeting durations
    meeting_durations = [
        (meeting_id, random.randint(10, 60))
        for meeting_id in meetings_df["meeting_id"].unique()
    ]
    durations_df = pd.DataFrame(
        meeting_durations, columns=["meeting_id", "duration_minutes"]
    )

    # Identify meetings including Florian
    meetings_with_flo = meetings_df[meetings_df["person_name"] == "Florian"][
        "meeting_id"
    ].unique()

    # Increase duration for meetings with Florian
    for _, row in durations_df.iterrows():
        if row["meeting_id"] in meetings_with_flo:
            row["duration_minutes"] += random.randint(50, 55)

    # Merge participant and duration data
    merged_df = meetings_df.merge(durations_df, on="meeting_id")
    return merged_df
