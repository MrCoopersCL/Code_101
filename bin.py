#COnvert the number 68 to binary code.
def bin_fun():
    x = int(input('Please enter a number: '))
    return (bin(x))

print('Print your binary number is ', bin_fun())

def bin_fun_2(a, b, c, d, e, f, g):
    bin_1 = bin(a)
    bin_2 = bin(b)
    bin_3 = bin(c)
    bin_4 = bin(d)
    bin_5 = bin(e)
    bin_6 = bin(f)
    bin_7 = bin(g)
    print('Your integer values are: ', a, b, c, d, e, f, g)
    print('Your binary values are : ', bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7)
    
bin_fun_2(1, 2, 3, 4, 5, 6, 7)
bin_fun_2(10, 20, 30, 40, 50, 60, 70)
bin_fun_2(100, 200, 300, 400, 500, 600, 700)
bin_fun_2(1000, 2000, 3000, 4000, 5000, 6000, 7000)