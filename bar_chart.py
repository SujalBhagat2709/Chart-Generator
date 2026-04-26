import matplotlib.pyplot as plt

def create_bar_chart():
    
    labels = ["A", "B", "C", "D"]
    values = [10, 25, 15, 30]
    
    plt.bar(labels, values)
    plt.title("Bar Chart")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":
    create_bar_chart()