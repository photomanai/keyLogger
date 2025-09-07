with open("myfile.txt",mode="w") as my_file:
file_write = my_file.write("sa")
with open("myfile.txt",mode="a") as my_file:
file_append = my_file.write("sa")
with open("myfile.txt",mode="r") as my_file:
file_read = my_file.read()
