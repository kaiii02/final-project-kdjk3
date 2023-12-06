import streamlit as st
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

#Title
st.title("Analisis Trafik Jaringan dan Visualisasi Line Chart dan Bar Chart")

st.header("Final Project Komunikasi Data dan Jaringan Komputer")
st.subheader("Kelompok 7")

st.text("Nisaul Husna           2210511055")
st.text("Ika Kusuma Wardani     2210511058")
st.text("Muhammad Rizky Aulia   2210511060")
st.text("Yusuf Martinus Arief   2210511081")

data = pd.read_csv("./CICDS_Wednesday.csv")

data['Timestamp'] = pd.to_datetime(data['Timestamp'])

#st.dataframe(data)

st.subheader("Dataset CICDS_Wednesday.csv")
safe = data[data['Label'] == 'BENIGN']
attacked = data[data['Label'] != 'BENIGN']
#print(attacked)

a = len(safe)
b = len(attacked)
st.text("Dari sumber dataset Wednesday diketahui terdapat")
st.text(str(a) + " komunikasi yang aman dan " + str(b) + " komunikasi yang tidak aman")

st.subheader("Data Komunikasi yang Terdapat Serangan")
st.dataframe(attacked)

#most_port = attacked['Source Port'].value_counts().idxmax()

#most_suffer = attacked['Destination Port'].value_counts().idxmax()

# VISUALISASI LINE CHART
attacks_per_hour = attacked.groupby(attacked['Timestamp'].dt.strftime('%H:%M'))['Flow ID'].count()
max = attacks_per_hour.max()
time = attacks_per_hour.idxmax()

plt.figure(figsize=(10, 6))
attacks_per_hour.plot(kind='line', marker='o', color='#A52A2A')
plt.title('Tren Serangan')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Aktivitas')
#plt.show()

st.subheader("Line Chart Tren Serangan per Waktu")
st.pyplot(plt)

st.text("Berikut disajikan tabel terurut mulai dari waktu terbanyak adanya serangan :")
st.subheader("Tabel Waktu dan Jumlah Serangan")
most_timestamp = attacked['Timestamp'].dt.strftime('%H:%M:%S').value_counts().reset_index()
most_timestamp.columns=['Waktu','Jumlah']
st.dataframe(most_timestamp)

most_timestamp = attacked['Timestamp'].value_counts().idxmax()
waktu = most_timestamp.strftime("%H:%M:%S")
st.text("Dari tabel diatas terlihat bahwa serangan paling banyak terjadi pada pukul " + waktu)

# VISUALISASI BAR CHART
plt.figure(figsize=(10, 6))
sns.set_palette(["#450201"])
sns.countplot(x='Label', data=attacked).set_facecolor('#000000')
plt.title('Jumlah Tiap Jenis Serangan')
plt.xlabel('Jenis Serangan')
plt.ylabel('Jumlah')
#plt.show()

st.subheader("Bar Chart Jumlah Tiap Jenis Serangan")
st.pyplot(plt)

#print("Dari diagram batang di atas, didapatkan jumlah serangan terbanyak adalah serangan dengan jenis Dos Hulk yakni")

st.subheader("Tabel Jenis Serangan dan Jumlah Masing - masing Serangan")
most_label = attacked['Label'].value_counts().reset_index()
most_label.columns=['Jenis Serangan','Jumlah']
#print(most_label)

st.text("Berikut disajikan tabel terurut mulai dari jenis serangan terbanyak :")
st.table(most_label)
jumlah = attacked['Label'].value_counts().idxmax()
st.text("Dari tabel diatas terlihat bahwa jenis serangan yang paling banyak terdetect adalah " + jumlah)