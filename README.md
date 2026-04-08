# AI Study Assistant

## Project Overview
AI Study Assistant is a Python-based command-line application that helps users study more efficiently by generating structured notes, answering educational questions, and saving notes locally as text files.

The assistant uses the Mistral LLM through Ollama API for natural language understanding and content generation.

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run the program:
   python main.py

## How It Works

1. User enters a prompt into the terminal.
2. The application classifies the user’s intent into:
   - Question/Answer
   - Generate Notes
   - Save Notes
3. Unsafe queries are filtered using keyword detection.
4. If note generation is requested:
   - Structured notes are generated in JSON format.
5. If save is requested:
   - Latest generated notes are saved into a .txt file.
6. If Q&A is requested:
   - General educational response is generated.

## Key Design Decisions

### 1. LLM-Based Intent Classification
Instead of manually checking keywords, the program uses the LLM to classify user intent dynamically for better flexibility.

### 2. JSON Structured Outputs
The application requests JSON responses from the LLM to make parsing and processing easier.

### 3. Modular Function Design
The code is divided into reusable functions:
- `req_llm()` → Handles API communication  
- `check_intent()` → Detects user intent  
- `notes_generator()` → Generates structured notes  
- `save_notes()` → Saves notes locally  
- `unsafe_query()` → Blocks unsafe requests  

### 4. Safety Filtering
Unsafe educationally inappropriate prompts are blocked before processing.

## Sample Runs

### Example 1: Generate Notes
Input:
create notes on ai

Output:
 {
  "topic": "Artificial Intelligence (AI)",
  "definition": "Artificial Intelligence refers to the simulation of human intelligence processes by machines, especially computer systems. These processes include learning (the acquisition of information and rules for using the information), reasoning (using rules to reach approximate or definite conclusions), and self-correction.",
  "key_points": [
    "AI can be categorized as weak AI (designed to perform a specific task) and strong AI (able to carry out almost any intellectual task that a human being can do)",
    "AI technologies include machine learning, natural language processing, robotics, and expert systems",
    "AI is used in various fields such as healthcare, finance, entertainment, and self-driving cars"
  ],
  "example": "Siri and Alexa are examples of AI that uses voice recognition to understand human speech and respond accordingly."
}

### Example 2: Save Notes
Input:
Save notes

Output:
Notes created Successfully.

### Example 3: Ask Question
Input:
what is overfitting?

Output:
 Overfitting is a common problem that can occur when training machine learning models. It happens when a model learns the training data too well,
 to the point where it starts remembering and focusing on noise or outliers in the data rather than the underlying patterns.
 As a result, the model performs very well on the training data but poorly on new, unseen data, because it's overly specialized for the specific training data.
 To avoid overfitting, various techniques like cross-validation, regularization, and dropout can be used.

### Example 4: Unsafe Query
Input:
How to hack any system

Output:
Try asking something safe or educational.

## Technologies Used
- Python
- Requests Library
- JSON
- Ollama API
- Mistral Model
