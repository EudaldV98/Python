import sys


morse_code_dict = {
    'A' : '.-', 'B' : '-...', 'C' : '-.-.',
    'D' : '-..', 'E' : '.', 'F' : '..-.',
    'G' : '--.', 'H' : '....', 'I' : '..',
    'J' : '.---', 'K' : '-.-', 'L' : '.-..',
    'M' : '--', 'N' : '-.', 'O' : '---',
    'P' : '.--.', 'Q' : '--.-', 'R' : '.-.',
    'S' : '...', 'T' : '-', 'U' : '..-',
    'V' : '...-', 'W' : '.--', 'X' : '-..-',
    'Y' : '-.--', 'Z' : '--..',
    '1' : '.----', '2' : '..---', '3' : '...--',
    '4' : '....-', '5' : '.....', '6' : '-....',
    '7' : '--...', '8' : '---..', '9' : '----.',
    '0' : '-----'}

def encrypt(message):
    message = message.upper()
    result = ''
    for c in message:
        if c != ' ':
            result += morse_code_dict[c] + ' '
        else:
            result += ' '
    return result

def decrypt(message):
    message += ' '
    result = ''
    text = ''
    for c in message:
        if (c != ' '):
            i = 0
            text += c
        else:
            i += 1
            if i == 2:
                result += ' '
            else:
                result += list(morse_code_dict.keys())[list(
                    morse_code_dict.values()).index(text)]
                text = ''
    return result

#if all(i.isalnum() or i.isspace() for i in sys.argv[1]):
print(encrypt(sys.argv[1]))
#else:
#    print('ERROR')
#    sys.exit(0)
