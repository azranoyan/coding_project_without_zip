

def get_lines(file_name):
    with open(file_name, 'r') as f:
        l = f.read().splitlines()
    print(l)
fname = input("Insert the file name: ")
get_lines(fname)
