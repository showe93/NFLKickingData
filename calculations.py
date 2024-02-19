"""This file will perform all calculations"""
from FGPercentageStats import *
from graphs import *


def calculations(data):
    FieldGoalPercentage_Total(data)
    PercentageMadeByDistance(data)


"""This function is responsible for taking Field Goal Percentage, finding the average, standard deviation, and graphs"""


def FieldGoalPercentage_Total(data):
    FGAvg = FieldGoalAvgTotal(data)
    FGSD = FieldGoalSDTotal(data, FGAvg)
    Good_kickers, good_percentage, Bottom_bar, Top_bar, GoodKickersList = SD_Spread(data, FGAvg, FGSD)
    Elite_kickers, elite_percentage, EliteKickersList = BeatTheSpread(data, Top_bar)
    Poor_kickers, poor_percentage, PoorKickersList = NotBeatTheSpread(data, Bottom_bar)
    tableData = KickerPerformanceNameList(PoorKickersList, GoodKickersList, EliteKickersList)
    kickerNameTable(tableData)
    NumbersData = {f'Field Goal Percentages < {Bottom_bar}% (-1SD)': Poor_kickers,
                   f'Field Goal Percentages between {Bottom_bar}% (-1SD) and {Top_bar}% (1SD)': Good_kickers,
                   f'Field Goal Percentages > {Top_bar}% (1SD)': Elite_kickers}
    kickerSDgraph(NumbersData)
    PercentageData = {f'Field Goal Percentages < {Bottom_bar}% (-1SD)': poor_percentage,
                      f'Field Goal Percentages between {Bottom_bar}% (-1SD) and {Top_bar}% (1SD)': good_percentage,
                      f'Field Goal Percentages > {Top_bar}% (1SD)': elite_percentage}
    kickersSDgraphPercentage(PercentageData)
    statement = f'Across the league, NFL kickers were successful with kicking Field Goals {FGAvg}% of the time. The ' \
                f'Average NFL kicker was successful between {Bottom_bar}% and {Top_bar}% on Field Goal Attempts. {Poor_kickers} kickers ({poor_percentage}%) performed below ' \
                f'average, well {Elite_kickers} ({elite_percentage}%) kickers performed above average. The remaining {Good_kickers} ({good_percentage}%) kickers ' \
                f'fall in this range.'
    print(statement)

    # print(poor_percentage, elite_percentage, good_percentage)  # these add up to 100%
    # make a histogram of overall make percentage

    """This function is responsible for taking the data, finding the average for each of the distances(0-19), (20-29), 
    (30-39), (40-49), and (50+). WWe will graph this data later."""


def PercentageMadeByDistance(data):
    yards19, yards29, yards39, yards49, yards50 = ByDistancePercentage(data)
# print(yards19, yards29, yards39, yards49, yards50)  # successfully returns and prints data of each field goal range
# make a histogram here of data results for percentage ofr each yard marker
