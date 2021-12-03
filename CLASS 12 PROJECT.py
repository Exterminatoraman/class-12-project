# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:57:22 2021

@author: Aman Agrawal
"""


import pymysql as m
def purchase():
    global purchase_count
    global total0    
    cursorobj.execute("create table if not exists purchaser(product_id varchar(4) PRIMARY KEY, purchaser_name char(20),item_name char(15),stamp char(6),unit varchar(3),gold_weight varchar(3),diamond_weight varchar(4),diamond_price int(3),rate varchar(5),labour varchar(4),total varchar(9))")
    choice=int(input("choose your option 1-insert entry,2-delete entry,3-update  "))
    if choice==1:
        
        sql="insert into purchaser values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        itemcode=int(input("enter the item code-"))
        purchaser_name=input("enter the name of the purchaser-")
        itemname=input("enter the name of the product-")
        stamp=input("choose the stamp gm,carat,kg-")
        unit=int(input("enter the amount of unit-"))
        goldweight=float(input("enter the weight of gold-"))
        diamondweight=float(input("enter the weight of diamond-"))
        diamondprice=float(input("enter the price of diamond-"))        
        rate=int(input("enter the rate of gold-"))
        labour=int(input("enter the labour cost-"))
        totallabourcost=int(unit*goldweight*labour)
        total0=int(((unit*goldweight)*rate)+totallabourcost+(diamondweight*diamondprice))
        val=(itemcode,purchaser_name,itemname,stamp,unit,goldweight,diamondweight,diamondprice,rate,labour,total0)
        cursorobj.execute(sql,val)
        cursorobj.execute("select * from purchaser")
        purchase_data=cursorobj.fetchall()
        print('(itemcode','name','name of product','stamp','unit','weight of gold','weight of diamond','price of diamond','rate','labour)',sep=",")
        for row in purchase_data:
            print(row)
        print(cursorobj.rowcount, "record inserted.")
    elif choice==2 :
        delete=("delete from purchaser where product_id=%s")
        delete_val=(int(input("enter the itemcode which you want to delete  ")))
        cursorobj.execute(delete,delete_val)
        cursorobj.execute("select * from purchaser")
        purchase_data=cursorobj.fetchall()
        print('(itemcode','name','name of product','stamp','unit','weight of gold','weight of diamond','price of diamond','rate','labour)',sep=",")
        for row in purchase_data:
            print(row)
    elif choice==3:
        cursorobj.execute("select * from purchaser")
        purchase_data=cursorobj.fetchall()
        print('(itemcode','name','name of product','stamp','unit','weight of gold','weight of diamond','price of diamond','rate','labour)',sep=",")
        for row in purchase_data:
            print(row)
        
        product_code=int(input("enter the itemcode which you want to update "))
        a=("select * from purchaser where product_id=%s")
        cursorobj.execute(a,product_code)
        b=cursorobj.fetchall()
        print('''enter the choice which you want to update
1-PURCHASER NAME
2-PRODUCT NAME
3-STAMP
4-UNIT
5-GOLD WEIGHT
6-DIAMOND WEIGHT
7-DIAMOND PIECE
8-RATE
9-LABOUR CHARGE''')
        c=int(input("-------------"))
        if c==1:
            d=input("enter the new name")
            cursorobj.execute("update purchaser set purchaser_name=%s where product_id=%s",(d,product_code))
        elif c==2:
            d=input("enter the new name")
            cursorobj.execute("update purchaser set item_name=%s where product_id=%s",(d,product_code))
        elif c==3:
            d=input("enter the new stamp")
            cursorobj.execute("update purchaser set stamp=%s where product_id=%s",(d,product_code))
        elif c==4:
            d=input("enter the new unit")
            cursorobj.execute("update purchaser set unit=%s where product_id=%s",(d,product_code))

        elif c==5:
            d=input("enter the new weight")
            cursorobj.execute("update purchaser set gold_weight=%s where product_id=%s",(d,product_code))
        elif c==6:
            d=input("enter the new diamond weight")
            cursorobj.execute("update purchaser set diamond_weight=%s where product_id=%s",(d,product_code))
        elif c==7:
            d=input("enter the new diamond price")
            cursorobj.execute("update purchaser set diamond_price=%s where product_id=%s",(d,product_code))
        elif c==8:
            d=input("enter the new rate")
            cursorobj.execute("update purchaser set rate=%s where product_id=%s",(d,product_code))
        elif c==9:
            d=input("enter the new unit")
            cursorobj.execute("update purchaser set labour=%s where product_id=%s",(d,product_code))

        else:
            print("enter the valid choice")
        
    con.commit()
    return purchase_data


def sale():
    global sale_count
    global total
    cursorobj=con.cursor()
    cursorobj.execute("show tables")   
    cursorobj.execute("create table if not exists sale (product_id int(4) PRIMARY KEY,purchaser_name char(20), item_name char(15), stamp char(6), unit varchar(3), gold_weight varchar(3),diamond_weight varchar(4),diamond_piece int(3), rate varchar(5), labour varchar(4), total varchar(10))")
    choice=int(input("choose your option 1-insert entry,2-delete entry,3-update,4-show table"))
    if choice==1:
        sql="insert into sale values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        itemcode=int(input("enter the item code-"))
        purchaser_name=input("enter the name of the customer-")
        itemname=input("enter the name of the product-")
        stamp=input("choose the stamp gm,carat,kg -")
        unit=int(input("enter the amount of unit-"))
        goldweight=float(input("enter the weight of gold-"))
        diamondweight=float(input("enter the weight of diamond-"))
        diamondprice=float(input("enter the price of diamond-"))
        rate=int(input("enter the rate of gold-"))
        labour=int(input("enter the labour cost-"))
        totallabourcost=(unit*goldweight*labour)
        total=float(((unit*goldweight)*rate)+totallabourcost+(diamondweight*diamondprice))
        val=(itemcode,purchaser_name,itemname,stamp,unit,goldweight,diamondweight,diamondprice,rate,labour,total)
        cursorobj.execute(sql,val)
        purchase_data=cursorobj.fetchall()
        print('(ITEMCODE','NAME','NAME OF PRODUCT','STAMP','UNIT','WEIGHT OF GOLD','WEIGHT OF DIAMOND','PRICE OF DIAMOND','RATE','LABOUR)',sep=",")
        for row in purchase_data:
            print(row)
        print(cursorobj.rowcount,"record inserted")
    elif choice==2:
        delete=("delete from sale where product_id=%s")
        delete_val=(int(input("enter the itemcode which you want to delete  ")))
        cursorobj.execute(delete,delete_val)
        print("record deleted succesfully")
        con.commit()
    
        
        
        
    elif choice==3:
        cursorobj.execute("select * from purchaser")
        purchase_data=cursorobj.fetchall()
        print('(ITEMCODE','NAME','NAME OF PRODUCT','STAMP','UNIT','WEIGHT OF GOLD','WEIGHT OF DIAMOND','PRICE OF DIAMOND','RATE','LABOUR)',sep=",")

        for row in purchase_data:
            print(row)
        
        product_code=int(input("enter the itemcode which you want to update "))
        a=("select * from purchaser where product_id=%s")
        cursorobj.execute(a,product_code)
        b=cursorobj.fetchall()
        print('''enter the choice which you want to update
1-PURCHASER NAME
2-PRODUCT NAME
3-STAMP
4-UNIT
5-GOLD WEIGHT
6-DIAMOND WEIGHT
7-DIAMOND PRICE
8-RATE
9-LABOUR CHARGE''')
        c=int(input("-------------"))
        if c==1:
            d=input("enter the new name")
            cursorobj.execute("update purchaser set purchaser_name=%s where product_id=%s",(d,product_code))
        elif c==2:
            d=input("enter the new name")
            cursorobj.execute("update purchaser set item_name=%s where product_id=%s",(d,product_code))
        elif c==3:
            d=input("enter the new stamp")
            cursorobj.execute("update purchaser set stamp=%s where product_id=%s",(d,product_code))
        elif c==4:
            d=input("enter the new unit")
            cursorobj.execute("update purchaser set unit=%s where product_id=%s",(d,product_code))

        elif c==5:
            d=input("enter the new weight")
            cursorobj.execute("update purchaser set gold_weight=%s where product_id=%s",(d,product_code))
        elif c==6:
            d=input("enter the new diamond weight")
            cursorobj.execute("update purchaser set diamond_weight=%s where product_id=%s",(d,product_code))
        elif c==7:
            d=input("enter the new diamond piece")
            cursorobj.execute("update purchaser set diamond_price=%s where product_id=%s",(d,product_code))
        elif c==8:
            d=input("enter the new rate")
            cursorobj.execute("update purchaser set rate=%s where product_id=%s",(d,product_code))
        elif c==9:
            d=input("enter the new unit")
            cursorobj.execute("update purchaser set labour=%s where product_id=%s",(d,product_code))

        else:
            print("enter the valid choice")
    con.commit()



def stock():

    cursorobj=con.cursor()
    cursorobj.execute("create table if not exists stock (product_id int(4) PRIMARY KEY, item_name char(15), stamp char(6), unit varchar(3), gold_weight varchar(3),diamond_weight varchar(4),diamond_price int(3), rate varchar(5), labour varchar(4), total varchar(10))")
    cursorobj.execute("insert into stock(product_id, item_name,stamp,unit,gold_weight,diamond_weight,diamond_price,rate,labour,total) select product_id, item_name,stamp,unit,gold_weight,diamond_weight,diamond_price,rate,labour,total from purchaser p where not exists(select * from stock where product_id=p.product_id) ")
    cursorobj.execute("select * from stock")
    stock_data=cursorobj.fetchall()
    if opt==2:
        cursorobj.execute("delete from stock where stock.product_id=sale.product_id")
    if opt==3:
        print('(ITEMCODE','NAME','NAME OF PRODUCT','STAMP','UNIT','WEIGHT OF GOLD','WEIGHT OF DIAMOND','PRICE OF DIAMOND','RATE','LABOUR)',sep=",")
        for column in stock_data:
            print(column)
    return stock_data

def payment():
    global total
    print("CHOOSE MODE OF PAYMENT 1-CASH,2-CARD")
    option=int(input("Enter your choice"))
    if option==1:    
        cash_recieved=int(input("enter the cash recieved"))
        final_payment=total-cash_recieved
    if option==2:
        print("swipe your card")
    if final_payment==0:
        print("transaction completed")
    else:
        print("insufficient cash")
    


con=m.connect(
        host="localhost",
        user="root",
        password="aman",
        database="mysql")
cursorobj=con.cursor()
purchase_count=0 
sale_count=0
stock_count=0
print("1-PURCHASE")
print("2-SALE")
print("3-STOCK ")
print("4-EXIT")

while True: 
    opt=int(input("enter the function number you want to perform or press 5 for preview  "))
    if opt==1:
        purchase()
        purchase_count+=1
        stock()
        
    elif opt==2:
        sale()
        sale_count+=1
       
    elif opt==3:
        stock()
    elif opt==4:
        break
    elif opt==5:
        print("1-PURCHASE")
        print("2-SALE")
        print("3-STOCK ")
        print("4-EXIT")
    else:
        print("invalid choice ")
        
        