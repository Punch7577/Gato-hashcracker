import hashlib, os


def MD5_encode(data):
    MD5_hash = hashlib.blake2b()

    MD5_hash.update(data.encode('utf-8'))

    hashed_data = MD5_hash.hexdigest()

    return hashed_data


def sha1_encode(data):
    sha1_hash = hashlib.sha1()

    sha1_hash.update(data.encode('utf-8'))

    hashed_data = sha1_hash.hexdigest()

    return hashed_data


def sha224_encode(data):
    sha224_hash = hashlib.sha224()

    sha224_hash.update(data.encode('utf-8'))

    hashed_data = sha224_hash.hexdigest()

    return hashed_data


def sha256_encode(data):
    sha256_hash = hashlib.sha256()

    sha256_hash.update(data.encode('utf-8'))

    hashed_data = sha256_hash.hexdigest()

    return hashed_data


def sha384_encode(data):
    sha384_hash = hashlib.sha384()

    sha384_hash.update(data.encode('utf-8'))

    hashed_data = sha384_hash.hexdigest()

    return hashed_data


def sha512_encode(data):
    sha512_hash = hashlib.sha512()

    sha512_hash.update(data.encode('utf-8'))

    hashed_data = sha512_hash.hexdigest()

    return hashed_data


def hashfile(word):
    if os.path.exists('hashes'):
        with open('hashes', 'r') as hash_fileread:
            hashes = hash_fileread.readlines()
            for hash in hashes:
                if hash.strip() == MD5_encode(word):
                    print(f'* MD5 HASH CRACKED: {hash} = {word}', '\n')
                elif hash.strip() == sha512_encode(word):
                    print(f'* SHA-512 HASH CRACKED: {hash} = {word}', '\n')
                elif hash.strip() == sha384_encode(word):
                    print(f'* SHA-384 HASH CRACKED: {hash} = {word}' '\n')
                elif hash.strip() == sha256_encode(word):
                    print(f'* SHA-256 HASH CRACKED: {hash} = {word}', '\n')
                elif hash.strip() == sha224_encode(word):
                    print(f'* SHA-224 HASH CRACKED: {hash} = {word}', '\n')
                elif hash.strip() == sha1_encode(word):
                    print(f'* SHA-1 HASH CRACKED: {hash} = {word}', '\n')
                elif hash.strip() != MD5_encode(word) or sha512_encode(word) or sha384_encode(word) or sha256_encode(word) or sha224_encode(word) or sha1_encode(word):
                    pass
    else:
        print('You have not provided a list of hashes. Please provide a list of hashes to use the software.')


def wordlistopen():
    if os.path.exists('Wordlist'):
        with open('Wordlist', 'r') as wordlist:
            passwords = wordlist.readlines()
            for password in passwords:
                hashfile(password.strip())
    else:
        print('There is no wordlist. Please specify a wordlist.')

wordlistopen()
