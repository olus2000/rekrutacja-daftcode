#!/bin/bash


coverage run -m pytest --html=result.html >/dev/null
coverage html
