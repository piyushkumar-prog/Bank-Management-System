    #---------------------------------Movie Ticket Booking---------------------------------#

print ("\n\n           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print     ("           ------------------| GALAXY THEATRE Mashrak |-----------------")
print     ("           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print("___________________________\n")
print ("1.New User")
print ("2.Existing User")
print ("3.Exit")
print("___________________________\n")

#Reading UserData(csv File)
import pandas as pd
user_data=pd.read_csv(r"D:\Documents\Informatics practices\Programming\user_data.csv")
user_data= user_data[['user_id','user_pass']] #Reading only Two columns

option=int(input("Choose Any One Option (1/2/3): "))

#For Wrong Input
while option > 3:
    print("\n uff!!,You have choosen wrong Option!!")
    option=int(input(" Please select any one option(1/2/3): "))
#1.New User
if option==1:
    print("Welcome!!")
    user_name=input("Please Enter Your Name: ")
    user_id=input("Create Your User ID : ")
    print("\nPassword should have atleast 8 characters")
    password=input("Create Your Password: ")
        
    #Saving User Details in csv file(user_data)
    user_data.loc[user_data.shape[0]] = [user_id,password]
    user_data[['user_id','user_pass']].to_csv(r"D:\Documents\Informatics practices\Programming\user_data.csv")
    print("\n\nCongratulations!! You Have Successfully Logged in!!\n")
    Continue=input("Do You Want To Continue Type(Y/N): ")
    if Continue=='N'or Continue=='n':
        print("See You Next Time :( ")
        exit()

#2.Existing User
elif option==2:
    print("Welcome Back!!")
    u_id=input("Please Enter Your UserID: ")
    index = int(user_data[user_data['user_id']==u_id].index.values)
    for i in range(5):
        pswrd=input("                Password: ")
        if pswrd== user_data.loc[index,'user_pass']:
            print('\nPassword Matched!!')
            break
        else:
            print('Wrong password',4-i,'attempt left')
            
    else:
        print('Access Denied!! maximum attempt used ')
        print("See You Next Time :( ")
        exit()
    
    print("Congrats! Mr/Mrs",u_id,",You Have Successfully Entered!!")

#3.Exit
elif option==3:
    print("See You Next Time :( ")
    exit()
    
#Reading Movie_List(csv File)
df=pd.read_csv(r"D:\Documents\Informatics practices\Programming\movie_list.csv")
input("\nPress <Enter Key> To Check Available Movies.........")
print("------------------------------------")

#Printing Only 'Movie_Name'(Column) From 'Movie_List'
for (i,j) in df.iterrows():
    print(i+1,'. ',j['Movie_Name'])
    print("------------------------------------")
print()

#Printing Details Of Movie Choosen by User
m_name = int(input("Enter index-value of That Movie would You like to Book(Like:1/2/3/4): "))
total_no_movie = df.Movie_Name.count()
while m_name > total_no_movie:
    print('\nWrong index Value!!')
    m_name=int(input("Please re-enter index-value of that Movie(Mentioned above) would You like to Book(Like:1/2/3): "))
else:
    m_name2 = m_name-1 #Making index-value(Given by user) equal to index-value(stored in csv file)
    print("\nYou Have Choosen:")
    print("---------------------------------------------")
    print("       Movie:",df.iat[m_name2,0])
    print("    Director:",df.iat[m_name2,1])
    print("        Cast:",df.iat[m_name2,2])
    print("    Duration:",df.iat[m_name2,3])
    print("Ticket Price: Rs",df.iat[m_name2,4],"/- Only")
    print("---------------------------------------------\n\n")

#Selection of ticket Category
input("Press <Enter Key> For Next Step.....")
print("=============================================================================")
print("\n_________________________\n")
print("1.General(Non-AC)")
print("2.AC")
print("3.Exit")
print("_________________________\n")
ch=int(input(" Enter your choice(1/2/3): "))
print()

while ch > 3:
    print("\n UFF!!,Please Select the Suitable Option (given above)!")
    ch=int(input(" Re-enter your choice (1/2/3): "))
else:
    #1.General(Non-AC)
    if ch==1:
        print("\n\n------------------>> General(Non-AC) <<------------------")
        ticket = int(input("How Many Tickets!! You want to Book: "))
        cost   = df.at[m_name2,'Price']
        total_price=ticket*cost
        print("\n\n\n\nTake a Look of Your Bill:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("       Ticket Price: ",cost)
        print(" Numbers Of Tickets: ",ticket)
        print(" You Have To Pay RS:",cost,"*",ticket)
        print("                   =",total_price,'/- only')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    #2.AC
    elif ch==2:
        print("\n\n----------------->> AC <<-----------------")
        ticket = int(input("How many Tickets!! You want to Book: "))
        cost   =int(df.at[m_name2,'Price'])
        ac_cost=300
        total_price=(ticket*cost)+(ticket*ac_cost)
        print("\n\n\n\nTake a Look of Your Bill:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("       Ticket Price: ",cost)
        print("  Number of Tickets: ",ticket)
        print("Total Tickets Price: ",ticket,"X",cost)
        print("                   = ",(ticket*cost))
        print("          AC Charge: ",ac_cost)
        print("   Total Charge(AC): ",ticket,"X",ac_cost)
        print("                   = ",(ticket*ac_cost))
        print(" You Have To Pay RS:",ticket*cost,"+",ticket*ac_cost)
        print("                   =",total_price,"/- Only")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    
    #3.Exit    
    elif ch==3:
        print("See You Next Time  ")
        print(":(")
        input()
        exit()

#Confirmation before buying tickets 
Continue=input("Do You Want To Buy Tickets (y/n):")
if Continue=='N'or Continue=='n':
        print("See You Next Time :( ")
        input()
        exit()
else:
    print("Congratulations! Your Tickets Are Booked!!\n")
    input("Press <Enter Key> To Collect Your Tickets........")
    print("\n\n\n\n\n\n\n\n\n")

#Ticket Printing
    print("___________________________________________________")
    print("---------------------------------------------------")
    print("              GALAXY THEATRE MASHRAK\n")
    print("         Movie:",df.iat[m_name2,0])
    print("      Duration:",df.iat[m_name2,3])
    print("        Timing:","10:00AM-01:00PM")
    print(" Total Tickets:",ticket)
    print("   Total Price:",total_price,"\n")
    print("                                 Status: confirmed ")
    print("___________________________________________________")
    print("---------------------------------------------------\n\n")
    input("\n")
    print("Thank You for Visiting GALAXY THEATRE :)\n")
    
#----------------------------------------------END----------------------------------------------#



#Replace CVS file location link with yours.
#Make two csv files one for users data and second one for movies list.

#NOTE:
#This project is created for learning purpose ,its open source but copying and pasting project is not learning. So,learn and create your own.
#Follow us of Github (finalboss077) for more projects.