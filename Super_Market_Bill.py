from datetime import datetime
name=input("enter your name:")

#list of items

lists="""
         Rice  Rs 20/kg
         Sugar Rs 30/kg
         Salt  Rs 20/kg
         Oil   Rs 80/liter
         Maggi Rs 50/kg
         Boost Rs 90/each
         Colgate Rs 85/each
         """

# print(lists)

#declaration

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#Rates for items

items={'Rice':20,
       'Sugar':30,
       'Salt':20,
       'Oil':80,
       'Maggi':50,
       'Boost':90,
       'Colgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)

for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or press 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
# print(price)
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            plist.append(price)
            qlist.append(quantity)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
    else:
        print("sorry you entered item is not available")

else:
    print("you entered wrong number")
inp=input("can i bill the items yes or No:")
if inp=='yes':
    pass
    if finalamount!=0:
        print(25*"=","PRAVEEN SUPER MARKET",25*"=")
        print(28*" ","ACHAMPET")
        print("Name:",name,30*"","Date:",datetime.now())
        print(75*"-")
        print("sno",8*" ","items",8*" ","Quantity",3*" ","price")

for i in range(len(pricelist)):
    print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
    print(75*"-")
    print(50*" ","TotalAmount:",'Rs',totalprice)
    print("gst Amount",50*" ",'Rs',gst)
    print(75*"-")
    print(50*" ","finalamount",'Rs',finalamount)
    print(75*"-")
    print(20*" ","Thank for Visiting")
    print(75*"-")
