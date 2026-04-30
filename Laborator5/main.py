import sklearn.datasets as datasets

def main():
    
    iris=datasets.load_iris()
    print(iris.data)
    print("Numarul de exemple: ", len(iris.data))
    print("Numele atributelor: ", iris.feature_names)
    print("Numele claselor: ", iris.target_names)

if __name__ == "__main__":
    main()