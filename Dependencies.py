import glob
import os
import json

from nltk import PorterStemmer
from pathos.multiprocessing import ProcessingPool as Pool

from Constants import NLTK_WORDS, MAIN_COLLECTION_DIRECTORY, CLEANED_COLLECTION_DIRECTORY, INVERTED_INDEX_PATH, THREADS_COUNT
from FileManager import FileManager
from FileTokenizer import FileTokenizer
from InvertedIndexManager import InvertedIndexManager


threads_pool = Pool(THREADS_COUNT)
stemmer = PorterStemmer()
file_tokenizer = FileTokenizer(stemmer, NLTK_WORDS)
file_manager = FileManager(glob, os, json, MAIN_COLLECTION_DIRECTORY, CLEANED_COLLECTION_DIRECTORY)
inverted_index_manager = InvertedIndexManager(
    INVERTED_INDEX_PATH,
    file_manager,
    file_tokenizer,
    threads_pool,
)
