import unittest

from flask import jsonify

from app import app
from tests import SomeTest

@app.route('/')
def index():
	return ""

@app.route('/api/<string:project>/run-test/<string:test_name>')
def run_test(project, test_name):
	if(

	)

	suite = unittest.TestSuite()

	test = SomeTest('test_image')

	suite.addTest(test)

	response = None
	try:
		response = unittest.TextTestRunner().run(suite)
	except Exception as e:
		print response
		print test

	return jsonify({"":""})