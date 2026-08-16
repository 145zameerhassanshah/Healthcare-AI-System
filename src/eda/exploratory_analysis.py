from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "diabetic_data.csv"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "reports"
    / "figures"
)


def load_data():
    """Load the raw healthcare dataset."""

    df = pd.read_csv(DATA_PATH)

    # Dataset-specific missing marker.
    df = df.replace("?", np.nan)

    # Binary target:
    # 1 = readmitted within 30 days
    # 0 = otherwise
    df["early_readmission"] = (
        df["readmitted"] == "<30"
    ).astype(int)

    return df


def save_plot(filename):
    """Save the current matplotlib figure."""

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


def plot_target_distribution(df):
    """Visualize target-class distribution."""

    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=df,
        x="early_readmission",
    )

    plt.title("Early Readmission Distribution")
    plt.xlabel("Early Readmission")
    plt.ylabel("Number of Encounters")

    save_plot("target_distribution.png")


def plot_age_distribution(df):
    """Visualize patient age groups."""

    plt.figure(figsize=(10, 5))

    sns.countplot(
        data=df,
        x="age",
        order=sorted(df["age"].dropna().unique()),
    )

    plt.title("Patient Age Distribution")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Encounters")

    plt.xticks(rotation=45)

    save_plot("age_distribution.png")


def plot_hospital_stay(df):
    """Visualize length of hospital stay."""

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="time_in_hospital",
        bins=14,
        kde=True,
    )

    plt.title("Time in Hospital Distribution")
    plt.xlabel("Days in Hospital")
    plt.ylabel("Number of Encounters")

    save_plot("hospital_stay_distribution.png")


def plot_medications(df):
    """Visualize medication counts."""

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="num_medications",
        bins=30,
        kde=True,
    )

    plt.title("Number of Medications Distribution")
    plt.xlabel("Number of Medications")
    plt.ylabel("Number of Encounters")

    save_plot("medication_distribution.png")


def plot_lab_procedures(df):
    """Visualize laboratory procedure counts."""

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="num_lab_procedures",
        bins=30,
        kde=True,
    )

    plt.title("Laboratory Procedures Distribution")
    plt.xlabel("Number of Lab Procedures")
    plt.ylabel("Number of Encounters")

    save_plot("lab_procedures_distribution.png")


def plot_readmission_by_age(df):
    """Compare early readmission across age groups."""

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="age",
        y="early_readmission",
        estimator=np.mean,
        errorbar=None,
    )

    plt.title(
        "Early Readmission Rate by Age Group"
    )

    plt.xlabel("Age Group")
    plt.ylabel("Early Readmission Rate")

    plt.xticks(rotation=45)

    save_plot("readmission_by_age.png")


def plot_correlation(df):
    """Visualize correlations among numerical variables."""

    numerical_columns = [
        "time_in_hospital",
        "num_lab_procedures",
        "num_procedures",
        "num_medications",
        "number_outpatient",
        "number_emergency",
        "number_inpatient",
        "number_diagnoses",
        "early_readmission",
    ]

    correlation = df[
        numerical_columns
    ].corr()

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
    )

    plt.title(
        "Correlation Matrix of Numerical Features"
    )

    save_plot("correlation_heatmap.png")


def main():

    print("\n--- STARTING EDA ---")

    df = load_data()

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\n--- TARGET DISTRIBUTION ---")
    print(
        df["early_readmission"]
        .value_counts()
    )

    print("\n--- NUMERICAL SUMMARY ---")

    numerical_columns = df.select_dtypes(
        include=["number"]
    ).columns

    print(
        df[numerical_columns]
        .describe()
        .round(2)
    )

    print("\n--- GENERATING VISUALIZATIONS ---")

    plot_target_distribution(df)
    print("✓ Target distribution")

    plot_age_distribution(df)
    print("✓ Age distribution")

    plot_hospital_stay(df)
    print("✓ Hospital stay distribution")

    plot_medications(df)
    print("✓ Medication distribution")

    plot_lab_procedures(df)
    print("✓ Laboratory procedure distribution")

    plot_readmission_by_age(df)
    print("✓ Readmission rate by age")

    plot_correlation(df)
    print("✓ Correlation heatmap")

    print(
        f"\nFigures saved to: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()