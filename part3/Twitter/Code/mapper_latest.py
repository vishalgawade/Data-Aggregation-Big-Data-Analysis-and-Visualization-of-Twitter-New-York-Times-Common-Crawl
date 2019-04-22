#!/usr/bin/python3.6

import sys
import re
import csv
import numpy as np
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
import textcleaner as tc


def main(separator='\t'):
    # input comes from STDIN (standard input)
    words = read_input(sys.stdin);
    for word in words:
        for w in word:
            print ('%s%s%d' % (w, separator, 1));


def read_input(file):
    for line in file:
        line = strip_text(line.strip());  # strip the line and remove unnecessary parts
        yield line.split();  # split the line

# def strip_line(text):  # strip smileys,emojis,urls from tweet text to get only text
#     smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^)
#              :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D""".split();
#     pattern = "|".join(map(re.escape, smileys));
#     kaomojis = r'[^0-9A-Za-zぁ-んァ-ン一-龥ovっつ゜ニノ三二]' + '[\(∩　（]' + '[^0-9A-Za-zぁ-んァ-ン一-龥ｦ-ﾟ\)∩　）]' + '[\)∩　）]' + '[^0-9A-Za-zぁ-んァ-ン一-龥ovっつ゜ニノ三二]*'
#     text = text.strip().lower();
#     link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
#     links = re.findall(link_regex, text)
#     for link in links:
#         text = text.replace(link[0], ' ');
#     text = re.sub(pattern, "", text);
#     text = re.sub(kaomojis, "", text);
#     text = strip_emoji(text);
#     text = re.sub(r'@\w+ ?', '', text);  # remove mentions
#     for separator in string.punctuation:  # remove punctuations
#         if separator != '#':
#             text = text.replace(separator, ' ');
#     # nltk.download("stopwords");
#     text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))]);  # remove stopwords
#     text = ' '.join([word for word in text.split() if not word.endswith("…")]);  # remove …
#     return text;  # remove leading and trailing white space

def strip_text(text):
    smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^) 
                :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D""".split();
    pattern = "|".join(map(re.escape, smileys));
    kaomojis = r'[^0-9A-Za-zぁ-んァ-ン一-龥ovっつ゜ニノ三二]' + '[\(∩　（]' + '[^0-9A-Za-zぁ-んァ-ン一-龥ｦ-ﾟ\)∩　）]' + '[\)∩　）]' + '[^0-9A-Za-zぁ-んァ-ン一-龥ovっつ゜ニノ三二]*'
    text=text.lower();
    text = re.sub(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', '', text);  # remove links
    text = ' '.join([word for word in text.split() if not word.endswith("…")]);  # remove ss…
    text = re.sub(pattern, "", text);
    text = re.sub(kaomojis, "", text);
    text = strip_emoji(text);
    text = re.sub(r'[\)\( \/\.-\][0-9]+[ \)\/\.\(-]', ' ', text);  # replace (123)-> 123
    text = re.sub(r'\([^()]*\)', '', text);  # replace (vishal)-> vishal
    text = re.sub(r'[.,]', ' ', text);  # remove . ,
    text = re.sub(r'@\w+ ?', ' ', text);  # remove mentions
    text = text.replace("'s", "");  # replace vishal's->vishal
    text = re.sub(r'\W+', ' ', text);  # replace vishal123@@@-> vishal123
    text = re.sub(r'[ ][0-9]+ ', '', text); # remove
    text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))]);  # remove stopwords
    text = ' '.join(word for word in tc.document(text).lemming().data); #do lemming
    return text;
def strip_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string);


if __name__ == "__main__":
    main()