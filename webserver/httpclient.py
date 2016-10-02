from twisted.internet import reactor
from twisted.web.client import Response, getPage
from twisted.web.http import HTTPClient
from twisted.internet.endpoints import connectProtocol, TCP4ClientEndpoint


def printResponse(data):
	print("callBack")
	print(data)
	if reactor.running:
		reactor.stop()

if len(sys.argv) < 2:
    print("No arguments given. Quitting...")
else:
    d = getPage("http://127.0.0.1/" + sys.argv[1])
    print(d)
    d.addCallback(printResponse)
    reactor.run()
