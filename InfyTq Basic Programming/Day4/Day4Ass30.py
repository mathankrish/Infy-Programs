# Run Length Encoding
def encode(message):
    wordsize = 0
    encode_msg = ''  # it is used to display when the message is null string

    for i in range(len(message)):
        ch = message[i]
        wordsize = wordsize + 1

        if (i == len(message) - 1):  # if it is the last character
            encode_msg = encode_msg + str(wordsize) + ch
            break
        else:
            if (ch == message[i + 1]):  # if the next character is same as the ch for eg:aa
                pass
            else:  # if the next charcter is different as the ch Eg:ab
                encode_msg = encode_msg + str(wordsize) + ch  # encode_msg must be used to join all the strings
                wordsize = 0

    return encode_msg


encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)