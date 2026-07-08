name=input("Enter your name: ")
marks =int(input("Enter total marks(out of 300): "))
percentage=(marks/300)*100
if percentage>=90:
    grade='A+'
    remark='outstanding'
elif percentage>=75:
    grade='A'
    remark='excellent'
elif percentage>=60:
    grade='B'
    remark='good'
elif percentage>=50:
    grade='C'
    remark='average'
elif percentage>=40:
    grade='D'
    remark='pass'
else:
    grade='F'
    remark='fail'
print(f"percentage:{percentage:.2f}")
print(f"grade:{grade}")
print(f"remark:{remark}")
status = "PASS" if percentage >= 40 else "FAIL"
with open("results.txt", "a") as file:
    file.write(f"{name}, {marks}, {percentage:.2f}%, {grade}, {remark}, {status}\n")


print("Result saved successfully!")
print("\nSaved Results:")
with open("results.txt", "r") as file:
    print(file.read())