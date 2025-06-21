# chatbot_app
# 🤖 Chatbot with NLP, Real-Time Weather & Current Time

Welcome! I'm your chatbot assistant.
You can ask me about:
```
-Greetings
-Farewells
-Help & support
-Jokes
-Real-time features such as **current local time** and **live weather information** fetched from a weather API
```
---

## Features

- **NLP-based Intent Classification:**  
  Uses tokenization, lemmatization, and a neural network model to classify user queries into predefined intents.

- **Real-Time Weather Information:**  
  Integrates with [WeatherAPI.com](https://www.weatherapi.com/) to fetch live weather data for any specified city.

- **Current Time Response:**  
  Provides the exact current system time in response to user queries.

- **Expandable:**  
  Easily extendable by adding more intents and responses in the `intents.json` file.

---

## Project Structure

```chatbot_app/ 
├── app.py # Streamlit app interface
├── chatbot.py # Core chatbot logic and response generation
├── train_chatbot.py # Script to preprocess data and train the NLP model
├── intents.json # JSON file with intents, patterns & responses
├── chatbot_model.h5 # Saved trained model (do NOT share sensitive files publicly)
├── words.pkl # Vocabulary saved from preprocessing
├── classes.pkl # List of classes (intents)
├── requirements.txt # Project dependencies
├── README.md # This file ```
---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/chatbot_app.git
cd chatbot_app
3. Install dependencies
pip install -r requirements.txt
4. Obtain a WeatherAPI key
Sign up at WeatherAPI.com to get your free API key.
Replace the API key placeholder in chatbot.py with your actual key.

5. Run the chatbot app
streamlit run app.py
