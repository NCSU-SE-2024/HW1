def main():
    for i in range(10):
        print(i, end=" ")
    print("\n")
    return i+1

if __name__=="__main__":
    print("before print", "\n")
    main()
    print("after print", "\n")