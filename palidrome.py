def is_palidrome(string):
    return string == string[::-1]


def main():
    print(is_palidrome('alma'))
    print(is_palidrome('görög'))

if __name__ == '__main__':
    main()