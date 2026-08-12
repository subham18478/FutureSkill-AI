import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "business_data.csv"


def load_data():
    return pd.read_csv(DATA_FILE)


def get_future_skills():
    df = load_data()
    return df["future_skill"].value_counts()


def get_declining_skills():
    df = load_data()
    return df[df["ai_impact"] == "Declining"]["current_skill"].value_counts()


def get_reskilling_roles():
    df = load_data()

    declining = df[df["ai_impact"] == "Declining"]

    return (
        declining.groupby("role")
        .size()
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    df = load_data()

    print("\nTotal records:", len(df))

    print("\nFuture Skills:")
    print(get_future_skills())

    print("\nDeclining Skills:")
    print(get_declining_skills())

    print("\nRoles requiring reskilling:")
    print(get_reskilling_roles())