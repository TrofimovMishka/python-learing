import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)

def get_direction():
    return input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()


def you_message():
    return input('Type your message: \n')


def you_shift():
    return int(input('Type your shift number: \n'))


def encoder(text, shift):
    result_array = []
    counter = 0

    for i in text:
        if i in alphabet:
            index = alphabet.index(i.lower())
            if index + int(shift) <= len(alphabet)-1:
                result_array.insert(counter, alphabet[index+int(shift)])
            else:
                new_index = (index + int(shift)) - len(alphabet)
                result_array.insert(counter, alphabet[new_index])
        else:
            result_array.insert(counter, i)
        counter += 1

    print(f"Here's the encoded result: {''.join(result_array)}")


def decoder(text, shift):
    result_array = []
    counter = 0

    for i in text:
        if i in alphabet:
            index = alphabet.index(i.lower())
            if index - int(shift) >= 0:
                result_array.insert(counter, alphabet[index - int(shift)])
            else:
                new_index = len(alphabet) + (index - int(shift))
                result_array.insert(counter, alphabet[new_index])
        else:
            result_array.insert(counter, i)
        counter += 1

    print(f"Here's the decoded result: {''.join(result_array)}")


is_no_finish = True

while is_no_finish:

    direction = get_direction()
    message = you_message()
    shift = you_shift()

    if direction == 'encode':
        encoder(message, shift)
    else:
        decoder(message, shift)

    if input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower() == ('no'):
        is_no_finish = False
        print('Goodbye!')
