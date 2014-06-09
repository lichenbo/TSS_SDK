import sae
from flask import Flask, g, request, jsonify, render_template
import TSS.TSS as TSS

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
	return render_template('readme.html')

@app.route('/api/v1.0/course/<string:courseid>/announcement', methods=['GET'])
def announcement(courseid):
	return jsonify({'result':'ok','announcements':TSS.getCourseAnnouncement(courseid)})


@app.route('/api/v1.0/course/<string:courseid>/assignment', methods=['GET'])
def assignment(courseid):
	return jsonify({'result':'ok','assignments':TSS.getCourseAssignment(courseid)})

@app.route('/api/v1.0/user/<string:userid>/courselist', methods=['POST'])
def courselist(userid):
	if request.method == 'POST':
		password = request.form['password']
		try:
			TSS.login(userid,password)
		except TSS.InvalidUsernamePasswordError:
			return jsonify({'result':'wrong username or password'})
		if not TSS.isLogin():
			return jsonify({'result':'login error'})
		return jsonify({'result':'ok','courselist':TSS.getMyCourse()})

application = sae.create_wsgi_app(app)
