def main():
    openF = open("/Users/harrisonowen/bootDev/bot/books/Frankenstein.txt", "r")
    book = openF.read()
    local_word_count = get_num(book)
    local_char_count = get_chars(book)
    sortedList = sortedDict(local_char_count)


def get_chars(book):
    localV = 0
    localdic = {}
    splitWords = book.split()
    for words in splitWords:
        lower_word = words.lower()
        for characters in lower_word:
            if characters in localdic:
                localdic[characters] += 1
            else:
                localdic[characters] = 1
    return localdic


def get_num(text):
    localV = 0
    nextWord = text.split()
    for words in nextWord:
        localV += 1
    return localV


def sortedDict(dictV):
    for i in sorted(dictV.keys()):
        print(f"The '{i}', character was found {dictV[i]} times")


main()
