# cipher.py
def encode_message(message, shift):
    """Encodes a message by shifting each letter by 'shift' positions."""
    encoded = ""
    for char in message:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_base + shift) % 26 + ascii_base
            encoded += chr(shifted)
        else:
            encoded += char
    return encoded

def decode_message(encoded_message, shift):
    """Decodes a message by reversing the shift."""
    return encode_message(encoded_message, -shift)

def hide_in_sentence(encoded_message):
    """Hides the encoded message in a fake sentence."""
    fake_words = ["The", "quick", "brown", "fox", "jumps", "over"]
    import random
    hidden = " ".join(random.choice(fake_words) for _ in range(3)) + " " + encoded_message
    return hidden