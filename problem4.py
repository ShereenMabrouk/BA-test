# Shereen Mabrouk
'''
A tool that constructs a graph given text in a natural language as input, such that a node represents a sentence, 
and an edge exists from one sentence (node) to another if text similarity between the two is above a user-defined threshold.
'''
import spacy
from spacy.lang.en import English
from spacy.tokens import Doc
from collections import defaultdict

# Function to compute similarity between two sentences
def compute_sentence_similarity(sentence1, sentence2):
    return sentence1.similarity(sentence2)

# Function to construct a graph
def construct_graph(sentences, similarity_threshold):
    nlp = English()
    nlp.add_pipe("sentencizer")
    doc = Doc(nlp.vocab, words=sentences)
    nlp.get_pipe("sentencizer")(doc)

    sentence_graph = defaultdict(list)
    for i, sentence1 in enumerate(doc.sents):
        for j, sentence2 in enumerate(doc.sents):
            if i != j:
                similarity = compute_sentence_similarity(sentence1, sentence2)
                if similarity >= similarity_threshold:
                    sentence_graph[i].append(j)

    return sentence_graph

def main():
    input_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence
    concerned with the interactions between computers and human language, in particular how to program computers
    to process and analyze large amounts of natural language data.

    The field of NLP involves making computers understand, interpret, and generate human language in a way that is
    both meaningful and useful.

    Some of the tasks in NLP include text classification, sentiment analysis, named entity recognition, machine translation,
    and question answering.

    NLP is a challenging area because human language is often ambiguous, context-dependent, and diverse in structure.
    """
    similarity_threshold = 0.6

    # Preprocess the input text by removing newline characters and extra spaces
    input_text = " ".join(input_text.split())

    sentences = input_text.split(". ")
    graph = construct_graph(sentences, similarity_threshold)

    if graph:
        print("Constructed Graph:")
        for i, neighbors in graph.items():
            for neighbor in neighbors:
                print(f"Node {i} -> Node {neighbor}")
    else:
        print("No edges found. The graph is empty.")

if __name__ == "__main__":
    main()
