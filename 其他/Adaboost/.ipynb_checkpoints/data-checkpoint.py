from sklearn import datasets
import matplotlib.pyplot as plt



# 创建数据
def create_data():
    iris = datasets.load_iris()
    X = iris.data[:100, :2]
    y = iris.target[:100]
    for i in range(50):
        y[i] = -1
    return X, y


# 绘画出数据
def plan_data(X, y):
    plt.scatter(X[:50, 0], X[:50, 1], label="0")
    plt.scatter(X[50:100, 0], X[50:100, 1], label="1")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    X, y = create_data()
    print(y)
    plan_data(X, y)
