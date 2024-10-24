import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import phik


#---------------------------------#
# Page layout
# Page expands to full width
st.set_page_config(page_title='Student Performance Factors', layout='wide')
#---------------------------------#
def app():
    data = pd.read_csv('StudentPerformanceFactors.csv')
    df = data.copy()

    # Visualisasi Faktor yang Memengaruhi Seseorang Memperoleh Hasil Ujian
    st.title('Faktor yang Memengaruhi Seseorang Memperoleh Hasil Ujian')
    faktor = df.phik_matrix(interval_cols=['Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores', 'Physical_Activity', 'Exam_Score'])
    fig1, ax1 = plt.subplots()
    sns.heatmap(faktor, ax=ax1)
    st.write(fig1)

    # Visualisasi persentase jarak tempuh yang dilalui siswa dari rumah menuju sekolah
    st.title('Banyaknya Siswa dengan Variasi Jarak dari Rumah Menuju Sekolah')
    jarak = df[['Distance_from_Home', 'Exam_Score']].groupby(['Distance_from_Home']).count().rename(columns={'Exam_Score': 'Total Siswa'})
    fig2, ax2 = plt.subplots()
    jarak['Total Siswa'].plot(kind='pie', autopct='%.2f%%',ax=ax2)
    st.write(fig2)

    # Visualisasi Hubungan Tingkat Motivasi Belajar terhadap `Exam_Score`
    st.title('Hubungan Tingkat Motivasi Belajar terhadap Hasil Ujian')
    motivation = df[['Motivation_Level', 'Exam_Score']].groupby(['Motivation_Level']).mean()
    fig3, ax3 = plt.subplots()
    motivation['Exam_Score'].plot(kind='pie', autopct='%.2f%%',ax=ax3)
    st.write(fig3)

    # Visualisasi persentase Peran Orang Tua dalam Memengaruhi Pembelajaran Siswa
    st.title('Peran Orang Tua dalam Memengaruhi Pembelajaran Siswa')
    parent = df[['Parental_Involvement', 'Exam_Score']].groupby(['Parental_Involvement']).mean()
    fig4 ,ax4 = plt.subplots()
    parent['Exam_Score'].plot(kind='pie', autopct='%.2f%%',ax=ax4)
    st.write(fig4)

