from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.web.http import HTTPFactory
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File

root = File('/home/fady/Documents/GitRepo/twisted-experiments/webcontents')
endpoint = TCP4ServerEndpoint(reactor, 80)
d = endpoint.listen(Site(root))
reactor.run()
