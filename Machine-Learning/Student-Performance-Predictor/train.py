import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")

X = data[["StudyHours"]]
y = data["Marks"]

model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

hours = float(input("Enter study hours: "))

prediction = model.predict(
    pd.DataFrame({"StudyHours": [hours]})
)

print(f"Predicted Marks: {prediction[0]:.2f}")