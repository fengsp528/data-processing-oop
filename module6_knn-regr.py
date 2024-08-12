import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.X = None
        self.y = None

    def fit(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)

    def predict(self, X):
        X = np.array([X])
        distances = np.sqrt(np.sum((self.X - X)**2, axis=1))
        nearest_neighbor_ids = distances.argsort()[:self.k]
        nearest_neighbor_values = self.y[nearest_neighbor_ids]
        return np.mean(nearest_neighbor_values)

def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k for k-NN: "))

    if k > N:
        print("Error: k cannot be greater than N")
        return

    X = np.zeros(N)
    y = np.zeros(N)
    #print(X)
    #print(y)

    for i in range(N):
        X[i] = float(input(f"Enter x value for point {i+1}: "))
        y[i] = float(input(f"Enter y value for point {i+1}: "))

    knn = KNNRegressor(k)
    knn.fit(X.reshape(-1, 1), y)
    X_pred = float(input("Enter X value for prediction: "))

    y_pred = knn.predict(X_pred)

    print(f"The predicted Y value is: {y_pred}")

if __name__ == "__main__":
    main()
