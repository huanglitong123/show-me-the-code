# -*- coding: utf-8 -*-


def filter_word(path):
    with open(path, 'r')as f:
        filter = [line.rstrip() for line in f]

    while True:
        text = raw_input("please input:")
        print filter
        if text == 'exit':
            break
        for x in filter:
            if x in text:
                print "Freedom"
                break
        else:
            print "Human Rights"
filter_word('filtered_words.txt')
