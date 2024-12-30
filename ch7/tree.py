from os import listdir
from os.path import isfile, join
from collections import deque


def print_file_name(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        directory = search_queue.popleft()
        for file in sorted(listdir(directory)):
            full_path = join(directory, file)
            if isfile(full_path):
                print(file)
            else:
                search_queue.append(full_path)

def print_names(start_dir):
    for file in sorted(listdir(start_dir)):
        full_path = join(start_dir, file)
        if isfile(full_path):
            print(file)
        else:
            print_names(full_path)




if __name__ == "__main__":
    print_file_name('/Users/neoni/Movies')
    print("\n")
    print("-"*50)
    print("\n")
    print_names('/Users/neoni/Movies')