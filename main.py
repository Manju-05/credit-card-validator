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
    elif number.startswith('30') and len(number) == 16 :
        return "Diners Club"
    else:
        return "Unknown or Unsupported"

def cardvalidator(text):
    cc_number = input("Enter your credit card number: ")
    cc_number = cc_number.replace("-", "").replace(" ", "")
    
    print("🔍 Detected Card Type:", detect_card_type(cc_number))

    cc_number = cc_number[::-1]

    sum_odd = sum(int(i) for i in cc_number[::2])

    sum_even = 0
    for i in cc_number[1::2]:
        doubled = int(i) * 2
        sum_even += doubled if doubled < 10 else (doubled - 9)

    total = sum_odd + sum_even

    if total % 10 == 0:
        print("✅ Valid Credit Card Number!")
    else:
        print("❌ Invalid Credit Card Number.")

cardvalidator("")
