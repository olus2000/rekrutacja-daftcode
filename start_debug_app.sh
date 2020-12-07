#!/bin/bash
source venv/bin/activate
export FLASK_APP=rekrutacja
export FLASK_ENV=developement
export FLASK_DEBUG=1
flask run
