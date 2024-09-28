class Student3:
    def student_details(self,name,email):
        print(name, email)

    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)


Student3 = Student3()
Student3.student_details("Vipin", "Vipin@text.com")
Student3.mentor_class(["Vipin", "Ajay", "Manish"])
