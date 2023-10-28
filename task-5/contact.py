# ----------------------------------------------------- Import -------------------------------------------------------------- #

import os

class FileSaver:
     def saveToFile(self):
         print(f'\n\n\n{"-"*65} Add Contact {"-"*65}\n')
         self.fullname = input('Enter Full Name : ')
         self.phonenumber = input('Enter Phone Number : ')
         self.email = input('Enter Email : ')
         self.address = input('Enter Address : ')

         with open("contact.txt") as f:
            f = eval(f.read())
            list = [self.fullname,self.phonenumber,self.email,self.address]
            f.append(list)
         with open("contact.txt",'w') as file:
            file.write(str(f))
         input('\n\nYour Contact Was Added Successfully.\n\n\nPress Enter to continue ! ')
         os.system('cls')
         return

class PhoneBook():

    def saveToFile(self):
         fs = FileSaver()
         fs.saveToFile()

    def View(self, list):
        print(f"\n\n\t\t\t\t\t{'-'*25} Contact Dirictory {'-'*25}\n\n")
        print(f'{"="*120}')
        temp = ("\t\t{Name:20s}{PhoneNo:20s}{Email:20s}{Address:25s}\n{line:s}\n")
        strg=temp.format("\t\t",Name = "NAME",PhoneNo= "PHONE NUMBER",Email = "EMAIL",Address = "ADDRESS",line = "="*120)
        for item in list:
            strg += temp.format("\t\t",Name =item[0], PhoneNo=item[1],Email= item[2],Address=item[3],line="-"*120)
        print(strg)
        input('\n\nPress Enter to continue ! ')
        os.system("cls")
        return
    def readFromFile(self):
        with open('contact.txt', 'r') as f:
            f = eval(f.read())
        self.View(f)

    def search(self):
        list = []
        self.name  = input('\n\n\nEnter Valid Name : ')
        with open("contact.txt") as f:
            f = eval(f.read())
        for item in f:
            # print(item)
            if self.name in item[0]:
                list.append(item)
        self.View(list)

    def UpdateContact(self):
        while True:
            os.system('cls')
            print(f'\n\n\n{"-" * 65} Update Contact {"-" * 65}\n')
            print('Enter valid full name for Update contact')
            u = input('\n\nPress Y for  continue and B for back! ').upper()
            os.system("cls")
            if u == "Y":
                print(f'\n\n\n{"-" * 65} Update Contact {"-" * 65}\n')
                self.search()
                count = 0
                with open("contact.txt") as f:
                    f = eval(f.read())
                for item in f:
                    count +=1
                    if self.name == item[0]:
                        while True:
                            user = input('\nSelect, that you want to update !!\n\n1. Full Name\n2. Phone Number\n3. Email\n4. Address\n\n')
                            if user == "1":
                                user = input('Enter Fullname  : ')
                                item[0] = user
                                f[count-1] = item
                            elif user == "2":
                                user = input('Enter Phone number : ')
                                item[1] = user
                                f[count-1] = item
                            elif user == "3":
                                user = input('Enter Email : ')
                                item[2] = user
                                f[count-1] = item
                            elif user == "4":
                                user = input('Enter Address : ')
                                item[3] = user
                                f[count-1] = item
                            else:
                                input('Invalid input !! \n\nPress Enter To Continue ')
                                os.system("cls")
                                break
                            with open("contact.txt",'w') as file:
                                file.write(str(f))
                            print('\n\nYour Contact Was Successfully Update !')
                            user1 = input("Press Y for Continue and B for Back  ").upper()
                            os.system("cls")
                            if user1 == "Y":
                                pass

                            elif user1 == "B":
                                break
                            else:
                                input('Invalid input\n\nPress Enter to continue ! ')
                                os.system("cls")

            elif u =="B":
                return
            else:
                input('Invalid input\n\nPress Enter to continue ! ')
                os.system("cls")

    def DeleteContact(self):
        while True:
            os.system('cls')
            print(f'\n\n\n{"-" * 65} Delete Contact {"-" * 65}\n')
            print('Enter valid full name for Update contact')
            u = input('\n\nPress Y for  continue and B for back! ').upper()
            os.system("cls")
            print(f'\n\n\n{"-" * 65} Delete Contact {"-" * 65}\n')
            if u == "Y":
                with open("contact.txt") as f:
                    f = eval(f.read())
                self.View(f)
                print(f'\n\n\n{"-" * 65} Delete Contact {"-" * 65}\n')
                user = input('Enter Fullname, That you want to Delete  : ')
                count = 0
                for item in f:
                    if user == item[0]:
                        f.pop(count)
                        with open("contact.txt", 'w') as file:
                            file.write(str(f))
                        print('\nYour Contact Was Successfully Delete !')
                        input('\n\nPress Enter to continue ! ')
                    count += 1

            elif u == "B":
                return
            else:
                input('Invalid input\n\nPress Enter to continue ! ')
                os.system("cls")


 # --------------------------------------------------------- Test Run -------------------------------------------------------#

if __name__ ==  '__main__' :
    while True:
        object = PhoneBook()
        user = input(f"\n\n\n{'-'*140}\n\n\t\t\t\t\t\t\t< WELCOME TO THE ~ PHONE BOOK ~ >\n\n{'-'*140}\n"
                     "\n1. Add Contact\n2. View Contact\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n\n[q] Quit \n\n")

        os.system("cls")

        if user == "1":
            object.saveToFile()

        elif user == "2":
            object.readFromFile()

        elif user == "3":
            object.search()

        elif user == "4":
            object.UpdateContact()

        elif user == "5":
            object.DeleteContact()

        elif user == "q":
            os.system("cls")
            break

        else:
            input('Invalid input\n\n Press Enter to continue ! ')
            os.system("cls")
