import re
from collections import defaultdict

d = defaultdict(int)


def strip_and_clean(x):
    x = x.strip()
    x = re.sub("_", " ", x)
    return x


def classifier(x, y, a, b, p):
    for entry in pos_list:
        if entry in p:
            x += 1
    for entry in neg_list:
        if entry in p:
            y += 1
    print("\nFor posTweet.txt:\n")
    print("number of positive words are", x)
    print("number of negative words are", y)
    if x != y:
        if y >= (x / 2):
            print("\nIt is a negative tweet")
            b += 1
        else:
            print("\nIt is a positive tweet")
            a += 1
    else:
        print("\nMixed Tweet")
    return a, b


pos_word_bag = open('pos.wn', 'r').readlines()
neg_word_bag = open('neg.wn', 'r').readlines()
pos = open('posTweets.txt', encoding="utf8").readlines()
neg = open('negTweets.txt', encoding="utf8").readlines()

pos_list = []
neg_list = []
for i in pos_word_bag:
    i = strip_and_clean(i)
    pos_list.append(i)
for j in neg_word_bag:
    j = strip_and_clean(j)
    neg_list.append(j)
print("\nPositive words after cleaning:", len(pos_list), "\nNegative words after cleaning:", len(neg_list))

posTweet = 0
negTweet = 0

for l in pos:
    posTweet, negTweet = classifier(0, 0, posTweet, negTweet, l)
print("\nThe total number of positive tweets are:", posTweet)
print("\nThe total number of negative tweets are:", negTweet)

posTweet = 0
negTweet = 0

for k in neg:
    posTweet, negTweet = classifier(0, 0, posTweet, negTweet, k)
print("\nThe total number of positive tweets are:", posTweet)
print("\nThe total number of negative tweets are:", negTweet)
