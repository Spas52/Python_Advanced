import os, shutil


def get_all_files(directory_path):
    # Get the list of all files in directory tree at given path
    list_of_files = []
    for (dirpath, dirnames, filenames) in os.walk(directory_path):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]
    return list_of_files


def get_file_extensions_count(files):
    files = {}
    for file_path in list_of_files:
        file = file_path.split('\\')
        file_name, file_extension = file[-1].split('.')
        file_extension = '.' + file_extension
        if file_extension in files:
            files[file_extension].append(file[-1])
        else:
            files[file_extension] = [file[-1]]
    return files


def get_report_data(files):
    file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    files = dict(sorted(files.items(), key=lambda s: (s[0], s[1])))
    with open(file_path + '/report.txt', 'w') as report_file:
        for extension, files in files.items():
            report_file.write(extension + '\n')
            for file in files:
                report_file.write('- - - ' + file + '\n')
    return report_file


directory_path = ''
list_of_files = get_all_files(directory_path)
files = get_file_extensions_count(list_of_files)
print(files)
print(get_report_data(files))