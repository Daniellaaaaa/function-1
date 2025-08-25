

students_db={}
student_id=1
# Function to start our program

def start():
	while True:
		print('''
1. To add a student
2. To delete a student
3. Update a student record
4. Get a student
5. Display all the students
6. Search student by name
7. Count number of students
8. filter students by age
0. exit
''')
		user_choice=int(input("Please enter the task you want to perform: "))
		if user_choice==0:
			print("exiting...")
			exit()
		elif user_choice == 1:
			add_student()
		elif user_choice == 2:
			delete_student()
		elif user_choice == 3:
			update_student()		
		elif user_choice == 4:
			get_student()	
		elif user_choice==5:
			display_students()
		elif user_choice==6:
			search_student_by_name()
		elif user_choice==7:
			count_students()
		elif user_choice==8:
			filter_by_age()			
		else:
			print("Invalid input")		

# Function to add students to database
def add_student():
	name=input("Please enter the student name: ")
	age=int(input("Please enter the student age: "))
	department=input("Please enter the student department: ")
	key=len(students_db) + 1
	students_db[key]={"name":name, "age": age, "dept":department}
	print(students_db)

# Function to delete
def delete_student():
	student_id=int(input("Student Id to delete: "))
	if student_id in students_db:
		del students_db[student_id]
		print(f"student with id {student_id} deleted successfully")
		print(f"{students_db}")
	else:
		print("Student not found")	

# Function to update
def update_student():
	print('''
1. Update name
2. Update age
3. Update department	

''')	
	student_id=int(input("Please enter the student id to update: "))
	if student_id in students_db:

		update=int(input("What do you want to update: "))
		if update == 1:
			print(students_db)
			update_name=input("Enter new name: ")

			students_db[student_id].update({"name":update_name})
			print("updated successfully")
			print(students_db)
		elif update == 2:
			update_age=int(input("Enter new age: "))
			students_db[student_id].update({"age":update_age})
			print("updated successfully") 
			print(students_db)
		elif update == 3:
			update_dept=input("Enter new department: ")
			students_db[student_id].update({"dept":update_dept})	 	
			print("updated successfully") 
			print(students_db)
		else: 
			print("Invalid input")	
	else:
		print("Student not found")

# Function to get a student
def get_student():
	student_id=int(input("Enter the student id: "))
	if student_id in students_db:
		data=students_db[student_id]
		print(f'Student id {student_id}: The student name is {data["name"]}, His age is {data["age"]}, His department is {data["dept"]}' )
		

	else:
		print("Student does not exist")	

# Function to display all students
def display_students():
	print(students_db)
	for student_id, student_details in students_db.items():
		print(f'Student id {student_id}: Name is {student_details["name"]}, Age is {student_details["age"]}, Department is {student_details["dept"]}')


# Function to search student by name
def search_student_by_name():
	print(students_db)
	flag=False
	student_name=input("Enter name to search: ")
	for student_id, student_details in students_db.items():
		if student_details["name"]==student_name:
			flag=True
			print(f'Student id {student_id}, Name: {student_details["name"]}, Age:{student_details["age"]}, Department:{student_details["dept"]}')
	if flag == False:
		print("Student not found")	


# Function to count student
def count_students():
	print(students_db)
	num_students=len(students_db)
	print(f"The number of students in the database is {num_students}")

# Function to filter by age
def filter_by_age():
	print(students_db)
	flag=False
	student_age=int(input("Enter minimum age: "))
	for student_id, student_details in students_db.items():
		if student_details["age"]>student_age:
			flag=True
			print(f'Student id {student_id}, Name: {student_details["name"]}, Age:{student_details["age"]}, Department:{student_details["dept"]}')
	if flag==False:
		print("Age not found")		

#Start Program
start()

