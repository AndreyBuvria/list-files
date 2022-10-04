import os

class ListModel:
    def __init__(self, scan_path=None, output_file_name='listModels', input_file_extension=None):
        self.scan_path = scan_path
        self.output_file_name = output_file_name
        self.input_file_extension = input_file_extension

        self.search_argument = 'f'
        self.root_path = os.getcwd()


            

        

