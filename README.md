# Customer Churn Prediction — Greenweez (e-commerce)

> Le Wagon Data Analytics bootcamp (2026)

## Business question
Which customers are likely to buy again, and who should a retention campaign target?

## Data
Customer-level table from **Google BigQuery** (Greenweez, organic e-commerce retailer), with a binary target `re_purchase`.

## Approach
1. Feature preparation from the BigQuery table
2. **Logistic Regression** classifier predicting the probability of repurchase
3. Evaluation focused on business impact: confusion matrix, precision / recall trade-off
4. Segmentation of customers by predicted probability
5. Design of a targeted retention campaign

## Stack
Python · pandas · scikit-learn · Google BigQuery · Jupyter
