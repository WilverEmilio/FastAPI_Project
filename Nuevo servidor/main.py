from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [('Content-Type', 'text/plain')]
    
    start_response('200 OK', headers)
    
    return ['Hola mundo desde mi primer servidor en Python.'.encode('utf-8')]

server = make_server('localhost', 8000, application)
server.serve_forever()    