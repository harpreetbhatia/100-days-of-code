
with open("pytest.txt", mode="r") as bigfile:
    reader = bigfile.read()
    for i,part in enumerate(reader.split("import pytest")):
        with open("solution" + str(i+1)+ ".py", mode="w") as newfile:
            newfile.write("import pytest"+part)

# with open("pytest.txt", mode="r") as bigfile:
#     smallfile_prefix = "sol_"
#     file_count = 0
#     smallfile = open(smallfile_prefix + str(file_count), 'w')
#     for line in bigfile:
#         if line.startswith("import pytest"):
#             smallfile.close()
#             file_count += 1
#             smallfile = open(smallfile_prefix + str(file_count), 'w')
#         else:
#             smallfile.write(line)
#     smallfile.close()
 