import pandas as pd

# Load your dataset (adjust the path if needed)
df = pd.read_csv('sensor-fault-detection.csv')

# Check the first few rows
print(df.head())
# Check shape (rows and columns)
print("Shape of dataset:", df.shape)

# Check data types and non-null counts
print("\nInfo:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())
import pandas as pd

df = pd.read_csv("sensor-fault-detection.csv", sep=None, engine='python')
print(df.head())
print(df.shape)

print(df.info())
print(df.describe())
#after loading the dataset, i inspected the structure using info() and describe().the datset
#contains 62,629 sensor readings each with a timestamp,sensor id and measured value. no missing values
#values range from 6.9 to 149.6. however since most readings fall around 24 with a standard deviation of 5.4
#the max value of 149.6 looks like a potential outlier,which may indicate sensor fault or an anomaly

#let us confirm if 149.6 is really an outlier
import matplotlib.pyplot as plt

#plt.figure(figsize=(10,5))
#plt.boxplot(df['Value'])
#plt.title('Sensor Value Distribution')
#plt.ylabel('Value')
#plt.show()

outlier = df[df['Value'] > 100]
print(outlier)
# Count of all outliers
print("Number of outliers:", len(outlier))

# Show unique timestamps of outliers
print("Unique timestamps of outlier readings:")
print(outlier['Timestamp'].unique())
# Remove outlier readings above 100
clean_df = df[df['Value'] <= 100]

print("Old shape:", df.shape)
print("New shape after cleaning:", clean_df.shape)

clean_df.info()
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values(by='Timestamp')
df['SensorId'].unique()
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(df['Timestamp'], df['Value'], color='blue', linewidth=1)
plt.title('Sensor Reading Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Sensor Value')
plt.grid(True)
plt.show()


