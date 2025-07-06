# credit card number validator
"""
 Logic :
    1. remove ' - ' or any " " from the input
    2. detect the type of card based on starting digits and length
    3. add all the digits in the odd places from the right to left 
    4. double every second digit from the right to left 
       (if the result leads to a two-digit number then add them to get a single digit)
    5. sum the totals of step 3 & 4
    6. check if the sum is divisible by 10 then the credit card number is valid
    7. display card type and whether it is valid or not
"""

def detect_card_type(number):
    if number.startswith('4') and len(number) in [13, 16]:
        return "Visa"
    elif number.startswith(('51', '52', '53', '54', '55')) and len(number) == 16:
        return "MasterCard"
    elif number.startswith(('34', '37')) and len(number) == 15:
        return "American Express"
    elif number.startswith('6011') and len(number) == 16:
        return "Discover"
    elif number.startswith('35') and len(number) == 16:
        return "JCB"
    elif number.startswith(('36', '38')) and len(number) == 14:
        return "Diners Club"
    elif number.startswith('30') and len(number) == 16:
        return "Diners Club"
    else:
        return "Unknown or Unsupported"

cc_number = ""

def cardvalidator(text):
    # Step 1: Input and cleanup
    cc_number = input("Enter your credit card number: ")
    cc_number = cc_number.replace("-", "").replace(" ", "")
    
    # Step 2: Detect card type
    print("🔍 Card Type:", detect_card_type(cc_number))

    # Step 3: Reverse the number for validation
    cc_number = cc_number[::-1]

    # Step 4: Sum odd-position digits
    sum_odd = 0
    for i in cc_number[::2]:
        sum_odd += int(i)

    # Step 5: Sum even-position digits after doubling
    sum_even = 0
    for i in cc_number[1::2]:
        i = int(i) * 2
        if i > 9:
            sum_even += (i - 9)
        else:
            sum_even += i

    # Step 6: Final total
    total = sum_odd + sum_even

    # Step 7: Check if valid
    if total % 10 == 0:
        print("✅ Valid Credit Card Number!")
    else: 
        print("❌ Invalid Credit Card Number.")

cardvalidator(cc_number)
