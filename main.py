import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, original_text, shift_amount):
    new_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        # Modulo loops the list (no out of range error).
        if letter in alphabet:
            new_letter_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            new_text += alphabet[new_letter_index]
        else:
            new_text += letter

    print(f"##{encode_or_decode.upper()}D##    {new_text}    ##{encode_or_decode.upper()}D##")

print(art.logo)

want_to_continue = True
while want_to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    if input("Do you want to continue? (y/n)\n").lower() != "y":
        want_to_continue = False
    print("\n")
