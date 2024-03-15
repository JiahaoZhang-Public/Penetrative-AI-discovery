import mne
import matplotlib.pyplot as plt
# 读取EDF文件
file_path = "E:\Penetrative ai\Penetrative-AI-discovery\Dataset\Physionet\sleep-edf-database-expanded-1.0.0\sleep-edf-database-expanded-1.0.0\sleep-cassette\SC4001E0-PSG.edf"
raw = mne.io.read_raw_edf(file_path, preload=True)

# 查看文件内容
print(raw.info)

# 访问原始数据
data, times = raw[:, :]

# 例如，打印前10个数据点
print(data[:, :10])
raw.plot()
plt.show()