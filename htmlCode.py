import pdfkit
import base64

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


def html(FGPercentageStats):
    statement1 = f'Across the league, NFL kickers were successful with kicking Field Goals {FGPercentageStats[0]}% of the time. The ' \
                f'Average NFL kicker was successful between {FGPercentageStats[1]}% and {FGPercentageStats[2]}% on Field Goal Attempts. {FGPercentageStats[3]} kickers ({FGPercentageStats[4]}%) performed below ' \
                f'average, well {FGPercentageStats[5]} kickers ({FGPercentageStats[6]}%) performed above average. The remaining {FGPercentageStats[7]} kickers ({FGPercentageStats[8]}%) ' \
                f'fall in this range.'

    with open("Graphs/TotalFieldGoalPercentages.jpg", "rb") as image_file:
        encoded_string1 = base64.b64encode(image_file.read()).decode("utf-8")

    statement2 = (f'Another way we can view this data is with a histogram. The histogram will show us any skews that might appear within our data/where the outliers are. If...<br>'
                  f'&#x2022; The red tower(left) and the green tower(right) are roughly the same, then the graph is roughly symmetrical and we have a similar amount of outliers in either direction<br>'
                  f'&#x2022; The red tower is taller than the green tower, then their are more outliers that fall in the below average range<br>' 
                  f'&#x2022; The green tower is taller than the red tower, than their are more outliers that fall in the above average range<br>')

    with open("Graphs/TotalFieldGoalSDComparison.jpg", "rb") as image_file:
        encoded_string2 = base64.b64encode(image_file.read()).decode("utf-8")

    statement3 = f'Below is the list of individuals kickers listed by name in each category...'

    with open("Graphs/KickerNamesTotalFieldGoal.jpg", "rb") as image_file:
        encoded_string3 = base64.b64encode(image_file.read()).decode("utf-8")

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
        <p>{2}</p>
        <img src="data:image/jpg;base64, {3}">
        <hr>
        <footer>
            <div class="footer">
                &copy; Sean Howe 2024
            </div>
        </footer>
        <div class="page-break"></div>
        <p>{4}</p>
        <hr>
        <img src = "data:image/jpg;base64, {5}">
        <hr>
        <footer>
            <div class="footer">
                &copy; Sean Howe 2024
            </div>
        </footer>
        <div class="page-break"></div>
    </body>
    </html>
    '''
    css = 'format.css'


    pdfkit.from_string(html.format(statement1, encoded_string1, statement2, encoded_string2, statement3, encoded_string3), 'results.pdf', configuration=config, css=css)
    # print(poor_percentage, elite_percentage, good_percentage)  # these add up to 100%
    # make a histogram of overall make percentage