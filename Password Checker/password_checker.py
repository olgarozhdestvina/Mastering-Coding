import sys
import requests
import hashlib

# connect to the pwned api
def request_api_data(query_char):
    url ='https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code !=200:
        raise RuntimeError(f'{response.status_code}, check the API and try again')
    return response


# split the hashed response to return leak count
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    #return hashes
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check if the password exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(sha1password)
    first5_char, tail = sha1password[:5], sha1password[5:]

    # Reads all hashed passwords that match the first 5 characters 
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# loop through input passwords and check each
def main(passwords):
    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... You should change it!')
        else:
            print(f'{password} was not FOUND. It is quite good!')
    return 'done!'

    
if __name__ == '__main__':    
   sys.exit(main(sys.argv[1:]))
