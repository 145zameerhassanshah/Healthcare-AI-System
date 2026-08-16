from pathlib import Path
import joblib

from compare_models import (
    load_data,
    build_preprocessor,
    DROP_COLUMNS,
)

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "early_readmission_model.joblib"
)


def main():

    print("\n--- LOADING DATA ---")

    df = load_data()

    X = df.drop(
        columns=[
            column
            for column in [
                *DROP_COLUMNS,
                "early_readmission",
            ]
            if column in df.columns
        ]
    )

    y = df["early_readmission"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = Pipeline(
        steps=[
            (
                "preprocessor",
                build_preprocessor(X_train),
            ),
            (
                "model",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=42,
                ),
            ),
        ]
    )

    print("\n--- TRAINING FINAL MODEL ---")

    model.fit(X_train, y_train)

    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        model,
        MODEL_PATH,
    )

    print("\n--- MODEL SAVED ---")
    print(f"Path: {MODEL_PATH}")
    print("Format: Joblib")
    print("Model: Logistic Regression")
    print("Pipeline includes preprocessing + model")


if __name__ == "__main__":
    main()