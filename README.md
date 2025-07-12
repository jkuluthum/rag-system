# Project Title

An interactive AI-powered app built on 
langchain that answers questions from 
romeo and juliet PDF document using Groq lLLM

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Environment Variables](#environment-variables)

## Overview

This project is a chatbot application that allows users 
to ask natural language questions about  Romeo and Juliet. 
It uses large language models (LLMs) through LangChain 
and integrates a clean, interactive Streamlit UI for a 
seamless user experience.

## Features

- Chat with Romeo and Juliet:
Ask natural language questions about Shakespeare’s Romeo and 
Juliet and get clear, contextual responses from a local LLM or 
preloaded document.
- Retrieval-Augmented Generation (RAG):
Leverages document-based context with LangChain to provide accurate, 
grounded answers based on the play or uploaded text
- Interactive Chat Interface:
Clean, responsive interface powered by Streamlit, with persistent 
conversation memory during each session.

## Installation

To install and run the chatbot locally, follow these steps:

### Prerequisites

- Python 3.10 or higher
- Git
- Virtual environment

---

### Steps

1. **Clone the repository**:

   ```sh
   git clone https://github.com/jkuluthum/rag-system.git

1. **Enter the project directory**:

   ```sh
   cd rag-system

   ```

1. **Setup your virtual environment**:

   ```sh
   python -m venv myenv

   ```
1. **Activate your virtual environment**:

   ```sh
   myenv\Scripts\activate

   ```
1. Install all the necessary requirements:

   ```sh
   pip install -r requirements.txt

   ```

1. Run your application:

   ```sh
   streamlit run ui.py

   ```

   1. Check for it here:

   ```sh
   http://localhost:8501/

   ```

   ## Tech Stack

- **UI:** Streamlit
- **Pipeline:** RAG
- **Data Storage:** Chromadb

---

## Environment Variables

Before running the app, you need to create a `.env` file in the root directory and define the following environment variables:

### Required Environmental Variables

| Variable Name      | Type   | Description                                                   |
|--------------------|--------|---------------------------------------------------------------|
| `GROQ_API_KEY`      | string | Your API key from [Groq](https://console.groq.com/keys)           |
| `CHROMA_DB_PATH`     | string | Path where Chroma should store the vector database locally    |
