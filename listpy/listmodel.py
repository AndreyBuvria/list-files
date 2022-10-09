import os

class ListModel:
    def __init__(self, scan_path=None, search_argument=None, output_file_name=None, input_file_extension=None):
        self.scan_path = os.getcwd() if scan_path is None else scan_path
        self.output_file_name = 'listModels' if output_file_name is None else output_file_name
        self.search_argument = search_argument
        self.input_file_extension = input_file_extension

    def get_path(self, file_name):
        """
        Return full path of file
        """
        return os.path.join(self.scan_path, file_name)

    def write_list(self):
        """
        Retrieve file names based on provided searching argument
        and write them down in a text doc
        """
        if self.search_argument == 'f':
            file_names = (entrie for entrie in os.listdir(self.scan_path) if os.path.isfile(self.get_path(entrie)))
        elif self.search_argument == 'd':
            file_names = (entrie for entrie in os.listdir(self.scan_path) if os.path.isdir(self.get_path(entrie)))
        else:
            file_names = (entrie for entrie in os.listdir(self.scan_path))

        with open(f'{self.output_file_name}.txt', 'w') as f:
            for it in file_names:
                f.write(it + '\n')

            
