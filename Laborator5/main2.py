import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split

def main():
    iris = datasets.load_iris()
    
    X = iris.data
    y = iris.target
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )
    
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

if __name__ == "__main__":
    main()