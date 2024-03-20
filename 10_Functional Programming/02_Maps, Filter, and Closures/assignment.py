def mult2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2]

mapped_mult2 = map(mult2, my_list)
mapped_div2 = map(div2, my_list)
mapped_exp2 = map(exp2, my_list)

mapped_mult2_list = my_list(mapped_mult2)
print(mapped_mult2_list)