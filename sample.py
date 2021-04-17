import socket
import json as json
from person import person

host = socket.gethostname()
port = 10000         # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
student = person('Anjalika', 35, 'Behala')
jsonString = json.dumps(student.__dict__)

s.sendall(bytes(jsonString, 'utf-8'))
s.close()