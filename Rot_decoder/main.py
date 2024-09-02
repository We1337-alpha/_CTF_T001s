def rot_cipher_decode(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decoded_text += char
    return decoded_text

def rot47_decode(text):
    decoded_text = ""
    for char in text:
        if 33 <= ord(char) <= 126:
            decoded_text += chr(33 + ((ord(char) - 33 + 47) % 94))
        else:
            decoded_text += char
    return decoded_text

def decode_all_rots(text):
    decoded_versions = {}
    for shift in range(1, 26):
        decoded_versions[f"ROT-{shift:02}"] = rot_cipher_decode(text, shift)
    decoded_versions["ROT-47"] = rot47_decode(text)
    return decoded_versions

def print_decoded_versions(decoded_versions):
    for shift, decoded_text in decoded_versions.items():
        print(f"{shift}: {decoded_text}")

if __name__ == "__main__":
    input_text = input("Enter the text to decode: ")
    decoded_versions = decode_all_rots(input_text)
    print_decoded_versions(decoded_versions)

