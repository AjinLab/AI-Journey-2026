def main():
    n = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip('- ')

    if n == "42" or n == "forty-two" or n == "forty two":
        print('Yes')
    else:
        print('No')



main()
