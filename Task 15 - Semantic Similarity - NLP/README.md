# Task 15 - Semantic Similarity - NLP

This project uses Natural Language Processing (NLP) with `spaCy` to explore the concept of semantic similarity. It uses medium-sized English language model `en_core_web_md` from `SpaCy` for this task.

## Objectives:

The main objectives of this project are:

1. To compare semantic similarity between words, series of words and sentences.
1. Based on semantic similarity, recommend a movie from a text file of movie descriptions given a target movie description.

These objectives are accomplished in separate Python files, [semantic_similarity_basics.py](https://github.com/G-o-r-a-n/Learning-Python/blob/main/Task%2015%20-%20Semantic%20Similarity%20-%20NLP/semantic_similarity_basics.py) and [semantic_similarity_movie_recommendation](https://github.com/G-o-r-a-n/Learning-Python/blob/main/Task%2015%20-%20Semantic%20Similarity%20-%20NLP/semantic_similarity_movie_recommendation.py), which are explained below:

## Code Explained

### Script 1: Semantic Similarity Basics

This Python script demonstrates the basics of semantic similarity using `SpaCy`. It includes the comparison of individual words, series of words, and sentences. Here are the key steps:

- **Load Language Model**: The `spaCy` English language model `en_core_web_md` is loaded.
- **Single Word Comparison**: Semantic similarity between pairs of individual words is computed and displayed.
- **Series of Words Comparison**: Semantic similarity between pairs of words from a series of words is computed and displayed.
- **Sentence Comparison**: Semantic similarity between different sentences and a target sentence is computed and displayed.

### Script 2: Movie Recommendation based on Semantic Similarity

This Python script contains a function to recommend the next movie to watch based on the highest semantic similarity score with the target movie description. It demonstrates a practical application of semantic similarity. Here are the key steps:

- **Load Language Model**: The `spaCy` English language model `en_core_web_md` is loaded.
- **Next Movie Recommendation**: A function `watch_next(target_description)` is defined to recommend the next movie to watch based on the highest semantic similarity score with the target movie description. It reads from a text file of movie descriptions, calculates the semantic similarity with the target description, and returns the title of the movie with the highest similarity score.

## Usage:

To use these scripts, you need to install the `spaCy` library, which can be done using `pip`:

```
pip install spacy
python -m spacy download en_core_web_md
```

Then, you can run the scripts directly:

```
python semantic_similarity_basics.py
python movie_recommendation.py
```

Make sure to have the **'movies.txt'** file available in the same directory for the movie recommendation function.

### Note:

This project is part of a task series aimed at introducing semantic similarity in natural language processing (NLP) with `spaCy`. The task provides a practical example of how NLP can be used to compute semantic similarity and can be applied in areas such as recommendation systems.