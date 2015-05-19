cat =['mam','rep','ins']
ani =['cow','dog','pyt','liz','bee','fly']
whe = [[0,1],[2,3],[4,5]]
res = {y[1]: {x[1] for x in enumerate(ani) if x[0] in whe[y[0]]} for y in enumerate(cat)}
print res

st1 = [y for y in enumerate(cat)]
st2 = [x for x in enumerate(ani)]

print st1
print st2