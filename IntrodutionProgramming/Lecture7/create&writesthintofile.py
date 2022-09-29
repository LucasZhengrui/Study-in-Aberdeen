fh = open("file.txt", 'w') # r: only readable, w: can write | Here is the statement that you can create a new offline file in your laptop.

# fh.write("type sth here, congrats!")
# fh.write("\n1000") # check the difference between this line and the next line
# fh.write('''\n"100"''') # 100 will make an error: only string here, not int | So should be "100"

print("type sth here, congrats! 100000000", file = fh) # just like the write statement
fh.close()
