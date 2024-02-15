"""This file will initially confirm that our data is read correctly and will be used for future reference"""

"""This function will check that the player names can be returned in a loop one at a time and in order"""


def player_names(data):
    for row in data:
        print(row[0])


"""This function will check that the players total Field Goals made can be returned in a loop one at a time and in 
order"""


def fgm_total(data):
    totalAttempts = 0
    for row in data:
        print(row[12])
        totalAttempts = totalAttempts + int(row[12])
    print(totalAttempts)


"""This function will find the probability of a kicker making a field goal vs total field goal attempts across the 
league for the entire 2023-2024 NFL season"""


def fgm_vs_fga(data):
    totalAttempts = 0
    totalMade = 0
    for row in data:
        totalAttempts = totalAttempts + int(row[12])
        totalMade = totalMade + int(row[13])
    percentageMade = totalMade / totalAttempts
    percentageMade = f"{percentageMade: .2%}"
    return percentageMade
