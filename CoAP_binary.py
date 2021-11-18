def get_name(header_name: str, bits: str):
    
    headers = {
        'version' : version,
        'type' : type,
        'req_res_code': req_res_code
    }

    header = headers.get(header_name)

    name = [k for k,v in header.items() if v == bits]

    if len(name) > 0:
        name = name[0]
    else:
        name = "Unknown"
        
    return name

def get_bits(header_name: str, name: str):

    headers = {
        'version' : version,
        'type' : type,
        'req_res_code': req_res_code
    }

    header = headers.get(header_name)

    bits = header.get(name)

    return bits

version = {
    '0': '00',
    '1': '01',
    '2': '10',
    '3': '11',
}

type = {
    'Confirmable':'00',
    'Non-Confirmable':'01',
    'Acknowledgement':'10',
    'Reset ':'11'
}

req_res_code = {
    'EMPTY':    '00000000',
    'GET':      '00000001',
    'POST':     '00000010',
    'PUT':      '00000011',
    'DELETE':   '00000100',
    'FETCH':    '00000101',
    'PATCH':    '00000110',
    'iPATCH':   '00000111',
    'Created':  '01000001',
    'Deleted':  '01000010',
    'Valid':    '01000011',
    'Changed':  '01000100',
    'Content':  '01000101',
    'Continue': '01011111'

}