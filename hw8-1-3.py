# Author: SMR (AMDG) 12/10/21
height_feet = int(input("What's your  height in feet w/o inches ?: "))
height_inches = int(input("What's your height with inches added? (discluding ft): "))
weight = int(input("What's your current weight in lbs?: "))
def bmi(feet,inches,weight):
    weight_kg=weight/2.20
    height_inch=(feet * 12)+inches
    height_total=height_inch/39.37
    bmi =weight_kg/(height_total ** 2)
    if bmi < 19:
        bmi_info = "Underweight"
    elif bmi < 25:
        bmi_info = "Healthy"
    elif bmi < 30:
        bmi_info = "OverWeight"
    elif bmi < 40:
        bmi_info = "Obese"
    else:
        bmi_info = "Extremely Obese"
    return bmi_info
print(bmi(height_feet,height_inches,weight))