data = ("O!", "Megacom", "Beeline", "Katel", "Fonex", "0705", "0550", "0770", "0510", "0543")


designations = []
codes = []

for i in data:
   if i.isdigit():
      codes.append(i)
   elif i.isalpha():
       designations.append(i)

print(designations)
print(codes)

operators = dict(zip(designations, codes))
del operators['Katel'], operators['Fonex']

operators.popitem()
operators.popitem()

operators['O!'] = {'0704','0777','0705'}
operators['Megacom'] = {'0550','0999','505'}
operators['Beeline'] = {'0770','0777','0779'}

print(operators)

for key, value in operators.items():
    print(key, '-', value)
