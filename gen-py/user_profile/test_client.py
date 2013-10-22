from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from ttypes import UserProfile
import UserStorage

transport = TSocket.TSocket("localhost", 9090)

# Buffering is critical. Raw sockets are very slow
transport = TTransport.TFramedTransport(transport)

# Connect
transport.open()

protocol = TBinaryProtocol.TBinaryProtocol(transport)

service = UserStorage.Client(protocol)


up = UserProfile(uid=1,
                 name="Test User",
                 blurb="Thrift is great")

service.store(up)

transport.close()
