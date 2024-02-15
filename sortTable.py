"""This file will initially confirm that our data is read correctly and will be used for future reference"""
import sqlite3

"""This function will check that the player names can be returned in a loop one at a time and in order"""
def player_names():
    con = sqlite3.connect("NFL_Kicking_Data.sqlite")
    cur = con.cursor()

    ### CANT FIND THE TABLE - errror unrecognized token: "2023KickingData"
    # Print(con.fetchall()) returns []

    cur.execute('SELECT * FROM 2023KickingData')
    for row in cur:
        print(row[0])


"""This function will check that the players total Field Goals made can be returned in a loop one at a time and in 
order"""
def fgm_total():
    con = sqlite3.connect("NFL_Kicker_Data.sqlite")
    cur = con.cursor()
