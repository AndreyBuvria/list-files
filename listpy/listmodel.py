import os

class ListModel:
    def __init__(self, scan_path=None, output_file_name='listModels', input_file_extension=None):
        self.scan_path = scan_path
        self.output_file_name = output_file_name
        self.input_file_extension = input_file_extension

        self.search_argument = 'f'
        self.root_path = os.getcwd()

    def get_path(self, file_name):
        """
        Return full path of file
        """
        return os.path.join(self.root_path, file_name)

    def write_list(self):
        """
        Retrieve file names based on provided searching argument
        and write them down in a text doc
        """
        if self.search_argument == 'f':
            file_names = (entrie for entrie in os.listdir(self.root_path) if os.path.isfile(self.get_path(entrie)))
        elif self.search_argument == 'd':
            file_names = (entrie for entrie in os.listdir(self.root_path) if os.path.isdir(self.get_path(entrie)))
        else:
            file_names = (entrie for entrie in os.listdir(self.root_path))
        
        with open(f'{self.output_file_name}.txt', 'w') as f:
            for it in file_names:
                f.write(it + '\n')

            

        

