import os
import shutil

#print(os.path.dirname(__file__))

title = "Dragon Ball Z"
season = "S001"
extension = "txt"


print("Give me your directory: ")
user_dir = input()
user_file_list = os.listdir(user_dir)

try:
    if len(user_file_list) == 0:
        quit("nie ma plików leszczu")

except FileNotFoundError:
    quit("zła ścieżka baranie")

print(*user_file_list, sep="\n")
for x in user_file_list:
    if x.startswith(title):
        temp = x.split()
        shutil.move(user_dir + "/" + x,
                    user_dir + "/" + " ".join(temp[:temp.index(season) + 2]) + "." + extension)
