path1= input("enter the file name:")
x= path1.split('.')
ext=x[-1]
if ext == "py":
    print("The extension of file is: 'python'")

elif ext == "c":
    print("The extension of file is: 'c'")
    
elif ext == "cpp":
    print("The extension of file is: 'c++'") 
    
elif ext == "html":
    print("The extension of file is: 'HTML'")
    
elif ext == "pdf":
    print("The extension of file is: 'PDF'")
    
elif ext == "doc":
    print("The extension of file is: 'document(MS word)'")
    
elif ext == "exe":
    print("The extension of file is: 'Executable file'")
    
else: 
    print("unknown")
