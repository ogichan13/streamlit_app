import streamlit as st
import pandas as pd
import plotly.express as px 

st.title('長野県統計データ')

df = pd.read_csv('nagano_prefecture.csv')

with st.sidebar:
    
    st.write('以下の選択欄でデータを選択すると、表・グラフタブに選択したデータが表示されます。人口の差、性比の差、面積の差を確認することができます。')

    option2 = st.selectbox('表示したいデータを選択してください',
                           ['population_total','population_men','population_women','sex_ratio','area'])
    
df.set_index('city_name',inplace=True)

st.write('2015年、市のみの統計データです。人口性比（sex_ratio）は女性100人に対する男性の数を示しています。')

tab1, tab2, tab3 = st.tabs(['表・グラフ', '散布図', '数値'])

# 表・グラフタブ
with tab1:
    option1 = st.toggle("表を表示", value=True)
    if option1:
        st.dataframe(df, width=800)
    if option2 == 'population_total':
        st.write('総人口（単位：人）')
        st.bar_chart(df['population_total'])
    elif option2 == 'population_men':
        st.write('男性人口（単位：人）')
        st.bar_chart(df['population_men'])
    elif option2 == 'population_women':
        st.write('女性人口（単位：人）')
        st.bar_chart(df['population_women'])
    elif option2 == 'sex_ratio':
        st.write('人口性比（単位：人）')
        st.bar_chart(df['sex_ratio'])
    elif option2 == 'area':
        st.write('面積（単位：km^2）')
        st.bar_chart(df['area'])

# 散布図タブ
with tab2:

    st.write('散布図は総人口と面積の関係を示しています。人口密度に大きな差があることが読み取れます。')
    
    fig = px.scatter(
        df,
        x="area",
        y="population_total",
        hover_name=df.index,   # city_name（index）を表示
        labels={
            "area": "面積（km²）",
            "population_total": "総人口（人）"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

# 数値タブ
with tab3:
    items = {
        "総人口1位": "population_total",
        "男性人口1位": "population_men",
        "女性人口1位": "population_women",
        "人口性比1位": "sex_ratio",
        "面積1位": "area"
    }

    cols = st.columns(len(items))

    for col, (label, colname) in zip(cols, items.items()):
        r = df.loc[df[colname].idxmax()]

        #　人口の項目のみ小数点なし
        if colname in ["population_total", "population_men", "population_women"]:
            value_str = f"{int(r[colname]):,}"
        else:
            value_str = f"{r[colname]:.2f}"

        col.markdown(
            f"""
            <div style="font-size:22px;font-weight:700;">{label}</div>
            <div style="font-size:14px;color:#555;">{r.name}</div>
            <div style="font-size:32px;font-weight:700;">{value_str}</div>
            """,
            unsafe_allow_html=True
        )
