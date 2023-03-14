import streamlit as st
import pandas as pd
import openai

# Charger le fichier CSV et stocker les données dans un DataFrame
@st.cache
def load_data():
    df = pd.read_csv('monfichier.csv')
    return df

# Afficher les résultats de GPT-3
def afficher_resultats(reponse_gpt3, reponse_attendue):
    if reponse_gpt3.lower() == reponse_attendue.lower():
        st.success("Réponse correcte : " + reponse_gpt3)
    else:
        st.error("Réponse incorrecte. Attendue : " + reponse_attendue + ", GPT-3 a répondu : " + reponse_gpt3)

# Programme principal
def main():
    # Afficher le titre
    st.title("GPT-3 : Répondeur de questions")

    # Demander à l'utilisateur d'entrer la clé API OpenAI
    api_key = st.text_input("Entrez votre clé API OpenAI :")

    # Vérifier si la clé API a été entrée
    if api_key:
        # Définir la clé API OpenAI
        openai.api_key = api_key

        # Charger les données
        df = load_data()

        # Afficher les instructions
        st.write("Posez une question dans la zone de texte ci-dessous et appuyez sur Entrée. GPT-3 répondra en utilisant les contextes associés à la question.")

        # Zone de texte pour poser les questions
        question = st.text_input("Question :")

        # Vérifier si une question a été posée
        if question:
            # Boucle pour poser des questions à GPT-3
            contextes_concatenes = '\n'.join(df['contexte'].tolist())
            for index, row in df.iterrows():
                prompt = question
                params = {
                    "prompt": prompt,
                    "temperature": 0.5,
                    "max_tokens": 100,
                    "top_p": 1,
                    "frequency_penalty": 0,
                    "presence_penalty": 0
                }
                response = openai.Completion.create(engine="davinci", prompt=contextes_concatenes + "\n" + params["prompt"], **params)
                reponse_gpt3 = response.choices[0].text.strip()
                reponse_attendue = row['reponse'].strip()
                afficher_resultats(reponse_gpt3, reponse_attendue)

if __name__ == "__main__":
    main()
