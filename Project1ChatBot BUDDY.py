print("Hello!, I am BUDDY." )
print(" Type bye to exit.")

responses = {
    "Hi": "Hi, How can I help you?",
    "How are you": "I am fine, Thank you",
    "Who are you": "I sm your Chatbot",
    "What is your name": "My name is Buddy",
    "Motivate me": "Keep working hard",
    "coding is hard": "every bug of your project makes you a better developer"
    "What are functions?" "It is ablock of reusable code used to perform specific task."
}
def response(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses(eachkey)
    return "I am not able to tell you that yet. Sorry"
while True:
    doubt = input("Please ask your doubt, BUDDY will help you :) ")
    reply = response(doubt)
    print("Your answer is: ", reply)
    if "Bye" in doubt.lower():
        break