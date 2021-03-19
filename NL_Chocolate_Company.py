#comment like a pro
'''
sprint week 2 project:

By: Dryden Bussey and Jen Colford

Thursday, March 18th, 2021

'''

#Initialize a counter
claims_ctr = 0


#setting up the imports

import datetime

#set up the option functions

# built in function for per deim calculation
'''
calculatePerDiem:

a function used to calculate the per diem cost in the main function
num_days = the number of days calculated from the start date and end date of the claims
calc = per diem amount either low or high depending on the days traveled

'''
def calculatePerDiem(num_days, calc):
    return num_days * calc

# build in function for mileage calculation
'''
calculateMileage
a function used to calculate the mileage amount depending on if the car is owned or rented
number_of_days = the number of days the person has traveled
rental_rate = 56.00 per day
kilometers_travelled = a user imput asking how many kilometers they traveled in their own car
mileage_amount = 0.10 per km

'''
def calculateMileage(own_or_rented,rental_rate,mileage_amount, number_of_days):
    if own_or_rented == "R":
        return number_of_days * rental_rate
    else:
        kilometers_travelled = int(input("Enter total numbers of kilometers travelled: "))
        return kilometers_travelled * mileage_amount
    
    
#Main function for option 1
def Employee_Travel_Claim():
    while True:
        global claims_ctr
        
        print()
        print("Start a New Claim.")
        
        # Get the default values and set to variables
        
        f = open('Sprint_Week_2/TCDef.dat', 'r')
        INVOICE_NUMBER = int(f.readline())
        HST_rate = float(f.readline())
        per_diem_low = float(f.readline())
        per_diem_high = float(f.readline())
        rental_compensation = float(f.readline())
        rental_rate = float(f.readline())
        f.close()
    
            
        #Inputs for function
        
        employee_name = input("Please enter your name: ")
        employee_phone_number = input("Please enter your number: ")
        location_of_trip = input("Please enter your destination: ")
        own_or_rented = input("Did you rent a car or use your own? (O/R): ")
        own_or_rented = own_or_rented.upper()
        # use datetime to split up date imputs
        
        
        start_date = input("Enter the start date of your trip (YYYY,MM,DD): ")
        start_date_formatted = datetime.datetime.strptime(start_date,"%Y,%m,%d")
        start_date_finished = str(start_date_formatted.date()) #this one is string for printing
        
        
        end_date = input("Enter the end date of trip (YYYY,MM,DD): ")
        end_date_formatted = datetime.datetime.strptime(end_date,"%Y,%m,%d")
        end_date_finished = str(end_date_formatted.date())
        
        #end_date_finished = datetime.datetime.strptime(end_date_formatted, "%Y,%m,%d")
        
        number_of_days = ((end_date_formatted - start_date_formatted).days)
        
        
        print("Number of travel days: ", number_of_days)
        
        # owned or rented loop
        
        mileage_rate = calculateMileage(own_or_rented,rental_rate,rental_compensation,number_of_days)
                 
        # per diem function 
        
        if number_of_days <= 3:
            #per_deim = number_of_days * 85
            per_deim = calculatePerDiem(number_of_days, per_diem_low)
        else:
            #per_deim = number_of_days * 100
            per_deim = calculatePerDiem(number_of_days, per_diem_high)
            
                
        # Other Calculations       
        per_deim_hst = HST_rate * per_deim
        per_diem_with_hst = per_deim_hst + per_deim
            
        claim_amount = mileage_rate  + per_diem_with_hst
        
        # Writing data in file to be saved  
        f = open('Sprint_Week_2/Claims.dat', 'a')
        f.write("{},".format(str(INVOICE_NUMBER)))
        f.write("{},".format(employee_name))
        f.write("{},".format(per_deim)) 
        f.write("{},".format(per_diem_with_hst))
        f.write("{},".format(mileage_rate))
        f.write("{},".format(claim_amount))
        f.write("{},".format(start_date_finished))
        f.write("{},".format(end_date_finished))
        f.write("{},\n".format(location_of_trip))
        f.close() 
        
         
        #Print Statment after calculations were completed
        print()
        print("-------------------------")
        print()
        print("Your Per Diem is: ", per_deim)
        print("HST on per diem: ", per_deim_hst)
        print("Your mileage claim is: ", mileage_rate)
        print("Your total claim: ", claim_amount)
        print()
        print("The claim has been processed and the information has been saved")
        
        #adding one to the claim counter and invoice number
        claims_ctr += 1
        INVOICE_NUMBER +=1
        INVOICE_NUMBER = str(INVOICE_NUMBER)
        HST_rate = str(HST_rate)
        per_diem_low = str(per_diem_low)
        per_diem_high = str(per_diem_high)
        rental_compensation = str(rental_compensation)
        rental_rate = str(rental_rate)
        
        
        #rewriting the constants to the constant folder
        f = open('Sprint_Week_2/TCDef.dat', 'w')
        f.write(INVOICE_NUMBER + "\n")
        f.write(HST_rate + "\n")
        f.write(per_diem_low + "\n")
        f.write(per_diem_high + "\n")
        f.write(rental_compensation + "\n")
        f.write(rental_rate + "\n")
        f.close()
        
        
        
       
        # A input to ask if the user would like to continue
        Continue = input("Would you like to add another claim (Y/N): ")
        
        if Continue.upper() == "Y":
            continue
        
        else:
            break

    print("Number of claims saved: ",claims_ctr)
    Anykey = input("Press any key to continue.")
    
#Function for changing default values

def showDefaults():
    print()
    print("Edit system default settings.")
    print()
    
    # read the file to see the default values that are in the system already
    
    print("NL Chocolate Company Value Editor")
    f = open('Sprint_Week_2/TCDef.dat', 'r')
    ClaimNum = f.readline()
    HSTRate = f.readline()
    perDiemLow = f.readline()
    perDiemHigh = f.readline()
    mileage_rate = f.readline()
    rental_rate = f.readline()
    f.close()
    
    # Displays the current defaults
    
    print("Current default values: ")
    print(ClaimNum)
    print(HSTRate)
    print(perDiemLow)
    print(perDiemHigh)
    print(mileage_rate)
    print(rental_rate)
    
    # Ask the user for new values
    
    print("add a new claim number")
    new_claim = input("New Claim number: ")
    print("add the new HST rate")
    new_hst = input("New HST Rate: ")
    print("add the new low per diem")
    new_pd_low = input("New low per diem: ")
    print("add the new high per diem")
    new_pd_high = input("New high per diem: ")
    print("add the new mileage rate: ")
    new_mileage = input("New mileage rate: ")
    print("add the new rental rate: ")
    rental_rate = input("New rental rate: ")
    
    
    # shows the user the changed values inputted
    
    print()
    print("New values added")
    print()
    print("new claim number: ",new_claim)
    print("new HST rate: ",new_hst)
    print("new low per diem rate: ",new_pd_low)
    print("new high per diem rate: ",new_pd_high)
    print("new mileage rate: ",new_mileage)
    print("new rental rate: ",rental_rate)
    
    
    # Write those values back into the file, this will overwrite whatever is currently there
    
    f = open('Sprint_Week_2/TCDef.dat', 'w')
    f.write(new_claim + "\n")
    f.write(new_hst + "\n")
    f.write(new_pd_low + "\n")
    f.write(new_pd_high + "\n")
    f.write(new_mileage + "\n")
    f.write(rental_rate + "\n")
    f.close()
    
    #statement showing the values have changed in the file
    
    print()
    print()
    print("Default values have been successfully changed")
    Anykey = input("Press any key to continue.")
    
#Function for printing a travel report

def travel_report():
    print()
    print("print a report")
    
    #datetime formatting for print sheet
    
    current_time_now = datetime.datetime.now()
    current_time_month = current_time_now.strftime("%m")
    current_time_day = current_time_now.strftime("%d")
    current_time_year = current_time_now.strftime("%Y")
    
    #print statement
    print(" " * 11 +"1" + (" " * 10) + "2" + (" " * 10) + "3" + (" " * 10) + "4" + (" " * 10) + "5" + (" " * 10) + "6" + (" " * 10) + "7" + (" " * 10) + "8")
    print(9 * "1234567890")
    print()
    print()
    print(29 * " " + "SMAKERS CHOCOLATE COMPANY")
    print()
    print()
    print(22 * " " + "TRAVEL CLAIMS LISTING AS OF " + str(current_time_month) + "-" + str(current_time_day) + "-" + str(current_time_year))
    print()
    print()
    print("Claims" + 5 * " "  + "CLAIM" +8 * " " + "SALESPERSON" + 5 * " "  + "CLAIM" + 13 * " " + "PER DIEM" + 5 *" " + "MILEAGE" + 3 * " " + "CLAIM")
    print("NUMBER" + 6 * " " + "DATE" + 11 * " " + "NAME" + 8 * " " + "LOCATION" + 12 * " " + "AMOUNT" + 6* " " + "AMOUNT" + 4 * " " + "AMOUNT")
    print()
    print("="* 91) 
    
    # Setting up counters
    claim_ctr = 0
    claim_totalACC = 0 
    per_diem_ACC = 0
    mileage_amount_ACC = 0
    
    # open the file to read the values presented
    f = open('Sprint_Week_2/Claims.dat', 'r')
    
    
    # splitting the claim values so they can be easily printed

    for claims in f:
        claims_list = claims.split(",")
        claim_number = claims_list[0]
        claim_date = claims_list[6]
        salesperson_name = claims_list[1]
        location_of_trip = claims_list[8]
        per_diem = float(claims_list[2])
        mileage_amount = float(claims_list[4])
        claim_amount = float(claims_list[5])
        
        print("{:<6}{:<16}{:<16}{:<22}${:<9.2f}${:<9.2f}${:<9.2f}".format(claim_number,claim_date,salesperson_name,location_of_trip,per_diem,mileage_amount,claim_amount)) 
        
        print("                                          :                             ")
        print()
        print("                                          :                             ")
       
        
        
        claim_ctr += 1
        claim_totalACC += claim_amount
        per_diem_ACC += per_diem
        mileage_amount_ACC += mileage_amount
        
        
       
    
    #end of print statement
    print("="* 91)
    
    
    print("Claims Listed:{:<3}Per diem totals:${:<10.2f}Total mileage:${:<10.2f}Claims total:${:<10.2f}".format(claim_ctr,per_diem_ACC,mileage_amount_ACC,claim_totalACC))
    print()
    print(" " * 35 + "END OF REPORT") 
        
    
    #close file
            
    f.close()
        
    Anykey = input("Press any key to continue.")
    
#Function for graphing monthly totals

def graph_monthly_totals():
    
    
    
    #import matplotlib for graphing
    import matplotlib.pyplot as plt
    
    print()
    print("Graph the monthly claim totals.")
    
    janAcc = 0
    febAcc = 0
    marAcc = 0
    aprAcc = 0
    mayAcc = 0
    junAcc = 0
    julAcc = 0
    augAcc = 0
    septAcc = 0
    octAcc = 0
    novAcc = 0
    decAcc = 0 

    f= open("Sprint_Week_2/Claims.dat", 'r')
    
    
    for Claims in f:
        ClaimList = Claims.split(",")
        CDate = ClaimList[6].strip()
        CAmt = ClaimList[5].strip()
        CDate = datetime.datetime.strptime(CDate, "%Y-%m-%d")
        CAmt = float(CAmt)
        Month = CDate.month
        
        if Month == 1:
            janAcc += CAmt
        elif Month == 2:
            febAcc += CAmt
        elif Month == 3:
            marAcc += CAmt
        elif Month == 4:
            aprAcc += CAmt
        elif Month == 5:
            mayAcc += CAmt
        elif Month == 6:
            junAcc += CAmt
        elif Month == 7:
            julAcc += CAmt
        elif Month == 8:
            augAcc += CAmt
        elif Month == 9:
            septAcc += CAmt
        elif Month == 10:
            octAcc += CAmt
        elif Month == 11:
            novAcc += CAmt
        else:
            decAcc += CAmt
            
    xaxis = ["1", "2", "3", "4","5","6","7","8","9","10","11","12"]
    yaxis = [janAcc, febAcc, marAcc, aprAcc, mayAcc, junAcc, julAcc, augAcc, septAcc, octAcc, novAcc, decAcc]
    plt.plot(xaxis, yaxis)
    plt.show()
    
    # Pass the data into the plotter
    plt.title("Monthly Claim Total Graph:");
    plt.plot(xaxis, yaxis, color='darkblue', marker='X', label='Total Claims')
    
    plt.xlabel("Months of the year")
    plt.ylabel("Monthly claims")
    
    plt.grid(True)
    plt.legend()
    
    # Save the graph as an image so we can access it
    plt.savefig("Sprint_Week_2/Monthly_totals_graph.png")

    Anykey = input("Press any key to continue.")
    

#Set up the main function of the program
    
def main():
    while True:
        print("NL Chocolate Company")
        print("Travel Claims Processing System")
        print()
        print()
        print("1. Enter an employee travel claim.")
        print("2. Edit system default values.")
        print("3. Print the travel claim report")
        print("4. Graph monthly claim totals.")
        print("5. Quit program.")
        print()
        
        #get the users imput on what choice they would like to select
        choice = int(input("Enter a choice from (1-5): "))
            
        if choice == 1:
            Employee_Travel_Claim()
            
        elif choice == 2:
            showDefaults()
       
        elif choice == 3:
            travel_report()
           
        elif choice == 4:
            graph_monthly_totals()
            
        elif choice == 5:
            print()
            print("Thank You for using our program! Have a grrrrrr-eat day.")
            exit(0)
            
        else:
            exit(0)
                
if __name__ == "__main__":
    main()
            
            
