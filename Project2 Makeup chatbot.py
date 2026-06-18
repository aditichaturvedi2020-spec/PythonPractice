print("Welcome, I am beautify. Your makeup chatbot")
print("Ask me about makeup") 
responses = {
    "What is foundation?": "foundation hides pigmentation, darkness and dark spots from face",
    "Which is my shade?": "choose a foundation that matches your skin tone.",
    "What is lipstick?": "Used to colour lips, you should choose nude shades.",
    "what is mascarra": "To make eyelashes dark and uplifted. Apply mascara from root to tip",
    "acne": "Avoid picking pimples and use gentle cleanser",
    "primer": "It creates a base to avoid unevenness",
}
def thing(userQues):
    userQues = userQues.lower()
    for keys in responses:
        if keys in userQues:
            return responses[keys]
    return "Sorry I can only answer about makeup and skincare.\n What else would you like to know?"
while True:
    doubt = input("What would you like to know?")
    if doubt.lower() == "bye":
        print("Thank you for using Beautify chatbot!!")
        break   
    answer = thing(doubt)
    print(answer)

