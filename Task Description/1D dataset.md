# 1. Task Description
Find a one-dimensional time series dataset to expand the exploration of ChatGPT's potential in comprehending digitized sensor signals.

# 2. Dataset Characteristics
To evaluate large models' ability to detect anomalies based on their understanding of the physical world, the dataset should exhibit the following characteristics:
1. **Labeled Data**: Essential for facilitating the calculation of accuracy and other performance metrics, the dataset must contain labeled anomalies.
2. **Real-World Physical Quantities**: Data should represent physical quantities (e.g., temperature, pressure, electrical consumption, vibration levels) that mirror real-world conditions, enabling the model to apply its embedded world knowledge for anomaly detection.
3. **Temporal or Spatial Context**: Incorporating temporal or spatial context aids large models in understanding the dynamics of physical processes, making it easier to spot deviations from normal patterns.
4. **Diverse Anomaly Types**: The dataset should feature various types of anomalies (e.g., point anomalies, contextual anomalies, collective anomalies) to test the model's generalization capabilities across different anomaly detection tasks.
5. **Complexity and Noise**: A dataset with complexity and noise presents a challenge for the model's ability to differentiate between normal variability and true anomalies.
6. **Cross-Domain Applicability**: Datasets from different domains (e.g., healthcare, industrial monitoring, cybersecurity) can be used to assess the model's adaptability and performance in various fields.

# 3. Potential Datasets
## 3.1. [Numenta Anomaly Benchmark (NAB)](https://github.com/numenta/NAB)
### 3.1.1 Description
For further details, visit: https://github.com/numenta/NAB/blob/master/data/README.md
### 3.1.2 Problem
This dataset presents very rare positive cases, posing a challenge for anomaly analysis.

## 3.2. [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
### Possible Dataset

## 3.3. [Yahoo Labs Benchmark for Time Series Anomaly Detection](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)
### [S5 - A Labeled Anomaly Detection Dataset](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)
#### Description
This dataset is partly synthetic (simulated) and partly based on real traffic to Yahoo services. It includes timestamps, characters, and anomaly labels (1 for positive). The real part of the dataset consists of time series data for various Yahoo services metrics.

## 3.4. [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
### 3.4.1 Description
This dataset includes:
   1. Time
   2. Amount
   3. Class (label: 1 for fraud, positive cases; 0 for other, negative cases)
   4. Other columns are PCA components, from v1 to v28.
### 3.4.2 Problems
1. **Imbalance of Positive and Negative Data**: The dataset is highly unbalanced, with 492 frauds out of 284,807 transactions. The positive class (frauds) accounts for only 0.172% of all transactions, which is a significant issue.
2. **Indistinguishable Source of Funds**: The dataset does not allow for the distinction of the source of money, complicating anomaly detection due to unknown data distribution.

## 3.5 Environment Monitoring Datasets
Characteristics of these datasets are straightforward, with predefined standards for anomalies.
### 3.5.1 [Air Quality Dataset](https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database)
#### Description
Released in April 2022 (5th edition), with measurements mostly ranging from 2010 to 2019. The dataset covers a broad time interval, offering only ten years of data points for each location.

## 3.6 [PhysioNet](https://physionet.org/)
### Research Resource for Complex Physiologic Signals
(Not yet explored)
