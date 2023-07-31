import os
import json

def return_change(diff): #5,10,20,50
    coins=[50,20,10,5]
    dic_coins= {}
    for i in coins:
        cc = amout // i
        amount -= dic_coins[i] * i
        if cc > 0 :
            dic_coins[i] = cc

    return dic_coins





# with open('/code/menu.txt','r') as f:
#     print(f.readlines())

    while True:
        drink = input('what do u want to drink :') 
        drink = drink.lower()
        dict_drink= {
            'cafe noir' : {"numero" : 1, "prix":30},
            'cafe au lait' : {"numero" : 2, "prix":25},
            'the' : {"numero" : 3, "prix":20},
            'chocolat au lait' : {"numero" : 4, "prix":35} ,
            'cappucino' : {"numero" : 5, "prix":40}
        }
        #dict_drink = {'cafe noir':30,'chocolat au lait':35,'cappuccino':40,'cafe au lait':25,'the':20}

        match drink:
            case '1':
            money = input('please enter the money you want to pay')
            price = dict_drink[drink]['prix']
            if int(money) >= price:
                return_money(money - price)
            else:
                print('not enough money')


            case '2' :
            if int(money) >= price:
                
                return_money()
            else:
                print('not enough money')

            case '3':
                money = input('please enter the money you want to pay')
            price = dict_drink[drink]['prix']
            if int(money) >= price:
                return_money(money - price)
            else:
                print('not enough money')
            

            case '4' :
                money = input('please enter the money you want to pay')
            price = dict_drink[drink]['prix']
            if int(money) >= price:
                return_money(money - price)
            else:
                print('not enough money')

            case '5':  
                money = input('please enter the money you want to pay')
            price = dict_drink[drink]['prix']
            if int(money) >= price:
                return_money(money - price)
            else:
                print('not enough money')

            case '0' :
                break
            
            case _:
                print('invalid input!')