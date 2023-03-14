import openai
import streamlit as st

# Ajouter votre clé API OpenAI
openai.api_key = "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"

# Définir les paramètres pour GPT-3
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 100

# Définir la base de connaissances
knowledge_base = """
Q: Quelle est la capitale de la France ?
A: La capitale de la France est Paris.

Q: Quand a été fondée l'OpenAI ?
A: L'OpenAI a été fondée en 2015.

Q: Qui est l'inventeur de la théorie de la relativité ?
A: L'inventeur de la théorie de la relativité est Albert Einstein.
"""

# Créer l'interface utilisateur avec Streamlit
def main():
    st.title("Bot GPT-3")

    question = st.text_input("Posez votre question :")

    if st.button("Répondre"):
        response = generate_response(question)
        st.write(response)

# Définir une fonction pour générer une réponse à partir de GPT-3
def generate_response(question):
    prompt = f"{knowledge_base}\nQ: {question}\nA:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text

if __name__ == "__main__":
    main()
