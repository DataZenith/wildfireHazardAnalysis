<div align="center">

# Under Fire: Rethinking Wildfire Predictions

<br><br>

**A Critical Analysis of Oregon State's Wildfire Hazard Model**

<br><br>

*Examining the probabilities and performance in forecasting wildfire occurrences*

<br><br><br><br>
---
<br><br>

**Curated by:** Jeremy Kauwe <br>
**Date:** 2/5/2025

<br><br>

</div>

<hr>

# 1. Executive Summary

In public policy, models are expected to provide reliable, evidence-based insights that inform critical decisions. They must be rigorously validated and demonstrate predictive performance well above trivial baselines. It is unacceptable for a model—especially one that influences resource allocation and public safety—to perform on par with a random number generator.

Our analysis of Oregon State's Wildfire Hazard Model reveals alarming shortcomings:
- **Inaccuracy in Probability Assignment:** The model fails to distinguish between fire and no-fire events.
- **Randomness Equivalence:** When benchmarked against a random number generator, the model's ability to classify fire occurrences is no better than chance.
- **Severe Risk Overestimation:** The model inflates wildfire risk by nearly 80%, potentially leading to misdirected policy and resource decisions.

These findings raise serious questions about the validity of the methods used in assessing the model's outputs. For a tool intended to guide public policy, the expectation is clear: models must deliver actionable, robust, and clearly superior predictions—not results that mimic random chance.

<hr>


# 2. Introduction

**Background:**  
Wildfire hazard assessment is a critical tool for land management, public policy, and disaster preparedness. These assessments rely on models that estimate the likelihood and potential impact of wildfires based on environmental conditions, historical data, and fire behavior simulations. A key component of these assessments is burn probability, which represents the estimated likelihood of a fire occurring in a given area. This probability is often combined with fire intensity predictions to produce a final hazard rating used in risk mitigation strategies. However, the modeling process used to esimate the 2025 Oregon Wildfire hazard map is not well documented, making it difficult to assess the validity of its outputs.

**Purpose:**  
This report evaluates the relationship between the model’s probability output and its ability to distinguish between large fire events and non-fire events.

**Scope:**  
This analysis focuses on probability model outputs for all of Oregon to determine whether the model meets the necessary standards for guiding public policy and wildfire risk management.


<hr>

# 3. Data and Methodology

## Data Sources  

The data used in this analysis comes from multiple sources, including model outputs from Oregon State University, historical wildfire occurrence records, and a transformed dataset created by combining these sources. These datasets were obtained through Oregon State’s Wildfire Hazard Risk **Point of Contact (POC)** and serve as the foundation for evaluating the burn probability component of the wildfire hazard model.

- **1) Transformed Data:**  
  This dataset is derived from a combination of **burn probability estimates** from the wildfire hazard model and **historical wildfire records**. Each row in the dataset represents a single **pixel** where these two datasets overlap. The dataset includes:  
  - **Burn Probability:** The probability of fire occurrence for that pixel, as assigned by the wildfire hazard model.  
  - **Fire Occurrence Flag:** A binary indicator (1 = fire occurred, 0 = no fire) derived from historical wildfire data.  
  - **Spatial Resolution:** Each pixel is spaced **500 feet apart** both vertically and horizontally, ensuring a uniform grid structure.

  The dataset consists of two columns:

    1. **Burn Probability**  
     - Represents the probability of a fire occurring in a given pixel, ranging from **0.000000** to **0.074283**.  
     - Uses a **grayscale gradient**, where black represents low probability and white represents high probability.  
     - **Descriptive Statistics:**
       - **Total Count**: 12,019,460 pixels
       - **Mean**: 0.00925
       - **Median (50%)**: 0.00621
       - **Standard Deviation**: 0.01021
       - **Min Value**: 0.000000
       - **25th Percentile**: 0.00108
       - **75th Percentile**: 0.01401
       - **Max Value**: 0.07428

         <br>

    2. **Fire Occurrence (Binary Indicator)**  
     - Indicates whether a fire historically occurred in that pixel (**2000–2021**).  
     - **0 (No Fire)**: 78.45% of pixels  
     - **1 (Fire Occurred)**: 21.55% of pixels  


  
- **2) Wildfire Hazard Model Data:**  
  This dataset, provided by Oregon State, was used to build the wildfire hazard model. The burn probability outputs are stored in a geodatabase and were extracted for analysis.  
  **Path to Burn Probabilities:**  
  `SB80PublicData >> FireModelingData >> FireModeling_FuelscapeData.gdb >> BurnProbability`

- **3) Historical Fire Data:**  
  This dataset contains recorded wildfire events from **2000 to 2021** and was used to validate the model’s predictive accuracy. The dataset includes only fire events where **acres burned exceeded 247**, ensuring that only significant fire occurrences were considered. To maintain the focus on naturally occurring and uncontrolled wildfire events, **prescribed burns and resource management fires were excluded** from the analysis.

A full list of dataset links and additional details can be found in the **[GitHub README](https://github.com/yourusername/wildfire-risk-analysis/blob/main/README.md)**. For further information or verification, inquiries can be directed to **OSUwildfirerisk@oregonstate.edu**.

  ## Wildfire Burn Probability Map  
  The chart represents probability values using a grayscale gradient, where lower probabilities are darker (black) and higher probabilities are lighter (white).

  ### Color Mapping:
  - **Black (0.000000 probability)**: Represents the lowest probability.
  - **White (0.072378 probability)**: Represents the highest probability.
  - **Gradient Transition**: Intermediate probabilities transition from black to white.

  ### Interpretation:
  - **Darker Regions (Near Black)**: Indicate areas with **low probability**.
  - **Lighter Regions (Near White)**: Indicate areas with **high probability**.
  - **Gradual Shading**: Helps visualize the probability distribution smoothly.

  ### Purpose:
  - The grayscale mapping **enhances visibility** of probability changes.
  - It provides a **clear, intuitive** representation without requiring numerical labels.


![Burn Probability Map](images/burn_prob.JPG)

## Burn Probability Overlaid with Historical Fire Data  
This map overlays the model’s burn probability layer with historical fire occurrences (2000-2021), highlighting areas where the model predicted fire risk versus actual fire events.  The gradient color is just to make it more visually appealing

![Burn Probability + Fire Overlay](images/burn_overlay.JPG)


## Data Preparation  

The data was processed using **QGIS**, an open-source geographic information system. A full guide to downloading and installing **QGIS** can be found in the **[GitHub README](https://github.com/yourusername/wildfire-risk-analysis/blob/main/README.md)**. The following steps were taken to compile the **Transformed Data** for analysis:  

1. **Loading the Data:**  
   - The **burn probability layer** from the wildfire hazard model was uploaded into QGIS.  
   - The **historical fire occurrence dataset** was also uploaded.  

2. **Ensuring Consistent Coordinate Reference System (CRS):**  
   - Both datasets were checked to confirm they used the same **Coordinate Reference System (CRS)** to ensure spatial accuracy.

3. **Creating a Grid of Points:**  
   - A grid of points was generated, with each point spaced **500 feet apart** both **vertically** and **horizontally** across Oregon.  
   - This ensured that the data was evenly sampled across the study area.

4. **Extracting Burn Probability and Fire Occurrence:**  
   - For each grid point, the corresponding **burn probability** value was captured from the model output.  
   - The historical fire dataset was overlaid, and a **binary fire occurrence flag** was assigned:  
     - `1` if a fire was recorded at that location.  
     - `0` if no fire was recorded.

5. **Handling Null Values:**  
   - Some fires extended beyond **Oregon's boundaries**, resulting in missing burn probability values.  
   - These **null values** were removed to ensure clean and complete data.

6. **Exporting the Final Dataset:**  
   - The cleaned grid layer was saved and exported as a **CSV file**.  
   - This CSV file, referred to as the **Transformed Data**, is available in the **ZIP file linked in the README**.  

This transformed dataset serves as the foundation for evaluating the **relationship between burn probability estimates and actual fire occurrences** in Oregon.


---
# **Methodology**

To evaluate how well the model predicts fire occurrences, we conducted several tests. These tests help determine whether the model provides meaningful predictions or if its results are no better than random guessing. Below, we explain these tests in simple terms and why they matter.

---
# **1. Evaluating Model Performance**

Predicting fire occurrences requires a balance between two key factors: **precision and recall**. Additionally, we use the **Precision-Recall Curve and its Area Under the Curve (PR-AUC)** to assess the model’s overall effectiveness.

### **1.1 Precision and Recall**
When predicting fire occurrences, we measure how well the model identifies fire-prone areas using two key metrics:

- **Precision (How many predicted fires were correct?)**  
  - If the model predicts **100 locations** where fire will occur and **60 of them actually had a fire**, the precision is **60%**.
  - **Higher precision** means fewer false alarms (incorrect fire predictions).

- **Recall (How many actual fires did the model catch?)**  
  - If there were **100 actual fire locations** and the model correctly identified **60 of them**, the recall is **60%**.
  - **Higher recall** means fewer missed fires.

These two measures often **trade off** against each other.  
- If the model is **too aggressive**, it catches **all** real fires but **creates many false alarms** (low precision, high recall).  
- If the model is **too cautious**, it avoids false alarms but **misses many real fires** (high precision, low recall).  

We need a **balance**, which leads us to the **Precision-Recall Curve**.

### **1.2 Precision-Recall Curve and AUC Calculation**
Since precision and recall change depending on the model’s confidence threshold, we plot a **Precision-Recall Curve** to analyze its performance across different thresholds.

- The model assigns a **probability score** (e.g., 0.02, 0.08, 0.15, etc.) to each location, estimating the likelihood of fire occurring.
- We **vary the threshold** (the cutoff point for deciding what counts as a "fire prediction") and calculate precision and recall at **each threshold**.
- These precision-recall points are **plotted on a graph**, forming the **Precision-Recall Curve**.
- The **AUC (Area Under the Curve)** is then calculated by measuring the total area beneath this curve, representing the **average performance** of the model across all confidence levels.

### **1.3 Interpreting PR-AUC and Industry Standards**
Since PR-AUC is particularly useful for **imbalanced datasets**, it is important to compare model performance to known industry standards:

#### **Industry Benchmarks**
- **0.2 – 0.4** → Slightly better than random guessing but still weak.
- **0.4 – 0.6** → Moderate predictive power; some meaningful patterns detected.
- **0.6 – 0.8** → Good performance; the model is effective in distinguishing fire-prone areas.
- **0.8 and above** → Strong predictive ability; highly reliable for decision-making.

#### **Baseline (Random Model)**
- A **random model** will have a PR-AUC equal to the proportion of fire occurrences in the dataset.  
- If **21.55% of the data represents fire occurrences**, a random classifier would achieve a PR-AUC of **0.2155**.
- If the model’s PR-AUC is **above 0.2155**, it is **better than random** and can help identify fire-prone areas.
- If it is **close to 0.2155**, it is **not useful** because it performs similarly to random guessing.
- If it is **below 0.2155**, the model is misleading and should not be used.

By comparing the model’s **actual PR-AUC to the baseline (0.2155),** we determine whether it provides **useful predictions** or just reflects the natural frequency of fire occurrences.

---

### **1.4 Why This Matters**
✅ **A high PR-AUC** means the model is **better than random guessing** and can help identify fire-prone areas.  
✅ **Understanding precision and recall** helps determine whether the model is prone to **false alarms or missed fires**.  
✅ **The PR-AUC score reflects the model’s overall ability** to distinguish fire-prone areas, rather than relying on a single threshold.  
✅ **Comparing to the baseline (random model)** ensures we are measuring true predictive power rather than overfitting.  
✅ **Industry benchmarks provide context** for interpreting whether the PR-AUC score is good enough for real-world applications.  

---

### **Why This Works Better:**
✅ **More structured** – The entire **model performance evaluation** is in **one place**.  
✅ **Logical flow** – **Concepts → Calculation → Interpretation → Why it Matters**  
✅ **Easier to digest** – The **"Why This Matters"** bullet points wrap up everything cleanly.  

---

Would you like any **further refinements** to formatting, such as bolded keywords or additional clarifications? 🚀



# **References**

Below are the sources used to support the methodology and evaluation of the model:

1. **Precision and Recall Definitions**  
   - Google Developers Machine Learning Crash Course:  
     [Classification: Accuracy, Precision, Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)

2. **Precision-Recall Curve and AUC Calculation**  
   - Scikit-learn documentation:  
     [Precision-Recall — scikit-learn documentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

3. **Industry Standards for PR-AUC in Imbalanced Datasets**  
   - Aporia Machine Learning Guide:  
     [Ultimate Guide to PR-AUC: Calculations, Uses, and Limitations](https://www.aporia.com/learn/ultimate-guide-to-precision-recall-auc-understanding-calculating-using-pr-auc-in-ml/)  
   - Deepchecks Blog:  
     [Understanding F1 Score, Accuracy, ROC-AUC & PR-AUC Metrics](https://www.deepchecks.com/f1-score-accuracy-roc-auc-and-pr-auc-metrics-for-models/)

4. **Overestimation Rate Calculation**  
   - Python Scikit-learn Guide:  
     [Compute the AUC of Precision-Recall Curve](https://sinyi-chou.github.io/python-sklearn-precision-recall/)

5. **Comparison to a Random Model**  
   - Arize AI Blog:  
     [What Is PR AUC?](https://arize.com/blog/what-is-pr-auc/)

6. **Visual Analysis Using Histograms**  
   - Medium Article on Precision-Recall Curves:  
     [Precision-Recall Curves](https://medium.com/@douglaspsteen/precision-recall-curves-d32e5b290248)

7. **Importance of Precision-Recall Curves in Imbalanced Datasets**  
   - Scikit-learn Documentation:  
     [Precision-Recall — scikit-learn documentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)


