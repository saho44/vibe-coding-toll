import streamlit as st
from transformers import pipeline
from textblob import TextBlob

# Kleineres Modell laden (distilgpt2 statt gpt2)
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

# Streamlit App-Header
st.title("Vibe Coding: Text in verschiedene Stimmungen umschreiben!")

# Eingabefeld für den Benutzertext
text = st.text_area("Gib einen Text ein:", "Heute war ein schöner Tag!")

def analyze_sentiment(text):
    """
    Analysiert die Stimmung des Textes mithilfe von TextBlob.
    Gibt 'positiv', 'negativ' oder 'neutral' zurück.
    """
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
    st.write(f"Die aktuelle Stimmung des Textes ist: {stimmung}")

# Auswahl einer neuen Stimmung
vibe = st.selectbox(
    "Wähle eine neue Stimmung für den Text:",
    ["humorvoll", "dramatisch", "motivierend", "poetisch", "sarkastisch", "formell"]
)

def rewrite_text_with_vibe(text, vibe):
    """
    Schreibt den Text mithilfe des distilgpt2-Modells in einem bestimmten Stil um.
    """
    prompt = f"Schreibe den folgenden Text im Stil von '{vibe}': {text}"
    
    # Reduziere max_length, damit kein Speicherfehler auftritt
    response = generator(
        prompt,
        max_length=80,         # Gesamtlänge: Prompt + generierte Tokens
        num_return_sequences=1
    )
    
    return response[0]["generated_text"]

if st.button("Text umschreiben"):
    neuer_text = rewrite_text_with_vibe(text, vibe)
    st.subheader("Neuer Text:")
    st.write(neuer_text)
