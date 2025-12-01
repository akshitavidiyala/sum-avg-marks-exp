# sum_avg_marks.py

# You can change these numbers any time
numbers = [43, 40,37, 27]  # you can change the numbers

total = sum(numbers)
average = total / len(numbers)

print("Marks:", numbers)
print("Sum:", total)
print("Average:", average)

# 👉 Extra part: save the same output to artifacts.txt
with open("artifacts.txt", "w") as f:
    f.write(f"Marks: {numbers}\n")
    f.write(f"Sum: {total}\n")
    f.write(f"Average: {average}\n")

