
from PromptBuilderMetaLike import PromptBuilder
import TestConfig
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('[INFO] Must pass in a configuration file!')
        sys.exit(1)

    tc = TestConfig.parseConfig(sys.argv[1])

    pb = PromptBuilder(test_file_path=tc.test_file_path,
                       included_files_list=tc.included_files)

    prompt = pb.build_prompt()
    
    user_prompt = prompt.get('user')

    with open('test.txt', 'w') as file:
        file.write(user_prompt)
    