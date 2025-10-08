
import csv
file_csv = r"C:\Users\emmab\OneDrive\Desktop\proo\file.csv"

# code to read the contents of the file
# with open(file_csv, "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
# Result:
# {'Name': 'Alice', 'Age': '14', 'Grade': 'B'}
# {'Name': 'Micheal', 'Age': '15', 'Grade': 'A'}
# {'Name': 'John', 'Age': '13', 'Grade': 'C'}
# {'Name': 'Mary', 'Age': '14', 'Grade': 'A'}
# {'Name': 'Grace', 'Age': '15', 'Grade': 'B'}


# append new data
# list_of_students = [
#     ["Alice", 14, "B"],
#     ["Micheal", 15, "A"],
# ]
# with open(file_csv, "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(list_of_students)

### task 4  read te updated file and calculate  the total number of students, and how many students got an A
# empty_list = []
# A_students = []
# with open(file_csv, "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         empty_list.append(row)
#     # for the total number of students
#     print(f"Total number of students: {len(empty_list)}")
#     # to find the students that got an A:
#     for row in empty_list:
#         if "A" in row:
#             A_students.append(row)

#     print(f"Number of students that got an A: {len(A_students)}")


### task 5: Create another csv file named grades_summary.csv. Write a summary that shows how many students fall into each grade category.
# with open("grades_summary.csv", "w", newline="") as summary:
#     writer = csv.writer(summary)
#     writer.writerow(["Grade", "Number of Students"])
#     empty_list = []
#     A_students = []
#     B_students = []
#     C_students = []
#     D_students = []
#     E_students = []
#     F_students = []
#     with open(file_csv, "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             empty_list.append(row)
#         # to find the students that got an A:
#         for row in empty_list:
#             if "A" in row:
#                 A_students.append(row)
#         # to find the students that got an B:
#         for row in empty_list:
#             if "B" in row:
#                 B_students.append(row)
#         # to find the students that got an C:
#         for row in empty_list:
#             if "C" in row:
#                 C_students.append(row)
#         # to find the students that got an D:
#         for row in empty_list:
#             if "D" in row:
#                 D_students.append(row)
#         # to find the students that got an E:
#         for row in empty_list:
#             if "E" in row:
#                 E_students.append(row)
#         # to find the students that got an F:
#         for row in empty_list:
#             if "F" in row:
#                 F_students.append(row)

#         list_of_grades = [
#             ["A", len(A_students)],
#             ["B", len(B_students)],
#             ["C", len(C_students)],
#             ["D", len(D_students)],
#             ["E", len(E_students)],
#             ["F", len(F_students)],
#         ]

#         writer.writerows(list_of_grades)


        
