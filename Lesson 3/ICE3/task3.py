l1 = [{'course ': 'python', 'LastGPA' : 90, 'CurrentGPA': 80},
{ 'course': 'python',  'LastGPA' : 95, 'CurrentGPA': 85},
{ 'course': 'python',  'LastGPA' : 100,'CurrentGPA': 100}]
d1 = {'course ': 'python', 'LastGPA' : 90, 'CurrentGPA': 80}
d2 = { 'course': 'python',  'LastGPA' : 95, 'CurrentGPA': 85}
d3= { 'course': 'python',  'LastGPA' : 100,'CurrentGPA': 100}

x=[]
y=[]
for item in d1:
    x.append(item)
    y.append(d1[item])

n1 =  d1['LastGPA']
d1.pop('LastGPA')
n2 =  d1['CurrentGPA']
d1.pop('CurrentGPA')

d1.update({'LastGPA+CurentGPA':((n1+n2)/2)})

n1 =  d2['LastGPA']
d2.pop('LastGPA')
n2 =  d2['CurrentGPA']
d2.pop('CurrentGPA')

d2.update({'LastGPA+CurentGPA':(n1+n2)/2})

n1 =  d3['LastGPA']
d3.pop('LastGPA')
n2 =  d3['CurrentGPA']
d3.pop('CurrentGPA')

d3.update({'LastGPA+CurentGPA':(n1+n2)/2})

l1 = [d1,d2,d3]
print(l1)
