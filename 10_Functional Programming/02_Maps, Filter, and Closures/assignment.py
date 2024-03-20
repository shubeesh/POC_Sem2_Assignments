<<<<<<< HEAD
def mult2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2]

mapped_mult2 = map(mult2, my_list)
mapped_div2 = map(div2, my_list)
mapped_exp2 = map(exp2, my_list)

mapped_mult2_list = my_list(mapped_mult2)
print(mapped_mult2_list)#
=======
def times2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2] #You make

mapped_times2 = map(times2, my_list)
#YOUDO:  repeate for div2, exp2

mapped_times2_list = list(mapped_times2)
print(mapped_times2_list)
#YOUDO:  repeat for the other maps 


>>>>>>> 62c5c49131800e7eba24bad8aa9cac64d1c9aff4
