'''
Author: Jiahao Zhang
Date: 2024/3/14
Description:Extracting sleep stage labels from annotations
'''

import os
import mne
import pandas as pd


def extract_metadata(file_path):
    # Load the EDF file
    raw = mne.io.read_raw_edf(file_path, preload=False)

    # Extract subject number and night number from the file name
    file_name = os.path.basename(file_path)
    subject_number = file_name[3:5]
    night_number = file_name[5:6]

    # Get the metadata
    file_info = {
        "File name": file_name,
        "Subject number": subject_number,
        "Night number": night_number,
        "Number of channels": len(raw.ch_names),
        "Channel names": ", ".join(raw.ch_names),
        "Sampling frequency (Hz)": raw.info['sfreq'],
        "Start time": raw.info['meas_date'],
        "Duration (seconds)": raw.n_times / raw.info['sfreq']
    }

    # Read annotations directly using mne.read_annotations()
    annotations = mne.read_annotations(file_path)

    # Extract annotation information
    annotation_info = []
    for idx in range(len(annotations)):
        onset = annotations.onset[idx]
        duration = annotations.duration[idx]
        description = annotations.description[idx]
        annotation_info.append({
            "Onset (seconds)": onset,
            "Duration (seconds)": duration,
            "Description": description
        })

    file_info["Number of annotations"] = len(annotations)
    file_info["Annotations"] = annotation_info

    return file_info

# Provide the path to the folder containing the Hypnogram.edf files
folder_path = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette"

# Get a list of all *Hypnogram.edf files in the folder
hypnogram_files = [file for file in os.listdir(folder_path) if file.endswith("Hypnogram.edf")]
metadata_list =[]
# Process each Hypnogram.edf file and extract metadata
for file_name in hypnogram_files:
    file_path = os.path.join(folder_path, file_name)
    metadata = extract_metadata(file_path)
    metadata_list.append(metadata)
    print(f"Metadata for {file_name}:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
    print("---")

df = pd.DataFrame(metadata_list)

# Save the DataFrame to a CSV file
output_file = "E:\Penetrative ai\Penetrative-AI-discovery\TestResult\Sleep-edf\labels\hypnogram_metadata.csv"
df.to_csv(output_file, index=False)

print(f"Metadata saved to {output_file}")

