def app(environ, start_response):
    qs = environ['QUERY_STRING']
    resp = [par + '\n' for par in qs.split('&')]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return  resp
