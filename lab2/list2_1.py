def merge(a, left, mid, right):
comparisons = 0
assignments = 0
n1 = mid - left
n2 = right - mid
L = a[left:mid]
R = a[mid:right]
assignments += n1 + n2

it1 = 0
it2 = 0
k = left
assignments += 3
while it1 &lt; n1 and it2 &lt; n2:
comparisons += 1
if L[it1] &lt;= R[it2]:
a[k] = L[it1]
it1 += 1
else:
a[k] = R[it2]
it2 += 1
assignments += 2
k += 1
while it1 &lt; n1:
a[k] = L[it1]
it1 += 1
k += 1
assignments += 1
while it2 &lt; n2:
a[k] = R[it2]
it2 += 1
k += 1
assignments += 1
return comparisons, assignments
def merge_sort_iterative(a):
n = len(a)
comparisons = 0
assignments = 0
i = 1
while i &lt; n:
j = 0
while j &lt; n - i:
left = j
mid = j + i
right = min(j + 2 * i, n)
c, a_count = merge(a, left, mid, right)
comparisons += c
assignments += a_count
j += 2 * i
i *= 2
return a, comparisons, assignments
# Варіант 18
my_list = [21, 44, 22, 50, 63, 68, 97, 12, 15]
print(&quot;Оригінальний список:&quot;, my_list)
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
print(&quot;Відсортований список:&quot;, sorted_list)
print(f&quot;Кількість порівнянь: {comps}&quot;)
print(f&quot;Кількість присвоювань: {assigs}&quot;)
