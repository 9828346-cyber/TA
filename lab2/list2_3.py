def partition(a, l, r):
comparisons = 0
assignments = 0
pivot = a[l]
assignments += 1
i = l - 1
j = r + 1
assignments += 2
while True:
i += 1
assignments += 1
while a[i] &lt; pivot:
comparisons += 1
i += 1
assignments += 1
comparisons += 1
j -= 1
assignments += 1
while a[j] &gt; pivot:
comparisons += 1
j -= 1
assignments += 1
comparisons += 1
comparisons += 1
if i &gt;= j:
return j, comparisons, assignments

a[i], a[j] = a[j], a[i]
assignments += 3
def quicksort(a, l, r):
comparisons = 0
assignments = 0
recursive_calls = 1
if l &lt; r:
q, c1, a1 = partition(a, l, r)
comparisons += c1
assignments += a1
c2, a2, r2 = quicksort(a, l, q)
c3, a3, r3 = quicksort(a, q + 1, r)
comparisons += c2 + c3
assignments += a2 + a3
recursive_calls += r2 + r3
else:
return 0, 0, 0
return comparisons, assignments, recursive_calls
# Варіант 18
my_list = [21, 44, 22, 50, 63, 68, 97, 12, 15]
original_list = my_list.copy()
print(&quot;Оригінальний список:&quot;, original_list)
total_comparisons, total_assignments, total_recursive_calls = quicksort(
my_list, 0, len(my_list) - 1
)
print(&quot;Відсортований список:&quot;, my_list)
print(f&quot;Загальна кількість порівнянь: {total_comparisons}&quot;)
print(f&quot;Загальна кількість присвоювань: {total_assignments}&quot;)
print(f&quot;Загальна кількість рекурсивних викликів: {total_recursive_calls}&quot;)
