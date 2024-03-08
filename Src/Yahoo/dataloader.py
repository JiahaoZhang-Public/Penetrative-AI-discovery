import pandas as pd
import os
import re


class DataLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.data_files = self.find_matching_files()
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
                data = pd.read_csv(file_path, header=None, names=['timestamp', 'value', 'is_anomaly'])
                data['is_anomaly'] = data['is_anomaly'].astype(int)  # 确保异常标记为整型
                data['file'] = os.path.basename(file_path)  # 添加文件名作为一列，以便于识别
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

