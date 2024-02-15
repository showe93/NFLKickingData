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


