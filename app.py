import socket
import CoAP_encoder
import CoAP_decoder
import CoAP_binary

HOSTNAME = "coap.me"
PORT = 5683

# Connect to coap.me
ip_address = socket.gethostbyname(HOSTNAME)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((ip_address, PORT))

# Build & send packet
built_packet = CoAP_encoder.build_packet(
    method = 'PUT',
    option = 11,
    option_value = 'sink',
    payload = '11')
client_socket.send(built_packet)

# Recieve packet
recieved_data = client_socket.recv(1024)
print(f'{recieved_data=}')

# Decode & print packet
decoded_packet = CoAP_decoder.decode_packet(recieved_data)
print(decoded_packet)
