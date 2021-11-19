import CoAP_binary

def decode_packet(packet: bytes):

    decoded_packet = []

    packet_length = len(packet)
    #print(f'Packet length: {packet_length}')

    if len(packet) < 4:
        return "Too small packet"


    octet_0 = packet[0]
    octet_0_bits = format(octet_0, '08b')

    # Version
    version_bits = octet_0_bits[:2]
    version = CoAP_binary.get_name('version', version_bits)
    decoded_packet.append('Version: ' + version)

    # Type
    type_bits = octet_0_bits[2:4]
    type = CoAP_binary.get_name('type', type_bits)
    decoded_packet.append('Type: ' + type)

    # Token length
    token_length_bits = octet_0_bits[4:8]
    token_length = str(int(token_length_bits,2))
    decoded_packet.append('Token length: ' + token_length)

    # Response code
    octet_1 = packet[1]
    octet_1_bits = format(octet_1, '08b')
    response_code = CoAP_binary.get_name('req_res_code', octet_1_bits)
    decoded_packet.append('Response code: ' + response_code)

    # Message ID
    octet_2 = packet[2]
    octet_2_bits = format(octet_2, '08b')
    octet_3 = packet[3]
    octet_3_bits = format(octet_3, '08b')
    message_id_bits = octet_2_bits + octet_3_bits
    message_id = str(int(message_id_bits,2))
    decoded_packet.append('Message ID: ' + message_id)

    if len(packet) == 4:
        return [version, type, token_length, response_code, message_id]

    current_byte = 4

    # Token
    if int(token_length) > 0:
        token_octets = packet[current_byte:current_byte+int(token_length)]
        token_bits = format(token_octets, f'0{str(8*int(token_length))}b')
        token = str(int(token_bits,2))
        current_byte += 1
    else:
        token = ''
    decoded_packet.append('Token: ' + token)

    # Options
    octet_option = packet[current_byte]
    current_byte += 1

    octet_option_bits = format(octet_option, '08b')
    option_delta = int(octet_option_bits[:4],2)
    option_length = int(octet_option_bits[4:],2)

    # Option Delta Extended check
    if option_delta <= 12:
        option = str(option_delta)
        decoded_packet.append('Option: ' + option)
    elif option_delta == 13:
        octet_5 = packet[current_byte]
        current_byte += 1
        option_delta_bits = format(octet_5, '08b')
        option_delta_extended = int(option_delta_bits, 2)
        option = str(option_delta_extended + 13)
        decoded_packet.append('Option: ' + option)
    elif option_delta == 14:
        octet_5 = packet[current_byte]
        current_byte += 1
        octet_5_bits = format(octet_5, '08b')

        octet_6 = packet[current_byte]
        current_byte += 1
        octet_6_bits = format(octet_6, '08b')

        option_delta_bits = octet_5_bits + octet_6_bits
        option_delta_extended = int(octet_5_bits + octet_6_bits, 2)
        option = str(option_delta_extended + 269)
        decoded_packet.append('Option: ' + option)

    if option_length <= 12:
        pass
    elif option_length == 13:
        octect_option_length_1 = packet[current_byte]
        current_byte += 1
        octect_option_length_1_bits = format(octect_option_length_1, '08b')

        option_length = int(octect_option_length_1_bits, 2)
        option_length = option_length + 13
    elif option_length == 14:
        octect_option_length_1 = packet[current_byte]
        current_byte += 1
        octect_option_length_1_bits = format(octect_option_length_1, '08b')

        octect_option_length_2 = packet[current_byte]
        current_byte += 1
        octect_option_length_2_bits = format(octect_option_length_2, '08b')

        option_length_bits = octect_option_length_1_bits + octect_option_length_2_bits
        option_length = int(option_length_bits, 2)
        option_length = option_length + 269

    # Get option value
    option_value = packet[current_byte:current_byte+option_length]
    current_byte += option_length
    decoded_packet.append('Option value next')
    decoded_packet.append(option_value)

    # ???? 10000000
    payload_found = False
    payload = ''
    while payload_found == False and current_byte < packet_length:
        octet_next = packet[current_byte]
        current_byte += 1

        if octet_next != 255:
            continue
    
        if octet_next == 255:
            payload = octet_next
            payload_found = True

    if payload_found == False:
        return decoded_packet
    else:
        payload = packet[current_byte:]
        decoded_packet.append('Payload: ' + payload.decode())
        return decoded_packet
