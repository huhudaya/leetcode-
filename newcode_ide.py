from collections import defaultdict

#
# role1 = defaultdict(set)
# role2 = defaultdict(set)
# role3 = defaultdict(str)
# while 1:
#     line = input()
#     if line == "performance":
#         while 1:
#             line = input()
#             if line:
#                 role, cnt = line.strip().split(",")
#                 role3[role] = cnt
#             else:
#                 break
#     line = input()
#     if line == "organization":
#         while 1:
#             line = input()
#             if line != "eof":
#                 r1, r2, r3 = line.strip().split(",")
#                 role1[r1].add(r2)
#                 role2[r2].add(r3)
#             else:
#                 break
#     break


role1 = {"Aaron": ["Abel", "Jone"]}
role2 = {"Abel": ["Adam", "Andy"], "Jone": ["Evan", "Bill"]}
role3 = {"Adam": 125, "Andy": 110, "Bill": 92, "Evan": 154}

role1_cnt = []
role2_cnt = []
role3_cnt = []
print_r1 = defaultdict(list)
print_r2 = defaultdict(list)
print_r3 = defaultdict(list)
for r1 in role1.keys():
    # 每次更新role2_cnt
    role2_cnt = []
    r1_cnt = 0
    r2_list = role1[r1]
    for r2 in r2_list:
        # 每次更新role3
        role3_cnt = []
        r2_cnt = 0
        r3_list = role2[r2]
        for r3 in r3_list:
            r1_cnt += int(role3[r3])
            r2_cnt += int(role3[r3])
            role3_cnt.append((role3[r3], r3))
        role2_cnt.append((r2_cnt, r2))
        role3_cnt.sort(reverse=True)
        print_r2[r2].extend(role3_cnt)
    role2_cnt.sort(reverse=True)
    print_r1[r1].extend(role2_cnt)
    role1_cnt.append((r1_cnt, r1))

role1_cnt.sort(reverse=True)
for r1_cnt, r1 in role1_cnt:
    print(r1 + "<" + str(r1_cnt) + ">")
    r2_list = print_r1[r1]
    r2_list
    for r2_cnt, r2 in r2_list:
        print("-" + r2 + "<" + str(r2_cnt) + ">")
        r3_list = print_r2[r2]
        for r3_cnt, r3 in r3_list:
            print("--" + r3 + "<" + str(r3_cnt) + ">")
