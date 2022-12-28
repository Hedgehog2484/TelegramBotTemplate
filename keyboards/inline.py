from aiogram.utils.callback_data import CallbackData

from utils import InlineMarkupConstructor


class ExampleMarkup(InlineMarkupConstructor):
    callback_data = CallbackData('test', 'number')

    def get(self):
        schema = [3, 2]
        actions = [
            {'text': '1', 'callback_data': self.callback_data.new('1')},
            {'text': '2', 'callback_data': self.callback_data.new('2')},
            {'text': '3', 'url': "google.com"},
            {'text': '4', 'callback_data': self.callback_data.new('4')},
            {'text': '5', 'switch_inline_query': ""},
        ]
        return self.markup(actions, schema)
