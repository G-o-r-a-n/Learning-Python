import spacy

nlp = spacy.load('en_core_web_md')

def watch_next(target_description):
    """
    This function takes in a target movie description, compares it with the 
    descriptions of movies in a text file, and recommends the next movie to 
    watch based on the highest semantic similarity score with the target 
    description.
    
    Args:
        target_description (str): The description of the target movie as a string.
        
        Returns:
        recommended_movie (str): The title of the movie with the highest semantic
        similarity score to the target description. If multiple movies have 
        the same highest score, it will return the title of the first movie it
        encountered with that score.
    """
    
    # Similarity is measured from 0 to 1. Starting at -1 ensures each iteration
    # will update "max_similarity" if it scores higher than previous iteration.
    max_similarity = -1
    # Empty string to capture movie title later.
    recommended_movie = ""
    # Converts 'Planet Hulk' description into a SpaCy doc.
    hulk_description = nlp(target_description)
    
    with open('movies.txt', 'r') as movie_file:
        for line in movie_file:
            # Strips leading and trailing whitespaces.
            # Splits data at colon to separate movie title and description.
            title, movie_descriptions = line.strip().split(" :")
            # Converts 'movie_descriptions' to a SpaCy doc.
            nlp_descriptions = nlp(movie_descriptions)
            # Calculates semantic similarity score.
            similarity = nlp_descriptions.similarity(hulk_description)
            # Checks if current iteration yields a higher similarity score than
            # previous stored value, updating 'max_similarity' if so.
            if similarity > max_similarity:
                max_similarity = similarity
                # Updates 'recommended_movie" with the title of the movie 
                # with the highest similarity score throughout iterations.
                recommended_movie = title
    # Returns the movie title with the highest semantic similarity after all
    # iterations are complete.
    return recommended_movie

# Target description to compare 'movies.txt' data to.
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print("----------------------------------------")
print("If you enjoyed 'Planet Hulk', watch this next: " + watch_next(planet_hulk))
print("----------------------------------------")