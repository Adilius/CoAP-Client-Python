import socket
import CoAP_encoder
import CoAP_decoder

HOSTNAME = "coap.me"
PORT = 5683

# Connect to coap.me
ip_address = socket.gethostbyname(HOSTNAME)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)
client_socket.connect((ip_address, PORT))

method = input('Enter method in uppercase: ')
path = input('Enter path: ')
if method in ['GET','DELETE']:
    payload = ''
else:
    payload = input('Enter payload: ')

# Build & send packet
built_packet = CoAP_encoder.build_packet(
    method = method,
    option = 11,
    option_value = path,
    payload = payload)


client_socket.send(built_packet)

# Recieve packet
try:
    recieved_data = client_socket.recv(1024)
except TimeoutError:
    print('Recieving packet timed out...')
else:
    #print(f'{recieved_data=}')

    # Decode & print packet
    decoded_packet = CoAP_decoder.decode_packet(recieved_data)
    print(decoded_packet[-1:])
