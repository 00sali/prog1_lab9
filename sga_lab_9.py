def encode(password):
    encode_list = ''
    for i in password:
        i = int(i)
        x = i + 3
        if x >= 10:
            x = x % 10
        encode_list += x
    return encode_list

def decode(password):