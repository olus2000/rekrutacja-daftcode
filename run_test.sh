#!/bin/bash


coverage run -m pytest --html=result.html | less
coverage html
