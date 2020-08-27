def div_parts(a, tab):
    d, r = divmod(a, tab)
    return [d + (1 if i < r else 0) for i in range(tab)]

print(div_parts(8, 3))
'''
This function allows you to split a number into tab parts
'''
# num_tab = []
#
# a = 8
# tab = 3
# d, r = divmod(a, tab)
#
# for i in range(tab):
#     if i < r:
#         g = 1
#         c = d + g
#         num_tab.append(c)
#     else:
#         g = 0
#         c = d + g
#         num_tab.append(c)
