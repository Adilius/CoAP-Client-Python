import CoAP_binary

def decode_packet(packet: bytes):

    print(f'Packet length: {len(packet)}')

    if len(packet) < 4:
        return "Too small packet"

    octet_0 = packet[0]
    octet_0_bits = format(octet_0, '08b')
    version_bits = octet_0_bits[:2]
    version = CoAP_binary.get_name('version', version_bits)
    type_bits = octet_0_bits[2:4]
    type = CoAP_binary.get_name('type', type_bits)
    token_length_bits = octet_0_bits[4:8]
    token_length = str(int(token_length_bits,2))

    octet_1 = packet[1]
    octet_1_bits = format(octet_1, '08b')
    response_code = CoAP_binary.get_name('req_res_code', octet_1_bits)

    octet_2 = packet[2]
    octet_2_bits = format(octet_2, '08b')
    octet_3 = packet[3]
    octet_3_bits = format(octet_3, '08b')
    message_id_bits = octet_2_bits + octet_3_bits
    message_id = str(int(message_id_bits,2))

    if int(token_length) > 0:
        token_octets = packet[4:4+int(token_length)]
        token_bits = format(token_octets, f'0{str(8*int(token_length))}b')
        pass

    return [version, type, token_length, response_code, message_id]
    pass