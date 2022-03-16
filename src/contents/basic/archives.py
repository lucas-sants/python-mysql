#Open archive
archive = open("archiveTxt.txt")

#Read line by line
lines = archive.readlines()
for line in lines:
	print(line)

#Read archive complete
archiveComplete = archive.read()
print(archiveComplete)

#How to create a archive
# w = open("archiveTxt2.txt", "w")
