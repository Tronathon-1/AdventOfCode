import re

res = []

regex = r"mul\([0-9]+,[0-9]+\)"
tot = 0
nres = []
with open("input.txt") as file:
    for l in file:
        res.extend(re.findall(regex, l))
for i in range(len(res)):

    nres.extend(re.findall(r"[0-9]+", res[i]))
for i in range(0, len(nres)-1, 2):
    tot += int(nres[i]) * int(nres[i+1])

print(tot)





# import resource
# import os

# file_name = "input.txt"

# print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

# txt_file = open(file_name)

# count = 0

# for line in txt_file:
#     # we can process file line by line here, for simplicity I am taking count of lines
#     count += 1

# txt_file.close()

# print(f'Number of Lines in the file is {count}')

# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)
