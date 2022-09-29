# make sure that the file and the code file are in the same place, so that you can read it, otherwise, you cannot do it.
f = open("configcrashsolution.txt") # just read
# item = f.read() # Read all of stuff in the file, you can define any variable here
# print(item) # show the stuff in the file (single strying)

# for c in item:
#    print(c) # read every stuff, but separate every characters in different line

# for line in f:
#    print(line) # add extra space between the different sentences (remember to disable the third and the forth line in the page, which mean that you cannot use this line with read() statement)

# print(f.readline()) # display only one line in the file, here is the first line in the file, if you want show more lines, use this statement one more times.
# print(f.readlines()) # put everything into a list, and display them all. Pay attention to the difference between this line and the last line!
f.close() # after using a open() statement, you should use close() statement to close your file.
