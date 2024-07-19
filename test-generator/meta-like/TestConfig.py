
import json


class TestConfig:
    def __init__(self) -> None:
        self.test_file_path = None
        self.included_files = None


def parseConfig(config_file_path):

    with open(config_file_path, 'r') as file:
        test_config = json.load(file)

    test_file_path = test_config.get('test_file_path')
    included_files = test_config.get('included_files', [])
    
    print('')
    print('----------- test configuration ---------------')
    print('')
    print('source file path')
    print(test_file_path)
    print('')
    print('included files')

    for file in included_files:
        print(file)
    print('')

    tc = TestConfig()

    tc.test_file_path = test_file_path
    tc.included_files = included_files

    return tc


    