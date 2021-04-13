string = 'Hi! My name is Olga'

def reverse(string):
    if type(string) is not str:
        return 'Restart with a string'
    return string[::-1]

print(reverse([]))