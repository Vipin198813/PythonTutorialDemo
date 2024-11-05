# def mentor(cls, list_of_mentors):
#     print(list_of_mentors)
# class Student:
#     mobile_num = 23923490843
#
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#     @classmethod
#     def change_number(cls,mobile):
#         Student.mobile_num = mobile
#
#     @classmethod
#     def details(cls,name,email):
#         return cls(name,email)
#
#     def student_details(self):
#         print(self.name,self.email, self.mobile_num)
# #
# # obj = Student()
# # print(obj.mobile_num)
# S1 = Student.mobile_num
# print(S1)
# Student.change_number(452424234)
# S2 = Student.mobile_num
# print(S2)
#
# obj = Student("Vipin", "vipin@text.com")
# obj.student_details()
#
# Student.mentor = classmethod(mentor)
# Mentor1 = Student.mentor(["Vipin", "Rathore"])


class MyClass:
    class_var = 0  # Class variable

    def __init__(self, value):
        self.instance_var = value  # Instance variable

    @classmethod
    def increment_class_var(MyClass):
        MyClass.class_var += 1
        return MyClass.class_var

# Calling class method
print(MyClass.increment_class_var())  # Outputs: 1
print(MyClass.increment_class_var())  # Outputs: 2
