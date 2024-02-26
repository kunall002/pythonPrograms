string ="greek"
def test(string):
    string ="Greeks got greeeks"
    print("inside function:\n",string)
test(string)
print("outside Function:\n", string)


def add_more(list):
    list.append(50)
    print("inside function ",list)
mylist=[10,20,30,40]
add_more(mylist)
print("outside Function:",mylist)
