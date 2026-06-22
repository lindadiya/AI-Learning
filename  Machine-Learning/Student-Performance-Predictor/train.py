import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")

X = data[["StudyHours"]]
y = data["Marks"]

model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

prediction = model.predict([[7]])

print(f"Predicted Marks: {prediction[0]:.2f}")