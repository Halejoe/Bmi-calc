height=float(input("Enter your height: " ))
weight=float(input("Enter your weight: " ))
def Bmi_calc(height,weight):
    return weight/(height ** 2)
    
    
a=Bmi_calc(height,weight)

print(a,"bmi")