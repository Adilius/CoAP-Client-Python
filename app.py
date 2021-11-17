import socket
import CoAP_encoder
import CoAP_decoder
import CoAP_binary

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


#print(f'{bit_packet=}')
bytes_packet = int(bit_packet,2).to_bytes(9, byteorder='big')
#print(f'{bytes_packet=}')

built_packet = CoAP_encoder.build_packet('GET', 11, 'test')

client_socket.send(built_packet)

recieved_data = client_socket.recv(1024)
print(f'{recieved_data=}')

#print(CoAP_encoder.build_packet('GET', 11, 'test'))

decoded_packet = CoAP_decoder.decode_packet(recieved_data)
print(decoded_packet)

version = CoAP_binary.get_name('version', '01')
print(version)

version_bits = CoAP_binary.get_bits('version', 'Version 1')
print(version_bits)