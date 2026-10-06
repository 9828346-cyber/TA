def merge(left, right):
merged_arr = []
comparisons = 0
assignments = 0
i = 0
j = 0
while i &lt; len(left) and j &lt; len(right):
comparisons += 1
if left[i] &lt;= right[j]:
merged_arr.append(left[i])
i += 1
else:
merged_arr.append(right[j])
j += 1
assignments += 1
while i &lt; len(left):
merged_arr.append(left[i])
i += 1
assignments += 1
while j &lt; len(right):
merged_arr.append(right[j])
j += 1
assignments += 1
return merged_arr, comparisons, assignments
def merge_sort_recursive(arr):
comparisons = 0
assignments = 0
recursive_calls = 0
if len(arr) &lt;= 1:
return arr, comparisons, assignments, recursive_calls
mid = len(arr) // 2
assignments += 1
recursive_calls += 2
left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])
comparisons += c1 + c2
assignments += a1 + a2
recursive_calls += r1 + r2
merged_arr, c_merge, a_merge = merge(left_half, right_half)
comparisons += c_merge
assignments += a_merge
return merged_arr, comparisons, assignments, recursive_calls

# Варіант 18
my_list = [21, 44, 22, 50, 63, 68, 97, 12, 15]
print(&quot;Оригінальний список:&quot;, my_list)
sorted_list, total_comparisons, total_assignments, total_recursive_calls = merge_sort_recursive(my_list)
print(&quot;Відсортований список:&quot;, sorted_list)
print(f&quot;Загальна кількість порівнянь: {total_comparisons}&quot;)
print(f&quot;Загальна кількість присвоювань: {total_assignments}&quot;)
print(f&quot;Загальна кількість рекурсивних викликів: {total_recursive_calls}&quot;)
