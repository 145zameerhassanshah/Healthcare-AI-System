from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    confusion_matrix,
    roc_auc_score,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = PROJECT_ROOT / "reports" / "figures"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def plot_confusion_matrix(y_test, y_pred):

    matrix = confusion_matrix(
        y_test,
        y_pred,
    )

    plt.figure(figsize=(7, 5))

    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=[
            "No Early Readmission",
            "Early Readmission",
        ],
        yticklabels=[
            "No Early Readmission",
            "Early Readmission",
        ],
    )

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "confusion_matrix.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


def plot_roc_curve(y_test, y_probability):

    auc = roc_auc_score(
        y_test,
        y_probability,
    )

    plt.figure(figsize=(7, 5))

    RocCurveDisplay.from_predictions(
        y_test,
        y_probability,
    )

    plt.title(
        f"ROC Curve (AUC = {auc:.3f})"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "roc_curve.png",
        dpi=150,
        bbox_inches="tight",
    )

    plt.close()


def main():

    print(
        "Evaluation visualization module created."
    )

    print(
        f"Output directory: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()