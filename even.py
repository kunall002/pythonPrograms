def contain_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("list contains an even number")
            break
    else:
        print("list does not contain an even number")
print("for list 1:")
contain_even_number([1,29,8])
print("\n for list2:")
contain_even_number([1,3,5])