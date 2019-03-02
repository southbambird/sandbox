#!/usr/bin/python
#-*- coding: utf-8 -*-

from bottle import route, run

@route('/hello')
def index(name):
    return '<h1>Hello</h1>'

run(host='0.0.0.0', port=8000)