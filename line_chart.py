import matplotlib.pyplot as plt

def create_line_chart():
    
    x = [1, 2, 3, 4, 5]
    y = [5, 9, 7, 12, 10]
    
    plt.plot(x, y, marker="o")
    plt.title("Line Chart")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()


if __name__ == "__main__":
    create_line_chart()