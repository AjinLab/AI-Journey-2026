def main():
    userInput = input("File name: ").lower().strip()

    extension = userInput.rsplit(".")[-1]

    match extension:
        case 'gif' | 'jpg' | 'jpeg' | 'png':
            if extension == 'jpg':
                print("image/jpeg")
            else:
                print("image/" + extension)
        case 'pdf' | 'zip':
            print("application/" + extension)
        case 'txt':
            print("text/plain")
        case _:
            print("application/octet-stream")

main()
