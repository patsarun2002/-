def showline():
    i = 1
    while i <=30:
        print("-",end="")
        i+=1
def showline2():
    i = 1
    while i <=60:
        print("-",end="")
        i+=1 
while True:
    try:
        price = float(input("\nกรุณากรอก ราคาสุทธิ(บาท):"))
        showline()
        down_payment = float(input("\nกรุณากรอก เงินดาวน์(บาท):"))
        showline()   
        interest_rate = float(input("\nกรุณากรอก อัตราดอกเบี้ยต่อปี(%):"))
        showline() 
        period = int(input("\nกรุณากรอก ระยะเวลาผ่อนชำระ(ปี):"))
        showline()
        if price:
            price_net = price-down_payment
            balance = price_net+((price_net/100*interest_rate)*period)
        else:
            ()
        if interest_rate:
            interest_rate_net = interest_rate/12/100
        else:
            ()
        if period:
            period_net = period*12
        else:
            ()                  
        print("\nราคาสุทธิ {0:,.2f} บาท".format(price))
        print("เงินดาวน์ {0:,.2f} บาท".format(down_payment))
        print("อัตราดอกเบี้ยต่อปี(%) {0}% ปี".format(interest_rate))
        print("ระยะเวลาผ่อนชำระ(ปี) {0} ปี".format(period))
        showline2()
        print("\nราคาหักเงินดาวน์ {0:,.2f} บาท".format(price_net))
        print("ราคาหักเงินดาวน์พร้อมดอกเบี้ย {0:,.2f} บาท".format(balance))
        showline2()
        net_balance = balance
        print("{0:25}{1:25}{2:25}".format("\nจำนวณงวดที่ต้องผ่อน","ค่าผ่อนงวดแต่ละงวด","ราคาสุทธิที่ต้องผ่อนคงเหลือ"))
        for day in range(1,(period_net)+1):
            monthly_payment = balance/period_net
            net_balance-=(monthly_payment)
            print("- งวดเดือนที่ {0:<5d}{1:13,.2f} บาท {2:>19,.2f} บาท".format(day,monthly_payment,net_balance))
        showline2()
    except ValueError:
        print("\nกรุณาโปรดกรอกข้อมูลให้ครบทุกช่อง")
