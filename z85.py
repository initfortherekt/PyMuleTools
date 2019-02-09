import re

decoders = [
            0x00, 0x44, 0x00, 0x54, 0x53, 0x52, 0x48, 0x00, 0x4B, 0x4C, 0x46, 0x41, 0x00, 0x3F, 0x3E, 0x45,
            0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x40, 0x00, 0x49, 0x42, 0x4A, 0x47,
            0x51, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32,
            0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x4D, 0x00, 0x4E, 0x43, 0x00,
            0x00, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
            0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x4F, 0x00, 0x50, 0x00, 0x00
]

encoders = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '.', '-', ':', '+', '=', '^', '!', '/', '*', '?', '&', '<', '>', '(', ')', '[', ']', '{',
            '}', '@', '%', '$', '#'
]

regex_z85 = re.compile("^[0-9A-Za-z\\.\\-:\\+\\=\\^!\\/\\*\\?&<>\\(\\)\\[\\]\\{\\}\\@%\\$\\#]+$")
regex_hex = re.compile("^[0-9A-Fa-f]+$")


def is_z85(payload):
    return True if regex_z85.match(payload) and regex_hex.match(payload) is None else False


def encode(payload_as_bytes):
    remainder = len(payload_as_bytes) % 4
    padding = 4 - remainder if remainder > 0 else 0
    value = 0
    ret = []
    for i in range(0, len(payload_as_bytes) + padding):
        is_padding = i >= len(payload_as_bytes)

        value = value * 256 + (0 if is_padding else payload_as_bytes[i] & 0xFF)
        if (i + 1) % 4 == 0:
            div = pow(85, 4)
            for j in reversed(range(1, 6)):
                if not is_padding or j > padding:
                    code = (value // div) % 85
                    ret.append(encoders[code])

                div = div // 85
            value = 0

    return ''.join(ret)


def decode(s):
    remainder = len(s) % 5;
    padding = 5 - (5 if remainder == 0 else remainder)
    for p in range(0, padding):
        s += encoders[len(encoders) - 1];

    length = len(s)
    ret = [None] * ((length * 4 // 5) - padding)
    index = 0
    value = 0
    for i in range(0, length):
        code = ord(s[i]) - 32
        value = value * 85 + decoders[code];
        if (i + 1) % 5 == 0:
            div = pow(256, 3)
            while div >= 1:
                if index < len(ret):
                    ret[index] = ((value // div) % 256)
                    index = index + 1

                div = div // 256

            value = 0

    return bytes(ret)
