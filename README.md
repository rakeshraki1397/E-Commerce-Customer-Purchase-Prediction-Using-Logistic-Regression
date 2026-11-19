# ShopSmart – E-Commerce Purchase Prediction (Logistic Regression)
Run order: open `Ecommerce_Purchase_Prediction.ipynb` (keep the dataset CSV beside it) -> Run All.
Requires: pandas, numpy, scikit-learn, matplotlib, seaborn, joblib, jupyter.

Files
- Ecommerce_Purchase_Prediction.ipynb  – full executed notebook (EDA, preprocessing, model, evaluation, new-customer predictions)
- Ecommerce_Purchase_Prediction_Report.docx / .pdf – written project report (8 pages)
- Ecommerce_Purchase_Prediction.html   – same notebook as a readable report
- Ecommerce_Purchase_Prediction_DataSet.csv – original data
- outputs/Ecommerce_Purchase_Cleaned.csv – cleaned data (imputed, outliers capped)
- outputs/model_metrics.csv, feature_coefficients.csv, new_customer_predictions.csv
- outputs/logistic_regression_pipeline.joblib – trained preprocessing + model pipeline
- outputs/plots/ – all charts (PNG)

Results (20% hold-out): Accuracy 0.705, Precision 0.728, Recall 0.869, F1 0.792, ROC-AUC 0.741
