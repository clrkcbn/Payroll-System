while True:    
    try:
        print("Simple Company Payroll System")
        print("-----------------------------------------------")
        
        workers = int(input("How many workers do you have: "))
        if workers <= 0:
            print("You don't have any workers on your company")
            print("-----------------------------------------------")
            continue        
    except ValueError:
            print("Please type a valid whole number")
            print("-----------------------------------------------")
            continue
       
    for i in range(1, workers + 1):       
        while True:
            name = input(f"Employee Number {i} Name: ")    
            if name.strip() == "":
                print("We can't have a blank name.")
                continue
            break
                
        while True:    
            hourly_rate = float(input(f"What is the hourly rate of {name}? "))
            try:
                if hourly_rate <= 0:
                    print("You should rate properly your workers")
                    continue
            except ValueError:
                    print("Invalid hourly rate, please try again")
                    continue
            break
        while True:
            work_hours = float(input(f"How many hours did {name} work? "))
            try:
                if work_hours < 0:
                    print("We only accept positive and zero number of hours of work")
                    continue
            except ValueError:
                print("Invalid number of hours work, please try again")
                continue
            break
        while True:
            ot_hours = float(input(f"Total Hours of Overtime: "))
            try:
                if ot_hours < 0:
                    print("We only accept positive and zero number of hours of overtime")
                    continue
            except ValueError:
                print("Invalid number of hours work, please try again")
                continue
            break
        while True:
            late_hours = float(input("Total Hours of Late: "))
            try:
                if late_hours < 0:
                    print("We only accept positive and zero number of hours of late")
                    continue
            except ValueError:
                print("Invalid number of hours late please try again")
                continue
            break
                        
        #Formula
        deduction = late_hours * hourly_rate
        ot_payment = (hourly_rate / 8) * ot_hours
        salary = (hourly_rate * work_hours) + ot_payment - deduction
                            
        print(f"Payroll Summary of Employee No.{i}: {name}")
        print(f"Employee Number: {i}")
        print(f"Employee Name: {name}")
        print(f"Hourly Rate: {hourly_rate:.1f} hours")
        print(f"Total Work Hours: {work_hours:.1f} hours")
        print(f"Total Hours of Overtime: {ot_hours:.1f} hours")
        print(f"Overtime Payment of {name}: {ot_payment:.1f}")
        print(f"Total Hours of Late: {late_hours:.1f}")
        print(f"Total Deduction of {name}: {deduction:.1f}")
        print(f"Total Salary of {name}: {salary:.1f}")
        
        print("-----------------------------------------------")

    while True:
        if_continue = input("Would you like to process another payroll? Y/N: ").upper()

        try:
            if if_continue == "Y":
                break #restart program
            else:
                print("Exiting Program")
                exit()
        except ValueError:
            print("Invalid input, please try again either Y or N")
            continue
                    
    print("\n")            
        
    