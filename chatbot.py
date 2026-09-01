import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
with open("data/faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)
























def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])

    similarities = cosine_similarity(user_vector, question_vectors)

    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    if best_score < 0.2:
        return "Sorry, I don't know the answer to that question."

    return answers[best_match_index]

















