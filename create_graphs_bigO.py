import matplotlib.pyplot as plt
import math


def create_graph_1():
    x_numbers = []
    for i in range(0, 31):
        x_numbers.append(i)

    y_numbers = []
    for i in range(0, 31):
        y_numbers.append(1)

    plt.plot(x_numbers, y_numbers, linewidth=3)
    ax = plt.gca()
    #ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.plot(linewidth=7.0)
    plt.xlim([0, 30])
    plt.ylim([0, 3])
    ax.set_title('O(1)',
                  fontsize = 20,
                  weight = 'heavy',
                  color = 'orange',
                  backgroundcolor = 'green')
    box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
    ax.text(0.05, 2.5, "max_O=" + str(max(y_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    ax.text(26, 0.2, "n=" + str(max(x_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    plt.show()

def create_graph_n():
    x_numbers = []
    for i in range(0, 31):
        x_numbers.append(i)

    y_numbers = []
    for i in range(0, 31):
        y_numbers.append(i)

    plt.plot(x_numbers, y_numbers, linewidth=3)
    ax = plt.gca()
    #ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim([0, 30])
    plt.ylim([0, 30])
    ax.set_title('O(n)',
                  fontsize = 20,
                  weight = 'heavy',
                  color = 'orange',
                  backgroundcolor = 'green')
    box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
    ax.text(0.05, 25, "max_O=" + str(max(y_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    ax.text(26, 2, "n=" + str(max(x_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    plt.show()

def create_graph_log_n():
    x_numbers = []
    for i in range(1, 31):
        x_numbers.append(i)
    y_numbers = []
    for x,item in enumerate(x_numbers):
        y = math.log2(item)
        y_numbers.append(y)

    plt.plot(x_numbers, y_numbers, linewidth=3)
    ax = plt.gca()
    #ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim([0, 30])
    plt.ylim([0, 10])
    ax.set_title('O(log n)',
                  fontsize = 20,
                  weight = 'heavy',
                  color = 'orange',
                  backgroundcolor = 'green')
    box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
    ax.text(0.05, 7, "max_O=" + str(round(max(y_numbers), 2)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    ax.text(26, 0.5, "n=" + str(max(x_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    plt.show()


def create_graph_n_log_n():
    x_numbers = []
    for i in range(1, 31):
        x_numbers.append(i)
    y_numbers = []

    for x,item in enumerate(x_numbers):
        y = item * math.log2(item)
        y_numbers.append(y)

    plt.plot(x_numbers, y_numbers, linewidth=3)
    ax = plt.gca()
    #ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim([0, 30])
    plt.ylim([0, 160])
    ax.set_title('O(n * log n)',
                  fontsize = 20,
                  weight = 'heavy',
                  color = 'orange',
                  backgroundcolor = 'green')
    box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
    ax.text(0.05, 140, "max_O=" + str(round(max(y_numbers), 2)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    ax.text(26, 10, "n=" + str(max(x_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    plt.show()


def create_graph_n_2():
    x_numbers = []
    for i in range(31):
        x_numbers.append(i)
    y_numbers = []

    for x,item in enumerate(x_numbers):
        y = item ** 2
        y_numbers.append(y)

    plt.plot(x_numbers, y_numbers, linewidth=3)
    ax = plt.gca()
    #ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim([0, 30])
    plt.ylim([0, 961])
    ax.set_title('O(n^2)',
                  fontsize = 20,
                  weight = 'heavy',
                  color = 'orange',
                  backgroundcolor = 'green')
    box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
    ax.text(0.05, 700, "max_O=" + str(max(y_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    ax.text(26, 50, "n=" + str(max(x_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    plt.show()

def create_graph_n_factorial():
    x_numbers = []
    for i in range(0, 31):
        x_numbers.append(i)

    y_numbers = []
    for i,item in enumerate(x_numbers):
        y = math.factorial(item)
        y_numbers.append(y)

    plt.plot(x_numbers, y_numbers, linewidth=3)
    ax = plt.gca()
    #ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim([0, 30])
    plt.ylim([0, 1024])
    ax.set_title('O(n!)',
                  fontsize = 20,
                  weight = 'heavy',
                  color = 'orange',
                  backgroundcolor = 'green')
    box_1 = {'facecolor':'black',    #  цвет области
       'edgecolor': 'red',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
    ax.text(0.05, 800, "max_O=" + str(max(y_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    ax.text(26, 50, "n=" + str(max(x_numbers)),
        bbox = box_1,
        color = 'white',    #  цвет шрифта
        fontsize = 15)
    plt.show()


if __name__ == "__main__":
    create_graph_1()
    create_graph_n()
    create_graph_log_n()
    create_graph_n_log_n()
    create_graph_n_2()
    create_graph_n_factorial()
