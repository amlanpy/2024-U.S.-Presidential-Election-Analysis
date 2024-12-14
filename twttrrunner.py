import re
from collections import Counter

with open("dataset1aug50k.txt", "r") as file:
    lines = file.readlines()


class User:
    def __init__(self, lang, likes, hashtags, text):
        self.lang = lang
        self.likes = likes
        self.hashtags = hashtags
        self.text = text


    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def get_likes(self):
        return self.likes
    def set_likes(self, likes):
        self.likes = likes
    def get_hashtags(self):
        return self.hashtags
    def set_hashtags(self, hashtags):
        self.hashtags = hashtags
    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text


def getAllUsernames(lines, list):
    for line in lines[1:]:
        first_word = line.split()[0]
        list.append(first_word)


tweets = []
count = 0


def getNumUsernames(lines, list, num):
    for line in lines[1:num]:
        first_word = line.split()[0]
        list.append(first_word)


def getAllHashtags(lines, list):
    for line in lines[1:]:
        start_index = line.find("[{")
        end_index = line.find("}]") + 2
        substring = line[start_index:end_index]
        text_start = 0
        while True:
            text_start_index = substring.find("'text': '", text_start)
            if text_start_index == -1:
                break
            text_start = text_start_index + len("'text': '")
            text_end_index = substring.find("'", text_start)

            if text_end_index != -1:
                extracted_text = substring[text_start:text_end_index]
                list.append(extracted_text)


def getNumHashtags(lines, list, num):
    for line in lines[1:num]:
        start_index = line.find("[{")
        end_index = line.find("}]") + 2
        substring = line[start_index:end_index]
        text_start = 0
        while True:
            text_start_index = substring.find("'text': '", text_start)
            if text_start_index == -1:
                break
            text_start = text_start_index + len("'text': '")
            text_end_index = substring.find("'", text_start)

            if text_end_index != -1:
                extracted_text = substring[text_start:text_end_index]
                list.append(extracted_text)


def getAllText(lines, list):
    for line in lines[1:]:
        end_index = line.find("}]\t")
        if end_index != -1:
            substring_after = line[end_index + 3:]
            list.append(substring_after)
        else:
            end_index = line.find("[]\t")
            substring_after = line[end_index + 3:]
            list.append(substring_after)


def getNumText(lines, list, num):
    for line in lines[1:num]:
        end_index = line.find("}]\t")
        if end_index != -1:
            substring_after = line[end_index + 3:]
            list.append(substring_after)
        else:
            end_index = line.find("[]\t")
            substring_after = line[end_index + 3:]
            list.append(substring_after)


def allHashtagRankingTopTen(lines):
    list = []
    getAllHashtags(lines, list)
    count = Counter(list)
    sorted_count = count.most_common(10)
    for string, count in sorted_count:
        print(f"{string}: {count}")

def allLikesRankingTopTen(lines):
    dic1 ={}
    for line in lines:
        parts = line.split("\t")
        dic1[parts[2]] = parts[4]
    dic1 = {int(k): v for k, v in dic1.items() if k.isdigit()}
    sorted_dict = sorted(dic1.items(), key=lambda x: x[0], reverse=True)
    for key, value in sorted_dict[:10]:
        print(f"{key}: {value}")



def allHashtagRankingTopTen(lines):
    list = []
    getAllHashtags(lines, list)
    count = Counter(list)
    sorted_count = count.most_common(10)
    for string, count in sorted_count:
        print(f"{string}: {count}")


#allHashtagRankingTopTen(lines)
#allLikesRankingTopTen(lines)



