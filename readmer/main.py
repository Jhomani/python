import markdown

md = open('test.md', 'r')
text = md.read()
htmlBody = markdown.markdown(text, extensions=['fenced_code', 'tables'])

with open('test.html', 'w') as f:
  html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Backend Documantation</title>
      <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
      {htmlBody}  
    </body>
    </html>
  """ 
  f.write(html)