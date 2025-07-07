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
├── LICENSE
│
├── data/
│   ├── example_input.csv            # Template file (no real data)
│   └── README.md                    # Explanation of input variables
│
├── notebooks/
│   ├── 1_preparar_dataframe.ipynb
│   ├── 2_normalizacion_variables.ipynb
│   ├── 3_creacion_variables.ipynb
│   ├── 4_comparacion_logreg_rf.ipynb
│   ├── 5_comparacion_rf_xgb.ipynb
│   ├── 6_modelo_xgboost_final.ipynb
│   ├── 7_aplicacion_modelo.ipynb
│   └── 8_graficos.ipynb
│
├── models/
│   └── xgboost_model.pkl            # Trained model (serialized)
│
└── src/
    ├── train_model.py
    ├── predict.py
    ├── preprocessing.py
    └── visualization.py
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

### Train the model

1. Prepare your dataset with the same structure as `example_input.csv`.
2. Open and run `6_modelo_xgboost_final.ipynb` or use `src/train_model.py`.

### Apply model to new students

- Use `7_aplicacion_modelo.ipynb` or `src/predict.py`.

### Generate graphics

- Run `8_graficos.ipynb` or call visualization functions in `src/visualization.py`.

---

## Data

You must provide your own student dataset. See `data/README.md` for a list of required variables and formats.

---

## Ethical & Usage Statement

- This repository shares **only simulated data**.
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
