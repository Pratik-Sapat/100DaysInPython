# from art import logo
# print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 



#Code Below

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1  #5 = 5*-1 = 5 if decode
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount#12+(-5)=7
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"the {cipher_direction}d text is {end_text}")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n" )
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25 #print shift before and after this line to check what id did.

    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

    result = input(f"Type 'yes' if you want to go again. otherwise type 'no'.")

    if result == "no":
        should_continue = False
        print("Good Bye!")


#comments or hints.

# simple do using 2 different function if not understand above code.

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"the decoded text is {plain_text}")


#in alphabet list we did repeat alphabet bcz we get letter like zulo then it should go forword to get encrypt letter.
#and also index will only check first apperance of repeated word.


#45%25 = 20 to get result if shift is too big


#todo - we can do some modification like on yes no encode decode word constant.