# This is created by sugan😎😍😀
'''First enter your equations and press run'''
print("this program is created by sugan under MIT lisence 2.0")
def find(a):
    num1 = a[0] # instead use x1 ,1
    num2 = a[1] # y1 ,1
    num3 = a[2] # c2 ,5
    num4 = a[3] # x2 ,2
    num5 = a[4] # y2 ,2
    num6 = a[5] # c2 ,4

    if num1 == num4:
        if num2 == num5:           """  if num2 == num5 and num3 == num6
                                              print("Invalid1")
                                              return 
                                        else:
                                              print("Invalid2") next just use an if                       """
            if num3 == num6:
                print("Invalid1")
            else:
                print("Invalid2")
        elif num2 != num5:
            if num3 != num6:
                print('y = ', (num3 - num6) / (num2 - num5), 'x = ', (num3 - (num2*((num3 - num6) / (num2 - num5))))/num1)#very confusing use two line or store the value in a variable like y = (num3 - num6) / (num2 - num5)
                # so in second eqn x = (num3 - num2 * y)/num1   much more readble
                return " "
            elif num3 == num6:
                print('y = 0 and x = ', b[2]) # whh is b whf is it's third value it must be num3 or num6 i hope
                return " "
            else:
                print("Invalid3")
        else:
            print("Invalid4")
    elif num1 != num4: # if it is not equal then it must be not equal so you didn't need elif simple else is enough
        if num2 == num5:
            if num3 == num6:
                print("x = 0 and y  = ", b[2]) # again wtf num3 or num6
                return " "
            elif num3 != num6: # you didn't need elif 
              # x = (num6 - num3) / (num4 - num1)
              # y = (num3 - num1* x )/num2 y is wrong in your calculation
                print("x =", (num6 - num3) / (num4 - num1), 'y = ', (num3 - num1)/(num2))
                return " "
            else: # this else simply waste
                print("Invalid5")
        elif num2 != num5: # else is enough 
            mullist1 = [i * num4 for i in a[:3]]
            mullist2 = [i * num1 for i in a[3:]]
            # use variable name for mullist1[1] and mullist2[2]
            # and wtf is mullist1
            # because u are using it again and again
            if mullist1[1] > mullist2[1] or mullist1[1] == mullist2[1]:
                #wtf is w,a,s,d
                w = mullist1[1] - mullist2[1]
                a = mullist1[2] - mullist2[2]
                s = a / w # atleat name is y
                d = (num3 - num2 * s) / num1 
                print("x = ", d, "y = ", s)
                return " "
            else:
                # u are doing the same thing as above waste of space
                w = mullist1[1] - mullist2[1]
                a = mullist1[2] - mullist2[2]
                s = a / w
                d = (num3 - num2 * s) / num1
                print("x = ", d, "y = ", s)
                return " "
        else: # waste else
            print("invalid6")
    else:#waste else
        print("invalid7")


while True:
    first_equ = str(input().replace(' ', '')) #input itself is a string you don't need str()
    second_equ = str(input().replace(' ', ''))
    try:
        listconv1 = first_equ.split('=')# x + y = 5  ['x+y' , '5']
        listconv2 = second_equ.split("=")# 2x + 2y = 4 ['x+2y' , '4']
        """ bad variable names
        wtf is w c s d """
        w = listconv1[0].split("x")# 'x+y' ['','+y']
        c = w[1].split('y') # '+y' ['+','']
        c.remove('') # ['+']
        w += c # ['','+y','+']
        s = listconv2[0].split("x") # '2x+2y' ['2','+2y']
        c = s[1].split('y') # ['+2','']
        c.remove('') # ['+2y']
        s += c # ['2','+2y','+2']
        d = [[w[0], w[2], listconv1[1]], [s[0], s[2], listconv2[1]]] # [['','+',5],['2','+2','4']]
        a = []
        for x in d:
            for i in range(len(x)): # instead use "for idx,val in enumerate(x):"
                if x[i] == '' or x[i] == '+': 
                    x[i] = 1 
                elif x[i] == '-':
                    x[i] = -1
                else:
                    x[i] = int(x[i])
            a += x # use extend function to be more explict that you are using list it may confused with a number

        print(a) #[1,1,5,2,2,4]
        print(find(a))
    except:
        print('error')
        break

