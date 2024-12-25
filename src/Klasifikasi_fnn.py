import streamlit as st
import joblib
import tensorflow as tf
from pathlib import Path

def render(switch_page):
    st.title("Water Classification with Feedforward Neural Network")
    st.write("Input the characteristics of your water, and get a prediction about its safety!")

    # Input sliders for contaminants
    aluminium = st.slider('Aluminium Level', 0.0, 5.0, step=0.1)
    ammonia = st.slider('Ammonia Level', 0.0, 30.0, step=0.1)
    arsenic = st.slider('Arsenic Level', 0.0, 1.0, step=0.01)
    barium = st.slider('Barium Level', 0.0, 5.0, step=0.1)
    cadmium = st.slider('Cadmium Level', 0.0, 10.0, step=0.1)
    chloramine = st.slider('Chloramine Level', 0.0, 2.0, step=0.1)
    chromium = st.slider('Chromium Level', 0.0, 2.0, step=0.1)
    copper = st.slider('Copper Level', 0.0, 1.0, step=0.01)
    fluoride = st.slider('Fluoride Level', 0.0, 2.0, step=0.1)
    bacteria = st.slider('Bacteria Level', 0.0, 1.0, step=0.01)
    viruses = st.slider('Viruses Level', 0.0, 1.0, step=0.01)
    lead = st.slider('Lead Level', 0.0, 1.0, step=0.01)
    nitrates = st.slider('Nitrates Level', 0.0, 20.0, step=0.1)
    nitrites = st.slider('Nitrites Level', 0.0, 3.0, step=0.1)
    mercury = st.slider('Mercury Level', 0.0, 1.0, step=0.01)
    perchlorate = st.slider('Perchlorate Level', 0.0, 60.0, step=0.1)
    radium = st.slider('Radium Level', 0.0, 8.0, step=0.1)
    selenium = st.slider('Selenium Level', 0.0, 1.0, step=0.01)
    silver = st.slider('Silver Level', 0.0, 1.0, step=0.01)
    uranium = st.slider('Uranium Level', 0.0, 1.0, step=0.01)

    # Safe thresholds and health impacts
    thresholds = {
        "aluminium": (0.2, "Can cause nervous system damage and Alzheimer's disease."),
        "ammonia": (0.5, "Irritates the digestive and respiratory systems."),
        "arsenic": (0.01, "Can lead to skin cancer, lung cancer, and heart disease."),
        "barium": (2.0, "May cause high blood pressure, heart problems, and kidney damage."),
        "cadmium": (0.005, "Damages kidneys, lungs, and bones."),
        "chloramine": (4.0, "Can irritate eyes, nose, and throat."),
        "chromium": (0.1, "May harm kidneys, liver, and increase cancer risk."),
        "copper": (1.3, "Causes digestive issues and liver damage."),
        "fluoride": (4.0, "May lead to fluorosis, bone damage, and dental problems."),
        "bacteria": (0.0, "Risk of gastrointestinal infections."),
        "viruses": (0.0, "May cause infectious diseases like hepatitis."),
        "lead": (0.015, "Interferes with brain development in children and damages kidneys."),
        "nitrates": (10.0, "Causes methemoglobinemia or 'blue baby syndrome'."),
        "nitrites": (1.0, "Linked to cancer and blood disorders."),
        "mercury": (0.002, "Harms the brain, kidneys, and nervous system."),
        "perchlorate": (15.0, "Disrupts thyroid function."),
        "radium": (5.0, "Increases cancer risk."),
        "selenium": (0.05, "May cause selenium poisoning."),
        "silver": (0.1, "Leads to argyria, a permanent skin discoloration."),
        "uranium": (0.03, "Increases the risk of kidney damage."),
    }

    # Function to check if any contaminants exceed thresholds
    def check_thresholds(features):
        exceeded = []
        for i, (key, (limit, impact)) in enumerate(thresholds.items()):
            if features[i] > limit:
                exceeded.append((key, features[i], limit, impact))
        return exceeded

    # Prediction function
    def prediction(features):
        scaler = joblib.load(Path(__file__).parent / "./model/Tabular/scaler.joblib")
        model = tf.keras.models.load_model(Path(__file__).parent / "./model/Tabular/fnn_model.h5")
        data = scaler.transform([features])
        result = (model.predict(data) > 0.5).astype("int32")
        return result[0][0]

    if st.button("Predict", type="primary"):
        features = [
            aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, fluoride,
            bacteria, viruses, lead, nitrates, nitrites, mercury, perchlorate, radium, selenium,
            silver, uranium
        ]
        
        st.subheader("Prediction Result: ")
        classes = ["Unsafe", "Safe"]
        
        with st.spinner('Processing your data...'):
            result = prediction(features)
            
        st.write(classes[result])
        if result == 1:
            st.success("Congrats, your water is safe to consume!")
        else:
            st.error("Sorry, your water is unsafe to consume. Please consider filtering or treating it.")
        
        exceeded = check_thresholds(features)
        if exceeded:
            st.warning("Some contaminants exceed safe levels:")
            for key, value, limit, impact in exceeded:
                st.write(f"- **{key.capitalize()}**: {value:.2f} (Safe Limit: {limit}) - {impact}")

    if st.button("Back to Home"):
        switch_page("home")  # Kembali ke halaman utama
