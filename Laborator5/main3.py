import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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

    print("Primele 3 exemple inainte de scalare:")
    print(X_train[:3])

    print("\nPrimele 3 exemple dupa scalare:")
    print(X_train_scaled[:3])

if __name__ == "__main__":
    main()