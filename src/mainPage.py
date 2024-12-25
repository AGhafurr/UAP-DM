import streamlit as st
import Klasifikasi_fnn

# Inisialisasi state untuk halaman
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Fungsi untuk mengganti halaman
def switch_page(page_name):
    st.session_state.current_page = page_name

# Render halaman berdasarkan state
if st.session_state.current_page == "classification":
    Klasifikasi_fnn.render(switch_page)  # Panggil halaman klasifikasi
else:
    # Halaman utama
    st.markdown("<h1 style='text-align: center;'>Smart Water Classification For Healthy Life</h1>", unsafe_allow_html=True)

    st.subheader("The Importance of Drinking Healthy Water")
    st.write("""
    Water is an essential resource for life. It makes up about 60% of the human body and is involved in every bodily function, 
    from digestion to temperature regulation. Consuming clean and healthy water is crucial for maintaining good health. 
    Impure or contaminated water can lead to a variety of health issues, such as dehydration, digestive problems, and even waterborne diseases.
    """)

    st.image("src/assets/air.jpeg")

    st.subheader("What Makes Water Healthy?")
    st.write("""
    Healthy water is clean, free from harmful pollutants, and safe for consumption. Here are the characteristics of healthy water:

    1. **Clear and Transparent**: Clean water should be free from visible impurities such as dirt, sand, or floating particles.
    2. **Odor-Free**: Healthy water should have no noticeable odors. A musty or chemical smell indicates contamination.
    3. **Low TDS (Total Dissolved Solids)**: Healthy water should have a low level of dissolved solids, ensuring it's free from harmful minerals or chemicals.
    4. **Free from Microorganisms**: Water should be free of harmful bacteria, viruses, and pathogens that can cause illness.
    """)

    st.markdown("<h4 style='text-align: center;'>For More Details, let's test the content of the water you consume!!!</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Try Smart Water Classification"):
            switch_page("classification")  # Pindah ke halaman klasifikasi

    with col2:
        if st.button("Learn More About Water Safety"):
            st.write("Learn more about water safety and tips for maintaining water health.")
