# Task 14 - Introduction to NLP

This Python script performs Named Entity Recognition (NER) on a list of garden path sentences. It uses the `spaCy` library, a leading software for natural language processing in Python.

## Objective:

The main objectives of this task are:

1. Process a list of sentences, specifically garden path sentences.
1. Tokenize each sentence and identify named entities within them.
1. Explore how `spaCy` has categorized each entity and explain their labels.

The Python script that accomplishes this can be found in the file: [nlp_entity_recognition.py](https://github.com/G-o-r-a-n/Learning-Python/blob/main/Task%2014%20-%20Introduction%20to%20NLP/nlp_entity_recognition.py).

## Code Explained:

The script executes the following steps:

- **Load Language Model**: The `spaCy` English language model `en_core_web_sm` is loaded.
- **Define Sentences**: A list of garden path sentences is defined.
- **Tokenize and Identify Named Entities**: Each sentence in the list is tokenized and processed to identify named entities.
- **Display Results**: Identified entities, along with their labels, are displayed. If no entities are identified within a sentence, it is communicated to the user.
- **Explain Entity Labels**: For each unique entity label identified in the sentences, `spaCy`'s explain function is used to provide a definition of what the label represents.

## Usage:
To use this script, you need to install the `spaCy` library, which can be done using `pip`:

```
pip install spacy
python -m spacy download en_core_web_sm
```

Then, you can run the script directly:

```
python nlp_entity_recognition.py
```

### Note:

This script is a part of a task series aimed at introducing natural language processing (NLP) with `spaCy`. The task provides a practical example of how NLP can be used to perform named entity recognition on various types of sentences, including garden path sentences, which can be particularly challenging due to their ambiguous nature.