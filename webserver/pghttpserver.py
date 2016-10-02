import sys
sys.path.append("/home/fady/Documents/PlayGround/firsttest/src/")
import playground
from playground.twisted.endpoints import GateServerEndpoint, GateClientEndpoint


from datetime import datetime as dt

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.web.http import HTTPFactory
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File

root = Resource().putChild('', File('/webserver'))
endpoint = GateServerEndpoint.CreateFromConfig(reactor, 80, "gatekey0z17z221")
endpoint.listen(Site(root))
reactor.run()
