#สร้างฟังก์ชันแบบไม่มี Return
def hello (name):
    print("Hello %s"%name)


#การเรียกใช้งานฟังก์ชัน
hello("Kanchit Suwannarat")


#สร้างฟังก์ชันแบบมี Return Value
def area(width , height):
    total = width * height
    return total


#เรียกใช้งานพังก์ชัน
print (area(10,20))


#ฟังก์ชันแบบมีการกำหนดค่าเริ่มต้นไว้
def show_info(name,salary=0.00,lang="not define"):
    print("Name::%s"%name)
    print("Salary: %s"%salary)
    print("Language: %s"%lang)


show_info("Kanchit")
print()
show_info("Kanchit",20000)
print()
show_info("Kanchit",20000, "Java")