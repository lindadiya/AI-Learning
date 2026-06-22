from sklearn.linear_model import LinearRegression
import numpy as np

# Hours studied
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Marks obtained
y = np.array([50, 60, 70, 80, 90])

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[10]])

print("Predicted Marks:", prediction[0])