import unittest
from src.llm.chat_bot import ChatBot


class TestChatBot(unittest.TestCase):
    def test_conversation(self):
        bot = ChatBot()
        test_message = 'hi'
        result = bot.predict(test_message)
        self.assertIsInstance(obj=result, cls=str)