import requests
import streamlit as st

# Función para hacer la solicitud POST
def get_prediction(data):
    # URL del endpoint donde se realizará la solicitud POST
    url = "http://api:8000/predict"

    # Hacer la solicitud POST con los datos ingresados por el usuario
    response = requests.post(url, json=data)

    # Obtener la respuesta en formato JSON
    prediction = response.json()

    return prediction

# Crear la interfaz de usuario con Streamlit
def main():
    st.title('Clasificador de datos')

    st.write('Ingrese los datos para realizar la predicción:')

    # Obtener los datos ingresados por el usuario
    age = st.number_input('Edad', value=0, step=1)
    sex = st.number_input('Sexo (0 o 1)', value=0, step=1)
    cp = st.number_input('Chest Pain Type', value=0, step=1)
    trestbps = st.number_input('Trestbps', value=0, step=1)
    chol = st.number_input('Chol', value=0, step=1)
    fbs = st.number_input('Fbs', value=0, step=1)
    restecg = st.number_input('Restecg', value=0, step=1)
    thalach = st.number_input('Thalach', value=0, step=1)
    exang = st.number_input('Exang', value=0, step=1)
    oldpeak = st.number_input('Oldpeak', value=0.0, step=0.1)
    slope = st.number_input('Slope', value=0, step=1)
    ca = st.number_input('Ca', value=0, step=1)
    thal = st.selectbox('Thal', ['normal', 'fixed', 'reversible'])

    # Botón para realizar la predicción
    if st.button('Realizar predicción'):
        # Crear un diccionario con los datos ingresados por el usuario
        user_data = {
            'age': int(age),
            'sex': int(sex),
            'cp': int(cp),
            'trestbps': int(trestbps),
            'chol': int(chol),
            'fbs': int(fbs),
            'restecg': int(restecg),
            'thalach': int(thalach),
            'exang': int(exang),
            'oldpeak': float(oldpeak),
            'slope': int(slope),
            'ca': int(ca),
            'thal': str(thal)
        }

        # Hacer la solicitud POST con los datos ingresados por el usuario
        prediction = get_prediction(user_data)

        # Mostrar el resultado de la predicción
        st.write(f'Clase: {prediction["label"]}')
        st.write(f'Probabilidad: {prediction["probability"]}')

if __name__ == "__main__":
    main()
