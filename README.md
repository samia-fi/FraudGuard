# FraudGuard – AI Fraud Detection

## 1. Project Description

FraudGuard is a fraud detection project designed to identify potentially fraudulent credit card transactions using Machine Learning.

This repository contains the dataset and the data preparation stage.

## 2. Dataset

* Source: OpenML
* Dataset name: creditcard
* OpenML ID: 1597
* Number of transactions: 284,807
* Number of features: 29
* Target column: Class

The target column contains:

* 0: Legitimate transaction
* 1: Fraudulent transaction

**Note:** The downloaded OpenML dataset contains V1–V28, Amount and Class. It does not contain the Time column mentioned in the project specification. This difference must be considered during the next development stages.

## 3. Project Structure

```text
FraudGuard22/
│
├── data/
│   ├── raw/
│   │   └── creditcard.csv
│   │
│   └── processed/
│       └── train_test_indices.npz
│
├── src/
│   └── fraudguard_ai/
│       ├── __init__.py
│       └── data_preparation.py
│
├── models/
├── notebooks/
├── reports/
│
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md
```

## 4. Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd FraudGuard22
```

Install Git LFS:

```bash
git lfs install
git lfs pull
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 5. Data Preparation

Run the following command from the project root:

```bash
python src/fraudguard_ai/data_preparation.py
```

The script:

* Loads the original dataset.
* Checks missing values and target labels.
* Groups identical feature rows.
* Performs a stratified grouped Train/Test split.
* Saves the indices in `data/processed/train_test_indices.npz`.

The split uses:

* 80% Training data
* 20% Testing data
* Random state: 42
* StratifiedGroupKFold

## 6. Train/Test Results

| Description             | Training | Testing |
| ----------------------- | -------: | ------: |
| Transactions            |  227,845 |  56,962 |
| Fraudulent transactions |      393 |      99 |
| Fraud rate              |  0.1725% | 0.1738% |

## 7. Important Notes

* The dataset is highly imbalanced.
* Original data is stored in `data/raw/`.
* Train/Test indices are stored in `data/processed/`.
* The original dataset is tracked using Git LFS.
* The split indices can be reused to ensure reproducibility.

## 8. Team Collaboration

All team members should install the dependencies and download the dataset using Git LFS before running the preparation script.

**Current stage:** Dataset analysis and data preparation.
