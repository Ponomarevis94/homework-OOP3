import os

def get_info_and_writing_to_list(file_names):
    my_data = []
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            lines = f.read().splitlines()
            my_data.append([file, len(lines)])
            my_data[len(my_data)-1] += lines
    my_data.sort(key=len)
    return my_data


def writing_info_to_file(my_data, my_file):
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in my_data:
            for elem in file:
                f.write(f'{elem}\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

print(writing_info_to_file(get_info_and_writing_to_list(['1.txt', '2.txt', '3.txt']), 'result.txt'))