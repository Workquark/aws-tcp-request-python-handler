import socketserver

class TcpHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(8192).strip()
        print("{} wrote: {}".format(self.client_address[0],self.data))
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

    # Create the server, binding to localhost on port 9999
