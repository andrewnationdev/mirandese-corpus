import random
import re

sentences = []

n_grams = {}

def process_corpus(text):
    bare_sentences = re.split(r"[.!?]+", text)

    for sentence in bare_sentences:
        if not sentence.strip():
            continue
       
        words = sentence.split()
        sentences.append(words)

def generate_sentence(num=7):
    words = []
    next_word = random.choice(list(n_grams.keys()))
    words.append(next_word)

    while len(words) < num:
        next_word = random.choice(n_grams[next_word])
        words.append(next_word)

    return " ".join(words)

with open("corpus-limpo.txt", "r", encoding="utf-8") as corpus:
    text = corpus.read()

process_corpus(text)

for sentence in sentences:
    words = [word for word in sentence if word[0].isalpha()]
    for index in range(len(words) - 1):
        try:
            n_grams[words[index]].append(words[index + 1])
        except KeyError as _:
            n_grams[words[index]] = []
            n_grams[words[index]].append(words[index + 1])

print(generate_sentence(16))