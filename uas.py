import streamlit as st

# Fungsi untuk melakukan perhitungan prediksi diabetes
def predict_diabetes(gender, age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level):
    # Kriteria medis untuk prediksi diabetes
    if gender == "Pria" and age > 40 and hypertension == "Ya" and heart_disease == "Ya":
        return "Risiko Tinggi"
    elif gender == "Wanita" and age > 50 and hypertension == "Ya" and heart_disease == "Ya":
        return "Risiko Tinggi"
    elif bmi >= 30:
        return "Risiko Tinggi"
    elif hba1c_level >= 6.5:
        return "Risiko Tinggi"
    elif blood_glucose_level >= 200:
        return "Risiko Tinggi"
    else:
        return "Risiko Rendah"

# Tampilan aplikasi web
def main():
    st.title("Diabetes Predictor")

    # Mengambil input dari pengguna
    gender = st.selectbox("Gender", ["Pria", "Wanita"])
    age = st.slider("Usia", 1, 100, 25)
    hypertension = st.selectbox("Hipertensi", ["Tidak", "Ya"])
    heart_disease = st.selectbox("Penyakit Jantung", ["Tidak", "Ya"])
    bmi = st.number_input("BMI")
    hba1c_level = st.number_input("Tingkat HbA1c")
    blood_glucose_level = st.number_input("Tingkat Glukosa Darah")

    # Tombol untuk memulai perhitungan
    if st.button("Hitung"):
        result = predict_diabetes(gender, age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level)
        
        if result == "Risiko Rendah":
            st.success("Hasil Prediksi: Risiko Rendah")
        else:
            st.error("Hasil Prediksi: Risiko Tinggi")

if __name__ == "__main__":
    main()
