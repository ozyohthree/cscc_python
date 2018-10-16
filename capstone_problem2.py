cipher_symbols = 'abcdefghijklmnopqrstuvwxyz'

def cipher(char):
    if char in cipher_symbols:
        return cipher_symbols[(cipher_symbols.index(char) + 13) % len(cipher_symbols)]
    else:
        return char


def encrypt(string):
    encrypted = ''
    for char in string:
        encrypted += cipher(char)
    return encrypted


if __name__ == '__main__':
    secret_message = encrypt('the password is secret')
    print(secret_message)
    secret_secret = encrypt(secret_message)
    print(secret_secret)


advisory_list.append([
            item('td')[1].find('a').text.strip(),                       # 0: advisory ID
            item('td')[1].find('a')['href'],                            # 1: advisory URL
            parser.parse(item('td')[2].text.strip(), fuzzy=True),       # 2: published date
            item('td')[3].text.strip(),                                 # 3: severity
            item('td')[4].find('a').text.strip()                        # 4: advisory title
        ])


