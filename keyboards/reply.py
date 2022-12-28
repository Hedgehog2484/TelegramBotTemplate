from aiogram.types import KeyboardButtonPollType

from utils import ReplyMarkupConstructor


class ExampleReplyMarkup(ReplyMarkupConstructor):
    test_btn_text = "TEST"

    def get(self):
        schema = [1, 2, 3]
        actions = [
            {'text': '1', },
            {'text': '2', 'contact': True},
            {'text': '3', 'location': True},
            {'text': '4', 'request_contact': True},
            {'text': '5', 'request_location': True},
            {'text': self.test_btn_text}
        ]
        return self.markup(actions, schema, resize_keyboard=True)
