class BeautifyBot:
    def __init__(self):
        self.responses = {
            "acne": "Avoid picking pimples",
            "primer": "Creates a smooth base",
            "foundation": "face putty"

}


    def answer(self, userQues):
        userQues = userQues.lower()

        for key in self.responses:
            if key in userQues:
                return self.responses[key]

        return "Sorry, I can only answer about makeup."
bot = BeautifyBot()
print(bot.answer("acne"))