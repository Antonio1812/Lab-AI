import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
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
    X_test_scaled = scaler.transform(X_test)

    valori_k = range(1, 16)
    acurateti = []

    for k in valori_k:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, y_train)

        y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)

        acurateti.append(accuracy)

        print("k =", k, "Acuratete =", accuracy)

    plt.plot(valori_k, acurateti, marker='o')
    plt.xlabel("Valoarea lui k")
    plt.ylabel("Acuratete")
    plt.title("Impactul valorii k asupra acuratetii")
    plt.grid(True)
    plt.show()

    max_accuracy = max(acurateti)
    best_k = valori_k[acurateti.index(max_accuracy)]

    print("\nValoarea optima pentru k pare sa fie:", best_k)
    print("Acuratete maxima:", max_accuracy)

if __name__ == "__main__":
    main()