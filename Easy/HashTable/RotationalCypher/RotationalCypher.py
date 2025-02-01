


def rotationalCipher(input_str, rotation_factor):
    result = ""
    for i, v in enumerate(input_str):
        if v.isalpha():
            t = ord(v.lower()) - 96
            new_t = (t + rotation_factor) % 26
            if new_t == 0:
                new_t = 26
            new_char = chr(new_t + 96)
            if v.isupper():
                new_char = new_char.upper()
            result += new_char
        elif v.isnumeric():
            result += str((int(v) + rotation_factor) % 10)
        else:
            result += v
    return result


rotationalCipher("Zebra-493?", 3)
rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39)