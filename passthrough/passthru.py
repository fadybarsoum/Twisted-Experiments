import sys
sys.path.append("/home/fady/Documents/PlayGround/firsttest/src/")
import playground
from playground.network.common.Protocol import StackingTransport, StackingProtocolMixin, StackingFactoryMixin
from playground.network.message.ProtoBuilder import MessageDefinition
from playground.network.message.StandardMessageSpecifiers import STRING

from twisted.internet.protocol import Protocol, Factory

class PassThroughMessage(MessageDefinition):
    PLAYGROUND_IDENTIFIER = "apps.samples.passthru.PassThroughMessage"
    MESSAGE_VERSION = "1.0"
    
    BODY = [ ("data", STRING) ]
    
class PassThroughTransport(StackingTransport):
    def __init__(self, lowerTransport):
        StackingTransport.__init__(self, lowerTransport)

    def write(self, data):
        ptMessage = PassThroughMessage()
        ptMessage.data = data
        self.lowerTransport().write(ptMessage.__serialize__())

class PassThroughProtocol(StackingProtocolMixin, Protocol):
    def __init__(self):
        self.buffer = ""

    def connectionMade(self):
        higherTransport = PassThroughTransport(self.transport)
        self.makeHigherConnection(higherTransport)

    def dataReceived(self,data):
        self.buffer += data
        try:
            ptMessage, bytesUsed = PassThroughMessage.Deserialize(data)
            self.buffer = self.buffer[bytesUsed:]
        except Exception, e:
            #print "We had a deserialization error", e
            return

        self.higherProtocol() and self.higherProtocol().dataReceived(ptMessage.data)
        self.buffer and self.dataReceived("")

class PassThroughFactory(StackingFactoryMixin, Factory):
    protocol = PassThroughProtocol
	
ConnectFactory = PassThroughFactory
ListenFactory = PassThroughFactory
