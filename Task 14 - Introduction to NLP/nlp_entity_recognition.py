"""
This script performs named entity recognition on a list of garden path 
sentences using the spaCy library.
"""

import spacy

nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "The old man the boat",
    "The man whistling tunes pianos",
    "The Eiffel Tower the tourists visited impressed all.",
    "Mary gave the child a Band-Aid",
    "That Jill is never here hurts",
    "The cotton clothing is made of grows in Mississippi"
    ]

# Empty set to store named entity labels.
entity_labels = set()

#Iterating over each sentence within list.
for sentence in gardenpathSentences:
    #Tokenising sentences.
    nlp_garden = nlp(sentence)
    #Identifying named entities within each sentence.
    print(f"{sentence}\n")
    # Checks if sentence does not have named entities so that this is fed back
    # to user.
    if not nlp_garden.ents:
        print("No entities identified within sentence.")
        print("----------")
    else:
        # Identified named entity and label will be displayed to user.
        for entity in nlp_garden.ents:
            print(f"Entity: {entity.text}\nLabel: {entity.label_}")
            print("----------")
            # Named entity label added to previously empty set.
            entity_labels.add(entity.label_)

# Displaying each named entity label explanation identified.
for label in entity_labels:
    print(f"{label}: {spacy.explain(label)}")