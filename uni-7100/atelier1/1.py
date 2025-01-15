import random

def random_number_between(a, b):
    return random.randint(a, b)

if __name__ == '__main__':
    print(random_number_between(1, 10))
    
    assert 1 <= random_number_between(1, 10) <= 10
    assert random_number_between(2,2) == 2

