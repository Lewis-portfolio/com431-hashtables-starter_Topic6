# Lewis
# Date: 05, 11, 2025
# Main file:

from hash_table import HashTable

table = HashTable()
print(len(table.buckets))

table.put("cat", "cats")
table.put("act", "acting")
print(table.get("cat"))
print(table.get("act"))
print(table.buckets[table.hash("act") % len(table.buckets)])
