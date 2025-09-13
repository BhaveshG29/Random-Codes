Num1 = input("Enter Your First Number: ")
operator = input("Enter the operator you want to you (+, -, *, /, %): ")
Num2 = input("Enter Your Second Number: ")




if operator =="+":
   
    print(int(Num1) + int(Num2))

elif operator =="-":
  
    print(int(Num1) - int(Num2))

elif operator =="*":
          print(int(Num1)*int(Num2))

elif operator =="/":
          print(int(Num1)/int(Num2))

elif operator == "%":
          print(int(Num1)%int(Num2))

else:

          print("Error! Please Specify The Correct Operator")



