operation = input("Do you want to encode or decode? ")

if operation == "encode":
    message = input("Enter the message to Encode: ")

    if len(message) > 3:
        first_ch = message[0]
        rem_msg = message[1:]
        new_msg = rem_msg + first_ch  # Use + to join strings
        print("Encoded message:", new_msg)
    else:
        for c in range(1, len(message) + 1):
            print(message[-c], end="")  # print from back

else:
    message1 = input("Enter the message to Decode: ")

    if len(message1) > 3:
        last_char = message1[-1]      # Correct way to get last character
        rem_msg = message1[:-1]
        new_msg = last_char + rem_msg  # Join last char + rest of string
        print("Decoded message:", new_msg)
    else:
        for f in range(1, len(message1) + 1):
            print(message1[-f], end="")  # print from back
