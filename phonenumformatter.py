def clean_number(text):
    return text.strip().replace("-","")

def is_valid(number):
    return len(number) == 10 and number.isdigit() and number.startswith("0")

def format_number(number):
    return number[:3] + "-" + number[3:6] + "-" + number[6:]

def hide_number(number):
    return number[:3] + "-" + "xxx" + "-" + number[6:]

def digit_sum(number):
    total = 0
    for digit in number:
        total += int(digit)
    return total

phone = input("phone number: ")
number = clean_number(phone)

if not is_valid(number):
    print("Invalid phone number")
else:
    print("Formatted:", format_number(number))
    print("Hidden:", hide_number(number))
    print("Digit Sum:", digit_sum(number))
