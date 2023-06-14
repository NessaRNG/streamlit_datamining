import streamlit as st

# Fungsi untuk melakukan perhitungan prediksi diabetes
def predict_diabetes(gender, age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level):
    # Di sini Anda dapat menggantikan bagian ini dengan pemodelan yang sesuai
    # Misalnya, jika Anda menggunakan model scikit-learn, Anda dapat memuatnya dan memanggil metode predict
    # Dalam contoh ini, saya hanya mengembalikan "Risiko Tinggi" untuk semua prediksi
    return "Risiko Tinggi"

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
        st.success("Hasil Prediksi: {}".format(result))

if __name__ == "__main__":
    main()
