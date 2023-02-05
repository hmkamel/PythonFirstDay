guyName = input("What is the guys name?").lower()
girlName = input("What is the girls name?").lower()
i = 0
j = 0
k = 0
r = 0
q = 0
p = 0

love = "Love".lower()
true = "True".lower()

for i in guyName:
    for j in love:
        if i == j:
            k = k + 1
    for j in true:
        if i == j:
            q = q + 1
print("For " + guyName)
print("There are ", q , " letters in True")
print("There are " , k , " letters that match in Love\n")


for i in girlName:
    for j in love:
        if i == j:
            r = r + 1
    for j in true:
        if i == j:
            p = p + 1
print("For " + girlName)
print("There are " , p , " letters in True")
print("There are " , r , " letters that match in Love\n")

total_true = q + p
total_love = k + r
tt_true = total_true.__str__()
tt_love = total_love.__str__()
tt_total = tt_true + tt_love
print(tt_total, "\n")
tt_final = int(tt_total)
print(tt_final)

if tt_final < 10 or tt_final > 90:
    print("Your score is ", tt_final, " and you go together like coke and mentos\n")

if tt_final > 40 and tt_final < 50:
    print("Your score is ", tt_final, " and you are alright together")

