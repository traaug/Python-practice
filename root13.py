""""
A = 65,Z = 90
a = 97,z = 122
str = "test"
"""
def root13(str):
    encoded_str = ""
    for char in str:
        encoded_char = char
        if "A" <= encoded_char <= "Z":
            encoded_char = chr(ord(encoded_char)+13)
            if encoded_char > "Z":
                encoded_char = chr(65+ord(encoded_char)-91)
        if "a" <= encoded_char <= "z":
            encoded_char = chr(ord(encoded_char)+13)
            if encoded_char > "z":
                encoded_char = chr(97+ord(encoded_char)-123)
        encoded_str += encoded_char

    return encoded_str

print(root13("test"))
