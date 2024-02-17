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
    Good_kickers, good_percentage, Bottom_bar, Top_bar = SD_Spread(data, FGAvg, FGSD)
    Elite_kickers, elite_percentage = BeatTheSpread(data, Top_bar)
    Poor_kickers = len(data) - (Good_kickers + Elite_kickers)
    poor_percentage = Poor_kickers / len(data)
    NumbersData = {f'Field Goal Percentages < {Bottom_bar}% (-1SD)': Poor_kickers,
                   f'Field Goal Percentages between {Bottom_bar}% (-1SD) and {Top_bar}% (1SD)': Good_kickers,
                   f'Field Goal Percentages > {Top_bar}% (1SD)': Elite_kickers}
    kickerSDgraph(NumbersData)
    PercentageData = {f'Field Goal Percentages < {Bottom_bar}% (-1SD)': poor_percentage,
                      f'Field Goal Percentages between {Bottom_bar}% (-1SD) and {Top_bar}% (1SD)': good_percentage,
                      f'Field Goal Percentages > {Top_bar}% (1SD)': elite_percentage}
    kickersSDgraphPercentage(PercentageData)
    EliteKickers = EliteKickerNames(data, Top_bar)



    # print(poor_percentage, elite_percentage, good_percentage)  # these add up to 100%
    # make a histogram of overall make percentage

    """This function is responsible for taking the data, finding the average for each of the distances(0-19), (20-29), 
    (30-39), (40-49), and (50+). WWe will graph this data later."""


def PercentageMadeByDistance(data):
    yards19, yards29, yards39, yards49, yards50 = ByDistancePercentage(data)
# print(yards19, yards29, yards39, yards49, yards50)  # successfully returns and prints data of each field goal range
# make a histogram here of data results for percentage ofr each yard marker
