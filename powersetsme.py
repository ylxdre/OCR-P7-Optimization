from math import log

def powerset(xs):
	result = [[]]
	for x in xs:
		newsubsets = [subset + [x] for subset in result]
		result.extend(newsubsets)
	return result

def powerset2(orig, newset):
	if orig == []:
		return [newset]
	else:
		res = []
		for s in powerset2(orig[1:], newset+[orig[0]]):
			res.append(s)
		for s in powerset2(orig[1:], newset):
			res.append(s)
		return res

def powerset3(orig, newset):
	if orig == []:
		yield newset
	else:
		for s in powerset3(orig[1:], newset+[orig[0]]):
			yield s
		for s in powerset3(orig[1:], newset):
			yield s

def powerset4(lst):
	if len(lst) <= 1:
		yield lst
		yield []
	else:
		for x in powerset4(lst[1:]):
			yield [lst[0]] + x
			yield x

def powerset5(lst):
	if lst == []:
		yield []
	else:
		for s in powerset5(lst[1:]):
			yield s + [lst[0]]
			yield s

def powerset6(lst):
	pairs = [(2**i, x) for i, x in enumerate(lst)]
	for i in xrange(2**len(pairs)):
		yield [x for (mask, x) in pairs if i & mask]

if __name__ == '__main__':
	l = [1,2,3]

#	print(powerset(l))
#	print(powerset2(l, []))
#	print list(powerset3(l, []))
#	print list(powerset4(l))
#	print list(powerset5(l))
#	print list(powerset6(l))

#	n = 8
#	for i in range(n):
#		b = str(bin(i))[2:]
#		if n % 2 != 0:
#			l = int(1.0+len(n, 2))
#		else:
#			l = int(log(n, 2))
#		b = '0'*(l - len(b)) + b
#		print b