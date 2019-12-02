class Unpack:

    def __getitem__(self, item):
        return [1,2,3][item]


unpack = Unpack()
(a,b,c) = unpack
print(a,b,c)

x, y, z = (1, 3, 'avc')
a, b, c = 'fri'

print(a,b,c)
print(x,y,z)

a,b,_,d = (3,6,12414,2)
print(a,b,d)