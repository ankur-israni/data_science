# Merge the two dictionaries to have unique values
d1 = {'v1':'k1','v2':'k2','v3':'k3'}

d2 = {'v3':'k3','v4':'k4','v5':'k5'}

d1_clone = d1

for d2_key,d2_value in d2.items():
    if(d2_key not in d1_clone):
        d1_clone[d2_key]=d2_value

print("merged dictionary = ",d1_clone)