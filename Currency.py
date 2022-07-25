def first():
    print("***************************************************")
    print("***********CURRENCY CONVERSION DASHBOARD***********")
    print("***************************************************")
    print("             1.US Dollars TO Indian Rupees")
    print("             2.Indian Rupees TO US Dollars")
    print("             3.EURO TO Indian Rupees")
    print("             4.Indian Rupees TO EURO")
    print("             5.Australian Dollar TO Indian Rupees")
    print("             6.Indian Rupees TO Australian Dollar")
    print("             7.New Zealand Dollar TO Indian Rupees")
    print("             8.Indian Rupees TO New Zealand Dollar")
    print("             9.BITCOIN TO Indian Rupees")
    print("             0.QUIT..!!")
    print("Enter Your Choice To Convert The Currency= ", end="")
    global no
    no = int(input())
    print("||===================================================||")


def usd_to_ind():
    print("Note: You're Converting Currency USD TO INR...")
    us = float(input("Enter USD Dollar: "))
    ind = 75
    result = us * ind
    print("______________________________")
    print(result, "₹/Rupees")
    val=us
    other(val,flag=0)
    con()


def ind_to_usd():
    ind = int(input("Enter Indian Rupees: "))
    print("Note: You're Converting Currency INR TO USD...")
    usd = 0.0137
    result = ind * usd
    print("______________________________")
    print(result, "$/USD")
    val = ind
    other(val, flag=1)
    con()


def eur_to_ind():
    print("Note: You're Converting Currency EURO TO INR...")
    eur = float(input("Enter Euro: "))
    ind = 89.81
    result = eur * ind
    print("______________________________")
    print(result, "₹/Rupees")
    val = eur
    other(val, flag=2)
    con()


def ind_to_eur():
    print("Note: You're Converting Currency INR TO EURO...")
    ind = int(input("Enter Indian Rupees: "))
    eur = 0.011
    result = ind * eur
    print("______________________________")
    print(result, "€/EURO")
    val = ind
    other(val, flag=3)
    con()


def aus_to_ind():
    print("Note: You're Converting Currency AUS TO INR...")
    aus = float(input("Enter Australian Dollar: "))
    ind = 56.35
    result = aus * ind
    print("______________________________")
    print(result, "₹/Rupees")
    val = aus
    other(val, flag=4)
    con()


def ind_to_aus():
    print("Note: You're Converting Currency INR TO AUS...")
    ind = int(input("Enter Indian Rupees: "))
    aus = 0.018
    result = ind * aus
    print("______________________________")
    print(result, "$/Australian Dollars")
    val = ind
    other(val, flag=5)
    con()


def new_to_ind():
    print("Note: You're Converting Currency NEW TO INR...")
    new = float(input("Enter New Zealand Dollar: "))
    ind = 52.55
    result = new * ind
    print("______________________________")
    print(result, "₹/Rupees")
    val = new
    other(val, flag=6)
    con()


def ind_to_new():
    print("Note: You're Converting Currency INR TO NEW...")
    ind = int(input("Enter Indian Rupees: "))
    new = 0.019
    result = ind * new
    print("______________________________")
    print(result, "$/New Zealand Dollars")
    val = ind
    other(val, flag=7)
    con()


def bit_to_ind():
    print("Note: You're Converting Currency Bitcoin TO INR...")
    bit = float(input("Enter New Bitcoin: "))
    ind = 2714145.23
    result = bit * ind
    print("______________________________")
    print(result, "₹/Rupees")
    con()


def main():
    if no == 0:
        exit();
    if no == 1:
        usd_to_ind();
    if no == 2:
        ind_to_usd();
    if no == 3:
        eur_to_ind();
    if no == 4:
        ind_to_eur();
    if no == 5:
        aus_to_ind();
    if no == 6:
        ind_to_aus();
    if no == 7:
        new_to_ind();
    if no == 8:
        ind_to_new();
    if no == 9:
        bit_to_ind();
    if no > 10:
        print("Please Enter Valid Choice..")


def other(val,flag):
    

    if flag==0:
        print("================================================")
        print("Other Conversions:")
        brazilian = 5.11
        r1 = val * brazilian
        canadian=1.29
        r2= val * canadian
        chinese=6.72
        r3= val * chinese
        russian = 66.80
        r4= val * russian
        suadi = 3.75
        r5= val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==1:
        print("================================================")
        print("Other Conversions:")
        brazilian = 0.066
        r1 = val * brazilian
        canadian = 0.017
        r2 = val * canadian
        chinese = 0.087
        r3 = val * chinese
        russian = 0.87
        r4 = val * russian
        suadi = 0.049
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==2:
        print("================================================")
        print("Other Conversions:")
        brazilian = 5.40
        r1 = val * brazilian
        canadian = 1.37
        r2 = val * canadian
        chinese = 7.09
        r3 = val * chinese
        russian = 71.71
        r4 = val * russian
        suadi = 3.96
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==3:
        print("================================================")
        print("Other Conversions:")
        brazilian = 0.066
        r1 = val * brazilian
        canadian = 0.017
        r2 = val * canadian
        chinese = 0.087
        r3 = val * chinese
        russian = 0.87
        r4 = val * russian
        suadi = 0.049
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==4:
        print("================================================")
        print("Other Conversions:")
        brazilian = 3.58
        r1 = val * brazilian
        canadian = 0.91
        r2 = val * canadian
        chinese = 4.71
        r3 = val * chinese
        russian = 46.75
        r4 = val * russian
        suadi = 2.63
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==5:
        print("================================================")
        print("Other Conversions:")
        brazilian = 0.066
        r1 = val * brazilian
        canadian = 0.017
        r2 = val * canadian
        chinese = 0.087
        r3 = val * chinese
        russian = 0.87
        r4 = val * russian
        suadi = 0.049
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==6:
        print("================================================")
        print("Other Conversions:")
        brazilian = 3.24
        r1 = val * brazilian
        canadian = 0.82
        r2 = val * canadian
        chinese = 4.26
        r3 = val * chinese
        russian = 42.30
        r4 = val * russian
        suadi = 2.38
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")
    elif flag==7:
        print("================================================")
        print("Other Conversions:")
        brazilian = 0.066
        r1 = val * brazilian
        canadian = 0.017
        r2 = val * canadian
        chinese = 0.087
        r3 = val * chinese
        russian = 0.87
        r4 = val * russian
        suadi = 0.049
        r5 = val * suadi
        print(" ", r1, "R$/Brazilian Real")
        print(" ", r2, "$/Canadian Dollar")
        print(" ", r3, "¥/Chinese Yuan")
        print(" ", r4, "₽/Russian Ruble")
        print(" ", r5, "﷼/Suadi Riyal")

def con():
    print(" ")
    print("Want to continue the conversion press 9 or For Exit press 0")
    press = int(input())
    if press != 0:
        print("===============================================")
        first()
        main()
    else:
        exit()


first()
main()





