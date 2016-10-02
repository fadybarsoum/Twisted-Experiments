import sys
sys.path.append("/home/fady/Documents/PlayGround/firsttest/src/")
import playground
from playground.twisted.endpoints import GateServerEndpoint, GateClientEndpoint

#import StringIO

from twisted.internet import reactor
from twisted.web.client import Response, getPage, HTTPClientFactory, URI, HTTPPageGetter
from twisted.internet.endpoints import connectProtocol


def callBack(data):
	print(data)
	if reactor.running:
		reactor.stop()

if len(sys.argv) < 2:
    print("No arguments given. Quitting...")
else:
	url = "http://20164.0.17.221/" + sys.argv[1]
	uri = URI.fromBytes(url)
	point = GateClientEndpoint.CreateFromConfig(reactor, "20164.0.17.221", 80, "gatekey0z17z223")

	factory = HTTPClientFactory(url)
	point.connect(factory)
	d = factory.deferred

	d.addCallback(callBack)
	reactor.run()
