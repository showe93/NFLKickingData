"""this file contains all functions related to graphing"""
import matplotlib.pyplot as plt
import numpy as np

"""this function graphs the number of kickers that fall within one standard deviation, fall below one standard 
deviation, and above one standard deviation."""


def kickerSDgraph(data):
    SDcalculations = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(15, 10))
    bar_colors = ['tab:red', 'tab:blue', 'tab:green']
    plt.bar(SDcalculations, values, color=bar_colors, width=0.4)
    plt.xlabel("Kicking Categories")
    plt.ylabel("Number of Kickers")
    plt.title("Kickers Field Goal Percentages Compared to -1 and 1 Standard Deviation")
    plt.savefig("Graphs/TotalFieldGoalSDComparison.jpg")


"""This function graphs the percentage of kickers that fall within one standard deviation, fall below one standard
deviation, and above one standard deviation."""


def kickersSDgraphPercentage(data):
    SDcalculations = list(data.keys())
    percentages = list(data.values())
    fig = plt.figure(figsize=(15, 5))
    bar_colors = ['tab:red', 'tab:blue', 'tab:green']
    plt.pie(percentages, labels=SDcalculations, autopct='%1.2f%%', colors=bar_colors)
    plt.title("Percentages of Kickers in Each Category Based on SD")
    plt.savefig("Graphs/TotalFieldGoalPercentages.jpg")


"""This function creates a table of kickers name based on the category they fall into"""


def kickerNameTable(data):
    column_header = data.pop(0)
    plt.figure(linewidth=2,
               tight_layout={'pad': 1},
               figsize=(5, 7),
               dpi=150
               )
    ccolors = plt.cm.Blues(np.full(len(column_header), 0.1))
    table = plt.table(cellText=data, colLabels=column_header, loc='center', colColours=ccolors, cellLoc='center')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    table.scale(1, 1.3)
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    plt.box(on=None)
    plt.savefig("Graphs/KickerNamesTotalFieldGoal.jpg", bbox_inches="tight")
