import streamlit as st
import joblib
import torch
import torch.nn as nn
from pathlib import Path

st.title("Water Classification with Feedforward Neural Network")
st.write("Inputkan Ciri Khas Water Anda, dan dapatkan prediksi klasifikasinya!")

# Input dari pengguna untuk level kontaminan
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

def prediction(features):
    # Load scaler and model
    scaler = joblib.load(Path(__file__).parent / "./model/Tabular/scaler.joblib")
    model = torch.load(Path(__file__).parent / "./model/Tabular/tabnet_model.pth")  # assuming the model is saved in .pth format
    model.eval()  # Set the model to evaluation mode
    
    # Transform the input data using the scaler
    features_scaled = scaler.transform([features])
    
    # Convert the scaled data to a PyTorch tensor
    features_tensor = torch.tensor(features_scaled, dtype=torch.float32)
    
    # Perform the prediction
    with torch.no_grad():
        output = model(features_tensor)
        
    # Assuming the model has a sigmoid activation function for binary classification
    result = torch.round(torch.sigmoid(output)).item()  # Convert the output to 0 or 1
    return result

if st.button("Prediksi", type="primary"):
    # Ambil semua fitur dari slider
    features = [
        aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, fluoride,
        bacteria, viruses, lead, nitrates, nitrites, mercury, perchlorate, radium, selenium,
        silver, uranium
    ]
    
    st.subheader("Hasil Prediksi: ")
    classes = ["Safe", "Unsafe"]
    
    with st.spinner('Memproses data untuk prediksi...'):
        result = prediction(features)
        
    # Menampilkan hasil prediksi
    st.write(classes[result])
