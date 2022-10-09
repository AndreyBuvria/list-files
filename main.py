import getopt, sys
from listpy.listmodel import ListModel

def main():
    argv = sys.argv[1:]

    scan_path = None
    output_file_name = None
    input_file_extension = None
    search_argument = None        

    try:
        opts, args = getopt.getopt(argv, 'p:o:i:s:')
    except:
        print('error')

    for opt, arg in opts:
        if opt in ['-p']:
            scan_path = arg
        elif opt in ['-o']:
            output_file_name = arg
        elif opt in ['-i']:
            input_file_extension = arg
        elif opt in ['-s']:
            search_argument = arg
    o = ListModel(scan_path, search_argument, output_file_name, input_file_extension)
    o.write_list()

if __name__ == '__main__':
    main()