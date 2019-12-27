from typing import Iterator

from nltk import PorterStemmer


class FileTokenizer:
    def __init__(self, porter_stemmer: PorterStemmer, stop_words_list: list):
        self.porter_stemmer = porter_stemmer
        self.stop_words_list = stop_words_list

    def tokenize(self, file) -> Iterator[str]:
        words = self.__get_words_list(file)
        stemmed_words = map(self.porter_stemmer.stem, words)
        return filter(lambda word: not self.__is_stop_word(word) and word.isalpha(), stemmed_words)

    def __get_words_list(self, file) -> list:
        return file.read().split(' ')

    def __is_stop_word(self, word) -> bool:
        return word in self.stop_words_list
