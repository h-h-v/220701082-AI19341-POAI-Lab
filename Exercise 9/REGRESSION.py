from sklearn.neural_network import MLPRegressor

# Define your training and testing data
X_train = [[0.1, 0.5], [1.2, 3.1], [2.4, 1.7], [3.5, 3.8]]
y_train = [0, 1, 0, 1]
X_test = [[1.0, 2.5], [3.1, 3.7], [2.2, 1.6], [0.5, 0.3]]
y_test = [0, 1, 0, 1]  # Adjusted length to match X_test

# Train the MLP Regressor model
regressor = MLPRegressor(max_iter=1000)
regressor.fit(X_train, y_train)

# Print R2 scores for both train and test sets
print(f"R2 Score (Train): {regressor.score(X_train, y_train)}")
print(f"R2 Score (Test): {regressor.score(X_test, y_test)}")