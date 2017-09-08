def get_initials(fullname):
    names = fullname.split()
    so_far = "" 
    for name in names:
        so_far += name[0].upper()
    return so_far
def main():
    full_name = input("What is your full name ?")
    print(full_name)
    initials = get_initials(full_name)
    print(initials)

if __name__ == "__main__":
    main()
