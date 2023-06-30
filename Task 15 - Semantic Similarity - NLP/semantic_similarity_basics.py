import spacy

# Load medium-sized English language model from SpaCy.
nlp = spacy.load('en_core_web_md')

print("---------------Single Word---------------\n")

# Define words to compare and convert to a SpaCy document.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Print semantic similarity scores for each pair of words.
print(f"{word1} + {word2} = {round(word1.similarity(word2), 2)}")
print(f"{word3} + {word2} = {round(word3.similarity(word2), 2)}")
print(f"{word3} + {word1} = {round(word3.similarity(word1), 2)}")
print()

"""
NOTE:
It is quite interesting to see that "cat" and "monkey" score differently in terms of semantic similarity to "banana". This is despite the fact that in both cases, an animal is being compared with a fruit. "monkey" and "banana" showing a stronger similarity than "cat" and "banana" suggests that context and cultural connotations play a somewhat significant role in the model's understanding of semantic relationships between words.
"""

print("---------------Single Word (2)---------------\n")

# Define new words to compare and convert to a SpaCy document.
car = nlp("car")
bicycle = nlp("bicycle")
wheel = nlp("wheel")

# Print semantic similarity scores for each pair of new words.
print(f"{car} + {bicycle} = {round(car.similarity(bicycle), 2)}")
print(f"{wheel} + {bicycle} = {round(wheel.similarity(bicycle), 2)}")
print(f"{wheel} + {car} = {round(wheel.similarity(car), 2)}")
print()

print("---------------Series of Words---------------\n")

# Create a series of words for comparison and convert to a SpaCy document.
tokens = nlp('cat apple monkey banana')

# Loop through the words and calculate semantic similarity for each pair.
for token1 in tokens:
    for token2 in tokens:
        # Prevents repetitive output.
        if token1 == token2:
            break
        else:
            word_similarity = round(token1.similarity(token2), 2)
            print(f"{token1.text} + {token2.text} = {word_similarity}")
print()

print("---------------Sentences---------------\n")

# Define sentence for comparison.
sentence_to_compare = "Why is my cat on the car"

# List of sentences to compare with the above sentence.
sentences = [
    "Where did my dog go",
    "Hello, there is my car",
    "I've lost my cat in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
    ]

# Convert 'sentence_to_compare' into a SpaCy document.
model_sentence = nlp(sentence_to_compare)

# Loop through the list of sentences and calculate the semantic similarity with
# 'sentence_to_compare'.
for sentence in sentences:
    sentence_similarity = round(nlp(sentence).similarity(model_sentence), 2)
    print(f"{sentence} = {sentence_similarity}")