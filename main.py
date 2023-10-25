def encode(password):
    return ''.join(str((int(i) + 3) % 10) for i in password)

def decode(password):
    return ''.join(str((int(i) - 3) % 10) for i in password)

def main():
    encoded = None
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        answer = int(input("Please enter an option: "))
        if answer == 1:
            encoded = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif answer == 2:
            if encoded is None:
                print("No password has been encoded!\n")
            else:
                decoded = decode(encoded)
                print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
        elif answer == 3:
            break

if __name__ == "__main__":
    main()
