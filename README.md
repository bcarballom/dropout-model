# Early Prediction of University Dropout Using XGBoost and Pre-Enrollment Data

This repository contains the code, model, and example data structure for the study titled:

**"Predicting Student Dropout from Day One: An XGBoost-Based Early Warning System Using Pre-Enrollment Data"**

## Overview

This project presents a machine learning pipeline for predicting the risk of university dropout using only information available at the time of student enrollment. The model was developed using XGBoost and trained on data from a public Mexican university, including socio-demographic, academic, and perceptual variables.

The repository follows the CRISP-DM methodology, and includes all necessary code to:
- Prepare and normalize data
- Train and evaluate various models
- Tune the XGBoost classifier
- Apply the trained model to new student cohorts
- Generate publication-ready figures

> **Note**: Due to privacy constraints, the full dataset cannot be shared. However, we include data templates and clear instructions to reproduce the process with similar data.

---

## Project Structure

```bash
student-dropout-prediction/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── 2024_example_input.csv            # Sample data (Anonymous)
│   ├── dropout_status.xslx            	  # Sample data (Anonymous)
│   ├── program_change_map.xslx           # Sample data (Anonymous)
│   ├── area_code_location_map.xslx       # Real data from Mexico
│   └── README.md                         # Explanation of input variables
│
├── notebooks/
│   ├── 1_prepare_dataframe.ipynb
│   ├── 2_normalize_variables.ipynb
│   ├── 3_create_variables.ipynb
│   ├── 4_model_comparison.ipynb
│   ├── 5_compare_logreg_rf.ipynb
│   ├── 6_compare_rf_xgb.ipynb
│   ├── 7_train_xgboost_model.ipynb
│   ├── 8_model_application.ipynb
│   ├── 9_visualizations.ipynb
│   └── README.md
│
├── model/
│   └── xgboost_model.joblib              # Trained model (bundle)
│
└── src/
    ├── predict.py
    └── preprocessing.py
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/student-dropout-prediction.git
cd student-dropout-prediction
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Use

### Prepare your input data

1. Ensure your input file matches the structure of data/2024_example_input.csv. If working with a new cohort (e.g., 2025), follow the same column format.
2. To clean and transform the raw input file, open and run python src/preprocessing.py --input data/2024_example_input.csv --output data/preprocessed.csv

This script will:
- Clean and format the data
- Apply LADA mapping and program grouping
- Normalize selected variables
- Create composite features and flags

### Use the Trained Model for Predictions 

- Open and run python src/predict.py --input data/preprocessed.csv --model models/xgboost_model_f1op.joblib --output results/predictions.csv

The trained model should be a `.joblib` file containing a dictionary with the following keys:
- 'model': trained XGBoost model
- 'features': list of selected features
- 'threshold': optimal decision threshold
- 'scaler': fitted scaler used in preprocessing

---

## Data

You must provide your own student dataset. See `data/README.md` for a list of required variables and formats.

---

## Notebooks

The notebooks/ folder contains all the exploratory, training, and evaluation notebooks used throughout the model development process, including data preparation, model comparison, final training, prediction, and visualization.

---

## Ethical & Usage Statement

- This repository shares **only example data**.
- No student-identifiable information is included.
- The use of this model should follow ethical guidelines regarding data governance, fairness, and non-discrimination.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## Authors

- Blanca Carballo-Mendívil (Lead author)
- Alejandro Arellano-González
- Nidia Josefina Ríos Vázquez
- María del Pilar Lizardi Duarte

---

## Citation

If you use this repository in your research, please cite the corresponding article (once published).

---

## Contact

For questions or collaborations, please contact:
**blanca.carballo19052@potros.itson.edu.mx**
