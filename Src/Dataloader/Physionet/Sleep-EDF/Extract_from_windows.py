"""
Author: Jiahao Zhang
Date: 2024/3/14
Description:Extracting datapoints from a time window:
"""
import mne
import numpy as np

def extract_info_window(psg_file, hypnogram_file, start_time, end_time, downsample_factor=100):
    # Load PSG and hypnogram files
    raw = mne.io.read_raw_edf(psg_file, preload=True)
    annotations = mne.read_annotations(hypnogram_file)

    # Extract data from the specified time window
    sfreq = raw.info['sfreq']
    start_sample = int(start_time * sfreq)
    end_sample = int(end_time * sfreq)
    data_window = raw.get_data(start=start_sample, stop=end_sample)

    # Downsample the data
    downsampled_data = data_window[:, ::downsample_factor]

    # Create textual descriptions for each channel
    channel_info = []
    for i, ch_name in enumerate(raw.ch_names):
        channel_data = downsampled_data[i]
        data_str = ','.join([f"{val}" for val in channel_data])
        unit = raw.info['chs'][i]['unit']
        channel_info.append(f"{ch_name} ({unit}): [{data_str}]")

    # Extract sleep stages in the time window
    sleep_stages = ['W', 'R', '1', '2', '3', '4']
    stage_durations = {}
    for stage in sleep_stages:
        duration = len(annotations[(annotations.description == stage) & (annotations.onset >= start_time) & (annotations.onset < end_time)]) * 30
        stage_durations[stage] = duration
    sleep_stage_info = f"Sleep stages in the window: {stage_durations}"

    # Combine the extracted information into a single string
    timestamp_info = f"Timestamp: {start_time} - {end_time} seconds"
    channel_info_str = '\n'.join(channel_info)
    text_info = f"{timestamp_info}\n{channel_info_str}\n{sleep_stage_info}"

    return text_info

if __name__ == '__main__':
    # example for usage:
    psg_file = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette\SC4001E0-PSG.edf"
    hypnogram_file = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette\SC4001EC-Hypnogram.edf"
    # Extract data from a 5-second window starting at 1000 seconds
    start_time = 1000
    end_time = 1005
    window_info = extract_info_window(psg_file, hypnogram_file, start_time, end_time,downsample_factor=1000)
    print(window_info)