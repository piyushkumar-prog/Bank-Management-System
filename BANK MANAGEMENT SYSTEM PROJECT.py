#BANK MANAGEMENT SYSTEM
import pandas as pd
import random
import numpy as np
pd.options.mode.chained_assignment=None #To avoid setting with copy warning
print('                           |BANK MANAGEMENT SYSTEM|                 ')
print('________________________________________________________________________________________')
print()
print('                       ~ WELCOME!TO HIGHER BANK OF INDIA ~               ')
print('________________________________________________________________________________________')

j='Y'
while j=='Y' or j=='y':
     print()
     print('1.OPEN A NEW ACCOUNT')
     print()
     print('2.MANAGE EXISTING ACCOUNTS')
     print()
     n=int(input('ENTER YOUR REQUEST(1,2):'))
     print()

     df = pd.read_csv(r"paste here your csv file location link")
     df = df[['NAME','ACCOUNT_NO','TOTAL_AMOUNT','AADHAR_NO','PAN','FATHER_NAME','MOTHER_NAME','PHONE','PASSWORD']]
     if n==1:
        print("*****Please fill the below form carefully*****")
        print()
        name=input('ENTER YOUR FULL NAME:')
        print()
        while True:
            try:
                adno=int(input('ENTER YOUR AADHAR NO:'))
            except ValueError:
                print()
                print('AADHAR MUST BE NUMBER')
                print()
                continue
            else:
                break
            
        d=str(adno)
        while True:
            if len(d)==12:
                break
           
            else:
                print()
                print('PLEASE CHECK YOUR AADHAR NUMBER AND TRY AGAIN!')
                print()
                print('ENTER YOUR 12 DIGITS AADHAR NUMBER')
                print()
                adno=int(input('ENTER YOUR AADHAR NO:'))
                d=str(adno)
                continue
        print()
        panno=input('ENTER YOUR PAN NO:')
        while True:
             if len(panno)==10:
                 break
           
             else:
                 print()
                 print('PLEASE CHECK YOUR PAN NUMBER AND TRY AGAIN!')
                 print()
                 print('ENTER YOUR 10 DIGITS PAN')
                 print()
                 panno=input('ENTER YOUR PAN NO:')
                 continue
        print()
        fname=input('ENTER YOUR FATHER NAME:')
        print()
        mname=input('ENTER YOUR MOTHER NAME:')
        print()
        while True:
            try:
                phno=int(input('ENTER YOUR PHONE NO:'))
            except ValueError:
                print()
                print('PHONE NUMBER MUST BE NUMBER')
                continue
            else:
                break
        ph=str(phno)
        while True:
            if len(ph)==10:
                break
           
            else:
                 print()
                 print('PLEASE CHECK YOUR PHONE NUMBER AND TRY AGAIN!')
                 print()
                 print('ENTER YOUR 10 DIGITS PHONE NO')
                 print()
                 phno=input('ENTER YOUR PHONE NO:')
                 ph=str(phno)
                 continue
        print()
        tamount=int(input('ENTER AN INITIAL AMOUNT:'))
        print()
        accno=random.randint(1000000,9999999)
        print('YOUR ACCOUNT NUMBER:',accno)
        print()
        print('**To make strong password,use @,&,1,2,3...with letters**')
        passwrd=input('CREATE YOUR PASSWORD:')
        while True:
             if len(passwrd)>=5:
                 break
           
             else:
                 print()
                 print('CREATED PASSWORD MUST BE AT LEAST 5 CHARACTERS LONG!')
                 print()
                 passwrd=input('CREATE YOUR PASSWORD:')
                 continue
        df.loc[df.shape[0]] = [name,accno,tamount,adno,panno,fname,mname,phno,passwrd]
        df.to_csv(r"paste here your csv file location link",index=False)
        print()
        print('YOUR ACCOUNT IS CREATED SUCCESSFULLY!')
        print()
        print('----------------------------------------')

     elif n==2:
            print('**********************************LOGIN PAGE********************************************')
            print()
            acno=int(input('ENTER YOUR ACCOUNT NUMBER:'))
            while True:
                  if acno in df.values:
                       break
                  else:
                       print()
                       print('Account Doesnot Exist!')
                       print()
                       print('Please Check The Account Number And Try Again!')
                       print()
                       acno=int(input('ENTER YOUR ACCOUNT NUMBER:'))
                       continue
            print()
            print('**Please Enter Password Carefully,only 3 attempts are allowed!**')
            print()
            index=int(df[df['ACCOUNT_NO']==acno].index.values)
            for i in range(3):
                pas=input('ENTER YOUR PASSWORD:')
                print()
                if pas==df.loc[index,'PASSWORD']:
                   break
                else:
                    print('WRONG PASSWORD!,only',2-i,'attempt left')
            else:
                print('Maximum number of attempts exhausted')
                print()
                print('Press <Enter>')
                exit()
        
            print('YOU HAVE SUCCESSFULLY LOGGED IN TO YOUR ACCOUNT!')
            print()
            print('WELCOME BACK! Mr/Mrs',df.loc[index,'NAME'])
            print()
    
            i ="y"
            while i=='Y'or i=='y':
                print()
                print('1.Check Available Balance')
                print()
                print('2.Check your details')
                print()
                print('3.Withdraw Money')
                print()
                print('4.Deposit Money')
                print()
                print('5.Account To Account Money Transfer')
                print()
                print('6.Close Account')
                print()
                print('7.Exit')
                print()
                n1=int(input('ENTER YOUR REQUEST:'))
                print()
       
                if n1==1:
                    print('Your Available balance is RS.',df.loc[index,'TOTAL_AMOUNT'],'/-')
                    print()
                elif n1==2:
                    print()
                    print('----------------------------------------')
                    print()
                    print('Name:',df.loc[index,'NAME'])
                    print()
                    print('Account no:',df.loc[index,'ACCOUNT_NO'])
                    print()
                    print('PAN:',df.loc[index,'PAN'])
                    print()
                    print('Phone no:',df.loc[index,'PHONE'])
                    print()
                    print('Aadhar no:',df.loc[index,'AADHAR_NO'])
                    print()
                    print('Available Balance:', 'Rs.',df.loc[index,'TOTAL_AMOUNT'],'/-')
                    print()
                    print('----------------------------------------')
                    print()
                elif n1==3:
                   print('-----------------------------------------------')
                   amount=int(input('ENTER YOUR WITHDRAW AMOUNT:'))
                   if amount==df.loc[index,'TOTAL_AMOUNT']or amount<df.loc[index,'TOTAL_AMOUNT']:
                      df['TOTAL_AMOUNT'].iloc[index]=df.loc[index,'TOTAL_AMOUNT']-amount
                      df.to_csv(r"paste here your csv file location link")
                      print()
                      print('RS.',amount,'/- IS DEBITED FROM YOUR ACCOUNT SUCCESSFULLY!')
                      print()
                      print('Your Available Balance is RS.',df.loc[index,'TOTAL_AMOUNT'],'/-')
                      print('--------------------------------------------------')
                      print()
                   else:
                       print('INSUFFICIENT BALANCE!')
                       print('-----------------------------------------------')
                       print()
                elif n1==4:
                   print('-----------------------------------------------')
                   amount=int(input('ENTER YOUR AMOUNT TO DEPOSIT:'))
                   df['TOTAL_AMOUNT'].iloc[index]=df.loc[index,'TOTAL_AMOUNT']+amount
                   df.to_csv(r"paste here your csv file location link")
                   print()
                   print('RS.',amount,'/- IS CREDITED TO YOUR ACCOUNT SUCCESSFULLY!')
                   print()
                   print('Your Available Balance is RS.',df.loc[index,'TOTAL_AMOUNT'],'/-')
                   print('-----------------------------------------------')
                   print()
                elif n1==5:
                  print('-----------------------------------------------')
                  ac1=int(input('ENTER ACCOUNT NO. IN WHICH YOU WANT TO TRANSFER MONEY:'))
                  while True:
                       if ac1 in df.values:
                            break
                       else:
                            print()
                            print('Account Doesnot Exist!')
                            print()
                            print('Please Check The Account Number And Try Again!')
                            print()
                            ac1=int(input('ENTER ACCOUNT NO. IN WHICH YOU WANT TO TRANSFER MONEY:'))
                            continue
                  print()
                  index1=int(df[df['ACCOUNT_NO']==ac1].index.values)
                  amount=int(input('ENTER AMOUNT TO TRANSFER:'))
                  df['TOTAL_AMOUNT'].iloc[index1]=df.loc[index1,'TOTAL_AMOUNT']+amount
            
                  df['TOTAL_AMOUNT'].iloc[index]=df.loc[index,'TOTAL_AMOUNT']-amount
            
                  df.to_csv(r"paste here your csv file location link")
                  print('AMOUNT TRANSFERED SUCCESSFULLY!')
                  print()
                  print('MONEY TRANSFERED DETAILS:')
                  print('FROM:',acno)
                  print('TO:',ac1)
                  print('AMOUNT:RS.',amount,'/-')
                  print()
                  print('Your Avaialble Balance is RS.',df.loc[index,'TOTAL_AMOUNT'],'/-')
                  print('-----------------------------------------------')
                  print()
             
                elif n1==6:

                     
                  print('-----------------------------------------------')
                  for i in range(3):
                      pas=input('RE-ENTER YOUR PASSWORD:')
                      if pas==df.loc[index,'PASSWORD']:
                         df=df.drop(index)
                         df.to_csv(r"paste here your csv file location link")
                         print('YOUR ACCOUNT HAS BEEN CLOSED SUCCESSFULLY!')
                         print('-----------------------------------------------')
                         print("Thanks for using our services!!")
                         print('Press <Enter> to Exit')
                         exit()
                      else:
                         print()
                         print('WRONG PASSWORD!,only',2-i,'attempt left')
                         print()
        
                  else:
                     print()
                     print('Maximum number of attempts exhausted!')
                     print('Press <Enter>')
                     exit()
                elif n1==7:
                  print("Thanks for using our services!!")
                  exit()
                else:
                   print('Please choose a valid option(1,2,3,4,5,6,7)')
                   print()
                i=input('Do you want to continue?(Y/N):')
            else:  
                print('Thanks For Visiting Here!')
                exit()
       
     else:
          print('Please choose a valid option(1,2)')
          print("Kindly Restart the Procedure")
          print('Press <Enter>')
          exit()
     j=input('Do you want to continue?(Y/N):')
else:
     print('Thanks For Visiting Here!')
     exit()

#Created By Piyush Kumar























































































   
    
    
    

    
          
          
