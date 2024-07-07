import logging
import Templates

MAX_TESTS_PER_RUN = 4

class PromptBuilder:

    def __init__(
        self,
        source_file_path: str,
        test_file_path: str = '',
        code_coverage_report: str = '', # I want to make this optional
        included_files: str = '',
        additional_instructions: str = '',
        failed_test_runs: str = '',
        language: str = "python",
    ):
        """
        The `PromptBuilder` class is responsible for building a formatted prompt string by replacing placeholders 
        with the actual content of files read during initialization. It takes in various paths and settings as 
        parameters and provides a method to generate the prompt.

        Attributes:
            prompt_template (str): The content of the prompt template file.
            source_file (str): The content of the source file.
            test_file (str): The content of the test file.
            code_coverage_report (str): The code coverage report.
            included_files (str): The formatted additional includes section.
            additional_instructions (str): The formatted additional instructions section.
            failed_test_runs (str): The formatted failed test runs section.
            language (str): The programming language of the source and test files.

        Methods:
            __init__(self, prompt_template_path: str, source_file_path: str, test_file_path: str, \
                    code_coverage_report: str, included_files: str = "", additional_instructions: str = "", \
                    failed_test_runs: str = "")
                Initializes the `PromptBuilder` object with the provided paths and settings.

            _read_file(self, file_path)
                Helper method to read the content of a file.

            build_prompt(self)
                Replaces placeholders with the actual content of files 
                read during initialization and returns the formatted prompt string.
        """
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
        self.included_files = (
            Templates.ADDITIONAL_INCLUDES_TEXT.format(included_files=included_files)
            if included_files
            else ""
        )
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
            return f"Error reading {file_path}: {e}"

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

        return {"system": system_prompt, "user": user_prompt}

