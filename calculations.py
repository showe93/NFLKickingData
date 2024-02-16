"""This file will perform all calculations"""
from FGPercentageStats import *


def calculations(data):
    FieldGoalPercentage_Total(data)
    PercentageMadeByDistance(data)


"""This function is responsible for taking Field Goal Percentage, finding the average, standard deviation, and graphs"""


def FieldGoalPercentage_Total(data):
    FGAvg = FieldGoalAvgTotal(data)
    FGSD = FieldGoalSDTotal(data, FGAvg)
    Good_kickers, good_percentage = SD_Spread(data, FGAvg, FGSD)
    Elite_Kickers, elite_percentage = BeatTheSpread(data, FGAvg, FGSD)
    Poor_kickers = len(data) - (Good_kickers + Elite_Kickers)
    poor_percentage = f'{Poor_kickers / len(data): .2%}'
    # print(poor_percentage, elite_percentage, good_percentage)  # these add up to 100%
    # make a histogram of overall make percentage

    """This function is responsible for taking the data, finding the average for each of the distances(0-19), (20-29), 
    (30-39), (40-49), and (50+). WWe will graph this data later."""


def PercentageMadeByDistance(data):
    yards19, yards29, yards39, yards49, yards50 = ByDistancePercentage(data)
    print(yards19, yards29, yards39, yards49, yards50)  # successfully returns and prints data of each field goal range
    # make a histogram here of data results for percentage ofr each yard marker
