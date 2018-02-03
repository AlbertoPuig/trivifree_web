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
		response = requests.get(url + str(question_id))

		if response.status_code == 200:
			jData = response.json()
			return jData
		else:
			return None
	except Exception as ex:
		print "Error_____________________: " + str(ex)

#main route load template
@app.route("/")
def main():
    return render_template('index.html')
#route with param. Call backend api
@app.route('/ajax/<question_id>', methods = ['POST'])
def ajax_request(question_id):
	jsondata = get_question(question_id)
	return json.dumps(jsondata)

if __name__ == "__main__":
    app.run(port="5001")