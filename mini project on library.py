class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendict={}
    def displayBook(self):
        print(f"We have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("Lender-Book batabase has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendict[book]}")
    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")
    def returnBook(self,book):
        self.lendict.pop(book)
if __name__=='__main__':
    Ravi=Library(['Python','C++','JAVA','JAVA SCRIPT','operating system'],"raviLibrary")

    while(True):
        print(f"Welcome to the {Ravi.name} Library. Enter Your choice to continue")
        print("1.Display books")
        print("2.Lend a books")
        print("3. ADD a books")
        print("4. Return a books")
        user_choice=(input())
        if user_choice not in ['1','2','3','4']:
            print("please enter the valid number")
            continue
        else:
            user_choice=int(user_choice)


        if user_choice==1:
            Ravi.displayBook()
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend:")
            user=input("Enter your name:")
            Ravi.lendBook(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add:")
            Ravi.addBook(book)
        elif user_choice==4:
            book=input("Enter the book you want to return:")
            Ravi.returnBook(book)
        else:
            print("please choice a shown number")

        print("Press q to quit and c to continue")
        user_choice2=" "
        while(user_choice2!="c"and user_choice!='q'):
            user_choice2=input()
            if user_choice=='q':
                exit()
            elif user_choice2=='c':
                continue
