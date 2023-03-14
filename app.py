import openai
import streamlit as st
from pydantic import BaseModel

class Query(BaseModel):
    question: str

# Ajouter votre clé API OpenAI
openai.api_key = "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"

# Définir les paramètres pour GPT-3
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 100

# Créer l'interface utilisateur avec Streamlit
def main():
    st.title("Bot GPT-3")

    query = Query(question="")
    query.question = st.text_input("Posez votre question :")

    if st.button("Répondre"):
        response = generate_response(query.question)
        st.write(response)

# Définir une fonction pour générer une réponse à partir de GPT-3
def generate_response(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text

if __name__ == "__main__":
    main()
