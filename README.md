# Wildfire Hazard Risk Analysis

This repository contains the code and documentation used to analyze wildfire hazard risk datasets provided by the Wildfire Hazard Risk Proof of Concept (POC) at Oregon State. The analysis focuses on classifying burn areas, evaluating the distribution of burn probability estimates across fire and non-fire zones, and quantifying the percentage overestimate of predicted burn probabilities.

## Repository Overview

Due to file size limitations, the actual raw datasets are not stored in this repository. Instead, links to the original and transformed data sources are provided below. The repository contains all the code (scripts and notebooks) used to process, analyze, and visualize the data, along with documentation that explains the methodology in accessible terms.

## Data Sources

1. **Transformed Data**  
   - **Description:**  
     This dataset represents the cleaned and transformed version of the raw data, and serves as input for the analysis.  
   - **Access Link:**  
     [Transformed Data (ZIP)](https://drive.google.com/file/d/1ZfwCwuKY_bJ-gGvi1U3fAXznWS4qTicP/view?usp=sharing)

2. **Oregon State Wildfire Hazard Data**  
   - **Description:**  
     This primary dataset is provided by Oregon State and was used to build the wildfire hazard model.  
   - **Download Link:**  
     [OS Wildfire Hazard Data (ZIP)](https://oe.oregonexplorer.info/externalcontent/wildfire/data/SB80_Public_Data.zip)  
   - **Path to Final Burn Probabilities:**  
     After downloading, navigate through:  
     `SB80PublicData >> FireModelingData >> FireModeling_FuelscapeData.gdb >> BurnProbability`

3. **Historical Fire Data**  
   - **Description:**  
     This dataset contains historical fire events, which were used to validate and compare with the model outcomes.  This dataset contains recorded wildfire events from **2000 to 2021** and was used to validate the model’s predictive accuracy. The dataset includes only fire events where **acres burned exceeded 247**, ensuring that only significant fire occurrences were considered. To maintain the focus on naturally occurring and uncontrolled wildfire events, **prescribed burns and resource management fires were excluded** from the analysis. 
     
   - **Download Link:**  
     [Historical Fire Data](https://oregonstate.box.com/s/wllct446dgf76fcj1fc2x17vtbm0t14g)

> **Note:** The burn probability data and historical fire records were obtained via the POC at Oregon State. For further information or verification, please contact **OSUwildfirerisk@oregonstate.edu**.

## Code and Analysis Description

The code in this repository is organized to support reproducibility and transparency. It specifically performs the following analyses:

- **Classification of Burn Areas:**
- **File:** `prec_rec_auc.py`  
  The code identifies and categorizes regions based on burn data, distinguishing between areas that have experienced fire and those that have not.

- **Analysis of Probability Distributions:**
- **File:** `histogram_compare.py`  
  It evaluates and compares the distribution of predicted burn probabilities across fire-affected and non-fire zones.

- **Calculation of Overestimate Percentage:**
- **File:** `Overestimate.py`   
  The analysis computes the percentage overestimate in predicted burn probabilities relative to the actual burn data, providing insights into model performance.

### Programs Used

- **QGIS:**  
  QGIS, a free and open-source geographic information system, was used for spatial data analysis and visualization.  
  Download QGIS from [qgis.org](https://qgis.org/en/site/).



