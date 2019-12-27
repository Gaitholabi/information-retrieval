from FileManager import FileManager
from multiprocessing import Pool
import re
from bs4 import BeautifulSoup

from FileTokenizer import FileTokenizer
from Parser import Parser


class InvertedIndexManager:
    def __init__(self, index_path: str, file_manager: FileManager, file_tokenizer: FileTokenizer, threads_pool: Pool, bs4: BeautifulSoup):
        self.index_path = index_path
        self.file_manager = file_manager
        self.file_tokenizer = file_tokenizer
        self.threads_pool = threads_pool
        self.bs4 = bs4

    def get(self) -> dict:
        if self.file_manager.file_exists(self.index_path):
            return self.file_manager.read_from_json(self.index_path)
        return self.__build()

    def __build(self) -> dict:
        def clean_files(file):
            cleaned_file_path = self.file_manager.get_cleaned_path(file)
            with open(file, 'r') as html_file:
                parsed_string = Parser.clean_html_tags(BeautifulSoup(markup=html_file, features='html5lib'), re.compile(r'<.*?>'))
                with open(cleaned_file_path, 'w') as cleaned_output:
                    cleaned_output.write(parsed_string)

        def tokenize_file(file_path):
            with open(file_path, 'r') as file:
                return file_path, self.file_tokenizer.tokenize(file)

        collection_not_cleaned_files = filter(self.file_manager.file_not_cleaned, self.file_manager.get_html_files_list())

        self.threads_pool.map(clean_files, collection_not_cleaned_files)
        cleaned_collections_files = self.file_manager.get_clean_html_files_list()
        cleaned_files_tokens_map = self.threads_pool.map(tokenize_file, cleaned_collections_files)
        inverted_index = self.__build_inverted_index_with_frequency(cleaned_files_tokens_map)
        self.file_manager.write_to_json_file(inverted_index, self.index_path)
        self.threads_pool.close()
        return inverted_index

    def __build_inverted_index_with_frequency(self, files) -> dict:
        inverted_index = {}
        for document, words_list in files:
            doc_name = self.file_manager.get_file_base_name(document)
            for word in words_list:
                if word not in inverted_index:
                    inverted_index[word] = {doc_name: 1}
                else:
                    if document not in inverted_index[word]:
                        inverted_index[word][doc_name] = 1
                    else:
                        inverted_index[word][doc_name] += 1
        return inverted_index


