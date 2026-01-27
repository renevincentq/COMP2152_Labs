print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)

monday_class = {"Alice", "Bob", "Charlie", "Diana"}

wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
print("Monday Class", monday_class)
print("Wednesday Class", wednesday_class)

both_classes = monday_class & wednesday_class
print("Attended both classes: ", both_classes)

all_students = monday_class | wednesday_class
print("Attended either class: ", all_students)

monday_only = monday_class - wednesday_class
print("Only Monday: ", monday_only)

one_class = monday_class ^ wednesday_class
print("Only one class (not both): ", one_class)

print("Is Monday a subset of all students?", both_classes <= monday_class)