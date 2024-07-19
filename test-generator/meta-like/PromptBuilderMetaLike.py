import logging
import Templates
import sys

MAX_TESTS_PER_RUN = 4

class PromptBuilder:

    def __init__(
        self,
        test_file_path: str,
        included_files_list: list = None,
        language: str = "python",
    ):

        self.test_file_name = test_file_path.split("/")[-1]
        self.test_file = self._read_file(test_file_path)

        self.language = language



        # Conditionally fill in optional sections
        self.included_files = self._all_included_files(included_files_list)

    def _all_included_files(self, included_files_list):
        all_included_files = ""
        for file_path in included_files_list:
            file_name = file_path.split("/")[-1]
            tmp = self._read_file(file_path)
            file_contents = "\n".join([f"{i + 1} {line}" for i, line in enumerate(tmp)])
            all_included_files += Templates.INCLUDED_FILE.format(included_file_name=file_name,
                                                                 included_file_with_line_numbers=file_contents)
        return all_included_files


    def _read_file(self, file_path):
        """
        Helper method to read file contents.

        Parameters:
            file_path (str): Path to the file to be read.

        Returns:
            str: The content of the file.
        """
        try:
            with open(file_path, "r") as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            sys.exit(1)

    def build_prompt(self) -> dict:
        """
        Replaces placeholders with the actual content of files read during initialization, and returns the formatted prompt.

        Parameters:
            None

        Returns:
            str: The formatted prompt string.
        """
        system_prompt = ""
        user_prompt = ""

        user_prompt = Templates.OVERVIEW.format(language=self.language)
        user_prompt += Templates.TEST_FILE.format(test_file_name=self.test_file_name,
                                                  test_file=self.test_file)
        user_prompt += self.included_files

        return {"system": system_prompt, "user": user_prompt}

