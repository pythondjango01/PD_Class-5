# def hafiz():
#     print('Hafizul Islam')
# hafiz()

# def student(Name, Roll, Group, Deparment='Cmt'):
#     return Name,Roll,Group,Deparment

# print(student('Md Hafiuzl Islam',918784,'A'))
# print(student('Golam Rabbi',918785,'B'))
# print(student('Rokon uzzaman jaman',500,'B'))


# def price(*arge):
#     sum = 0
#     for result in arge:
#         sum += result
#     return sum
# hafiz = price(100,20,69)
# print(hafiz)

# def rrr(**kwarge):
#     sum = 0
#     for result in kwarge:
#         sum += kwarge[result]
#     return sum
# tt = rrr(alu=25, chips=10, panjabi=520, saloar=350)
# print(tt)


###########      Lemda              

prodact = lambda a,b,c : a+b+c
rr = prodact(20,30,52)
print(rr)