#  Hangman







def checking():
    from Web_Scraping.ws import words
    words = words()
    word = input('Enter a Word : ')
    if word in words:
        print('            ok')
    else :
        print('        not ok')



if __name__ == '__main__':

    while True:
        checking()
