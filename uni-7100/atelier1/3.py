class Block:
    pass

# Simple object creation

for _ in range(10):
    print(Block())

# Refers to the same instance 
print([Block()] * 4)

# Independent object creation 
print([Block() for _ in range(4)])