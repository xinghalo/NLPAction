import sys
import getopt
print "555"
from cmdtest2 import init,t
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
"""
https://www.cnblogs.com/kex1n/p/5975722.html



"""
print "444"
if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:],"m:",["retrain-model="])

    print "333"
    http_server = HTTPServer(WSGIContainer(t))
    http_server.listen(8000)

    # if (str(opts[0][1]).lower() == "true".lower()):
    #     retrain_model()
    print "222"
    IOLoop.instance().start()
    print "111"

opts, _ = getopt.getopt(sys.argv[1:],"m:",["retrain-model="])

if(opts[0][1] == "true"):
    init()

