import csv    #importing csv module is necessary to save the results in a file

class AddingCircuit:    #class declaration

    
    def __init__(self):     #init function initializes empty lists and variables everytime an instance/object of AddingCircuit class is created
        
        self.num1 = []  #list that will contain 4 digits of the first binary number passed by the user
        self.num2 = []  #list that will contain 4 digits of the second binary number passed by the user
        self.tup = []   #list that will contain pairs of digits ready to be added
        self.sumBackwards = [] #list where the final result will be appended, starting with the very last digit
        self.finalSum = []      #list where the final result will be stored in the right order
        self.binaryNum1 = 0     #this variable will be assigned with the first number entered by the user
        self.binaryNum2 = 0     #this variable will be assigned with the second number entered by the user
        self.binaryResult = 0   #this variable will be assigned with the sum in binary system
        self.decimalResult = 0  #this variable will be used to store sum converted into decimal system
        self.c = 0      #c is for carry. This variable will contain any extra value that needs to be carried forward during the addition
        self.s = 0      #s represents the result of adding 2 digits together
        

    def greeting(self):     #function prints information about the program
        print("Enter two 4 digit binary numbers, digit by digit, to find their sum." )

    def getUserInput(self):      #function that prompts user to enter digits. Function uses try/except blocks to raise value error if the user enters wrong number
        while True:             #while loop ensures that after raising error the user can enter digits again, from the beginning
            try:                #if the digit is valid, it is appended to num1 or num2 list respectively
                self.num1.append(int(input("Enter first digit of your first number (0 or 1)>")))
                if self.num1[0] != 1 and self.num1[0] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num1.append(int(input("Enter second digit of your first number (0 or 1)>")))
                if self.num1[1] != 1 and self.num1[1] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num1.append(int(input("Enter third digit of your first number (0 or 1)>")))
                if self.num1[2] != 1 and self.num1[2] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num1.append(int(input("Enter fourth digit of your first number (0 or 1)>")))
                if self.num1[3] != 1 and self.num1[3] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num2.append(int(input("Enter first digit of your second number (0 or 1)>")))
                if self.num2[0] != 1 and self.num2[0] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num2.append(int(input("Enter second digit of your second number (0 or 1)>")))
                if self.num2[1] != 1 and self.num2[1] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num2.append(int(input("Enter third digit of your first number (0 or 1)>")))
                if self.num2[2] != 1 and self.num2[2] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
                self.num2.append(int(input("Enter fourth digit of your first number (0 or 1)>")))
                if self.num2[3] != 1 and self.num2[3] != 0:
                    raise ValueError("Invalid value, please enter 0 or 1")
            except ValueError as excpt:
                print(excpt)
        

    def mergeTup(self):     #this method uses a for loop to pair digits with the same index into a tuple
        for i in range(0, 4):
            self.tup.append((self.num1[i], self.num2[i]))

    def andGate(self,a,b):  #method that compares two 0/1 inputs using AND logic
        if a == 1 and b == 1:
            return 1
        else:
            return 0

    def orGate(self,a,b):   #method that compares two 0/1 inputs using OR logic
        if a == 0 and b == 0:
            return 0
        else:
            return 1

    def xorGate(self,a,b): #method that compares two 0/1 inputs using XOR logic
        if a != b:
            return 1
        else:
            return 0

    def halfAdderCircuit(self, xyTup, c):       #halfAdderCircuit takes a tuple and the carry variable as parameters
        x, y = xyTup                            #tuple of 2 binary digits is being unpacked into x and y values that need to be added
        xXORy = self.xorGate(x, y)              #XOR gate is being called
        xANDy = self.andGate(x, y)              #AND gate is being called
        xXORyANDc = self.andGate(xXORy, c)      #the result of XOR gate is being compared with the carry value using AND gate
        s = self.xorGate(xXORy, c)              #XOR gate determines the final sum value of the tuple (it will become one of the digits in finalSum)
        c = self.orGate(xANDy, xXORyANDc)       #OR gate determines if there is any value that needs to be carried over to the next tuple addition
        return(s, c)                            #tuple sum and carry value are being returned from this function call

    def fullAdderCircuit(self): #fullAdderCircuit uses for loop to iterate through tuples, starting with last
        for j in range(len(self.tup)-1, -1, -1):
            self.s, self.c = self.halfAdderCircuit(self.tup[j], self.c) #current tuple and the carry are being passed to halfAdderCircuit to find s and new c value
            self.sumBackwards.append(self.s)                            #s is being append to the sumBackwards
        self.sumBackwards.append(self.c)                                #last carry value becomes the first digit of the final result

    def reverseSum(self):   #this method puts sumBackwards into the right order and stores the results in finalSum list
        for k in range(len(self.sumBackwards)-1, -1, -1):
            self.finalSum.append(self.sumBackwards[k])

    def convertPrintWrite(self):    #this function converts lists of digits into binary and decimal results, prints results to the screen and writes them into a file
        self.binaryNum1 = bin(int("".join(str(i)for i in self.num1), 2))
        self.binaryNum2 = bin(int("".join(str(i)for i in self.num2), 2))
        self.binaryResult = bin(int("".join(str(i)for i in self.finalSum), 2))
        self.decimalResult = int("".join(str(i)for i in self.finalSum), 2)
        print(self.binaryNum1, " + ", self.binaryNum2, " = ", self.binaryResult, " or ", self.decimalResult, " in decimal system")
        with open('BinaryCircuitAddingResults.csv', 'a+') as BinaryCircuitAddingResults:
            sumResults = csv.writer(BinaryCircuitAddingResults)
            
            sumResults.writerow("{} + {} = {} or {} in decimal system".format(self.binaryNum1, self.binaryNum2, self.binaryResult, self.decimalResult))
            
    def __del__(self): #destructor function. Used to delete the object. After the object is destroyed it can be created again, with empty values, ready for use.
        pass

quitOrStay = 's' #variable that decides if the while loop will run again or if the program ends
while quitOrStay != 'q': #while loop will run as long as quitOrStay variable isn't set to 'q'
    addition = AddingCircuit() #instance of AddingCircuit is created and called addition
    addition.greeting()         # class member function calls
    addition.getUserInput()
    addition.mergeTup()
    addition.fullAdderCircuit()
    addition.reverseSum()
    addition.convertPrintWrite()
    del addition                # object addition is being deleted
    quitOrStay = input("Press any key to continue, 'q' to leave the program.") #user has a chance to decide if they want to continue or close the program
    
            

        
        
        
                
        
