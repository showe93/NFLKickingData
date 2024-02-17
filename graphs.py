"""this file contains all functions related to graphing"""
import matplotlib.pyplot as plt

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
    plt.show()

def kickersSDgraphPercentage(data):
    SDcalculations = list(data.keys())
    percentages = list(data.values())
    fig = plt.figure(figsize=(15,5))
    bar_colors = ['tab:red', 'tab:blue', 'tab:green']
    plt.pie(percentages, labels=SDcalculations, autopct='%1.2f%%', colors=bar_colors)
    plt.title("Percentages of Kickers in Each Category Based on SD")
    plt.show()
