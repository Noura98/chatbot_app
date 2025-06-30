import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer,util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# 1. Preprocess the text filea
def preprocess(text_file='data/alice.txt'):
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    sentences = sent_tokenize(text)
    cleaned_sentences = []

    for sentence in sentences:
        if ("illustration" in sentence.lower()) or ("chapter" in sentence.lower()):
            continue
        words = word_tokenize(sentence.lower())
        words = [word for word in words if word not in stop_words and word not in string.punctuation]
        cleaned = ' '.join(words)
        cleaned_sentences.append(cleaned)

    return sentences, cleaned_sentences

# 2. Find most relevant sentence
original_sentences, cleaned_sentences = preprocess()
# Load the sentence transformer model (small and efficient)
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_most_relevant_sentence(user_query):
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    sentence_embeddings = model.encode(cleaned_sentences, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(query_embedding, sentence_embeddings)[0]
    best_idx = scores.argmax().item()
    best_score = scores[best_idx].item()

    if best_score < 0.4:
        return "Sorry, I couldn't find a relevant answer."

    # Add surrounding context (e.g., 1 before and 1 after if available)
    context = []
    if best_idx > 0:
        context.append(original_sentences[best_idx - 1])
    context.append(original_sentences[best_idx])
    if best_idx + 1 < len(original_sentences):
        context.append(original_sentences[best_idx + 1])

    return " ".join(context)


# 3. Define the chatbot function
def chatbot(user_input):
    return get_most_relevant_sentence(user_input)
