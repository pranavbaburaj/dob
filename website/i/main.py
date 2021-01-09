from flask import Flask
from views.home import Index
from flask import jsonify

app = Flask(__name__)

github_url_data = "https://github.com/pranavbaburaj/jodb"

@app.route("/api/github_url")
def github_url():
	return jsonify({"url" : github_url_data})

me = {
	"name" : "Pranav Baburaj",
	"website" : "pranavbaburaj.netlify.com"
}

cred = {
	"idea" : me,
	"created" : me,
	"url" : {
		"github" : github_url_data,
		"website" : "dobdatabase.herokuapp.com"
	}
}

@app.route("/api/credits")
def credits():
	return jsonify(cred)

app.add_url_rule("/", view_func=Index.as_view("index"))