def cel_to_fah(celsius):
    return (celsius * 9/5)+32
celsius=float(input("enter the temp:"))
fah=cel_to_fah(celsius)
print(f"{celsius} 'c is equal to {fah}'f")