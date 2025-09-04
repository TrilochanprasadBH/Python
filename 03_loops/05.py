# Learning  - zip 

names = ["alice", "bob", "charlie"]
names.append("david")
bills = [100, 200, 300,900]

for names,bills in zip(names,bills):
    print(f"{names} has to pay {bills}")
