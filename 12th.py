from __future__ import division

somelist =  [1,12,2,53,23,6,17] 
max_value = max(somelist)
min_value = min(somelist)
avg_value = 0 if len(somelist) == 0 else sum(somelist)/len(somelist)
print("max:",max_value)
print("min:",min_value)
print("avg:",avg_value)
