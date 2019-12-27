from typing import Generator


class FileManager:
    def __init__(self, glob, os, json, collection_directory, cleaned_collection_directory):
        self.glob = glob
        self.os = os
        self.json = json
        self.collection_directory = collection_directory
        self.cleaned_collection_directory = cleaned_collection_directory

    def get_clean_html_files_list(self) -> Generator[str, None, None]:
        return self.glob.iglob(self.cleaned_collection_directory + '**/*.html', recursive=True)

    def get_html_files_list(self) -> Generator[str, None, None]:
        return self.glob.iglob(self.collection_directory + '**/*.html', recursive=True)

    def get_file_base_name(self, file_abs_path) -> str:
        return self.os.path.basename(file_abs_path)

    def file_exists(self, file) -> bool:
        return self.os.path.isfile(file)

    def file_not_cleaned(self, file_abs_path) -> bool:
        cleaned_file_path = self.cleaned_collection_directory + self.get_file_base_name(file_abs_path)
        return not self.file_exists(cleaned_file_path)

    def get_cleaned_path(self, file) -> str:
        return self.cleaned_collection_directory + self.get_file_base_name(file)

    def write_to_json_file(self, dictionary, file_abs_path) -> None:
        with open(file_abs_path, 'w+') as file:
            file.write(self.json.dumps(dictionary))

    def read_from_json(self, file_abs_path) -> dict:
        if not self.file_exists(file_abs_path):
            raise FileNotFoundError

        with open(file_abs_path, 'r') as file:
            return self.json.loads(file.read())
