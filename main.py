#pip install -q -U google-genai

from google import genai
from google.genai import types

# Inizializzazione client
client = genai.Client(api_key="Insert API Key")

print("--- Verifica Modelli Disponibili ---")
try:
    # Elenchiamo i modelli per vedere il nome esatto richiesto
    for m in client.models.list():
        print(f"Disponibile: {m.name}")
except Exception as e:
    print(f"Errore nel recupero della lista: {e}")
print("------------------------------------")

# Usiamo uno dei modelli che hai confermato essere disponibili
MODEL_ID = "models/gemini-3.8-flash"

print(f"--- Chatbot avviato con {MODEL_ID} ---")

# Gestione sessione di chat
chat = client.chats.create(model=MODEL_ID)

while True:
    user_input = input("Tu: ")
    if user_input.lower() in ['esci', 'quit', 'exit']:
        break
    
    try:
        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}\n")

        print(f"--- Dettagli della risposta ---")
        print(f"Token usati: {response.usage_metadata.total_token_count}")
     
    except Exception as e:
        print(f"Errore tecnico: {e}")