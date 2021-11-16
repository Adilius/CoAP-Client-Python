import CoAP_message as COAP


def build_packet(method: str, option: int, option_value):

    # Version
    version = COAP.VERSION.SUPPORTED

    # Type
    message_type = COAP.TYPE.CON

    # Token length
    token_length = COAP.TOKEN_LENGTH.ZERO

    # Request Method
    if method == "GET":
        method = COAP.REQUEST_CODE.GET
    if method == "POST":
        method = COAP.REQUEST_CODE.POST
    if method == "PUT":
        method = COAP.REQUEST_CODE.PUT
    if method == "DELETE":
        method = COAP.REQUEST_CODE.DELETE

    # Message ID
    message_id = COAP.MESSAGE_ID.NONE

    # Option delta & option delta extendend
    if 0 <= option or option <= 12:
        option_delta = int_to_bits(option, 4)
        option_delta_extended = ""
    elif 13 <= option or option <= 268:
        option_delta = int_to_bits(13, 4)
        option_delta_extended = int_to_bits(option - 13, 8)
    else:
        option_delta = int_to_bits(14, 4)
        option_delta_extended = int_to_bits(option - 269, 16)

    # Option length
    if isinstance(option_value, str):
        value_length = len(option_value)
    # TODO implement uint
    else:
        pass

    if 0 <= value_length or value_length <= 12:
        option_length = int_to_bits(value_length, 4)
        option_length_extended = ""
    elif 13 <= option or option <= 268:
        option_length = int_to_bits(13, 4)
        option_length_extended = int_to_bits(value_length - 13, 4)
    else:
        option_length = int_to_bits(14, 4)
        option_length_extended = int_to_bits(value_length - 169, 4)

    # Option Value
    if value_length != 0:
        option_value = string_to_bits(option_value)
        pass
    else:
        option_value = ""

    bit_packet = (
        version
        + message_type
        + token_length
        + method
        + message_id
        + option_delta
        + option_length
        + option_delta_extended
        + option_length_extended
        + option_value
    )

    byte_packet = int(bit_packet, 2).to_bytes((len(bit_packet) + 7) // 8, byteorder='big')

    return byte_packet


def int_to_bits(value: int, length: int):
    bits = format(value, f"0{length}b")
    return bits


def string_to_bits(string: str):
    bits = [bin(ord(x))[2:].zfill(8) for x in string]
    bit_string = ""
    for char in bits:
        bit_string += char
    return bit_string
