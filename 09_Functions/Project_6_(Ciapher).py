alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

# choose = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# if choose == "encode":
#     data = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     encoded_data = ""
#     decoded_data = ""
#     for i in data:
#         if i in alphabet:
#             postion = alphabet.index(i)
#             new_postion = postion + shift
#             if new_postion > 25:
#                 new_postion = new_postion - 26
#             else:
#                 new_postion = new_postion

#             encoded_data += (alphabet[new_postion])
#         else:
#             encoded_data += i


#     print(f"The encoded text is {encoded_data}")
            
# elif choose == "decode":
#     data = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     for i in data:
#         if i in alphabet:
#             postion = alphabet.index(i)
#             new_postion = postion - shift
#             if new_postion < 0:
#                 new_postion = new_postion + 26
#             else:
#                 new_postion = new_postion

#             decoded_data += (alphabet[new_postion])
#         else:
#             decoded_data += i
            
#     print(f"The decoded text is {decoded_data}")

# well we have completed the algorithm to encode and decode the text using ceaser cipher
# BUt we need to make it using function so that we can call it any time we want without rewriting the whole code
# so let's do it


def encode(data, shift):
    encoded_data = ""
    for i in data:
        if i in alphabet:
            postion = alphabet.index(i)
            new_postion = postion + shift
            if new_postion > 25:
                new_postion = new_postion - 26
            else:
                new_postion = new_postion

            encoded_data += (alphabet[new_postion])
        else:
            encoded_data += i


    print(f"The encoded text is {encoded_data}")

def decode(data, shift):
    decoded_data = ""
    for i in data:
        if i in alphabet:
            postion = alphabet.index(i)
            new_postion = postion - shift
            if new_postion < 0:
                new_postion = new_postion + 26
            else:
                new_postion = new_postion

            decoded_data += (alphabet[new_postion])
        else:
            decoded_data += i
            
    print(f"The decoded text is {decoded_data}")

while True :
    choose = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choose == "encode":
        data = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encode(data, shift)
        
    elif choose == "decode":
        data = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decode(data, shift)
        
    else:
        print("Invalid input")
    
    choose = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if choose == "no":
        print("Goodbye")
        break

    