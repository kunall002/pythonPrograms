def myfunction(rollnos, names):
    yield (rollnos[0], names[0])
    yield (rollnos[1], names[1])
tuple1, tuple2= myfunction([1,2],['mike','ram'])
print(tuple1)
print(tuple2)