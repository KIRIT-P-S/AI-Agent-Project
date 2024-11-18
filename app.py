from flask import Flask, request, jsonify, render_template, send_file
import os
import csv
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Embeddings and LLM setup
embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, max_tokens=500)

# Global variables to store vectorstore and retriever
vectorstore = None
retriever = None
output_csv_path = 'output.csv'

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/upload', methods=['POST'])
def upload_csv():
    global vectorstore, retriever   
    file = request.files['csv_file']
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Load the CSV and process it
        loader = CSVLoader(file_path)
        data = loader.load()

        # Create vectorstore
        vectorstore = Chroma.from_documents(documents=data, embedding=embeddings_model)
        retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})

        return jsonify({'message': 'File uploaded and processed successfully.'})
    else:
        return jsonify({'error': 'No file provided.'}), 400

@app.route('/ask', methods=['POST'])
@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question')
    if not question or not retriever:
        return jsonify({'error': 'Invalid request or model not ready.'}), 400

    # Create the prompt template
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question with a direct, specific response only."
        "\n\n"
        "{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    response = rag_chain.invoke({"input": question})
    answer = response["answer"].strip()

    # Write only the answer to the CSV file
    with open(output_csv_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if os.stat(output_csv_path).st_size == 0:  # Check if the file is empty
            writer.writerow(['Question', 'Answer'])  # Write header row
        writer.writerow([question, answer])

    return jsonify({'answer': answer})


@app.route('/download', methods=['GET'])
def download_csv():
    if os.path.exists(output_csv_path):
        return send_file(output_csv_path, as_attachment=True)
    else:
        return jsonify({'error': 'No CSV file found.'}), 404


if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)