#file objects
#
"""f=open('file.txt','w')
f=open('file.txt','a')
f=open('file.txt','r+')


print(f.name)
print(f.mode)
f.close()
"""

#contact manager
with open('file.txt','r') as f:
    
    #f_contents = f.read(3)
    #f.readlines()
    #f.readlines()
    #print(f_contents, end='')
    size_to_read=10
    f_contents=f.read(size_to_read)
    print(f_contents,end='**')

    f.seek(0)

    f_contents=f.read(size_to_read)
    print(f_contents,end='**')



    #while len(f_contents)>0:
        #print(f_contents,end='*')
        #f_contents=f.read(size_to_read)
        #print(f.tell())
   
    #solves the memory issue
    """for line in f:
        print(line,end='')
        print(f.mode)"""
    

print(f.closed)


#writing files
with open('file2.txt', 'w') as f:
    f.write('Tesst')
    f.seek(0)
    f.write('R')
with open('file2.txt','r')as rf:
    with open('copyoffile2.txt','w') as wf:
        for line in rf:
            wf.write(line)
with open('Capture111.PNG','rb')as rf:
    with open('copyCapture111.PNG','wb') as wf:
        for line in rf:
            wf.write(line)


