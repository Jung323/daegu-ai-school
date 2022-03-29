members=['egoing','duru']
for member in members:
    print(member)
for i in range(len(members)):
    print(members[i])
print()
members2=[
    ['egoing','seoul','programmer'],
    ['duru','daegu','dba']
]
print(members2[0][0])
for member2 in members2:
    for member in member2:
        print(member)
print()
egoing = {'name':'egoing','city':'seoul','job':'programmer'}
for name in egoing:
        print(egoing[name])
print()
members3=[
    {'name':'egoing','city':'seoul','job':'programmer'},
    {'name':'duru','city':'daegu','job':'dba'}
]
for member in members3:
    print(member)
    