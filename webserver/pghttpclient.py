import sys
sys.path.append("/home/fady/Documents/PlayGround/firsttest/src/")
import playground
from playground.twisted.endpoints import GateServerEndpoint, GateClientEndpoint

#import StringIO

from twisted.internet import reactor
from twisted.web.client import Response, getPage
from twisted.web.http import HTTPClient
from twisted.internet.endpoints import connectProtocol


def callBack(p):
	p.sendCommand("GET","index.html")
	reactor.callLater(2, p.printResponse)

def printResponse(p):
	print(p.__buffer.getvalue())
	if reactor.running:
		reactor.stop()

if len(sys.argv) < 2:
    print("No arguments given. Quitting...")
else:
    point = GateClientEndpoint.CreateFromConfig(reactor, "20164.0.17.221", 80, "gatekey0z17z223")
    #d = getPage("127.0.0.1:45756" + sys.argv[1])
    d = connectProtocol(point, HTTPClient())
    d.addCallback(callBack)
    reactor.run()
