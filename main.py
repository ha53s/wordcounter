file = input(" Enter your file: ")
xfile = open(file)
count = {}
for line in xfile:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

lst = []
for k , v in count.items():
    lst.append((v , k))
    lst = sorted(lst, reverse=True)
print(lst[0])
