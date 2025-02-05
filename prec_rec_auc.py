import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc, roc_curve


np.random.seed(43)

#load data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "prob_fire.csv")
df = pd.read_csv(csv_path, index_col=0)



# Generate a new random column for comparison
df['Random_Values'] = np.random.rand(len(df))


# Calculate dataset balance
count_0 = (df['Fire_occurance'] == 0).sum()
count_1 = (df['Fire_occurance'] == 1).sum()
total = len(df)
percent_0 = (count_0 / total) * 100
percent_1 = (count_1 / total) * 100

# Display results
print(f"Class 0 (No Fire): {percent_0:.2f}%")
print(f"Class 1 (Fire): {percent_1:.2f}%")

x = df['Burn_probability']  # Model's predicted probabilities
y = df['Fire_occurance']  # binary repsons for fire present or not
z = df['Random_Values'] #randomly generated numbers to simulate probaiblities


# Compute Precision-Recall curve for the model
precision_model, recall_model, _ = precision_recall_curve(y, x)
pr_auc_model = auc(recall_model, precision_model)

# Compute Precision-Recall curve for random predictions
precision_rand, recall_rand, _ = precision_recall_curve(y, z)
pr_auc_rand = auc(recall_rand, precision_rand)

# Compute random performance baseline (proportion of positive samples)
random_baseline = y.mean()

# Print AUC values
print(f"Model Precision-Recall AUC: {pr_auc_model:.2f}")
print(f"Random Precision-Recall AUC: {pr_auc_rand:.2f}")

# Plot Precision-Recall Curve: Model vs. Random
plt.figure(figsize=(8, 6))
plt.plot(recall_model, precision_model, marker='.', label=f'Model PR AUC: {pr_auc_model:.2f}', color='blue')
plt.plot(recall_rand, precision_rand, linestyle='--', label=f'Random PR AUC: {pr_auc_rand:.2f}', color='orange')
plt.axhline(y=random_baseline, color='r', linestyle='--', label=f'Random Baseline: {random_baseline:.2f}')

# Labels and Title
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve: Model vs. Random")
plt.legend()
plt.grid()
plt.show()






