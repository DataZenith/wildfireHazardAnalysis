import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc, roc_curve, roc_auc_score
#import seaborn as sns


path = #insert path to downloaded data herer
df = pd.read_csv(path)



print(df.describe())
count_0 = (df['FIre_flag'] == 0).sum()
count_1 = (df['FIre_flag'] == 1).sum()
ex_cnt =(df['extreme'] == 1).sum()
mod_cnt = (df['moderate'] == 1).sum()
low_cnt = (df['low'] == 1).sum()
total = len(df)
percent_0 = (count_0 / total) * 100
percent_1 = (count_1 / total) * 100
perc_ex = (ex_cnt / total) * 100
perc_mod = (mod_cnt / total)*100
perc_low = (low_cnt/total)*100
percentile_90 = np.percentile(df["hazard_1"], 90)
percentile_40 = np.percentile(df["hazard_1"], 40)

print(f"Class 0 (No Fire): {percent_0:.2f}%")
print(f"Class 1 (Fire): {percent_1:.2f}%")
print(f"Percent Extreme: {perc_ex:.2f}%")
print(f"Percent Moderate: {perc_mod:.2f}%")
print(f"Percent Low: {perc_low:.2f}%")
print(f"hazard 90th percentile : {percentile_90}")
print(f"hazard 40th percentile : {percentile_40}")



#--------------------------------------------
#--analyze burn probability as a classifier--
#--------------------------------------------

X = df['burn_prob1']
y = df['FIre_flag']
h = df['hazard_1']
z = np.random.rand(len(df))


# Compute Precision-Recall curve for Model
precision_model, recall_model, thresh = precision_recall_curve(y, X)
pr_auc_model = auc(recall_model, precision_model)
precision_model = precision_model[1:-1]
recall_model = recall_model[1:-1]

# Compute Precision-Recall curve for Random Predictions
precision_rand, recall_rand, _ = precision_recall_curve(y, z)
pr_auc_rand = auc(recall_rand, precision_rand)
precision_rand = precision_rand[1:-1]
recall_rand = recall_rand[1:-1]

# Compute Precision-Recall curve for Random Predictions
precision_haz, recall_haz, _ = precision_recall_curve(y, h)
pr_auc_haz = auc(recall_haz, precision_haz)
precision_haz = precision_haz[1:-1]
recall_haz = recall_haz[1:-1]



# Calculate the random baseline precision (same as positive class proportion)
random_precision = np.mean(y)
overestimate = 1 - max(precision_model)


print(f'Overestimate : {overestimate}')
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(recall_model, precision_model, marker='.', label=f'Model PR AUC: {pr_auc_model:.2f}')
plt.plot(recall_rand, precision_rand, linestyle='--', label=f'Random PR AUC: {pr_auc_rand:.2f}', color='orange')
plt.plot(recall_haz, precision_haz, linestyle='--', label=f'Hazard PR AUC: {pr_auc_rand:.2f}', color='blue')

plt.axhline(y=random_precision, color='r', linestyle='--', label=f'Random Baseline: {random_precision:.2f}')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve: Model vs. Random & Hazard")
plt.legend()
plt.grid()
plt.show()

#-----------------
#histogram plots
#-----------------


df_fire = df[df["FIre_flag"] == 1]["burn_prob1"]  # Subset where fire occurred
df_no_fire = df[df["FIre_flag"] == 0]["burn_prob1"]  # Subset where no fire occurred

# Plot histograms (No KDE in Matplotlib)
plt.figure(figsize=(8, 6))

plt.hist(df_fire, bins=30, color="red", alpha=0.5, density= True, label="Fire Occurred", edgecolor='black')
plt.hist(df_no_fire, bins=30, color="blue", alpha=0.5, density = True, label="No Fire", edgecolor='black')

# Labels and title
plt.xlabel("Probability")
plt.ylabel("Frequency")
plt.title("Overlayed Histogram of Probabilities (Fire vs. No Fire)")
plt.legend()
plt.grid()

# Show plot
plt.show()
