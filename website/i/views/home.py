from flask import views
from flask import redirect
from flask import url_for, render_template

github_url = "https://github.com/pranavbaburaj/jodb"

class Index(views.MethodView):
	def get(self):
		return render_template("index.html")

	def pos(self):
		# post request
		return render_template("index.html")

class GithubRedirect():
	def get(self):
		return redirect(github_url)

	def post(self):
		return redirect(url_for("index"))