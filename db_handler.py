import sqlite3
from calculations import calculations
from htmlCode import *
"""This function starts all calculations"""


def main():
    try:
        connection = sqlite3.connect("Data/Database/NFL_Kicking_Data.sqlite")
        cursor = connection.cursor()
        data = cursor.execute('SELECT * FROM "main"."KickingData"').fetchall()
        FGAvgStats = calculations(data)
        html(FGAvgStats)
        cursor.close()
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        if connection:
            connection.close()
            print('Database connection closed.')
