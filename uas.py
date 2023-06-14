import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Fungsi untuk melakukan pelatihan model Naive Bayes
def train_model():
    # Membaca dataset diabetes (contoh: diabetes.csv)
    df = pd.read_csv("https://raw.githubusercontent.com/NessaRNG/DataMining/main/TugasPendat/diabetes_dataset.csv")

    # Membagi dataset menjadi fitur dan target
    X = df.drop("diabetes", axis=1)
    y = df["diabetes"]

    # Membagi data menjadi data pelatihan dan data pengujian
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat dan melatih model Naive Bayes
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Memprediksi label pada data pengujian
    y_pred = model.predict(X_test)

    # Menghitung akurasi model
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy

# Fungsi untuk melakukan prediksi diabetes menggunakan model yang telah dilatih
def predict_diabetes(model, data):
    prediction = model.predict([data])
    return prediction[0]

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
        # Memuat model yang telah dilatih dan akurasinya
        model, accuracy = train_model()

        # Membentuk data pengujian berdasarkan input pengguna
        data = [age, bmi, hba1c_level, blood_glucose_level]

        # Mengubah input kategorikal menjadi numerikal
        if gender == "Pria":
            data.append(0)
        else:
            data.append(1)

        if hypertension == "Tidak":
            data.append(0)
        else:
            data.append(1)

        if heart_disease == "Tidak":
            data.append(0)
        else:
            data.append(1)

        # Melakukan prediksi diabetes menggunakan model yang telah dilatih
        prediction = predict_diabetes(model, data)

        # Menampilkan hasil prediksi
        if prediction == 0:
            st.success("Hasil Prediksi: Risiko Rendah")
        else:
            st.error("Hasil Prediksi: Risiko Tinggi")

        # Menampilkan akurasi model yang telah dilatih
        st.info("Akurasi Model: {:.2f}%".format(accuracy * 100))

if __name__ == "__main__":
    main()
