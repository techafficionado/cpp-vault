#!/bin/sh
#myflaskapp is the python flask app that can be run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 myflaskapp:app
