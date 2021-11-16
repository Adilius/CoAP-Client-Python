#Enum implementation
def enum(**enums):
    return type('Enum', (), enums)

VERSION = enum(
    UNSUPPORTED = "00",
    SUPPORTED = "01"
)

TYPE = enum(
    CON =       "00",
    NONCON =    "01",
    ACK =       "10",
    RESET =     "11"
)

TOKEN_LENGTH = enum(
    ZERO = "0000"
)

REQUEST_CODE = enum(
    EMPTY =     "00000000",
    GET =       "00000001",
    POST =      "00000010",
    PUT =       "00000011",
    DELETE =    "00000100"
)


MESSAGE_ID = enum(
    NONE = "0000000000000000",
    ONE = "0000000000000001",
    ID = "0000010011010010"
    
)