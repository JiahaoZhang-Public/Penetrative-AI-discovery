'''
Author:Jiahao Zhang
Date； 2024/3/12
'''

import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import configparser
import matplotlib.pyplot as plt  # Import for visualization

current_script_path = os.path.abspath(__file__)
rootpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_script_path))))

# Load Configs
config = configparser.ConfigParser()
config.read(os.path.join(rootpath, 'config.ini'))

# Get the configuration paths
test_result_dir = os.path.join(rootpath, config.get('CreditCard', 'test_result_path'))
test_examples_dir = os.path.join(rootpath, config.get('CreditCard', 'test_examples_path'))


def parse_anomalies(response):
    """
    Parses anomalies from LLM's response. Assumes anomaly times are listed on the line
    immediately following the line that starts with "List of Anomalous Transaction Times:".

    :param response: LLM response as a string.
    :return: List of anomalous transaction times as floats.
    """
    anomalies = []
    lines = response.split("\n")
    found_anomalies_line = False  # Flag to check if the next line contains anomalies
    for line in lines:
        if found_anomalies_line:
            # The line immediately after the identified line contains the anomalies
            times = [float(time.strip()) for time in line.split(",") if time.strip()]
            anomalies.extend(times)
            break  # Assuming only one list of anomalies exists, break after processing
        if line.startswith("List of Anomalous Transaction Times:"):
            found_anomalies_line = True  # The next line will contain the anomalies
    return anomalies


def calculate_metrics(test_examples_path, anomalies):
    """
    Calculates accuracy, precision, recall, and F1-score based on predicted anomalies and actual data.

    :param test_examples_path: Path to the CSV file containing test examples.
    :param anomalies: List of detected anomalous transaction times.
    :return: A dictionary containing accuracy, precision, recall, and F1-score.
    """
    test_data = pd.read_csv(test_examples_path)
    test_data['Predicted'] = test_data['Time'].apply(lambda x: 1 if x in anomalies else 0)

    accuracy = accuracy_score(test_data['Class'], test_data['Predicted'])
    precision = precision_score(test_data['Class'], test_data['Predicted'])
    recall = recall_score(test_data['Class'], test_data['Predicted'])
    f1 = f1_score(test_data['Class'], test_data['Predicted'])

    return {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1}


def main(test_result_dir, test_examples_dir, num_experiments):
    """
    Main function to calculate and visualize metrics of multiple experiments.
    """
    metrics = {'accuracy': [], 'precision': [], 'recall': [], 'f1': []}

    for experiment in range(num_experiments):
        test_result_path = os.path.join(test_result_dir, f"result_{experiment + 1}.txt")
        test_examples_path = os.path.join(test_examples_dir, f"test_examples_{experiment + 1}.csv")

        with open(test_result_path, 'r') as file:
            response = file.read()
        anomalies = parse_anomalies(response)

        experiment_metrics = calculate_metrics(test_examples_path, anomalies)
        for key in metrics:
            metrics[key].append(experiment_metrics[key])
        print(f"Experiment {experiment + 1} Metrics: {experiment_metrics}")

    # Calculate the average of each metric
    averages = {key: sum(values) / len(values) for key, values in metrics.items()}
    print(f"Average Metrics: {averages}")

    # Visualization
    plt.figure(figsize=(10, 6))
    for key in metrics:
        plt.plot(range(1, num_experiments + 1), metrics[key], marker='o', linestyle='-', label=key.capitalize())
    plt.title('Experiment Metrics')
    plt.xlabel('Experiment Number')
    plt.ylabel('Metrics Value')
    plt.xticks(range(1, num_experiments + 1))
    plt.grid(True)
    plt.legend()
    plt.savefig('accuracy.png')
    plt.show()



if __name__ == '__main__':
    num_experiments = 20
    main(test_result_dir, test_examples_dir, num_experiments)