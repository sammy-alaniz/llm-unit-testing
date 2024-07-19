import logging
import Templates
import sys

MAX_TESTS_PER_RUN = 4

class PromptBuilder:

    def __init__(
        self,
        source_file_path: str,
        test_file_path: str = '',
        code_coverage_report: str = '', # I want to make this optional
        included_files_list: list = None,
        additional_instructions: str = '',
        failed_test_runs: str = '',
        language: str = "python",
    ):

        self.source_file_name = source_file_path.split("/")[-1]
        #self.test_file_name = test_file_path.split("/")[-1]
        self.source_file = self._read_file(source_file_path)
        #self.test_file = self._read_file(test_file_path)
        self.code_coverage_report = code_coverage_report
        self.language = language
        # add line numbers to each line in 'source_file'. start from 1
        self.source_file_numbered = "\n".join(
            [f"{i + 1} {line}" for i, line in enumerate(self.source_file.split("\n"))]
        )
        # self.test_file_numbered = "\n".join(
        #     [f"{i + 1} {line}" for i, line in enumerate(self.test_file.split("\n"))]
        # )

        # Conditionally fill in optional sections
        self.included_files = self._all_included_files(included_files_list)
        self.included_files = Templates.ADDITIONAL_INCLUDES_TEXT.format(included_files=self.included_files)


        self.additional_instructions = (
            Templates.ADDITIONAL_INSTRUCTIONS_TEXT.format(
                additional_instructions=additional_instructions
            )
            if additional_instructions
            else ""
        )
        self.failed_test_runs = (
            Templates.FAILED_TESTS_TEXT.format(failed_test_runs=failed_test_runs)
            if failed_test_runs
            else ""
        )

    def _all_included_files(self, included_files_list):
        all_included_files = ""
        for file_path in included_files_list:
            all_included_files += self._read_file(file_path)
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
            # return f"Error reading {file_path}: {e}"

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
        user_prompt += Templates.SOURCE_FILES.format(source_file_name=self.source_file_name,
                                              source_file_numbered=self.source_file_numbered)
        user_prompt += self.included_files

        return {"system": system_prompt, "user": user_prompt}

