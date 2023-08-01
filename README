# 1.Technical Support Ticketing Application [problem 1]

This is a text-based (non-GUI) technical support ticketing application where issue types are organized in categories and defined outside of the program in an external file.

## How to Use the Application

1. Clone the repository or download the `ticketing_application.py` file.

2. Make sure you have Python installed on your system.

3. Create a text file named `issue_categories.txt` in the same directory as the `ticketing_application.py`. This file will contain the issue categories and types in the following format:


Replace `Category1`, `Category2`, etc. with your desired category names, and `IssueType1`, `IssueType2`, etc. with the corresponding issue types for each category.

4. Run the application by executing the `ticketing_application.py` script using the following command:

python ticketing_application.py


5. The application will display a menu with the following options:

- **1. Create a new ticket:** Allows you to create a new technical support ticket by selecting the category, issue type, and providing a description.

- **2. Display all tickets:** Shows a list of all tickets created so far.

- **3. Exit:** Closes the application.

6. Follow the on-screen prompts to create new tickets and manage existing ones.

## File Structure

- `ticketing_application.py`: The main Python script that implements the technical support ticketing application.

- `issue_categories.txt`: An external file that contains the issue categories and types. The application reads this file to populate the available categories and issue types.

## Functions

- `read_issue_categories(filename)`: This function reads the issue categories and types from the `issue_categories.txt` file and returns a dictionary with the categories as keys and lists of issue types as values.

- `create_ticket(categories)`: This function allows users to create a new technical support ticket by selecting a category, issue type, and providing a description. The ticket information is stored in a dictionary and returned.

- `display_tickets(tickets)`: This function displays all the tickets created so far. If no tickets have been created, it notifies the user.

- `main()`: The main function of the application. It handles the menu and user interactions, calling other functions as needed.

## Notes

- Make sure to keep the `ticketing_application.py` and `issue_categories.txt` files in the same directory.

- If the `issue_categories.txt` file is missing or not found, the application will display an error message and exit.

- The application allows users to create multiple tickets and view them in the order they were created.

- This is a basic text-based application and can be further enhanced with additional features like ticket status, user information, or ticket assignment to support staff.

---

# 2. Graph Loop Finder and Sketcher [Problem 2]

This tool is designed to find and sketch loops in a graph (network) defined by edges in a CSV file. The graph is represented as a directed graph (DiGraph) where each edge connects a source node to a target node. Nodes are represented as arbitrary strings of characters.

## Usage

1. Prepare the CSV file: Create a CSV file with two columns, where column A represents the source node and column B represents the target node for each edge. Save this file as `graph.csv` in the same directory as the script.

2. Install Dependencies: Before running the tool, make sure you have installed the required dependencies. You can do this by executing the following command:

pip install networkx matplotlib

3. Run the Script: Execute the script `graph_loop_finder.py` using the following command:

python graph_loop_finder.py


4. Output: The tool will display any loops found in the graph and generate a visualization of the graph.

## File Structure

- `graph_loop_finder.py`: The main Python script that implements the graph loop finder and sketcher tool.

- `graph.csv`: The input CSV file containing the graph edges. The graph is read from this file to identify loops.

## Functions

- `read_graph_from_csv(csv_file)`: This function reads the graph edges from the CSV file and creates a directed graph (DiGraph) using the NetworkX library.

- `find_loops(graph)`: This function identifies all loops in the graph using NetworkX's `all_simple_paths` function. Loops are represented as lists of nodes.

- `sketch_graph(graph)`: This function visualizes the graph using NetworkX and Matplotlib. It displays the graph with labeled nodes and edges.

## Output

- If the tool finds loops in the graph, it will display a list of loops, where each loop is represented as a sequence of nodes.

- If no loops are found in the graph, it will display a message indicating that no loops were found.

- The graph sketch will be shown as a graphical representation using Matplotlib.

## Sample CSV File

The CSV file `graph.csv` should have the following format:


4. Output: The tool will display any loops found in the graph and generate a visualization of the graph.

## File Structure

- `graph_loop_finder.py`: The main Python script that implements the graph loop finder and sketcher tool.

- `graph.csv`: The input CSV file containing the graph edges. The graph is read from this file to identify loops.

## Functions

- `read_graph_from_csv(csv_file)`: This function reads the graph edges from the CSV file and creates a directed graph (DiGraph) using the NetworkX library.

- `find_loops(graph)`: This function identifies all loops in the graph using NetworkX's `all_simple_paths` function. Loops are represented as lists of nodes.

- `sketch_graph(graph)`: This function visualizes the graph using NetworkX and Matplotlib. It displays the graph with labeled nodes and edges.

## Output

- If the tool finds loops in the graph, it will display a list of loops, where each loop is represented as a sequence of nodes.

- If no loops are found in the graph, it will display a message indicating that no loops were found.

- The graph sketch will be shown as a graphical representation using Matplotlib.

## Sample CSV File

The CSV file `graph.csv` should have the following format:

source, target

A, B

B, C

C, A

C, D


In this example, the graph contains the edges A->B, B->C, C->A, and C->D.

## Dependencies

- [NetworkX](https://networkx.org/): A Python library for creating, analyzing, and visualizing complex networks.

- [Matplotlib](https://matplotlib.org/): A Python plotting library for creating visualizations.

## Note

- The tool supports directed graphs (DiGraphs) and is designed to handle loops within the graph efficiently.

- Make sure to have the required CSV file `graph.csv` in the same directory as the script before running the tool.

- Feel free to use this tool to analyze your own graphs and identify loops in them!

---

# 3.URL Extractor - Recursive URL Extraction from www.wikipedia.org [Problem 3]

This tool is designed to extract URLs recursively from either of www.curlie.org or www.wikipedia.org, including sub-pages. It uses Python's `requests`, `BeautifulSoup`, and `urllib.parse` libraries to parse web pages and extract URLs.

## Usage

1. Install Dependencies: Before running the tool, make sure you have installed the required dependencies. You can do this by executing the following command:

pip install requests beautifulsoup4

2. Run the Script: Execute the script `url_extractor.py` using the following command:

python url_extractor.py

3. Output: The tool will display the extracted URLs from the starting URL up to a specified depth.

## Functions

- `get_soup(url)`: This function sends an HTTP GET request to the given URL, retrieves the page's content, and returns a BeautifulSoup object for parsing.

- `extract_urls(url)`: This function extracts URLs from a given URL using the BeautifulSoup object. It filters URLs that either start with '/' or are part of the base URL.

- `recursive_extract_urls(url, max_depth=3, visited_urls=None, current_depth=0)`: This recursive function extracts URLs from the starting URL up to a specified maximum depth. It avoids revisiting URLs that have already been processed.

## Configuration

- The `starting_url` variable in the `main()` function specifies the URL from which the URL extraction will begin. Change this to the website link to extract URLs from the desired website.

- The `max_depth` variable in the `main()` function sets the maximum depth of recursion. By default, it is set to 3, meaning the tool will extract URLs up to three levels of sub-pages from the starting URL.

## Output

The tool will display the extracted URLs, including the URLs of sub-pages, from the starting URL up to the specified depth.

## Dependencies

- [requests](https://docs.python-requests.org/): A Python library for making HTTP requests.

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): A Python library for parsing HTML and XML documents.

- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html): A Python library for parsing URLs and handling URL components.

## Note

- The tool is designed to extract URLs recursively, which means it will follow links to sub-pages and continue the extraction process.

- The maximum depth of recursion can be adjusted by changing the `max_depth` variable in the `main()` function.

- Please respect the website's terms of use and ensure you are allowed to extract data from the specified URL.

- Feel free to use this tool responsibly for your URL extraction needs!

---

# 4.Natural Language Graph Constructor [Problem 4]

This tool constructs a graph given text in natural language as input. In the graph, each node represents a sentence from the input text, and an edge exists between two sentences if the text similarity between them is above a user-defined threshold.

## Usage

1. Install Dependencies: Before running the tool, make sure you have installed the required dependencies. You can do this by executing the following command:


2. Download SpaCy Model: The tool requires the SpaCy English model. Download it by executing the following command:

python -m spacy download en


3. Run the Script: Execute the script `graph_constructor.py` using the following command:

python graph_constructor.py



4. Output: The tool will display the constructed graph where each edge represents a text similarity above the user-defined threshold.

## Functions

- `compute_sentence_similarity(sentence1, sentence2)`: This function computes the similarity between two sentences using SpaCy's similarity scoring. It returns a similarity score between 0 and 1.

- `construct_graph(sentences, similarity_threshold)`: This function constructs the graph given a list of sentences and a similarity threshold. It uses the SpaCy library for sentence tokenization and similarity computation.

## Input

The `input_text` variable in the `main()` function represents the input text in natural language. Modify this variable with your desired text to create the graph.

## Configuration

The `similarity_threshold` variable in the `main()` function sets the threshold for text similarity. Edges will be added between sentences whose similarity score is equal to or above this threshold. Adjust this value based on your desired level of similarity.

## Output

The tool will display the constructed graph as a series of edges, where each edge represents a pair of sentences with a similarity score above the specified threshold.

## Dependencies

- [SpaCy](https://spacy.io/): An open-source natural language processing library in Python.

## Note

- The tool uses the SpaCy English model to tokenize sentences and compute similarity scores. Make sure to download the English model before running the script.

- Text similarity is based on word embeddings and might vary depending on the language used in the input text.

- The tool's effectiveness depends on the input text's content and the similarity threshold chosen. Experiment with different thresholds to achieve the desired graph structure.

- Feel free to use this tool to analyze the similarity between sentences and create a graph representation!

---

