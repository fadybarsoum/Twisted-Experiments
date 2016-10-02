import sys
sys.path.append("/home/fady/Documents/PlayGround/firsttest/src/")
import playground
from playground.network.common.Protocol import StackingTransport, StackingProtocolMixin, StackingFactoryMixin

from twisted.internet.protocol import Protocol, Factory

class PassThroughTransport(StackingTransport):
	def __init__(self, lowerTransport):
		StackingTransport.__init__(self, lowerTransport)

	def write(self, data):
		self.lowerTransport().write(data)

class PassThroughProtocol(StackingProtocolMixin, Protocol):
	def __init__(self):
		pass

	def connectionMade(self):
		higherTransport = PassThroughTransport(self.transport)

	def dataReceived(self,data):
		self.higherProtocol() and self.higherProtocol().dataReceived(plainData)

class PassThroughFactory(StackingFactoryMixin, Factory):
	protocol = PassThroughProtocol