print("Enter number of books purchased for each type:")
book1=int(input("No.of Introduction to Python Programming books: "))
book2=int(input("No.of Python Libraries Cookbook: "))
book3=int(input("No.of Data Science in Python books: "))
price = (499.0*book1)+(855.0*book2)+(645.0*book3)
gst= price*12/100
print("Total invoice amount:",price + gst + 250.0)