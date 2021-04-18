import socketserver
from TcpHandler import TcpHandler
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 10000
    print("start listening on {} on port {}".format(HOST,PORT))
    with socketserver.TCPServer((HOST, PORT), TcpHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
