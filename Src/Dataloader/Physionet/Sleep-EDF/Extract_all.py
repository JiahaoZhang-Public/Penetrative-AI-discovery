"""
Author: Jiahao Zhang
Date: 2024/3/14
Description:Extracting from the whole file with reduced datapoints:
"""
import mne
import numpy as np


def extract_info_reduced(psg_file, hypnogram_file, reduction_factor):
    # Load PSG and hypnogram files
    raw = mne.io.read_raw_edf(psg_file, preload=True)
    annotations = mne.read_annotations(hypnogram_file)

    # Resample the data to reduce datapoints
    new_sfreq = raw.info['sfreq'] // reduction_factor
    raw.resample(new_sfreq)

    # Extract relevant information
    subject_info = f"Subject: {raw.info['subject_info']}"
    recording_info = f"Recording duration: {raw.n_times / new_sfreq} seconds, Channels: {', '.join(raw.ch_names)}"

    # Extract sleep stage durations
    sleep_stages = ['W', 'R', '1', '2', '3', '4']
    stage_durations = {}
    for stage in sleep_stages:
        duration = len(annotations[annotations.description == stage]) * 30 // reduction_factor
        stage_durations[stage] = duration
    sleep_stage_info = f"Sleep stage durations: {stage_durations}"

    # Combine the extracted information into a single string
    text_info = f"{subject_info}\n{recording_info}\n{sleep_stage_info}"

    return text_info
if __name__ == '__main__':
    # example for usage:
    psg_file = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette\SC4001E0-PSG.edf"
    hypnogram_file = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette\SC4001EC-Hypnogram.edf"
    # Method 1: Extracting from the whole file with reduced datapoints
    reduced_info = extract_info_reduced(psg_file, hypnogram_file, reduction_factor=10)
    print(reduced_info)
