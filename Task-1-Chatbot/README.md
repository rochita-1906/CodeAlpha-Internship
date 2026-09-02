# CodeAlpha FAQ Chatbot 🤖

An AI-powered FAQ chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

## 📌 Project Description

This chatbot answers frequently asked questions about the CodeAlpha internship.

It uses Natural Language Processing (NLP) techniques to compare a user's question with a collection of predefined FAQ questions and return the most relevant answer.

## 🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- JSON

## ⚙️ How It Works

1. FAQ questions and answers are stored in a JSON file.
2. TF-IDF converts the FAQ questions into numerical vectors.
3. The user's question is converted into a vector.
4. Cosine similarity compares the user's question with the stored FAQ questions.
5. The chatbot selects the most similar question.
6. The corresponding answer is displayed to the user.

## 📁 Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── data/
│   └── faqs.json
│
├── app.py
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md