from calculations import calculations
import sqlite3

if __name__ == '__main__':
    try:
        connection = sqlite3.connect("Data/Database/NFL_Kicking_Data.sqlite")
        cursor = connection.cursor()
        data = cursor.execute('SELECT * FROM "main"."2023KickingData"').fetchall()
        calculations(data)
        cursor.close()
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        if connection:
            connection.close()
            print('Database connection closed.')