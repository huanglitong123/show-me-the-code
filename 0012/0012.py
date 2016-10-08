# -*- coding: utf-8 -*-


def filter_word(path):
    with open(path, 'r')as f:
        filter = [line.rstrip() for line in f]
    while True:
        text = raw_input("please input:")
        if text == 'exit':
            break
        for x in filter:
            if x in text:
                print len(x)
                text = text.replace(x, '*'*len(x))
        print text

filter_word('filtered_words.txt')
