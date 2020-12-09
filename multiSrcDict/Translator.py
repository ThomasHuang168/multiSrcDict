import abc

class Translator(abc.ABC):
    @abc.abstractmethod
    def translate(self, text):
        return ""

from .dict_util import MultiDict, search_by_char
class T_MultiDicts(Translator):
    def __init__(self, _dicts, dictPriorityList, out_stat_name=""):
        self.md = MultiDict()
        self.md.setDicts(_dicts)
        self.out_stat_name = out_stat_name
        self.md.setPriority(dictPriorityList)

    def translate(self, text):
        translated_text = self.md[text]
        if translated_text is None:
            translated_text = text
        return translated_text

    def __del__(self):
        if len(self.out_stat_name):
            self.md.export(self.out_stat_name)