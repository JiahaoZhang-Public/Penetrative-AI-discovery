'''
Author:Jiahao Zhang
Date； 2024/3/12
'''

import pandas as pd
from sklearn.model_selection import train_test_split


class CreditCardFraudDataLoader:
    def __init__(self, csv_file, test_size=0.3, random_state=42):
        """
        Initializes the DataLoader and splits the dataset into training and testing sets.

        :param csv_file: The file path to the credit card CSV dataset.
        :param test_size: The proportion of the dataset to include in the test split.
        :param random_state: The seed used by the random number generator.
        """
        data = pd.read_csv(csv_file)
        self.train_data, self.test_data = train_test_split(data, test_size=test_size, random_state=random_state,
                                                           stratify=data['Class'])

    def get_train_data(self):
        """Returns the training dataset."""
        return self.train_data

    def get_test_data(self, test_size=0.3, random_state=42, testset_size=100):
        """
        Splits the data into fraud and normal transactions and returns a test set
        of specified size with a proportional amount of fraud and normal transactions.

        :param test_size: Proportion of the fraud transactions to include in the test set.
        :param random_state: The seed used by the random number generator for reproducibility.
        :param testset_size: Total size of the test set to return.
        :return: A DataFrame containing the test data.
        """
        # Divide the data into fraud and normal transactions.
        frauds = self.test_data[self.test_data['Class'] == 1]
        normal = self.test_data[self.test_data['Class'] == 0]

        # Calculate the number of fraud and normal transactions to include in the test set.
        fraud_set_size = int(testset_size * test_size)
        normal_set_size = testset_size - fraud_set_size  # Ensure the total size matches the testset_size

        # Sample the fraud and normal transactions to get the test set.
        frauds_test = frauds.sample(n=fraud_set_size, random_state=random_state)
        normal_test = normal.sample(n=normal_set_size, random_state=random_state)

        # Combine fraud and normal transactions to form the test set.
        test_data = pd.concat([frauds_test, normal_test])

        # Shuffle the test set.
        test_data = test_data.sample(frac=1, random_state=random_state).reset_index(drop=True)
        return test_data

    def select_few_shot_examples(self, num_examples_per_class=10):
        """
        Selects few-shot examples from the training set only.

        :param num_examples_per_class: The number of examples to select per class.
        :return: A string containing few-shot examples descriptions.
        """
        fraudulent_examples = self.train_data[self.train_data['Class'] == 1].sample(n=num_examples_per_class)
        normal_examples = self.train_data[self.train_data['Class'] == 0].sample(n=num_examples_per_class)

        few_shot_examples_data = pd.concat([fraudulent_examples, normal_examples])
        few_shot_examples_data = self.sort_and_normalize(few_shot_examples_data)

        few_shot_examples = self.generate_textual_descriptions(few_shot_examples_data, include_class=True)
        return few_shot_examples

    def sort_and_normalize(self, data_subset):
        """
        Sorts the data subset by 'Time' and normalizes the 'Amount' column.

        :param data_subset: The subset of data to process.
        :return: The processed data subset.
        """
        sorted_data = data_subset.sort_values(by='Time')
        sorted_data['Amount_Normalized'] = (sorted_data['Amount'] - sorted_data['Amount'].min()) / (
                    sorted_data['Amount'].max() - sorted_data['Amount'].min())
        return sorted_data

    def generate_textual_descriptions(self, data_subset, include_class=False):
        """
        Generates textual descriptions for transactions in the data subset.

        :param data_subset: The subset of data to generate descriptions for.
        :param include_class: Whether to include the transaction class in the description.
        :return:  textual descriptions
        """
        descriptions = []
        for _, row in data_subset.iterrows():
            description = f"Transaction at time {row['Time']} has amount {row['Amount']}, with a normalized amount of {row['Amount_Normalized']}"
            if include_class:
                class_desc = "Fraudulent" if row['Class'] == 1 else "Normal"
                description += f" - {class_desc}"
            descriptions.append(description)
        return "\n".join(descriptions)


# Example usage
if __name__ == '__main__':
    loader = CreditCardFraudDataLoader('E:\Penetrative ai\Penetrative-AI-discovery\Dataset\CreditCard\creditcard.csv')
    few_shot_examples = loader.select_few_shot_examples()
    print(few_shot_examples)