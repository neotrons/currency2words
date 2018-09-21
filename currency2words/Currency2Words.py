from .utils import CURRENCY_FORMS
from num2words import CONVERTER_CLASSES
from num2words.currency import parse_currency_parts


class Currency2Words(object):

    def __init__(self, number, lang='es', currency='PEN', separator='con'):
        self.number = number
        self.lang = lang
        self.lang_object = self.get_lang_object(lang)
        self.currency = currency
        self.separator = separator.strip()
        self.integer_part, self.decimal_part, self.negative = parse_currency_parts(number)
        self.custom_currency_form = None

    def get_words_integer_part(self):
        return getattr(self.lang_object, 'to_cardinal')(self.integer_part)

    def get_words_decimal_part(self):
        return getattr(self.lang_object, 'to_cardinal')(self.decimal_part)

    def get_currency_form(self):
        if self.custom_currency_form is None:
            try:
                self.lang_object.CURRENCY_FORMS.update(CURRENCY_FORMS)
                return self.lang_object.CURRENCY_FORMS[self.currency]

            except KeyError:
                raise NotImplementedError(
                    'Currency code "%s" not implemented for "%s"' %
                    (self.currency, self.__class__.__name__))
        else:
            return self.custom_currency_form

    def get_negword(self):
        return self.lang_object.negword if self.negative else ''

    def get_lang_object(self, lang):
        if lang not in CONVERTER_CLASSES:
            lang = lang[:2]
        if lang not in CONVERTER_CLASSES:
            raise NotImplementedError()
        return CONVERTER_CLASSES[lang]

    def cent_text(self):
        currency_word, cent_word = self.get_currency_form()
        result = '%s%s %s %s %s %s' % (
            self.get_negword(),
            self.get_words_integer_part(),
            self.lang_object.pluralize(self.integer_part, currency_word),
            self.separator,
            self.get_words_decimal_part(),
            self.lang_object.pluralize(self.decimal_part, cent_word),
        )
        return result

    def __str__(self):
        return self.cent_text()


