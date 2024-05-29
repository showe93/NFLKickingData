import pdfkit
import base64

path_wkhtmltopdf = "C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


def html(FGPercentageStats):
    statement = f'Across the league, NFL kickers were successful with kicking Field Goals {FGPercentageStats[0]}% of the time. The ' \
                f'Average NFL kicker was successful between {FGPercentageStats[1]}% and {FGPercentageStats[2]}% on Field Goal Attempts. {FGPercentageStats[3]} kickers ({FGPercentageStats[4]}%) performed below ' \
                f'average, well {FGPercentageStats[5]} ({FGPercentageStats[6]}%) kickers performed above average. The remaining {FGPercentageStats[7]} ({FGPercentageStats[8]}%) kickers ' \
                f'fall in this range.'
    with open("Graphs/TotalFieldGoalPercentages.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>PDF Example</title>
    </head>
    <body>
        <p style="font-family:Arial">{0}</p>
        <img src="data:image/jpg;base64, {1}" style="width:100%;height:500px;">
    </body>
    </html>
    '''
    pdfkit.from_string(html.format(statement, encoded_string), 'results.pdf', configuration=config)
    # print(poor_percentage, elite_percentage, good_percentage)  # these add up to 100%
    # make a histogram of overall make percentage