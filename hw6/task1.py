f = open("hw3_q1.txt", "r")
data = []
jump_list = []
join_list=[]
count=0
for s, n in enumerate(f):
    if 'JUMP' in n:
        data=n
        jump_list.append(data)
    else:
        join_list.append(n)


print(jump_list,join_list)
