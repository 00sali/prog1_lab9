def encode(password):
    encode_list = ''
    for i in password:
        x = int(i) + 3
        if x >= 10:
            x = x % 10
        encode_list += str(x)
    return encode_list

def decode(password):
    decodedPass = ""
    for i in password:
        x = int(i) - 3
        if x < 0:
            x = x + 10
        decodedPass += str(x)
    return decodedPass

