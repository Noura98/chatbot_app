import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

# Load data
intents = json.load(open('data/intents.json'))
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')
from datetime import datetime
import requests


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]

def get_response(intents_list, intents_json):
    if len(intents_list) == 0:
        return "Sorry, I didn't understand that."

    tag = intents_list[0]['intent']

    if tag == "weather":
        # Optionally, parse city from user input, here default to Tunis
        return get_weather(city="Tataouine")

    if tag == "time":
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."

    for intent in intents_json["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])



import requests

def get_weather(city="Tunis"):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": "ac9aa884a9aa416fbc5141844252804",  # Your WeatherAPI key
        "q": city
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "error" in data:
            return f"Sorry, I couldn't find weather info for {city}."

        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        emoji = weather_emoji(condition)

        return f"The current weather in {city} is {condition} {emoji} with a temperature of {temp_c}°C."
    except Exception as e:
        return "Sorry, I couldn't fetch the weather right now."

def weather_emoji(condition):
    condition = condition.lower()
    if "sun" in condition or "clear" in condition:
        return "☀️"
    elif "rain" in condition or "drizzle" in condition:
        return "🌧️"
    elif "thunder" in condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "cloud" in condition:
        return "☁️"
    else:
        return "🌈"

def chatbot_response(msg):

    intents_list = predict_class(msg)
    return get_response(intents_list, intents)
