from flask import Flask, render_template, json
from ConfigParser import SafeConfigParser
import sys
import requests
from requests.auth import HTTPDigestAuth


app = Flask(__name__)


#load properties
def load_properties(env, pproperty):
	try:
		parser = SafeConfigParser()
		parser.read('conf/environ.properties')
		vproperty = parser.get(str(env), str(pproperty))
		return vproperty
	except Exception as ex_prop:
		print "Error______: " + str(ex_prop)

#call to trivifree_api
def get_question(question_id):

	try:
		url = load_properties('local','url')
		#url = 'http://127.0.0.1:5000/trivifree/api/v1/quest/1'
		response = requests.get(url + str(question_id))
		#response = requests.get(url)
		print "Antes de llamar a la api"
		if response.status_code == 200:
			jData = response.json()
			print "Devuelve un 200_____________-"
			print jData
			return jData
		else:
			return None
	except Exception as ex:
		print "Error_____________________: " + str(ex)




@app.route("/")
def main():
    #return "Welcome!"
    #return render_template('index.html', option1 = 'pepe', option2 = 'juan', option3 = 'pedro', question = 'Who is?')
    return render_template('index.html')

@app.route('/ajax/<question_id>', methods = ['POST'])
def ajax_request(question_id):
	#username = request.form['username']
	jsondata = get_question(question_id)
	print "Retornado el valor a /ajax__________________________--"
	return json.dumps(jsondata)
	#return json.dumps({'option1':'OPTION_1','option2': 'OPTION_2','option3': 'OPTION_3'});


if __name__ == "__main__":
    app.run(port="5001")