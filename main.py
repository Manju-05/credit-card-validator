# credit card number validator
"""
 Logic :
    1.remove ' - ' or any " " from the input
    2.add all the digits in the odd places from the right to left 
    3.double every second digit from the right to left (if the result leads to the two digit number then add them to get a single digit)
    4.sum_odd the totals of step 2& 3
    5.check if the sum_odd is divisible by 10 then the credit card number is valid.
    6.display whether the card is valid or not.

"""
cc_number = ""
def cardvalidator(text):
# removing the spaces from the input number
    cc_number = input("Enter your credit card number")
    cc_number = cc_number.replace("-", "").replace(" ", "")
    cc_number = cc_number[::-1]
    print(cc_number)

    # sum the odd digits from right to left (reverse of given number)
    sum_odd = 0
    for i in cc_number[::2]:
        sum_odd += int(i)
    print(sum_odd)

    # sum the even digits from right to left (reverse of given number)

    sum_even = 0
    for i in cc_number[1::2]:
        i = int(i)*2
        if i > 10:
            sum_even += (1+ (i%10))  #(ex : 18 = 1 + 8 = 9)
        else:
            sum_even += i
    total = sum_odd + sum_even
    
    if(total %10 == 0):
        print("valid")
    else: 
        print("Invalid")

cardvalidator(cc_number)




