"""This file will perform all calculations"""
from FGPercentageStats import *
from graphs import *


def calculations(data):
    """ First we will calculate below average,average, and above average kickers. We will use total FG percentage and
    -1 and 1 Standard Deviation to perform this calculation."""
    FieldGoalStats = FieldGoalPercentage_Total(data)
    """Now we will use box plots to determine if any of the below or above average kickers are outliers when compared
    to the rest of the data"""
    FieldGoalTotal_Outliers(data)
    """"This function determines averages for each of the 5 distance ranges. 0-19, 20-29, 30-39, 40-49 and 50+."""
    PercentageMadeByDistance(data)

    return FieldGoalStats
"""This function is responsible for taking Field Goal Percentage, finding the average, standard deviation, and graphs"""


def FieldGoalPercentage_Total(data):
    kickingStats = []
    FGAvg = FieldGoalAvgTotal(data)
    FGSD = FieldGoalSDTotal(data, FGAvg)
    Good_kickers, good_percentage, Bottom_bar, Top_bar, GoodKickersList = SD_Spread(data, FGAvg, FGSD)
    Elite_kickers, elite_percentage, EliteKickersList = BeatTheSpread(data, Top_bar)
    Poor_kickers, poor_percentage, PoorKickersList = NotBeatTheSpread(data, Bottom_bar)
    tableData = KickerPerformanceNameList(PoorKickersList, GoodKickersList, EliteKickersList, Top_bar, Bottom_bar)
    kickerNameTable(tableData)
    NumbersData = {f'Below Average (< {Bottom_bar}% (-1SD))': Poor_kickers,
                   f'Average ({Bottom_bar}% (-1SD) and {Top_bar}% (1SD))': Good_kickers,
                   f'Above Average > ({Top_bar}% (1SD))': Elite_kickers}
    kickerSDgraph(NumbersData)
    PercentageData = {f'Below Average (< {Bottom_bar}% (-1SD))': poor_percentage,
                      f'Average ({Bottom_bar}% (-1SD) and {Top_bar}% (1SD))': good_percentage,
                      f'Above Average (> {Top_bar}% (1SD))': elite_percentage}
    kickersSDgraphPercentage(PercentageData)
    kickingStats.extend((FGAvg, Bottom_bar, Top_bar, Poor_kickers, poor_percentage, Elite_kickers, elite_percentage, Good_kickers, good_percentage))
    return kickingStats

def FieldGoalTotal_Outliers(data):
    boxdata = boxPlot(data)
    BoxPlotGraph(boxdata)
    BoxplotOutliers(data, boxdata)


    """This function is responsible for taking the data, finding the average for each of the distances(0-19), (20-29), 
    (30-39), (40-49), and (50+). WWe will graph this data later."""


def PercentageMadeByDistance(data):
    yards19, yards29, yards39, yards49, yards50 = ByDistancePercentage(data)
# print(yards19, yards29, yards39, yards49, yards50)  # successfully returns and prints data of each field goal range
# make a histogram here of data results for percentage ofr each yard marker
