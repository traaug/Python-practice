def main():
    no_of_people = int(input("enter total number of people: "))
    people = []
    for i in range(no_of_people):
        man = []
        man.append(input("enter your name: "))
        man.append(float(input("enter your grade: ")))
        people.append(man)
        print(people)
    sorted_data = sorted(people, key=lambda x: x[1])
    second_smallest = sorted_data[1][1]
    second_smallest_key = sorted_data[1][0]

    print(sorted_data)
    print("The second smallest number is:", second_smallest)
    print("Key associated with the second smallest number:", second_smallest_key)



if __name__ == '__main__':
    main()



