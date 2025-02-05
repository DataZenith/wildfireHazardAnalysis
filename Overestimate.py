import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc, roc_curve, confusion_matrix



#load data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "prob_fire.csv")
df = pd.read_csv(csv_path, index_col=0)

#seperate the variables
x = df['Burn_probability']  # Model's predicted probabilities
y = df['Fire_occurance']  # binary repsons for fire present or not


# Compute Precision-Recall Curve
precision, recall, thresholds = precision_recall_curve(y, x)

# 1. Best Threshold: Equal Balance Between Precision & Recall
best_index_equal = np.argmin(np.abs(precision - recall))
best_threshold_equal = thresholds[best_index_equal]


# 2. Best Threshold: Highest F1-Score (Balanced Performance)
f1_scores = 2 * (precision * recall) / (precision + recall)
best_index_f1 = np.argmax(f1_scores)
best_threshold_f1 = thresholds[best_index_f1]


# Choose the threshold to apply (Pick one)
selected_threshold = best_threshold_equal  # Change to best_threshold_precision or best_threshold_f1 if needed

# Apply the chosen threshold to classify predictions
y_pred = (x >= selected_threshold).astype(int)

# Compute Confusion Matrix Values
tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()

# Compute Overprediction Rate
overprediction_rate = fp / (tp + fp) if (tp + fp) > 0 else 0

# Print results
print(f"Best Threshold (Equal Precision & Recall): {best_threshold_equal:.3f}")
print(f"Best Threshold (Highest F1-Score): {best_threshold_f1:.3f}")
print(f"Selected Threshold: {selected_threshold:.3f}")
print(f"Overprediction Rate at Selected Threshold: {overprediction_rate:.2%}")