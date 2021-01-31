import csv

def write_into_csv(info_list):
    with open('stud_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name ","Age ","Mob_no ","Email "])

        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    stud_num = 1
    while(condition):
        stud_info = input("Enter the Information for Student{} in following format (Name Age Mob_no Email ) ".format(stud_num))
        print("Following Information saved succesfully  " + stud_info)

        #split
        stud_info_list = stud_info.split(" ")
        print("Entered Split up Information " + str(stud_info_list))

        print("\nThe Entered Information is - \n Name: {} \n Age:{} \n Mob_no: {} \n Email: {} "
              .format(stud_info_list[0],stud_info_list[1],stud_info_list[2],stud_info_list[3]))
        choice_check = input("Is the entered information correct ? (yes/no) : ")

        if choice_check == "yes":
            write_into_csv(stud_info_list)
            cond_check = input("Enter 'yes'/'no' if You want to enter another student's data : ")
            if cond_check == "yes":
                condition = True
                stud_num = stud_num + 1
            elif cond_check == "no":
                condition = False
        elif choice_check == "no":
            print("Please Re-enter the information ! ")
