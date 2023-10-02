from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import os
from . import keys


class ChatBot:
    """Basic gpt3.5 chatbot with no memory"""
    def __init__(self):
        os.environ['OPENAI_API_KEY'] = keys.openai_api_key

        self.chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")
        self.conversation = ConversationChain(
                    llm=self.chat_model,
                    verbose=False)

    def predict(self, prompt):
        prediction = self.conversation.predict(input=prompt)
        return prediction


if __name__ == "__main__":
    bot = ChatBot()
    print(bot.predict(prompt='Hi'))
