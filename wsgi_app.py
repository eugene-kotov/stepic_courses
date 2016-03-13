from cgi import parse_qs, escape

def wsgi_application(environ, start_response):
	param = parse_qs(environ.get('QUERY_STRING', ''))
	for p in param:
		print p
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	start_response(status, headers)
	return ["\n".join(param)]