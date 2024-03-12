import pandas as pd
import os
import re


class DataLoader:
    def __init__(self, folder_path, file_index=None):
        """
        Initialize the DataLoader with a folder path and optionally specify the index of the file to load.

        :param folder_path: The path to the folder containing the CSV files.
        :param file_index: The index of the file to load, based on the matching pattern. If None, all matching files are loaded.
        """
        self.folder_path = folder_path
        self.data_files = self.find_matching_files()

        # If a file_index is specified, only load the file at that index; otherwise, load all matching files.
        if file_index is not None and 0 <= file_index < len(self.data_files):
            self.data_files = [self.data_files[file_index]]

        self.data = self.load_data()

    def find_matching_files(self):
        """Traverse folder to find all files matching a specific pattern."""
        pattern = re.compile(r'real_(\d+).csv')
        matching_files = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if pattern.match(file):
                    matching_files.append(os.path.join(root, file))
        return matching_files

    def load_data(self):
        """Load all matching CSV files into a list of Pandas DataFrames."""
        data_list = []
        for file_path in self.data_files:
            try:
                data = pd.read_csv(file_path)
                data['file'] = os.path.basename(file_path)
                data_list.append(data)
            except Exception as e:
                print(f"Error loading file {file_path}: {e}")
        return data_list

    def get_data(self):
        """Return all loaded datasets."""
        return self.data

    def get_batch(self, batch_size, start_index=0, file_index=0):
        """Return a batch of data from a specific file, based on batch size, start index, and file index."""
        if file_index < len(self.data):
            return self.data[file_index][start_index:start_index + batch_size]
        else:
            return None

    def load_data_as_tuples(self):
        """Convert 'timestamp' and 'value' columns in each DataFrame into a list of tuples."""
        tuple_list = []
        for data_frame in self.data:
            tuples = list(zip(data_frame['timestamp'], data_frame['value']))
            tuple_list.extend(tuples)
        return tuple_list

