## Project Title
**Problem Solver Tool for AI-Powered Q&A with CSV Processing**

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About the Project
This project is designed to help users process CSV files, create embeddings, and provide question-answering capabilities using advanced AI models. By using Flask, LangChain components, and embedding models from Google Generative AI, this tool allows users to upload CSV files, ask questions based on the content, and receive precise answers. Additionally, it logs questions and answers to an output CSV file for reference.

## Features
- Upload and process CSV files to create vector embeddings.
- Ask questions and receive context-based answers.
- Save questions and responses to an output CSV file.
- Download the generated CSV file with Q&A history.

## Getting Started
To get started with this project, follow these simple steps:
1. Clone the repository.
2. Ensure you have Python and necessary dependencies installed.
3. Follow the installation steps below.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/KIRIT-P-S/Chatbot-Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Chatbot-Project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure you have a `.env` file with your API keys and environment variables set up.

## Usage
1. Start the application:
   ```bash
   python main.py
   ```
2. Navigate to the home page by visiting `http://127.0.0.1:5000/` in your browser.
3. Upload a CSV file through the interface.
4. Use the `/ask` endpoint to submit questions in JSON format, e.g.,
   ```json
   {
       "question": "What information is in the uploaded CSV?"
   }
   ```
5. Download the Q&A log by accessing the `/download` endpoint.

## Contributing
Contributions are what make the open-source community such a fantastic place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact
KIRIT P S - [pskirit7545@gmail.com](mailto:pskirit7545@gmail.com)

Project Link: [https://github.com/KIRIT-P-S/Chatbot-Project](https://github.com/KIRIT-P-S/Chatbot-Project)
