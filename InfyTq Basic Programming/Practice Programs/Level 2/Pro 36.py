sen = input().split()
target_word = input()
l1 = [i for i in range(0, len(sen)) if target_word in sen[i]]
print(l1)
p = list(set(sen))
l3 = [[k for k in range(0, len(sen)) if i in sen[k]]for i in p]
s2 = {p[i]: l3[i] for i in range(0, len(l3))}
print(s2)

# a a a a b b m m a a