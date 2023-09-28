import pandas as pd
import zipfile
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from bs4 import BeautifulSoup

# Load datasets
dataset_paths = ["202301-bluebikes-tripdata.csv", "202302-bluebikes-tripdata.csv", "202303-bluebikes-tripdata.csv"]
all_data = pd.concat([pd.read_csv(path) for path in dataset_paths])

# Extract hour from the starttime for further analysis
all_data['hour'] = pd.to_datetime(all_data['starttime']).dt.hour

# Visualization of Most Popular Stations and Busiest Times
plt.figure(figsize=(15, 5))

# Most Popular Start Stations
plt.subplot(1, 2, 1)
popular_stations = all_data['start station name'].value_counts().head(5)
popular_stations.plot(kind='bar', color='skyblue')
plt.title('Top 5 Most Popular Start Stations')
plt.ylabel('Number of Trips')
plt.xlabel('Station Name')
plt.xticks(rotation=45, ha='right')

# Number of Trips by Hour of the Day
plt.subplot(1, 2, 2)
hourly_trips = all_data['hour'].value_counts().sort_index()
hourly_trips.plot(kind='line', marker='o', color='tomato')
plt.title('Number of Trips by Hour of the Day')
plt.ylabel('Number of Trips')
plt.xlabel('Hour of the Day')
plt.grid(True, axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()

plt.show()

# Regression Model for Predicting Trip Duration
label_encoders = {}
for column in ['start station name', 'end station name', 'usertype']:
    le = LabelEncoder()
    all_data[column] = le.fit_transform(all_data[column])
    label_encoders[column] = le

features = ['start station name', 'end station name', 'usertype', 'hour']
X = all_data[features]
y = all_data['tripduration']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}, R2 Score: {r2}")

# Clustering Stations based on their Usage Patterns
station_counts = all_data['start station name'].value_counts().reset_index()
station_counts.columns = ['station_id', 'trip_counts']

scaler = MinMaxScaler()
station_counts_scaled = scaler.fit_transform(station_counts[['trip_counts']])
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
station_counts['cluster'] = kmeans.fit_predict(station_counts_scaled)

# Visualization of Clusters
plt.figure(figsize=(12,6))
colors = ['red', 'blue', 'green', 'yellow']
for i in range(4):
    plt.scatter(station_counts[station_counts['cluster'] == i]['station_id'], 
                station_counts[station_counts['cluster'] == i]['trip_counts'], 
                s = 50, c = colors[i], label = f'Cluster {i+1}', alpha=0.7)
plt.title('Clusters of Stations by Number of Trips')
plt.xlabel('Station ID')
plt.ylabel('Number of Trips')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


