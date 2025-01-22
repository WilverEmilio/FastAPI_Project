from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Primer servidor en Python</title>
</head>
<body>
    <h1>Hola mundo desde mi primer servidor en Python.</h1>
</body>
</html>
"""

def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    
    start_response('200 OK', headers)
    
    return  [bytes(HTML, 'utf8')]

server = make_server('localhost', 8000, application)
server.serve_forever()    