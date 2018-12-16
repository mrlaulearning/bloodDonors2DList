#Import the itemgetter class from the operator module>
from operator import itemgetter
from datetime import datetime

def main():

    #Signing up new customers
    def addDonors():
        #Take their details
        firstname=input("What is the donor's first name:\n")
        lastname=input("What is the donor's last name:\n")
        patientNum=input("Please enter their patient number:\n")
        bloodGroup=input("Please enter their blood group (ABO+-):\n")
        dob=input("Please enter their DOB in format dd/mm/yyyy:\n")
        
        #Write to a list and then return this so it can be used by the fileWrite procedure>
        donorList=[]
        donorList.append(firstname)
        donorList.append(lastname)
        donorList.append(patientNum)
        donorList.append(bloodGroup)
        donorList.append(dob)

        return donorList
    #Take the donorList list as an arguement
    def fileWrite(donorDetails):
        
        #read the file and evaluate the list in the file
        donorFile=open("bloodDonors.txt","r")
        tempList=eval(donorFile.read())
        donorFile.close()

        #append the new customer's details to the list then write the list back to the file
        tempList.append(donorDetails)
        donorFile=open("bloodDonors.txt","w")
        donorFile.write(str(tempList))
        donorFile.close()
        

    #printing out all donors
    def fileRead():
        donorFile=open("bloodDonors.txt","r")
        readList=eval(donorFile.read())
        donorFile.close()

        pad=" "
        #paddding = pad*(12-len(str(donor details))
        print("All donors:")
        
        for count in range(len(readList)):
            for details in range(len(readList[0])):
                print(readList[count][details]+pad*(12-len(str(readList[count][details]))),end=" ")
            print()


        #two different ways of sorting the list by surname or (descending bloodGroup)

        #using a lambda function
        nameSort=sorted(readList, key=lambda name: name[3])

        print("\nSorted by blood group:")

        for count in range(len(nameSort)):
            for details in range(len(nameSort[0])):
                print(nameSort[count][details]+pad*(12-len(str(nameSort[count][details]))),end=" ")
            print()
            
        #using the itemgetter class
        nameSort2=sorted(readList, key=itemgetter(2),reverse=True)

        print("\nSorted by patient number:")
        for count in range(len(nameSort2)):
            for details in range(len(nameSort2[0])):
                print(nameSort2[count][details]+pad*(12-len(str(nameSort2[count][details]))),end=" ")
            print()

        #sort by date

        #convert all date strings into  datetime objects>
        for donors in range(len(readList)):
            readList[donors][4]=datetime.strptime(readList[donors][4], "%d/%m/%Y")

        #sort by date
        dateSort=sorted(readList, key=itemgetter(4))

        #convert the datetime objects back to strings
        for donors in range(len(readList)):
            readList[donors][4]=readList[donors][4].strftime("%d/%m/%Y")

        print("\nSorted by date:")
        for count in range(len(dateSort)):
            for details in range(5):
                print(dateSort[count][details]+pad*(12-len(str(dateSort[count][details]))),end=" ")
            print()

        
        
        
    def findDonor():
        #open and read the contents of the text file
        donorFile=open("bloodDonors.txt","r")
        readList=eval(donorFile.read())
        donorFile.close()

        pad=" "
        
        #our search term
        bloodGroup=input("Please enter the blood group you are looking for?")

        #a boolean flag 
        found=False

        #perform a linear search
        for count in range(len(readList)):
            for details in range(len(readList[0])):
                if bloodGroup == readList[count][3]:
                    found=True
                    #if found then output the record with padded formatting
                    print(readList[count][details]+pad*(12-len(str(readList[count][details]))),end=" ")
            print()
        #if the item is not found
        if found == False:
            print("No donors were found for blood group",bloodGroup)
            
        print()


    
    task=input("What do you want to do: \n\
A) Add a blood donor \n\
B) Output all blood donors\n\
C) Find a blood donor\n").upper()

    if task == "A":
        donorDetails=addDonors()
        fileWrite(donorDetails)
    elif task == "B":
        fileRead()
    elif task == "C":
        findDonor()
    else:
        print("This is not recognised")
        return main()
    main()

#if imported, call main straight away
if __name__ == "__main__":
    main()





