"""This file will find the average of all Field Goal Percentages, then will construct a graph using the standard
deviation and mean of the data"""
import math
"""This function will find the average Field Goal Percentage amongst all kickers in the NFL"""


def FieldGoalAvgTotal(data):
    FGTotalPercentage = 0.0
    Total = 0
    for row in data:
        FGTotalPercentage = FGTotalPercentage + float(row[14])
        Total += 1
    FGAvg = FGTotalPercentage / Total
    FGAvg = round(FGAvg, 2)
    return FGAvg


"""This function will calculate the Poopulation Standard Deviation Based on Field Goal Percentages of all kickers in 
the NFL"""


def FieldGoalSDTotal(data, FGAvg):
    PopulationSize = 0
    SumTotal = 0
    for row in data:
        SumTotal = SumTotal + (math.pow((float(row[14]) - FGAvg), 2))
        PopulationSize += 1
    StandardDeviation = math.sqrt(SumTotal / PopulationSize)
    StandardDeviation = round(StandardDeviation, 2)
    return StandardDeviation


"""This function will take +1 and -1 Standard Deviation and Calculate how many kickers fall within that range"""


def SD_Spread(data, FGAvg, StandardDeviation):
    PopulationSize = 0
    KickerCount = 0
    Bottom_bar = FGAvg - StandardDeviation
    Top_bar = FGAvg + StandardDeviation
    for row in data:
        PopulationSize += 1
        test_value = row[14]
        if Bottom_bar <= float(test_value) <= Top_bar:
            KickerCount += 1
    percentage = f"{KickerCount / PopulationSize: .2%}"
    return KickerCount, percentage
