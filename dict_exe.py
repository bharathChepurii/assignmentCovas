D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new': 3}

# Union of keys
D_UNION = {key: D1.get(key, D2.get(key)) for key in set(D1) | set(D2)}

# Intersection of keys
D_INTERSECTION = {key: D1[key] for key in set(D1) & set(D2)}

# D1 - D2 (Keys in D1 but not in D2)
D_DIFF = {key: D1[key] for key in set(D1) - set(D2)}

# Values are added for same keys
D_MERGE = {key: D1.get(key, 0) + D2.get(key, 0) for key in set(D1) | set(D2)}

print("D_UNION:", D_UNION)
print("D_INTERSECTION:", D_INTERSECTION)
print("D1 - D2:", D_DIFF)
print("D_MERGE:", D_MERGE)

