import webbrowser

f = open('bienvenida.html','w')

message = '<html>\n<head></head>\n<body>\n<p>Hello World!</p>\n<p>Estoy lanzando una web desde un programa en Python!</p>\n</body>\n</html>'

f.write(message)
f.close()

webbrowser.open_new_tab('bienvenida.html')
