import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def main():
    iris = datasets.load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train_scaled, y_train)

    plt.scatter(X[:, 2], X[:, 3], c=y)
    plt.xlabel("Lungime petala")
    plt.ylabel("Latime petala")
    plt.title("Vizualizarea florilor Iris dupa petale")
    plt.show()

    sepal_length = float(input("Introduceti lungimea sepalei: "))
    sepal_width = float(input("Introduceti latimea sepalei: "))
    petal_length = float(input("Introduceti lungimea petalei: "))
    petal_width = float(input("Introduceti latimea petalei: "))

    floare_noua = [[sepal_length, sepal_width, petal_length, petal_width]]
    floare_noua_scaled = scaler.transform(floare_noua)

    predictie = model.predict(floare_noua_scaled)

    print("Clasa prezisa:", iris.target_names[predictie[0]])

if __name__ == "__main__":
    main()