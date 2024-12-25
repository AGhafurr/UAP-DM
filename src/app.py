import streamlit as st

pg = st.navigation([
    st.Page("MainPage.py", title="Main Page"),
    st.Page("Klasifikasi_fnn.py", title="Klasifikasi Tabular with FNN"),
    st.Page("Klasifikasi_tabnet.py", title="Klasifikasi Tabular with Tabnet"),
])

pg.run()