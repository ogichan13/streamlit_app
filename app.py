import streamlit as st
import pandas as pd
import plotly.express as px 

st.title('長野県統計データ')

df = pd.read_csv('nagano_prefecture.csv')

with st.sidebar:
    population1 = st.multiselect('市名を選択してください（複数選択可）',
                                 df['city_name'].unique())
    
    option1 = st.selectbox('表示したいデータを選択してください',
                           ['population_total','population_men','population_women','sex_ratio','area','population_density'])
    
df.set_index('city_name',inplace=True)

st.write('2015年、市のみの統計データである。人口性比（sex_ratio）は女性100人に対する男性の数を示す。')

if option1 == 'population_total':
    st.write('総人口（単位：人）')
    st.bar_chart(df['population_total'])
elif option1 == 'population_men':
    st.write('男性人口（単位：人）')
    st.bar_chart(df['population_men'])
elif option1 == 'population_women':
    st.write('女性人口（単位：人）')
    st.bar_chart(df['population_women'])
elif option1 == 'sex_ratio':
    st.write('人口性比（単位：人）')
    st.bar_chart(df['sex_ratio'])
elif option1 == 'area':
    st.write('面積（単位：km^2）')
    st.bar_chart(df['area'])
