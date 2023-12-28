import numpy as np
import glob
import os

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1

    matrix = np.zeros((size_x, size_y))

    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )

    return matrix[size_x - 1, size_y - 1]

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
        return data.replace(' ', '')

def compare_files(file1_path, file2_path, plag_threshold):
    str1 = read_file(file1_path)
    str2 = read_file(file2_path)

    length = max(len(str1), len(str2))
    similarity = 100 - round((levenshtein(str1, str2) / length) * 100, 2)

    if similarity > plag_threshold:
        print(f"\nThe files '{file1_path}' and '{file2_path}' have {similarity}% similarity.")
    else:
        print("\nSimilarity is below the given threshold.")

def compare_folder_with_master(master_path, folder_path, plag_threshold):
    os.chdir(folder_path)
    my_files = glob.glob('*.txt')

    with open(master_path, 'r') as master_file:
        master_data = master_file.read().replace('\n', '')
        master_str = master_data.replace(' ', '')

    print("\nPlagiarised files are:")
    for file in my_files:
        file_str = read_file(file)
        length = max(len(master_str), len(file_str))
        similarity = 100 - round((levenshtein(master_str, file_str) / length) * 100, 2)

        if similarity > plag_threshold:
            print(f"'{master_path}' and '{file}' {similarity}% plagiarised")

def main():
    print("Welcome to Plagiarism Checker!")
    choice = int(input("Enter 1 for folder comparison with master file\n"
                       "Enter 2 to check for plagiarism in two files\n"
                       "Enter 3 to check for plagiarism in all files in a folder\n"))

    if choice == 1:
        plag = int(input("Enter the percentage of plagiarism allowed: "))
        master_path = input("Enter the path of the master file (not in the same folder): ")
        folder_path = input("Enter the path of the folder to scan: ")
        compare_folder_with_master(master_path, folder_path, plag)
    elif choice == 2:
        plag = int(input("Enter the percentage of plagiarism allowed: "))
        file1_path = input("Enter the path of the first file to scan: ")
        file2_path = input("Enter the path of the second file to scan: ")
        compare_files(file1_path, file2_path, plag)
    elif choice == 3:
        plag = int(input("Enter the percentage of plagiarism allowed: "))
        folder_path = input("Enter the path of the folder to scan: ")
        os.chdir(folder_path)
        my_files = glob.glob('*.txt')

        print("\nThe text files available are:")
        print(my_files)
        print("\n")

        for i in range(len(my_files)):
            for j in range(i, len(my_files)):
                if i != j:
                    file1_path = my_files[i]
                    file2_path = my_files[j]
                    compare_files(file1_path, file2_path, plag)

    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
