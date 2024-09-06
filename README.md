# Local RAG


## Description

### Project structure


```text
my_rag_project/
├── data/                       # add your PDFs and other documents HERE
├── models/                     # To store the models
├── src/                  
│   ├── __init__.py       
│   ├── main.py           
│   ├── document_loader.py      # script to load the documents 
│   ├── indexer.py              # for indexing the documents
│   ├── generator.py            # for generating 
├── requirements.txt      
├── Dockerfile                  # Dockerfile to build the image
└── README.md                   # Docs
```


## Installation

Create a virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Running the project

- Be sure to have the virtual environment activated
- Add at least one PDF file to the `data/` folder

```bash
python src/main.py
```

### Running with Docker

Command to run the project on a docker container

```bash
docker build -t local_rag .
docker run -it local_rag
```
