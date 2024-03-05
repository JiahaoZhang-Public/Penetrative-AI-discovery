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
The dataset  contains both real and synthetic data ,timestamp(continuous) and values with [labels](https://github.com/numenta/NAB/tree/master/labels) 
For further details, visit: https://github.com/numenta/NAB/blob/master/data/README.md
### 3.1.2 Problem
This dataset presents very rare positive cases, posing a challenge for anomaly analysis.

## 3.2. [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
### Possible Dataset

## 3.3. [Yahoo Labs Benchmark for Time Series Anomaly Detection](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)
### [S5 - A Labeled Anomaly Detection Dataset](https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70)
#### Description
This dataset is partly synthetic (simulated) and partly based on real traffic to Yahoo services. It includes timestamps, characters, and anomaly labels (1 for positive). The real part of the dataset consists of time series data for various Yahoo services metrics.


1. A1Benchmark/real_(int).csv
2. A2Benchmark/synthetic_(int).csv
3. A3Benchmark/A3Benchmark-TS(int).csv
4. A4Benchmark/A4Benchmark-TS(int).csv

A1Benchmark is based on the real production traffic to some of the Yahoo! properties.
The other 3 benchmarks are based on synthetic time-series. A2 and A3 Benchmarks include outliers,
while the A4Benchmark includes change-point anomalies. The bechmarks based on real-data have property
and geos removed. Fields in each data file are delimited with (",") characters.

The fields are:
    
    0 timestamp(with incresement of 1,represents 1 hour)
    1 value
    2 is_anomaly(boolean)
The is_anomaly field is a boolean indicating if the current value at a given timestamp is considered an anomaly.

Snippet:
   1,83,0
   2,605,0
   3,181,0
   4,37,0
   5,45,1

#### Problem:
The information in the A1Benchmark may be meaningless（since we do not know the physical meaning of the specific value） to LLMs and may be not useful to test the general literacy for LLMs.
   

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
### Descrpition:
### Options:
1. [Sleep Stages Detection](https://archive.physionet.org/physiobank/database/challenge/2018/)


# 4. Summary and Conclusion:
## 4.1 Classification of the dataset
1. Dataset with is_anomaly labels
These dataset are labeled (if anomaly or not),the amount of possitive data points(anomaly) are always fewer than the normal ones(without anomalies).
2. Dataset with physical meanings




# Notes:
