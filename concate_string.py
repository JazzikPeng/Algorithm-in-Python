string = 'aabbcddcef'
def delete_char(string):
    try:
        print(string[0] == string[0+1])
        for i in range(len(string)):
            if(string[i] == string[i+1]):
                print(string)
                string = string[:i] + string[i+2:]
                return True, string
    except IndexError:
        print('DONE')
        return False, string




t = delete_char(string)
while t:
    t, string = delete_char(string)
print(string)