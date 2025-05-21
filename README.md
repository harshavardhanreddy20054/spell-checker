# Spell Checker using N-grams

## Overview

This project implements a robust spell-checking system using Natural Language Processing (NLP) techniques. By leveraging N-grams, it detects and corrects spelling errors in a given text. The model analyzes sequences of words to ensure that corrections align with natural language patterns, providing accurate and context-aware suggestions. The system is equipped with a user-friendly interface built with Flask, allowing real-time interaction for spell checking.

## Features

* **N-gram-based Spell Correction**: Detects and corrects spelling errors by analyzing word patterns and context.
* **Real-time Interaction**: Flask-based web interface for quick and easy spell checking.
* **Custom Inputs**: Users can test the tool using their own text inputs.

## File Structure

```
spellchecker_ngram/
├── app.py               # Flask application script
├── spellcheck.py        # Core spell-checking logic
├── inputs.txt           # Sample input file for testing
├── requirements.txt     # Dependencies required to run the project
├── templates/           # HTML templates for the Flask interface
└── __pycache__/         # Compiled Python files
```

## Requirements

To run this project, ensure you have the following installed:

* Python 3.8 or higher
* Flask
* Other dependencies listed in `requirements.txt`

Install dependencies using:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository_url>
   cd spellchecker_ngram
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

* Enter a sentence or paragraph with potential spelling errors into the text box on the web interface.
* Click the **Check Spelling** button.
* View the corrected text displayed below the input area.

## Example

**Input:**

```
This is an exampel sentence with speling erors.
```

**Output:**

```
This is an example sentence with spelling errors.
```

## Contribution

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.
