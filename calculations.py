"""This file will perform all calculations"""
from FGPercentageStats import *

def calculations(data):
    FieldGoalPercentage_Total(data)

"""This function is responsible for taking Field Goal Percentage, finding the average, standard deviation, and graphs"""

def FieldGoalPercentage_Total(data):
    FGAvg = FieldGoalAvgTotal(data)
    FGSD = FieldGoalSDTotal(data, FGAvg)
    Good_kickers, percentage = SD_Spread(data, FGAvg, FGSD)
    print(Good_kickers, percentage)
