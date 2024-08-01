answer_set = set()
for a in range(2, 101):
    for b in range(2, 101):
        answer_set.add(a ** b)
print(len(answer_set))
