
from PromptBuilder import PromptBuilder
import TestConfig
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('[INFO] Must pass in a configuration file!')
        sys.exit(1)

    tc = TestConfig.parseConfig(sys.argv[1])

    # source_file_path = '/home/sammy/dev/school/cobra/args.go'
    # test_file_path = ''
    # code_coverage_report = ''
    # included_files = '/home/sammy/dev/school/cobra/command.go'
    # additional_instructions = ''
    # failed_test_runs = ''
    # language = ''

    pb = PromptBuilder(source_file_path=tc.source_file_path,
                       included_files_list=tc.included_files)
    prompt = pb.build_prompt()
    user_prompt = prompt.get('user')

    with open('test.txt', 'w') as file:
        file.write(user_prompt)
    