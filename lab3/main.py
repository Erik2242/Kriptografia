from knapsack import Knapsack

a = Knapsack(8)
print(a.generate_private_key())
print(a.create_public_key())
print(a.encrypt("Alma a fa alatt nyari prios alma"))