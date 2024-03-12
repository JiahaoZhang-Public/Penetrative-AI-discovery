import pandas as pd

class CreditCardFraudDataLoader:
    def __init__(self, csv_file):
        """
        creditcard.csv:
            columns:['Time','V1',...,'V28','Amount','Class']
            we only need Time,Amount,Class
            According to the dataset description,V1-28 refer to the PCA components.
        :param csv_file:
        """
        self.data = pd.read_csv(csv_file)

    def get_data(self):
        """Return all loaded datasets."""
        return self.data

    def get_test_data(self, test_size=0.3, random_state=42):
        # Divide the data into fraud and normal transactions.
        frauds = self.data[self.data['Class'] == 1]
        normal = self.data[self.data['Class'] == 0]

        # Sample the fraud and normal transactions to get the test set.
        frauds_test = frauds.sample(frac=test_size, random_state=random_state)
        normal_test_size = int(len(frauds_test) * (1 - test_size) / test_size)  # Calculate the number of normal transactions to get the desired ratio.
        normal_test = normal.sample(n=normal_test_size, random_state=random_state)

        # Combine fraud and normal transactions to form the test set.
        test_data = pd.concat([frauds_test, normal_test])

        # Shuffle the test set.
        test_data = test_data.sample(frac=1, random_state=random_state).reset_index(drop=True)

        self.testdata = test_data
        return test_data

    def load_data_as_tuples(self, data_subset):
        # Sort the data subset by 'Time' column.
        sorted_data = data_subset.sort_values(by='Time')

        # Convert the sorted data into a list of tuples (Time, Amount).
        data_as_tuples = list(sorted_data[['Time', 'Amount']].itertuples(index=False, name=None))

        return data_as_tuples


