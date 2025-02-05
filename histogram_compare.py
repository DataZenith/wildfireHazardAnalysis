import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#from sklearn.metrics import precision_recall_curve, auc, roc_curve



#load data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "prob_fire.csv")
df = pd.read_csv(csv_path, index_col=0)

#burn probability
burn_prob_fire = df[df['Fire_occurance'] == 1]['Burn_probability']
burn_prob_no_fire = df[df['Fire_occurance'] == 0]['Burn_probability']

# Plot histogram of burn probabilities for fire and no fire
plt.figure(figsize=(8, 6))
plt.hist(burn_prob_fire, bins=50, alpha=0.5, color='red', label='Fire Occurred (1)', density=True)
plt.hist(burn_prob_no_fire, bins=50, alpha=0.5, color='blue', label='No Fire (0)', density=True)

# Labels and Title
plt.xlabel("Burn Probability")
plt.ylabel("Density")
plt.title("Histogram of Burn Probabilities: Fire vs. No Fire")
plt.legend()
plt.grid()
plt.show()

