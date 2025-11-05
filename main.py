# Lewis
# Date: 05, 11, 2025
# Main file:

from hash_table import HashTable

table = HashTable()
print(len(table.buckets))

inputs = [("Q10201", "Andrea"),
          ("Q12321", "Barry"),
          ("Q14442", "Chantal"),
          ("Q25343", "Dexter"),
          ("Q34531", "Erin"),
          ("Q09878", "Fernand"),
          ("Q11333", "Gabrielle"),
          ("Q22224", "Humberto"),
          ("Q11144", "Imelda"),
          ("Q54555", "Jerry"),
          ("Q25856", "Karen"),
          ("Q43334", "Lorenzo")]

for index in inputs:
    table.put(index[0], index[1])

for bucket in table.buckets:
    print(bucket)
