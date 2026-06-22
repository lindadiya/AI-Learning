import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")

X = data[["StudyHours"]]
y = data["Marks"]

model = LinearRegression()
model.fit(X, y)

st.title("🎓 Student Performance Predictor")

st.write("Predict expected marks based on study hours.")

hours = st.slider("Study Hours", 1, 12, 5)

prediction = model.predict(
    pd.DataFrame({"StudyHours": [hours]})
)

st.metric("Predicted Marks", f"{prediction[0]:.2f}")

st.subheader("Dataset")

st.dataframe(data)