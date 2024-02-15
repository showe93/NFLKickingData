from sortTable import player_names, fgm_total
import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect("NFL_Kicking_Data.sqlite")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "main"."2023KickingData"')
    player_names(cursor)
    cursor.execute('SELECT * FROM "main"."2023KickingData"')
    fgm_total(cursor)

