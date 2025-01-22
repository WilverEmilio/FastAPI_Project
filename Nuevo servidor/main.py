from jinja2 import Environment, FileSystemLoader

from wsgiref.simple_server import make_server


def application(env, start_response):
    headers = [('Content-Type', 'text/html')]
    
    start_response('200 OK', headers)
    
    env = Environment(loader=FileSystemLoader('templates'))
    
    template = env.get_template('index.html')
    
    HTML = template.render(
        {
            'title': 'Mi primer servidor',
            'name': 'Jorge',
        }
    )
    
    return  [bytes(HTML, 'utf8')]

server = make_server('localhost', 8000, application)
server.serve_forever()    