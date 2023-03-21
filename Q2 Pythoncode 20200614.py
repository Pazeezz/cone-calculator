#Create Variables
r=0 
h=0
l=0
A=0
B=0
S=0
V=0
o=0
cal=0
run=0
#p is a Constant.(p=3.14 or 22/7)
p=3.214
#Get the True
E=True
#Apply True for While
while E:
#Inputs
    r=float(input("Enter the Radius = "))
    h=float(input(" Enetr the Height = "))
    l=float(input(" Enter the Slant Height = "))
#Need to check Are all inputs Positive numbers ? 
    if (r<0):
            print(" Error! Couldn't calculate, invalid input, Please enter the positive value for Radius")
    elif (h<0):
            print(" Error! Couldn't calculate, invalid input Please enter the positive value for Height")
    elif (l<0):
             print(" Error! Couldn't calculate, invalid input Please enter the positive value fot Slant Height")
#Input option for calculation
    else:
#Need to check options ?       
        o=input("Do you need to see what are the options  ? (Yes/No) = ")
        if o=="Yes":
#Display the options            
            print("A= all calculations")
            print("B= base area of cone")
            print("S= surface area of cone")
            print("V= volum of cone")
#Select your option   
        print("Which calculation do you want ? ") 
        cal= input("Please Enter the option (A/B/S/V) = ") 

#Proces
     #Option- A   
        if cal  =="A":
                    B=p*r*r
                    print("Base Area of a cone = ",B)
                    S=(p*r*r)+(p*r*l)
                    print("Surface Area of a cone = ",S)
                    V=1/3*p*r*r*h
                    print("Volume of the cone = ",V)

    #Option - B
        elif  cal=="B":
                    B=p*r*r
                    print("Base Area of a cone = ",B)

    #Option= S
        elif cal=="S":
                    S=(p*r*r)+(p*r*l)
                    print("Surface Area of a cone = ",S)

    #Option-V
        elif cal=="V":
                    V=1/3*p*r*r*h
                    print("Volume of the cone = ",V)

    #Display Error message for invalied options
        elif cal!=("A","B","S","V"):
                    print(" Error! Cannot calculate, Please enter the correct option..! ")

#Need to run/stop program?
    run=input("Do you want to run this program again ?(Yes/No) = ")
#True While for run program
    if run=="Yes":
        E=True
        
#Fales While for stop program        
    else:
        E=False
        print(" END!!! ")
