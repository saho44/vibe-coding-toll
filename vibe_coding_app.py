import streamlit as st
from transformers import pipeline
from textblob import TextBlob

# Hugging Face Modell laden (GPT-2 oder ein anderes)
generator = pipeline("text-generation", model="gpt2")

# Streamlit App-Header
st.title("🎭 Vibe Coding: Spiel mit Textstimmungen!")

# Eingabefeld für den Benutzertext
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

# Auswahl einer neuen Stimmung
vibe = st.selectbox("Wähle eine neue Stimmung für den Text:",
                    ["humorvoll", "dramatisch", "motivierend", "poetisch", "sarkastisch", "formell"])

def rewrite_text_with_vibe(text, vibe):
    """Schreibt den Text mit einer bestimmten Stimmung um (Hugging Face)."""
    prompt = f"Schreibe den folgenden Text im Stil von '{vibe}': {text}"
    
    response = generator(prompt, max_length=100, num_return_sequences=1)
    
    return response[0]["generated_text"]

if st.button("Text umschreiben"):
    neuer_text = rewrite_text_with_vibe(text, vibe)
    st.subheader("✍️ Neuer Text:")
    st.write(neuer_text)
