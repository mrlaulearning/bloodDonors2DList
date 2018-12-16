#Import the itemgetter class from the operator module
from operator import itemgetter
from datetime import time

def main():

    #Signing up new customers
    def addDonors():
        #Take their details
        firstname=input("What is the donor's first name:\n")
        lastname=input("What is the donor's last name:\n")
        patientNum=input("Please enter their patient number:\n")
        bloodGroup=input("Please enter their blood group (ABO+-):\n")
        dob=input("Please enter their DOB in format dd/mm/yyyy:\n")
        
        #Write to a list and then return this so it can be used by the fileWrite procedure
        

    #Take the donorList list as an arguement
    def fileWrite(donorDetails):
        pass
        #read the file and evaluate the list in the file
        

        #append the new customer's details to the list then write the list back to the file
        

    #printing out all donors
    def fileRead():
        
        pad=" "
        #paddiing = pad*12-len(str(donor details))
        print("All donors")
        
        print()

        #two different ways of sorting the list by surname or (descending price)

        #using a lambda function
        #nameSort=sorted(custList, key=lambda name: name[1])

        #print("\nSorted by surname, unformatted:")

            
        #using the itemgetter class
        #nameSort2=sorted(custList, key=itemgetter(4),reverse=True)

        #print("\nSorted by bloodGroup, unformatted:")
        
##        for names in range(len(nameSort2)):
##            print(nameSort2[names])    
        
    task=input("What do you want to do: \n\
A) Add a blood donor \n\
B) Find a blood donor\n").upper()

    if task == "A":
        donorDetails=addDonors()
        fileWrite(donorDetails)
    else:
        fileRead()
    main()

#if imported, call main straight away
if __name__ == "__main__":
    main()





