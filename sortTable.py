"""This file will initially confirm that our data is read correctly and will be used for future reference"""
import sqlite3

"""This function will check that the player names can be returned in a loop one at a time and in order"""


def player_names(data):
    for row in data:
        print(row[0])


"""This function will check that the players total Field Goals made can be returned in a loop one at a time and in 
order"""


def fgm_total(data):
    for row in data:
        print(row[13])
