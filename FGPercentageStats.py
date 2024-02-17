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


"""This function will calculate the Population Standard Deviation Based on Field Goal Percentages of all kickers in 
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
    percentage = KickerCount / PopulationSize
    return KickerCount, percentage, Bottom_bar, Top_bar


"""This function determines which kickers were greater then +1 Standard Deviation and returns the count and 
percentage """


def BeatTheSpread(data, Top_bar):
    PopulationSize = 0
    EliteKickersList = []
    KickerCount = 0
    for row in data:
        PopulationSize += 1
        test_value = row[14]
        if float(test_value) >= Top_bar:
            KickerCount += 1
            EliteKickersList.append(row[0])
    percentage = KickerCount / PopulationSize
    return KickerCount, percentage, EliteKickersList


"This function determines field goal percentage for each specific distance using all of the data"


def ByDistancePercentage(data):
    results = []  # a list of 5 numbers. { '0-19 yards%', '20-29 yards%','30-39 yards%', '40-49 yards%', '50+ yards'
    i = 0
    attemptRow = 2
    madeRow = 3
    for i in range(5):
        attempts = 0
        makes = 0
        for row in data:
            attempts = int(row[attemptRow]) + attempts
            makes = int(row[madeRow]) + makes
        percentage = f'{makes / attempts: .2%}'
        madeRow = madeRow + 2
        attemptRow = attemptRow + 2
        results.append(percentage)
    yards19 = results[0]
    yards29 = results[1]
    yards39 = results[2]
    yards49 = results[3]
    yards50 = results[4]
    return yards19, yards29, yards39, yards49, yards50

