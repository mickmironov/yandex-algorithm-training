def phone_numbers():
    wanted_number = get_phone(input())
    phone_book = []
    for i in range(3):
        phone_book.append(get_phone(input()))
    for phone in phone_book:
        if phone == wanted_number:
            print("YES")
        else:
            print("NO")

def get_phone(phone_input):
    phone_normalized = normalize_phone(phone_input)
    phone = {}
    if len(phone_normalized) == 7:
        phone["code"] = "495"
        phone["number"] = phone_normalized
    else:
        phone["code"] = phone_normalized[1:4]
        phone["number"] = phone_normalized[4:]
    return phone

def normalize_phone(phone_input):
    return "".join(filter(lambda x: x.isdigit(), phone_input))

if __name__ == "__main__":
    phone_numbers()
