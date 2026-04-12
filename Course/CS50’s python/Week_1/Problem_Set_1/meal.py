def main():
    time  = input("What time is it? ")

    converted = convert(time)

    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")


    converted = float(hours) + float(minutes) / 60

    return converted

if __name__ == "__main__":
    main()