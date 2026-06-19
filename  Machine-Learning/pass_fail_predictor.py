from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
    [95],
    [88],
    [75],
    [60],
    [45],
    [30]
])

y = np.array([
    "Pass",
    "Pass",
    "Pass",
    "Pass",
    "Fail",
    "Fail"
])

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[20]])

print("Prediction:", prediction[0])