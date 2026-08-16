from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "diabetic_data.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    # Treat '?' as missing
    df = df.replace("?", pd.NA)

    missing_count = df.isna().sum()

    missing_percentage = (
        missing_count
        .div(len(df))
        .mul(100)
        .round(2)
    )

    report = pd.DataFrame(
        {
            "missing_count": missing_count,
            "missing_percentage": missing_percentage,
        }
    )

    report = report.sort_values(
        "missing_percentage",
        ascending=False,
    )

    print("\n--- MISSING DATA ANALYSIS ---")
    print(report[report["missing_count"] > 0])

    print("\n--- FEATURES WITH >50% MISSING ---")
    print(
        report[
            report["missing_percentage"] > 50
        ]
    )


if __name__ == "__main__":
    main()