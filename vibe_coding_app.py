import streamlit as st
import openai
from textblob import TextBlob

# OpenAI API-Key (muss später noch ersetzt werden)
openai.api_key = "DEIN_API_KEY"

st.title("🎭 Vibe Coding: Spiel mit Textstimmungen!")

text = st.text_area("Gib einen Text ein:", "Heute war ein schöner Tag!")

def analyze_sentiment(text):
    """Analysiert die Stimmung des Textes."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positiv"
    elif sentiment < 0:
        return "negativ"
    else:
        return "neutral"

if st.button("Analyse starten"):
    stimmung = analyze_sentiment(text)
    st.write(f"🔍 Die aktuelle Stimmung des Textes ist: **{stimmung}**")

vibe = st.selectbox("Wähle eine neue Stimmung für den Text:",
                    ["humorvoll", "dramatisch", "motivierend", "poetisch", "sarkastisch", "formell"])

def rewrite_text_with_vibe(text, vibe):
    """Schreibt den Text mit einer bestimmten Stimmung um."""
    prompt = f"Schreibe den folgenden Text im Stil von '{vibe}':\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if st.button("Text umschreiben"):
    neuer_text = rewrite_text_with_vibe(text, vibe)
    st.subheader("✍️ Neuer Text:")
    st.write(neuer_text)
