import nltk
import time
import pynput
from itertools import chain, combinations, permutations

from pynput.keyboard import Key


def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss) + 1)))


def press_word(ss):
    keyboard = pynput.keyboard.Controller()
    for i in ss:
        keyboard.press(i)
        keyboard.release(i)
    keyboard.press(Key.enter)
    return


cnv_cache = ""

while True:
    # ask for input characters
    ss = ""
    if len(cnv_cache) > 0 and cnv_cache != "":
        ss = cnv_cache
        cnv_cache = ""
    else:
        ss = input("Enter characters: ")
    # check if input is empty
    if ss == "":
        break
    # check if input is a string
    if type(ss) != str:
        print("Please enter a string")
        continue
    # check if input is a string of characters
    if not all(c.isalpha() for c in ss):
        print("Please enter a string of characters")
        continue
    # grab the list from the string as characters
    ss = list(ss)
    # count down 5 seconds
    # for i in range(5, 0, -1):
    #     print(i)
    #     time.sleep(1)
    # make sender as set
    sender = set()
    # print the subsets longer then 3
    for s in all_subsets(ss):
        if len(s) < 3:
            continue
        # get all permutations
        for p in permutations(s):
            # add to sender
            sender.add(p)
    sender_list = list(sender).sort()
    final_result = set()
    # print the sender
    for s in sender:
        # get string from tuple s
        word = "".join(s)
        # if len(word) > 6:
        # check if in the dic
        # if nltk.corpus.wordnet.synsets(word):
        # final_result.add(word)
        # else:
        final_result.add(word)

    final_result = list(final_result)
    # sort by lenth then alphabet
    final_result.sort(key=len)
    # print the final result
    print(final_result)
    # ask to help with input?
    cfm = input("Do you want to help with input? (y/n): ")
    if cfm == "y":
        # sleep for 3 seconds
        time.sleep(3)
        for item in final_result:
            press_word(item)
            time.sleep(0.01)
    elif len(cfm) > 0:
        cnv_cache = cfm
