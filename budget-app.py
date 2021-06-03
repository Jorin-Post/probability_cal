class Category:
    def __init__(self,name):       # to construct a object
        self.n = name              # trou out the class you can get self. data if called up on
        self.ledger=list()

    def deposit(self,amount,description=""):    # description="" for emtey defalt
        self.dep=dict()     # 
        
        self.dep["amount"]=amount   # adding the amount and description to dictionary
        self.dep["description"]=description
        #adding the deposit to ledger list
        self.ledger.append(self.dep)

    def check_funds(self,amount):
        fund=0
        n=len(self.ledger)
        for i in range(n):
            fund=fund+self.ledger[i]["amount"]
        if fund<amount:
            return False
        else:
            return True

    def withdraw(self,amount,description=""):
        chash=self.check_funds(amount)  # checks is there is enough funds

        if(chash==True):
            self.withd=dict()
            self.withd["amount"]=-(amount)  # to get a negetif withdraw
            self.withd["description"]=description
            self.ledger.append(self.withd)  # places dict self.withd in ledger
            return True
        else:
            return False

    def get_balance(self):  # check if the withdraw amount can be subtracted form deposit
        fund=0
        n=len(self.ledger)
        #retrieving the total fund in ledger
        for i in range(n):
            fund=fund+self.ledger[i]["amount"]
        return fund

    def transfer(self,amount,obname):
        objectname=obname.n
        a=self.withdraw(amount,f"Transfer to {objectname}") # withdraw needs amound and transcript f"..{objectname}" \
        b=obname.deposit(amount,f"Transfer from {self.n}") # will change in string with curand name
        if(a==True):    # not used
            return True
        else:           # not used
            return False

    

    def __str__(self):
        # f".." for this string function, use {..:..} to get data in, * what sign you want to drown
        title = f"\n{self.n:*^30}\n"   # ^ to give amount of times used
        items = ""  # every time the for loop goes it adds the new line in here
        total = 0   # end som of catagorie
        for i in range(len(self.ledger)): # range makes int val of len self.ledger
            items += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f}" + '\n' # [0:23] for the lenght of the description, 
            #:23} for room from left befor start amount, \ to go on with the same python line on the next line
            #:>7 max leght befor moving right, .2 is for 2 digets after the ., f use for this function
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    
    food = val_withdraw(str(categories[0])) 
    clothing = val_withdraw(str(categories[1]))
    auto = val_withdraw(str(categories[2]))
    all_withdraw = food + clothing + auto
    food_percentage = round(food / all_withdraw * 10) * 10
    clothing_percentage = round(clothing / all_withdraw * 10) * 10
    auto_percentage = round(auto / all_withdraw * 10) * 10
    #print(food_percentage, clothing_percentage, auto_percentage)

    print ('\n''   Percentage spent by category')
    percentage = 100
    i=0
    while i < 11:
        print(f"{' ' if (len(str(percentage))) < 3 else ''}", f"{'  ' if (len(str(percentage))) < 2 else ' '}",\
            percentage, '|', f"{'o ' if food_percentage >= percentage else '   '}",\
            f"{'o ' if clothing_percentage >= percentage else '   '}",\
            f"{'o ' if auto_percentage >= percentage else '   '}")
        percentage += -10
        i += +1
    print("       ","----------")
    f = 'food    '
    c = 'clothing'
    a = 'auto    '
    i = 0
    while i < len(c):
        print("        ",f[i],"",c[i],"",a[i])
        i += +1

def val_withdraw(category):
    cval = category.split()
    i = 0
    withdraw_str = ''
    withdraw_total = 0
    while i < len(cval):
        try:
            c1 = cval[i].index('-')
            if c1 == 0:
                withdraw_str =  cval[i].replace('-','')
                withdraw_total += +float(withdraw_str)
            i += +1  
        except ValueError as v:
            i += +1
    withdraw_round = round(withdraw_total, 2)
    return (withdraw_round)

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(10)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

create_spend_chart([food, clothing, auto])