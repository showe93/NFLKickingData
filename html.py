import pdfkit
path_wkhtmltopdf = "C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>PDF Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
'''

pdfkit.from_string(html_content, 'out.pdf', configuration=config)
