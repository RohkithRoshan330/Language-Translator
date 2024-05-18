import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from langdetect import detect
from googletrans import Translator
import time

# Download NLTK resources
nltk.download('punkt')

# Title for Streamlit app
st.title("Text Translation and Analysis")
st.text("Break Down Language Barriers: Translate Your World with Ease")

# Sidebar for file upload
st.sidebar.title("Upload File")
uploaded_file = st.sidebar.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    # Open the file in read mode with utf-8 encoding
    Ftext = uploaded_file.read().decode("utf-8")

    with st.spinner("Analysing the input file"):
        time.sleep(10)

    # Display the content of the file
    st.subheader("Given Input Text")
    st.text(Ftext)

    with st.spinner("Converting into word tokenize"):
        time.sleep(5)

    # Tokenize into words
    words = word_tokenize(Ftext)
    st.subheader("Tokenized Words")
    st.write(words)

    with st.spinner("Converting into sentence tokenize"):
        time.sleep(5)

    # Tokenize into sentences
    sentences = sent_tokenize(Ftext)
    st.subheader("Tokenized Sentences")
    st.write(sentences)

    with st.spinner("Detecting language "):
        time.sleep(5)

    # Detect language
    detect_lang = detect(Ftext)
    st.subheader("Detected Language")
    st.write(detect_lang)

    with st.spinner("Calculating Number of Lines"):
        time.sleep(3)

    # Statistical analysis
    no_lines = Ftext.count('\n') + 1
    st.subheader("Number of Lines")
    st.write(no_lines)

    with st.spinner("Calculating Number of words"):
        time.sleep(3)

    count_words = Ftext.split()
    num_words = len(count_words)
    st.subheader("Number of Words")
    st.write(num_words)

    with st.spinner("Calculating Number of characters"):
        time.sleep(3)

    num_char = sum(len(word) for word in count_words)
    st.subheader("Number of Characters")
    st.write(num_char)

    with st.spinner("Translating...."):
        time.sleep(30)

    # Initialize the translator
    translator = Translator()

    # Translate the text
    translated_sentences = []
    for sentence in sentences:
        translated_sentence = translator.translate(sentence, dest='en').text
        translated_sentences.append(translated_sentence)

    # Display translated text
    st.subheader("Translated Text")
    st.write("\n".join(translated_sentences))
