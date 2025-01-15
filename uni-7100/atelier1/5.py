import secrets  
import random   

# Pseudo-random - used for modelling
print(random.choice(['Python', 'TypeScript', 'Rust', 'Cpp']))

# Random - used for cryptography/security
print(secrets.choice(['Python', 'TypeScript', 'Rust', 'Cpp']))