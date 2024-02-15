from sortTable import player_names, fgm_total, fgm_vs_fga
import sqlite3

if __name__ == '__main__':
    try:
        connection = sqlite3.connect("Data/Database/NFL_Kicking_Data.sqlite")
        cursor = connection.cursor()
      #  player_names(cursor.execute('SELECT * FROM "main"."2023KickingData"'))
      #  fgm_total(cursor.execute('SELECT * FROM "main"."2023KickingData"'))
        percentageMade = fgm_vs_fga(cursor.execute('SELECT * FROM "main"."2023KickingData"'))
        print(percentageMade)
        cursor.close()
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        if connection:
            connection.close()
            print('Database connection closed.')