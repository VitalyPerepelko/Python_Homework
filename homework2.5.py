#Vitaly Perepelko
#home_work2_5

price = [57.8, 46.51, 107, 75, 10.01, 35, 40.05, 500, 9077, 1, 17.03]
for cash in price:
    rub = int(cash)
    kk = (cash - int(cash)) * 100
    print(f'{rub} руб {kk:02.0f} коп')



price = [57.8, 46.51, 107, 75, 10.01, 35, 40.05, 500, 9077, 1, 17.03]
print(id(price))
price.sort()
print(id(price))
for cash in price:
    rub = int(cash)
    kk = (cash - int(cash)) * 100
    print(f'{rub} руб {kk:02.0f} коп') 


price = [57.8, 46.51, 107, 75, 10.01, 35, 40.05, 500, 9077, 1, 17.03]
for cash in sorted(price)[::-1][:5]:
    rub = int(cash)
    kk = (cash - int(cash)) * 100
    print(f'{rub} руб {kk:02.0f} коп') 

print([f'{int(cash)} руб {(cash - int(cash)) * 100:02.0f} коп' for cash in sorted(price)[::-1][:5]])


