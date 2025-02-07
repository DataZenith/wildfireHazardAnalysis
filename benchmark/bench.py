
import os 
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve, auc
import matplotlib.pyplot as plt

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file path
file_name = "forestfires.csv"  # Replace with your actual CSV file name
file_path = os.path.join(current_dir, file_name)

# Load the CSV
df = pd.read_csv(file_path)
df['fire'] = (df['area'] > 0).astype(int)

count_0 = (df['fire'] == 0).sum()
count_1 = (df['fire'] == 1).sum()
total = len(df)
percent_0 = (count_0 / total) * 100
percent_1 = (count_1 / total) * 100

# Display results
print(f"Class 0 (No Fire): {percent_0:.2f}%")
print(f"Class 1 (Fire): {percent_1:.2f}%")



def downsample_fire_data(df, fire_ratio):
    """
    Downsamples the dataset to ensure that 'fire' = 1 represents the specified percentage of total data.

    Parameters:
        df (pd.DataFrame): The input DataFrame with a 'fire' column.
        fire_ratio (float): The desired proportion of 'fire' = 1 in the final dataset (between 0 and 1).

    Returns:
        pd.DataFrame: The balanced dataset with the specified fire ratio.
    """

    # Count the number of fire = 1 and fire = 0 instances
    df_fire = df[df['fire'] == 1]
    df_no_fire = df[df['fire'] == 0]
    
    count_fire = len(df_fire)  # Total fire = 1
    count_no_fire = len(df_no_fire)  # Total fire = 0
    total_desired = int(len(df) * fire_ratio)  # Total desired fire = 1
    total_no_fire = int((total_desired / fire_ratio) - total_desired)  # Compute matching fire = 0 count

    # Ensure we don't sample more than available
    if count_fire > total_desired:
        df_fire = df_fire.sample(total_desired, random_state=42)
    if count_no_fire > total_no_fire:
        df_no_fire = df_no_fire.sample(total_no_fire, random_state=42)

    # Combine and shuffle
    df_balanced = pd.concat([df_fire, df_no_fire]).sample(frac=1, random_state=42).reset_index(drop=True)

    # Print results
    final_fire_count = df_balanced['fire'].sum()
    final_total = len(df_balanced)
    actual_ratio = final_fire_count / final_total

    print(f"Final 'fire' = 1 count: {final_fire_count}")
    print(f"Final 'fire' = 0 count: {final_total - final_fire_count}")
    print(f"Actual fire ratio: {actual_ratio:.4f} (Expected: {fire_ratio})")

    return df_balanced


df = downsample_fire_data(df, .2155)
selected_features = ['FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'fire']
df_subset = df[selected_features]

# Print summary statistics for the selected features
print("\nSummary Statistics:")
print(df_subset.describe())

# Define features (X) and target (y)
X = df_subset.drop(columns=['fire'])  # Drop the target variable
y = df_subset['fire']  # Target variable

# Standardize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Add intercept for statsmodels
X_sm = sm.add_constant(X_scaled)

# Fit logistic regression model
logit_model = sm.Logit(y, X_sm)
result = logit_model.fit()

# Print logistic regression summary
print("\nLogistic Regression Summary:")
print(result.summary())

# Get predicted probabilities from logistic regression
y_scores = result.predict(X_sm)

# Generate random probabilities for comparison
np.random.seed(42)  # Ensures reproducibility
y_random = np.random.rand(len(y))  # Random probabilities between 0 and 1

# Compute Precision-Recall curve for logistic regression
precision, recall, _ = precision_recall_curve(y, y_scores)
pr_auc = auc(recall, precision)

# Compute Precision-Recall curve for random predictions
precision_rand, recall_rand, _ = precision_recall_curve(y, y_random)
pr_auc_rand = auc(recall_rand, precision_rand)

# Compute baseline chance line (percentage of fire=1 in the dataset)
chance_level = np.mean(y)

# Plot Precision-Recall Curve
plt.figure(figsize=(8, 6))
plt.plot(recall, precision, label=f'Logistic PR AUC = {pr_auc:.4f}', color='blue')
plt.plot(recall_rand, precision_rand, label=f'Random PR AUC = {pr_auc_rand:.4f}', color='green', linestyle='dashed')
plt.axhline(y=chance_level, color='red', linestyle='dotted', label=f'Chance Level = {chance_level:.4f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve with Chance & Random Baselines')
plt.legend()
plt.grid()
plt.show()

# Print AUC scores
print(f'\nLogistic Regression PR AUC: {pr_auc:.4f}')
print(f'Random Predictions PR AUC: {pr_auc_rand:.4f}')
print(f'Chance Level Precision: {chance_level:.4f}')