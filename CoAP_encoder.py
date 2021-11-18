import CoAP_binary

def build_packet(
    method: str,
    option: int,
    option_value: str,
    payload: str):

    packet = ''

    # Version
    version = CoAP_binary.get_bits('version', '1')
    packet += version

    # Type
    message_type = CoAP_binary.get_bits('type', 'Confirmable')
    packet += message_type

    # Token length
    token_length = "0000"
    packet += token_length

    # Request code
    method = CoAP_binary.get_bits('req_res_code', method)
    packet += method

    # Message ID
    message_id = "0000000000000000"
    packet += message_id

    # Option delta & option delta extended
    option_delta = ""
    option_delta_extended = ""
    if 0 <= option or option <= 12:
        option_delta = int_to_bits(option, 4)
    elif 13 <= option or option <= 268:
        option_delta = int_to_bits(13, 4)
        option_delta_extended = int_to_bits(option - 13, 8)
    else:
        option_delta = int_to_bits(14, 4)
        option_delta_extended = int_to_bits(option - 269, 16)
    packet += option_delta

    # Option length
    value_length = len(option_value)
    option_length = ""
    option_length_extended = ""
    if 0 <= value_length or value_length <= 12:
        option_length = int_to_bits(value_length, 4)
    elif 13 <= option or option <= 268:
        option_length = int_to_bits(13, 4)
        option_length_extended = int_to_bits(value_length - 13, 4)
    else:
        option_length = int_to_bits(14, 4)
        option_length_extended = int_to_bits(value_length - 169, 4)
    packet += option_length
    packet += option_delta_extended
    packet += option_length_extended


    # Option Value
    if value_length != 0:
        option_value = string_to_bits(option_value)
        packet += option_value

    # If we have payload
    if payload:
        packet += "11111111" #payload marker
        packet += string_to_bits(payload)   #add payload

    encoded_packet = int(packet, 2).to_bytes((len(packet) + 7) // 8, byteorder='big')
    print(f'Sent packet: {encoded_packet}')
    print((
        ''
    ))

    return encoded_packet


def int_to_bits(value: int, length: int):
    bits = format(value, f"0{length}b")
    return bits


def string_to_bits(string: str):
    bits = [bin(ord(x))[2:].zfill(8) for x in string]
    bit_string = ""
    for char in bits:
        bit_string += char
    return bit_string
