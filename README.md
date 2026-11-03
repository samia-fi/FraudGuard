# FraudGuard

## AI-Powered Fraud Detection SaaS Platform

### 1. About the Project

FraudGuard is a SaaS platform designed to detect and prevent fraudulent financial transactions in real time using Machine Learning and configurable business rules.

The project is developed as part of an academic project at ENSAM Casablanca.

### 2. Main Features

* Real-time transaction scoring.
* Merchant authentication using API Keys.
* Configurable business rules.
* Machine Learning-based fraud detection.
* Transaction review and analyst decisions.
* Signed webhooks and notifications.
* Dashboard with fraud detection metrics.
* Multi-tenant architecture.

### 3. Technologies

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Scikit-learn
* Redis
* Docker

### 4. Dataset

* Source: OpenML
* Dataset name: creditcard
* OpenML ID: 1597
* Number of transactions: 284,807
* Number of features: 29
* Target column: Class

Target values:

* 0: Legitimate transaction
* 1: Fraudulent transaction

**Dataset note:** The downloaded OpenML dataset contains V1–V28, Amount and Class. It does not contain the Time column mentioned in the project specification. This difference must be considered during the next development stages.

### 5. Data Preparation

The data preparation stage includes:

* Loading the original dataset.
* Checking missing values and target labels.
* Grouping identical feature rows.
* Performing a stratified grouped Train/Test split.
* Saving the split indices for reproducibility.

Run the script from the project root:

```bash
python src/fraudguard_ai/data_preparation.py
```

The split uses:

* 80% Training data.
* 20% Testing data.
* Random state: 42.
* StratifiedGroupKFold.

### 6. Train/Test Results

| Description             | Training | Testing |
| ----------------------- | -------: | ------: |
| Transactions            |  227,845 |  56,962 |
| Fraudulent transactions |      393 |      99 |
| Fraud rate              |  0.1725% | 0.1738% |

The dataset is highly imbalanced.

### 7. Installation

Clone the repository:

```bash
git clone https://github.com/samia-fi/FraudGuard.git
cd FraudGuard
```

Install Git LFS:

```bash
git lfs install
git lfs pull
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 8. Project Structure

```text
FraudGuard/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── data/
│   ├── raw/
│   │   └── creditcard.csv
│   └── processed/
│       └── train_test_indices.npz
├── src/
│   └── fraudguard_ai/
│       ├── __init__.py
│       └── data_preparation.py
├── tests/
├── models/
├── notebooks/
├── reports/
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md
```

### 9. Team

* Backend & API
* Machine Learning
* Frontend & Dashboard

### 10. Project Status

Currently under development.

Current completed stage in this repository: Dataset analysis and data preparation.

The original dataset is tracked using Git LFS. Team members should install Git LFS and download the dataset before running the preparation script.
