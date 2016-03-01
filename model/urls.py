from bottle.bottle import route, run, debug, template
from traitement import traitement

@route('/test')
def test():
	return ("test, c'est bon j'ai reussi a faire fonctionnner un serveur je suis trop content je ne sais pas qoui faire d'autre")

@route('/')
def index():
    t = traitement()
    activites = t.getActivites()
    villes = t.getVilles()
    output = template('index', activites = activites, villes = villes)
    return output

run(host="localhost", port=8000, debug=True)
