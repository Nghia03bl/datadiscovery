import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
background_image = 'data-discovery-tools.png'

st.title('Khám phá dữ liệu')

st.header('Tải lên bộ dữ liệu')
uploaded_file = st.file_uploader("Chọn 1 file .csv", type=(['csv']))

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header('Hiển thị data')
    st.dataframe(df)

    st.header('Mô tả')
    st.table(df.describe())

    st.header('Show variables\' information')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.header('Trực quan hóa từng biến')
    for col in list(df.columns):
        fig, ax = plt.subplots()
        ax.hist(df[col], bins=20)
        plt.xlabel(col)
        plt.ylabel('Quantity')
        st.pyplot(fig)

    st.header('Hiển thị mối tương quan giữa các biến')
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(method='pearson'), ax=ax, vmax=1,square=True, annot=True, cmap='Reds')
    st.write(fig)

    depend_var = st.radio('Chọn biến phụ thuộc', df.columns)

    st.header('Hiển thị quan hệ giữ các biến')
    for col in list(df.columns):
        if col != depend_var:
            fig, ax = plt.subplots()
            ax.scatter(x=df[col], y=df[depend_var])
            plt.xlabel(col)
            plt.ylabel(depend_var)
            st.pyplot(fig)
