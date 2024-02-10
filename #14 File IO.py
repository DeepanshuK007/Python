'''
Opening a File:
open() func is used to open a file which takes two arguments: the name of the file and the mode in which the file should be opened.

The mode can be 'r' for reading, 'w' for writing, 'a' for appending.
'''

f = open('REALITY.txt', 'w')
contents = f.read()
print(contents)

#Modes in file:
'''
There are various modes in which we can open files:
1. read(r): This mode opens the file for reading only and gives an error if the file does not exist. Thsi is the default mod eof no moode is passed as param.

2. write(w): This mode opens the file for writing only and creates a new file if the file does not exist.

3. append(a): This mode opens the file for appending only and creates a new file if the file does not exist.

4. create(x): This mode creates a file an dgives an error if the file already exists

5. text(t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode.

There is no difference between r and rt or w and wt since text mode is the default.

The default mode is 'r' (open for reading text, synonym of 'rt').

6. binary(b): used to handle binary files (images, pdfs, etc)
'''

#Writing to a File:
f = open ('myfile.txt', 'w')
f.write('Yo X4')

# Writing in a file can overwrite its contents, if u wan to append to a file instead of overwriting it, you can open it in append mode. 

# Closing a File: 
# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.
f.close()

#The 'with' statement:
#Alternatively, you can use the with statement to automatically close the file afer u are done with with it.
with open ('xyz.txt', 'w') as f:
    # do something with the file