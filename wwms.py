import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

import cooperhewitt.api.client

access_token = os.environ['CH_API_KEY']
hostname = os.environ['CH_API_HOST']

@app.route('/')
def what_would_micah_say():
	api = cooperhewitt.api.client.OAuth2(access_token, hostname=hostname)
	method = 'cooperhewitt.labs.whatWouldMicahSay'
	args = {}

	rsp = api.call(method, **args)

	return render_template('index.html', title="What would Micah say?", says=rsp['micah']['says'])	