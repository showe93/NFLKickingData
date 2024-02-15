"""This file will perform all calculations"""
from FGPercentageStats import *

def calculations(data):
    FieldGoalPercentage_Total(data)

"""This function is responsible for taking Field Goal Percentage, finding the average, standard deviation, and graphs"""

def FieldGoalPercentage_Total(data):
    FGAvg = FieldGoalAvgTotal(data)
    FGSD = FieldGoalSDTotal(data, FGAvg)
    Good_kickers, good_percentage = SD_Spread(data, FGAvg, FGSD)
    Elite_Kickers, elite_percentage = BeatTheSpread(data, FGAvg, FGSD)
    Poor_kickers = len(data) - (Good_kickers + Elite_Kickers)
    poor_percentage = f'{Poor_kickers/len(data): .2%}'
    print(poor_percentage, elite_percentage, good_percentage)