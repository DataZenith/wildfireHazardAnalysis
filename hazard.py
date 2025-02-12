import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('D:/fire_data/final_analysis/scrub_data.csv')



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

print(f"Class 0 (No Fire): {percent_0:.2f}%")
print(f"Class 1 (Fire): {percent_1:.2f}%")
print(f"Percent Extreme: {perc_ex:.2f}%")
print(f"Percent Moderate: {perc_mod:.2f}%")
print(f"Percent Low: {perc_low:.2f}%")


# Define number of years (21-year period)
risk_groups = ["extreme", "moderate", "low"]

# Compute raw relative risk (fires per unit of land)
relative_risk = {
    group: df[df[group] == 1]["FIre_flag"].sum() / df[group].sum() for group in risk_groups
}

# Compute the overestimate hazard based on relative risk: 1 - relative risk (multiplied by 100 to get a percentage)
overestimate_hazard = {
    group: 100 * (1 - relative_risk[group]) for group in risk_groups
}

# Create a figure with two subplots (side by side)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot 1: Historical Relative Fire Risk per Risk Group (as in the original top right chart)
axes[0].bar(relative_risk.keys(), relative_risk.values(), color=['red', 'purple', 'brown'])
axes[0].set_xlabel("Risk Group")
axes[0].set_ylabel("Fires / Risk Area")
axes[0].set_title("Long Run Historical Fires Per Risk Group ")

# Plot 2: Overestimate of Hazard based on Relative Risk (1 - Relative Risk)
axes[1].bar(overestimate_hazard.keys(), overestimate_hazard.values(), color=['gray', 'black', 'brown'])
axes[1].set_xlabel("Risk Group")
axes[1].set_ylabel("Overestimate (%)")
axes[1].set_title("Long Run Hazard Overestimate Percentage")
# Adjusting y-limit if needed; adjust these values based on your data context.
axes[1].set_ylim(72, 100)

# Ensure layout does not overlap
plt.tight_layout()
plt.show()