# Semantic Similarity System for TOEFL Synonym Questions

This project is from ESC180 that implements an intelligent system designed to answer TOEFL "Synonym Questions" by calculating the semantic similarity between a target word and a list of possible synonyms. The system computes the semantic descriptor vectors for each word using the co-occurrence of words in a given text and then determines the word with the highest similarity using cosine similarity.

## Features

- **Semantic Descriptor Vector Calculation**  
  - For each word, the system computes a semantic descriptor vector, which records the frequency of co-occurrence with other words in the text.
- **Cosine Similarity Calculation**  
  - The cosine similarity between the semantic descriptor vectors of the target word and each possible synonym is calculated to measure how similar they are in meaning.
- **Answer Selection**  
  - The system selects the synonym with the highest cosine similarity as the correct answer to the synonym question.

## How It Works

1. **Input**  
   - A text is provided that contains words whose semantic relationships are to be explored.
   - A target word is given along with a list of possible synonyms.
2. **Descriptor Vector Construction**  
   - For each word, the system constructs a semantic descriptor vector based on the sentences in which the word appears, recording how often it co-occurs with other words.
3. **Cosine Similarity**  
   - The system calculates the cosine similarity between the descriptor vector of the target word and each of the potential synonyms.
4. **Selection**  
   - The synonym with the highest cosine similarity to the target word is selected as the correct answer.


## Usage

1. Provide a text input that contains words to compute semantic relationships.
2. Specify the target word and a list of possible synonyms.
3. The system will compute the semantic descriptor vectors and return the synonym with the highest cosine similarity.


## Acknowledgments

- All credit goes to the course instructor Michael Guerzhoy
