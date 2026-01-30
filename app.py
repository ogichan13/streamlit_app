import streamlit as st
import pandas as pd

st.title('長野県統計データ確認アプリ')

df = pd.read_csv('nagano_prefecture.csv')