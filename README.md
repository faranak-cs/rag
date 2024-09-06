# Retrieval-Augmented Generation (RAGs)
RAG models are seq2seq models with access to a retrieval mechanism providing relevant context documents at training and evaluation time.

# Setup
0. Install [Python 3.12.5](https://www.python.org/downloads/). Install [Ollama](https://ollama.com/download) and pull down Llama3.1 using following command on Terminal:
```
ollama pull llama3.1
```
1. Clone the repo
```
https://github.com/faranak-cs/rag.git
```
2. Checkout to dev branch
```
git checkout dev
```
3. Creat virtual envrionment
```
python3 -m venv rag.env
```
4. Activate virtual environment
```
source rag.env/bin/activate
```
5. Install packages
```
python -m pip install -r requirements.txt
```
6. Populate database
```
python populate_database.py
```
7. Ask questions
```
python query_data.py "How many players are there in monopoly?"
```
