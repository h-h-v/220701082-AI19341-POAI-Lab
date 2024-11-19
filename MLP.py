from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

# Example of custom data arrays
X_train = [[0.1, 0.5], [1.2, 3.1], [2.4, 1.7], [3.5, 3.8]]  # Replace with your X data for training
y_train = [0, 1, 0, 1]  # Replace with your y labels for training
X_test = [[1.0, 2.5], [3.1, 3.7], [2.2, 1.6], [0.5, 0.3]]  # Replace with your X data for testing

# Train the MLP model
clf = MLPClassifier(max_iter=1000)
clf.fit(X_train, y_train)

# Print R2 scores
print(f"Train Score: {clf.score(X_train, y_train)}")

# Get predictions
predictions = clf.predict(X_test)

# Plot test data with predictions
for i, point in enumerate(X_test):
    plt.scatter(point[0], point[1], color='blue' if predictions[i] == 0 else 'red')

plt.title("Test Data vs Prediction")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()