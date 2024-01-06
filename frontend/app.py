import requests
import streamlit as st

# Function to make POST
def get_prediction(data):
    """Make POST request to predict endpoint."""

    url = "http://api:8000/predict"
    response = requests.post(url, json=data)
    prediction = response.json()
    return prediction

def main():
    """Streamlit app to make inference on input data."""
    st.title('Heart Disease App Classifier')
    st.image('heart_disease.jpeg', width=300)
    st.write('This app predicts a heart disease based on certain variables...')  

    # Input data

    st.write('Enter data to make prediction:')
    age = st.number_input('Age', value=0, step=1)
    sex = st.number_input('Sex (0 o 1)', value=0, step=1)
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

    if st.button('Make prediction'):
        # Dict with input data
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

        # POST request
        prediction = get_prediction(user_data)

        # Show results
        st.write(f'Label: {prediction["label"]}')
        st.write(f'Probability: {prediction["probability"]}')

if __name__ == "__main__":
    main()
