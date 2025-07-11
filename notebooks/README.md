# Notebooks Overview

This folder contains the Jupyter notebooks used throughout the development, evaluation, and application of the student dropout prediction model. Each notebook corresponds to a specific phase of the machine learning pipeline.

## Contents

1. **1_prepare_dataframe.ipynb**  
   Loads and prepares the initial dataset for analysis. Filters variables, handles missing values, and defines the features used in training.

2. **2_normalize_variables.ipynb**  
   Applies standardization to the numerical features to ensure proper scaling prior to model training.

3. **3_create_variables.ipynb**  
   Generates new composite or derived variables from raw inputs. Includes aggregations and transformations relevant to dropout analysis.

4. **4_model_comparison.ipynb**  
   Conducts an exploratory comparison of several machine learning models to evaluate initial performance metrics.

5. **5_compare_logreg_rf.ipynb**  
   Specifically compares Logistic Regression and Random Forest classifiers using cross-validation.

6. **6_compare_rf_xgb.ipynb**  
   Focuses on comparing Random Forest with XGBoost using fine-tuned hyperparameters.

7. **7_final_xgboost_model.ipynb**  
   Trains the final XGBoost model, evaluates performance, selects optimal threshold by F1-score, and saves the model for deployment.

8. **8_model_application.ipynb**  
   Applies the trained model to new cohorts (2023 and 2024), generating predictions and risk scores.

9. **9_visualizations.ipynb**  
   Produces visual outputs used in the article, including confusion matrices, ROC curves, feature importance, and heatmaps by dimensions.

---

Each notebook is designed to be run sequentially, from data preparation to model interpretation and result reporting.
