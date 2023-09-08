print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

# Question 1
print("\nQuestion 1: What does HTML stand for in web development?")
print("a) Hyper Text Markup Language")
print("b) High-Level Text Management Language")
print("c) Hyper Transfer Markup Language")
print("d) High-Level Text Markup Language")

answer1 = input("Your answer (a/b/c/d): ")
if answer1.lower() == "a":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'a) Hyper Text Markup Language'.")


# Question 2
print("\nQuestion 2: Which programming language is known for its use in machine learning and data analysis?")
print("a) Java")
print("b) Python")
print("c) C++")
print("d) Ruby")

answer2 = input("Your answer (a/b/c/d): ")
if answer2.lower() == "b":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'b) Python'.")


# Question 3
print("\nIn JavaScript, which keyword is used to declare a variable with block ")
print("a) var")
print("b) let")
print("c) const")
print("d) function")

answer3 = input("Your answer (a/b/c/d): ")
if answer3.lower() == "b":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'b) let'.")


# Question 4
print("\nWhat does SQL stand for in database management? ")
print("a) Structured Query Language")
print("b) Sequential Query Language")
print("c) System Query Language")
print("d) Server Query Language")

answer4 = input("Your answer (a/b/c/d): ")
if answer4.lower() == "a":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'a) Structured Query Language'.")


# Question 5
print("\nWhich data structure follows the Last-In-First-Out (LIFO) principle? ")
print("a) Queue")
print("b) Stack")
print("c) Linked List")
print("d) Array")

answer5 = input("Your answer (a/b/c/d): ")
if answer5.lower() == "b":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'b) Stack'.")


# Question 6
print("\nIn object-oriented programming, what is the process of creating a new instance of a class called? ")
print("a) Inheritance")
print("b) Abstraction")
print("c) Instantiation")
print("d) Polymorphism")

answer6 = input("Your answer (a/b/c/d): ")
if answer6.lower() == "c":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'c) Instantiation'.")


# Question 7
print("\nWhich programming paradigm focuses on describing what a program should do, rather than how to do it? ")
print("a) Functional programming")
print("b) Object-oriented programming")
print("c) Procedural programming")
print("d) Imperative programming")

answer7 = input("Your answer (a/b/c/d): ")
if answer7.lower() == "a":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'a) Functional programming'.")


# Question 8
print("\nWhich sorting algorithm has an average and worst-case time complexity of O(n^2)? ")
print("a) Quick Sort")
print("b) Merge Sort")
print("c) Insertion Sort")
print("d) Bubble Sort")

answer8 = input("Your answer (a/b/c/d): ")
if answer8.lower() == "d":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'd) Bubble Sort'.")


# Question 9
print("\nWhat is the primary purpose of version control systems like Git? ")
print("a) To write and execute code")
print("b) To document code comments")
print("c) To track changes in code and collaborate with others")
print("d) To optimize code for performance")

answer9 = input("Your answer (a/b/c/d): ")
if answer9.lower() == "c":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'c) To track changes in code and collaborate with others'.")


# Question 10
print("\nWhich HTTP status code indicates a successful request in web development? ")
print("a) 200 OK")
print("b) 404 Not Found")
print("c) 500 Internal Server Error")
print("d) 302 Found")

answer10 = input("Your answer (a/b/c/d): ")
if answer10.lower() == "a":
    print("\nCORRECT!")
    score += 1
else:
    print("Incorrect. The correct answer is 'a) 200 OK' ")

# Display the final score
print("\nYour final score is:", score)
print("\nCorrect Answers:")
print("1. a) Hyper Text Markup Language")
print("2. b) Python")
print("3. b) let")
print("4. a) Structured Query Language")
print("5. b) Stack")
print("6. c) Instantiation")
print("7. a) Functional programming")
print("8. d) Bubble Sort")
print("9. c) To track changes in code and collaborate with others")
print("10. a) 200 OK")