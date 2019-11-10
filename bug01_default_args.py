def fn(name="Rishabh", lt=[]):
    lt.append(name)
    return lt

print(fn()) 
print(fn("Alice"))
print(fn("Bob"))
print(fn("Charlie"))
