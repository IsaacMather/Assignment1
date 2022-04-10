import matplotlib as mpl
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as \
#     FigureCanvas

def graph_maker(x_axis, y_axis, title):
    fix, ax = plt.subplots()
    ax.plot(x_axis, y_axis)
    ax.set_xlabel("Size")
    ax.set_ylabel("Average Time")
    ax.set_title(f"Complexity of {title}")
    ax.legend()
    plt.show()