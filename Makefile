#!/bin/bash
.PHONY: default
.SILENT:


default:

start_app:
	serverless --template aws-python

install:
	pip3 install -r requirements.txt

node_req:
	npm install -g serverless
	npm install serverless-offline
	npm install serverless-python-requirements
	npm i -D serverless-dotenv-plugin

serverless_req:
	serverless plugin install -n serverless-offline &&	serverless plugin install -n serverless-python-requirements && serverless plugin install -n serverless-dotenv-plugin

shell:
	docker exec -it app-node python3