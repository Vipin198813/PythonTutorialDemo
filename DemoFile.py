class MyClass:
    class_attribute = "I am a class attribute"
    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute
    def instance_method(self):
        return f"Instance attribute: {self.instance_attribute}"


obj = MyClass("I am an instance attribute")
print(obj.class_attribute)  # Accessing class attribute
print(obj.instance_attribute)  # Accessing instance attribute
print(obj.instance_method())  # Calling instance method
