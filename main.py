from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

end = "The End"

@app.route('/')
def hello_world():
	return render_template('start.html')

@app.route('/user/', methods=['GET','POST'])
def user():
	result = request.form['name']
	return redirect(url_for('state1',name = result))

@app.route('/user/<name>')
def show_user_profile(name):
	return 'User %s' % name

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/projects/')
def projects():
	return 'The projects page'

@app.route('/about')
def about():
	return 'The about page'


@app.route('/S1/<name>')
def state1(name):
	return render_template('s1.html', name = name)

@app.route('/C1/')
def case1_1():
	return


if __name__ == '__main__':
	app.run(debug=True)
