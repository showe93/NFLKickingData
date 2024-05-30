import pdfkit
import base64

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


def html(FGPercentageStats):
    statement = f'Across the league, NFL kickers were successful with kicking Field Goals {FGPercentageStats[0]}% of the time. The ' \
                f'Average NFL kicker was successful between {FGPercentageStats[1]}% and {FGPercentageStats[2]}% on Field Goal Attempts. {FGPercentageStats[3]} kickers ({FGPercentageStats[4]}%) performed below ' \
                f'average, well {FGPercentageStats[5]} kickers ({FGPercentageStats[6]}%) performed above average. The remaining {FGPercentageStats[7]} kickers ({FGPercentageStats[8]}%) ' \
                f'fall in this range.'
    with open("Graphs/TotalFieldGoalPercentages.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NFL Kicking Results</title>
    </head>
    <body>
        <div class="header-container">
           <h1>NFL Data</h1>
        </div>
        <div class="page-break"></div>
        <p>{0}</p>
        <hr>
        <img src="data:image/jpg;base64, {1}">
        <hr>
    </body>
    </html>
    '''
    css = 'format.css'
    pdfkit.from_string(html.format(statement, encoded_string), 'results.pdf', configuration=config, css=css)
    # print(poor_percentage, elite_percentage, good_percentage)  # these add up to 100%
    # make a histogram of overall make percentage