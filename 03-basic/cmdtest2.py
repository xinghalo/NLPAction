from flask import Flask

print "in cmd 2"

t = Flask(__name__, static_url_path="")

a = "123"

def init():
    #global t
    #t = "aaaa"
    print "cmd2 init"



