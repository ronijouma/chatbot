import random
from scraper import scrape_sigma_info
from encryption import log_communication

FAQ = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm here to help!",
    "what is your name": "I'm your friendly customer service chatbot!",
    "bye": "Goodbye! Have a great day!",
    "hej": "Hej! Hur kan jag hjälpa dig idag?",
    "hur mår du": "Jag är bara en bot, men jag mår bra och är här för att hjälpa dig!",
    "vad heter du": "Jag är din hjälpsamma kundtjänstbot!",
    "hejdå": "Hejdå! Ha en bra dag!"
}

default_responses = [
    "I'm sorry, I didn't understand that. Could you rephrase?",
    "Can you please provide more details so I can assist you better?",
    "I'm not sure about that. Let me connect you to a human representative.",
    "Jag är ledsen, jag förstod inte det. Kan du omformulera?",
    "Kan du ge mig fler detaljer så att jag kan hjälpa dig bättre?",
    "Jag är inte säker på det. Låt mig koppla dig till en mänsklig representant."
]

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for question in FAQ:
        if question in user_input:
            return FAQ[question]
    
    if "sigma" in user_input:
        sigma_info = scrape_sigma_info()
        return "Here is some information from Sigma's website:\n" + "\n".join(sigma_info)
    
    return random.choice(default_responses)
