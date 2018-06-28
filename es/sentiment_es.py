import json
import re
from textblob import TextBlob

def clean_data (text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())

def add_sentiment (feed):
    f = open(feed + '.json', encoding='latin-1', mode='r')
    data = json.load(f)
    f.close()
    for item in data:
        text = item['text']
        text = clean_data(text)
        testimonial = TextBlob(text)
        polarity = testimonial.sentiment.polarity
        if polarity > 0:
            item['marker-color'] = "#32ad67"
        elif polarity == 0:
            item['marker-color'] = "#3174af"
        else:
            item['marker-color'] = "#ce4437"
    f = open(feed + '.json', encoding='latin-1', mode='w')
    json.dump(data, f)

if __name__ == "__main__":
    add_sentiment("data_loc_es")