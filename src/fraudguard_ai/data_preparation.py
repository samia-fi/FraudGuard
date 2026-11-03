from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold


def main():
    # Project paths
    project_root = Path(__file__).resolve().parents[2]
    raw_file = project_root / "data" / "raw" / "creditcard.csv"
    output_dir = project_root / "data" / "processed"
    output_file = output_dir / "train_test_indices.npz"

    # Load dataset
    if not raw_file.exists():
        raise FileNotFoundError(f"Dataset not found: {raw_file}")

    df = pd.read_csv(raw_file)

    # Basic validation
    if "Class" not in df.columns:
        raise ValueError("The dataset must contain a 'Class' column.")

    if df.isnull().sum().sum() > 0:
        raise ValueError("The dataset contains missing values.")

    X = df.drop(columns="Class")
    y = df["Class"]

    if set(y.unique()) != {0, 1}:
        raise ValueError("Class must contain both labels: 0 and 1.")

    # Group identical feature rows to avoid leakage
    groups = pd.MultiIndex.from_frame(X).factorize()[0]

    # Stratified grouped train/test split
    cv = StratifiedGroupKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    train_idx, test_idx = next(cv.split(X, y, groups))

    # Save indices
    output_dir.mkdir(parents=True, exist_ok=True)

    np.savez(
        output_file,
        train_idx=train_idx,
        test_idx=test_idx
    )

    # Display results
    print("Data preparation completed successfully!")
    print(f"Dataset shape: {df.shape}")
    print(f"Training samples: {len(train_idx)}")
    print(f"Testing samples: {len(test_idx)}")
    print(f"Training fraud cases: {int(y.iloc[train_idx].sum())}")
    print(f"Testing fraud cases: {int(y.iloc[test_idx].sum())}")
    print(f"Training fraud rate: {y.iloc[train_idx].mean() * 100:.4f}%")
    print(f"Testing fraud rate: {y.iloc[test_idx].mean() * 100:.4f}%")
    print(f"Saved indices to: {output_file}")


if __name__ == "__main__":
    main()
