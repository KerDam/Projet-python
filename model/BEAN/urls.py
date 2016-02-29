from bottle.bottle import route, run

@route('/test')
def test():
	return ("test, c'est bon j'ai reussi a faire fonctionnner un serveur je suis trop content je ne sais pas qoui faire d'autre")

run(host="localhost", port=8000, debug=True)