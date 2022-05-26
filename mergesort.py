def merge(a, b):
	"""Assumes a and b are sorted arrays of length n%2 = 0.
		Returns sorted merged sorted array c."""
	i = 0
	j = 0
	n = max(len(a), len(b))
	result = []

	for k in range(2*n):
		print(result)
		if (i < n) and a[i] < b[j]:
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	return result

def sort(a):
	"""a and b are lists
		Returns sorted lists"""
	n = len(a)
	if n < 2:
		return a
	if n == 2:
		if a[0] > a[1]:
			return [a[1],a[0]]
		else:
			return a
	return merge(sort(a[:n//2]), sort(a[n//2:]))

print(sort([5,4,1,8,7,2,6,3]))
print(merge([1,3],[2,5]))