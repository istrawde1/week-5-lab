import plotly.express as px
import pandas as pd


# Exercise 1: Survival Patterns

df = pd.read_csv(
    "https://raw.githubusercontent.com/"
    "leontoddjohnson/datasets/main/data/titanic.csv"
)
df.columns = df.columns.str.lower().str.replace(" ", "_")


def survival_demographics():
    """Analyze Titanic survival rates by class, sex, and age group."""
    df["age_group"] = pd.cut(
        df["age"],
        bins=[
            float("-inf"),
            12,
            19,
            59,
            float("inf"),
        ],
        labels=["Child", "Teen", "Adult", "Senior"],
    )

    demographics = (
        df.groupby(
            ["pclass", "sex", "age_group"],
            observed=False,
        )
        .agg(
            n_passengers=("survived", "count"),
            n_survivors=("survived", "sum"),
            survival_rate=("survived", "mean"),
        )
        .reset_index()
        .sort_values(["pclass", "sex", "age_group"])
    )

    return demographics


def visualize_demographic():
    survival_demographics()
    plot_df = df.assign(pclass=df["pclass"].astype(str))
    fig = px.histogram(
        plot_df,
        x="age_group",
        y="survived",
        color="pclass",
        histfunc="avg",
        barmode="group",
        title="Survival Rate by Age Group and Passenger Class",
    )
    return fig


# Exercise 2: Family Size and Wealth


def family_groups():
    """Summarize ticket fares by family size and passenger class."""
    df["family_size"] = df["sibsp"] + df["parch"] + 1

    return (
        df.groupby(["family_size", "pclass"])
        .agg(
            n_passengers=("passengerid", "count"),
            avg_fare=("fare", "mean"),
            min_fare=("fare", "min"),
            max_fare=("fare", "max"),
        )
        .reset_index()
        .sort_values(["pclass", "family_size"])
    )


def last_names():
    """Count passengers by last name."""
    return (
        df["name"]
        .str.split(",", n=1)
        .str[0]
        .str.strip()
        .value_counts()
    )


def visualize_families():
    """Plot average fare by family size and passenger class."""
    family_data = family_groups().assign(
        pclass=lambda data: data["pclass"].astype(str)
    )
    fig = px.line(
        family_data,
        x="family_size",
        y="avg_fare",
        color="pclass",
        markers=True,
        title="Average Ticket Fare by Family Size and Passenger Class",
        labels={
            "family_size": "Family Size",
            "avg_fare": "Average Ticket Fare",
            "pclass": "Passenger Class",
        },
    )
    return fig


