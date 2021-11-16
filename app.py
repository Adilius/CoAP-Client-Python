import socket
import CoAP_message as COAP
import CoAP_encoder

HOSTNAME = "coap.me"
PORT = 5683

ip_address = socket.gethostbyname(HOSTNAME)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.connect((ip_address, PORT))

bit_packet = (
    '01' +                                  # Version
    '00' +                                  # Type
    '0000' +                                # Token length
    '00000001' +                            # Method
    '0000000000000000' +                    # Message ID
    '1011' +                                # Option Delta
    '0100' +                                # Option Length
    '' +                                    # Option Delta Extended
    '' +                                    # Option Length Extended
    '01110100011001010111001101110100'      # Option Value
    )


print(f'{bit_packet=}')
bytes_packet = int(bit_packet,2).to_bytes(9, byteorder='big')
print(f'{bytes_packet=}')

built_packet = CoAP_encoder.build_packet('GET', 11, 'test')

client_socket.send(built_packet)

data = client_socket.recv(1024)
print(data)

data_1 = data[0]
print(data_1)
print(format(data_1, '08b'))


#print(CoAP_encoder.build_packet('GET', 11, 'test'))