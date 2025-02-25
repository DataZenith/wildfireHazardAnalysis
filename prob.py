import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, precision_recall_curve, auc, roc_curve, roc_auc_score, confusion_matrix, recall_score
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




# Calculate the random baseline precision (same as positive class proportion)
random_precision = np.mean(y)
overestimate = 1 - max(precision_model)

max_precision_idx = np.argmax(precision_model)
best_threshold = thresh[max_precision_idx]

y_pred = (X >= best_threshold).astype(int)

# Compute confusion matrix
tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()
precision_at_best_threshold = precision_score(y, y_pred)
recall_at_best_threshold = recall_score(y, y_pred)


print(f'Overestimate : {overestimate}')
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(recall_model, precision_model, marker='.', label=f'Model PR AUC: {pr_auc_model:.2f}')
plt.plot(recall_rand, precision_rand, linestyle='--', label=f'Random PR AUC: {pr_auc_rand:.2f}', color='orange')

plt.axhline(y=random_precision, color='r', linestyle='--', label=f'Random Baseline: {random_precision:.2f}')
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve: Model vs. Random")
plt.legend()
plt.grid()
plt.show()

print(f'Random AUC:{pr_auc_rand}')
print(f'Probability AUC:{pr_auc_model}')
print(f"Best Threshold: {best_threshold}")
print(f"Precision at Best Threshold: {precision_at_best_threshold}")
print(f"Recall at Best Threshold: {recall_at_best_threshold}")

print(f"Confusion Matrix:\nTP={tp}, FP={fp}, TN={tn}, FN={fn}")

#-----------------
#histogram plots
#-----------------


df_fire = df[df["FIre_flag"] == 1]["burn_prob1"]  # Subset where fire occurred
df_no_fire = df[df["FIre_flag"] == 0]["burn_prob1"]  # Subset where no fire occurred

# Create the boxplot
plt.figure(figsize=(8, 6))
plt.boxplot([df_fire, df_no_fire], labels=["Fire Occurred", "No Fire"], patch_artist=False)

# Formatting
plt.ylabel("Probability")
plt.title("Boxplot Comparison: Fire vs No Fire Probabilities")
plt.grid(True)

# Show plot
plt.show()

# Show plot
plt.show()


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

#----------------------
#percentile comparison
#----------------------

# Example user input for the 40th and 90th percentiles
# For Variable 1:
var1_40 = percentile_40  # 40th percentile
var1_90 = percentile_90  # 90th percentile

# For Variable 2:
var2_40 = 0.001911  # 40th percentile
var2_90 = 0.137872 # 90th percentile

# Prepare data for each variable in the format expected by bxp
box_data = [
    {
        'label': 'Full Data',
        'whislo': var1_40,                  # Lower whisker (40th percentile)
        'q1': var1_40,                      # Lower quartile (set equal to the 40th percentile)
        'med': (var1_40 + var1_90) / 2,       # Median (here using the midpoint between 40th and 90th)
        'q3': var1_90,                      # Upper quartile (set equal to the 90th percentile)
        'whishi': var1_90,                  # Upper whisker (90th percentile)
        'fliers': []                        # No outliers to display
    },
    {
        'label': 'WUI Subset',
        'whislo': var2_40,
        'q1': var2_40,
        'med': (var2_40 + var2_90) / 2,
        'q3': var2_90,
        'whishi': var2_90,
        'fliers': []
    }
]

# Create the box and whisker plot using bxp
fig, ax = plt.subplots()
ax.bxp(box_data, showfliers=False)

# Add labels and title
ax.set_ylabel('Percentiles')
ax.set_title('Percentile Comparison')
plt.grid(True)

plt.show()


