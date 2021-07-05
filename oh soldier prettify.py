import os
def soldier(path,file,formate):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(file) as f:
        filelist=f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())

        if os.path.splittext(file)[1]==format:
            os.rename(file,f"{i}.{format}")
            i+=1

soldier(r"C:\Users\dell\Desktop\HTML\images",r"C:\Users\dell\Desktop\HTML\images",".png")


