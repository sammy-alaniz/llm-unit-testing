
from PromptBuilder import PromptBuilder
import json

if __name__ == "__main__":
    print('hello world')

    source_file_path = '/home/sammy/dev/school/cobra/args.go'
    test_file_path = ''
    code_coverage_report = ''
    included_files = '/home/sammy/dev/school/cobra/command.go'
    additional_instructions = ''
    failed_test_runs = ''
    language = ''

    pb = PromptBuilder(source_file_path=source_file_path,
                       included_files=included_files)
    prompt = pb.build_prompt()
    user_prompt = prompt.get('user')

    with open('test.txt', 'w') as file:
        # json.dump(prompt, file, indent=4)
        file.write(user_prompt)
    