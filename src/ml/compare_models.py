from pathlib import Path
import time

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "diabetic_data.csv"
)


DROP_COLUMNS = [
    "encounter_id",
    "patient_nbr",
    "weight",
    "max_glu_serum",
    "A1Cresult",
    "readmitted",
    "examide",
    "citoglipton",
]


def load_data():

    df = pd.read_csv(DATA_PATH)

    df = df.replace("?", pd.NA)

    df["early_readmission"] = (
        df["readmitted"] == "<30"
    ).astype(int)

    return df


def build_preprocessor(X):

    numerical_features = (
        X.select_dtypes(include=["number"])
        .columns
        .tolist()
    )

    categorical_features = (
        X.select_dtypes(
            include=["object", "string", "category"]
        )
        .columns
        .tolist()
    )

    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(
                    strategy="most_frequent"
                ),
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
            ),
        ]
    )

    return ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_features,
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features,
            ),
        ]
    )


def evaluate_model(name, model, X_train, X_test, y_train, y_test):

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                build_preprocessor(X_train),
            ),
            (
                "model",
                model,
            ),
        ]
    )

    start = time.time()

    pipeline.fit(
        X_train,
        y_train,
    )

    training_time = time.time() - start

    predictions = pipeline.predict(
        X_test
    )

    probabilities = pipeline.predict_proba(
        X_test
    )[:, 1]

    return {
        "Model": name,
        "Accuracy": accuracy_score(
            y_test,
            predictions,
        ),
        "Precision": precision_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "Recall": recall_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "F1": f1_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "ROC-AUC": roc_auc_score(
            y_test,
            probabilities,
        ),
        "Training Time (sec)": training_time,
    }


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

    print(
        f"Rows: {len(df)}"
    )

    print(
        f"Features: {X.shape[1]}"
    )

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y,
        )
    )

    models = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),

        "Decision Tree":
            DecisionTreeClassifier(
                max_depth=10,
                min_samples_leaf=10,
                class_weight="balanced",
                random_state=42,
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=100,
                max_depth=12,
                min_samples_leaf=5,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1,
            ),
    }

    results = []

    print("\n--- MODEL COMPARISON ---")

    for name, model in models.items():

        print(
            f"\nTraining {name}..."
        )

        result = evaluate_model(
            name,
            model,
            X_train,
            X_test,
            y_train,
            y_test,
        )

        results.append(result)

        print(
            f"Accuracy: {result['Accuracy']:.4f}"
        )

        print(
            f"Precision: {result['Precision']:.4f}"
        )

        print(
            f"Recall: {result['Recall']:.4f}"
        )

        print(
            f"F1: {result['F1']:.4f}"
        )

        print(
            f"ROC-AUC: {result['ROC-AUC']:.4f}"
        )

    results_df = pd.DataFrame(results)

    results_df = results_df.sort_values(
        by="ROC-AUC",
        ascending=False,
    )

    output_path = (
        PROJECT_ROOT
        / "reports"
        / "model_comparison.csv"
    )

    results_df.to_csv(
        output_path,
        index=False,
    )

    print("\n--- FINAL COMPARISON ---")

    print(
        results_df.to_string(
            index=False
        )
    )

    print(
        f"\nResults saved to: {output_path}"
    )


if __name__ == "__main__":
    main()