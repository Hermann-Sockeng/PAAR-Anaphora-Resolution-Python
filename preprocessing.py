#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:17:29 2023

@author: Hermann Sockeng,   Email: hermannsockeng@gmail.com
"""


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

class TextTokenizer:
    def __init__(self, language):
        self.language = language
#        nltk.download('punkt')  # Download the required NLTK data for tokenization

    def tokenize_sentences(self, text):
        """
        Tokenize the given text into sentences.

        Args:
            text (str): The input text.

        Returns:
            list: A list of sentences.
        """
        sentences = sent_tokenize(text, self.language)  # Tokenize into sentences
        return sentences

    def tokenize_words(self, text):
        """
        Tokenize the given text into words.

        Args:
            text (str): The input text.

        Returns:
            list: A list of words.
        """
        words = word_tokenize(text, self.language)  # Tokenize into words
        return words
    
   
# text1 = 'Die Freiherren von Erthal beanspruchten einst das alleinige Schankrecht in Untererthal, wofür sie eine Schänke an der wichtigsten, regionalen Verbindung, der Straße von Hammelburg nach Fulda, erbauten.'
# text2 = 'Bislang verwendete Knauf Gips aus Rauchgas-Entschwefelungsanlagen: Der fällt bei Kraftwerken an, wenn die Abgase entschwefelt werden. Wofür die Natur Million Jahre braucht, geschieht dann in wenigen Stunden.'








from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class TextLemmatizer:
    def __init__(self):
        nltk.download('punkt')  # Download the required NLTK data for tokenization
        nltk.download('wordnet')  # Download the WordNet corpus

        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_text(self, text):
        """
        Lemmatize the words in the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The lemmatized text.
        """
        tokens = word_tokenize(text)  # Tokenize the text into words

        # Lemmatize each word based on its part of speech
        lemmatized_tokens = [self._lemmatize_word(word) for word in tokens]

        lemmatized_text = ' '.join(lemmatized_tokens)  # Join the lemmatized words into a text
        return lemmatized_text
'''
    def _lemmatize_word(self, word):
        """
        Lemmatize a single word based on its part of speech.

        Args:
            word (str): The input word.

        Returns:
            str: The lemmatized word.
        """
        pos_tag = nltk.pos_tag([word])[0][1][0].upper()  # Get the part of speech tag

        # Map the part of speech tag to WordNet part of speech constants
        if pos_tag.startswith('J'):
            pos = wordnet.ADJ
        elif pos_tag.startswith('V'):
            pos = wordnet.VERB
        elif pos_tag.startswith('N'):
            pos = wordnet.NOUN
        elif pos_tag.startswith('R'):
            pos = wordnet.ADV
        else:
            pos = wordnet.NOUN  # Default to noun if the part of speech is unknown

        lemmatized_word = self.lemmatizer.lemmatize(word, pos)  # Lemmatize the word
        return lemmatized_word    '''