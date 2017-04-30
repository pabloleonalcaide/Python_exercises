import webbrowser

f = open('bienvenida.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p>
<p>Estoy lanzando una web desde un programa en Python!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('bienvenida.html')
