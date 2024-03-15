import mne
import matplotlib.pyplot as plt

def plot_edf_data(file_path, duration=30, n_channels=None):
    # Load the EDF file
    raw = mne.io.read_raw_edf(file_path, preload=True)

    # Get the sampling frequency
    sfreq = raw.info['sfreq']

    # Calculate the number of seconds to display
    n_seconds = min(duration, raw.n_times / sfreq)

    # Convert seconds to number of samples
    n_samples = int(n_seconds * sfreq)

    # Get the data for the specified duration
    data, times = raw[:, :n_samples]

    # Get the channel names
    ch_names = raw.ch_names

    # Select a subset of channels if specified
    if n_channels is not None:
        data = data[:n_channels]
        ch_names = ch_names[:n_channels]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the data for each channel
    for i, ch_data in enumerate(data):
        ax.plot(times, ch_data + i * 100, label=ch_names[i])

    # Set the title and labels
    ax.set_title('EDF Data')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')

    # Add a legend
    ax.legend(loc='upper right')

    # Display the plot
    plt.tight_layout()
    plt.show()


# Provide the path to your EDF file
file_path = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette\SC4001EC-Hypnogram.edf"

# Specify the duration in seconds and the number of channels to display (optional)
duration = 60  # Display the first 60 seconds of data
n_channels = 5  # Display the first 5 channels (set to None to display all channels)

# Plot the EDF data
plot_edf_data(file_path, duration, n_channels)
