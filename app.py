from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/kshitij")
def index():
	name=request.args.get('name')
	age=request.args.get('age')
	#print(requests.args)
	#return "<h1>helo {} your age is{} <h1>".format(name,age)
	return render_template("index.html",name=name,age=age)


@app.route("/login", methods=['GET','POST'])
def login():
	if request.method =='GET':
		return render_template("login.html")
	else:
		username=request.form.get('username')
		password=request.form.get('password')
		if username == password:
			return "success"
		else:
			return "incorrect"

if __name__=="__main__":
	app.run(use_reloader=True,debug=True)

