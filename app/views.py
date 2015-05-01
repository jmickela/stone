import unittest

from flask import jsonify

from app import app
from tests import SomeTest

@app.route('/')
def index():
	return ""

@app.route('/api/<string:project>/run-test/<string:test_name>')
def run_test(project, test_name):

	method = getattr(SomeTest(test_name), test_name, None)
	if callable(method):
		suite = unittest.TestSuite()

		try:
			test = SomeTest('test_image')
			suite.addTest(test)
		except:
			return jsonify({'status': 'failed', 'error_text': "Couldn't add test"})

		response = None
		try:
			response = unittest.TextTestRunner().run(suite)
		except Exception as e:
			return jsonify({"status": "failed"})

		return jsonify({"status": "passed"})
	return jsonify({'status': 'failed', 'error_text': 'Method not found'})