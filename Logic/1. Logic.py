# not, and, or, implication, double implication

# Negation (not)
# def negation(p):
# 	return (p, not p)

# for i in [True,False]:
# 	print(negation(i))

# Conjuction (and)
# def conjuction(val):
# 	for p,q in val:
# 		print(f'{p} and {q} = {p and q}')

# val = [(True, True), (True, False), (False, True), (False, False)]
# conjuction(val)


# disjunjuction (or)
# def disjuction(val):
# 	for p,q in val:
# 		print(f'{p} and {q} = {p or q}')

# val = [(True, True), (True, False), (False, True), (False, False)]
# disjuction(val)

# implies (->) (only True implies False is False and rest is True)
# def implies(val):
# 	for p,q in val:
# 		print(f'{p} and {q} = {not(p) or q}')

# val = [(True, True), (True, False), (False, True), (False, False)]
# implies(val)


# Bi-Implication or Double Implication <->
# Only T <-> T and F <-> F are True and the rest are false
# def double_implication(val):
# 	for p,q in val:
# 		print((not(p) or q) and (p or not(q)))

# val = [(True, True), (True, False), (False, True), (False, False)]
# double_implication(val)

# De Morgan's law
# not(p and q) = not(p) or not(q)
# not(p or q)  = not(p) and not(q)

# De Morgan's law
