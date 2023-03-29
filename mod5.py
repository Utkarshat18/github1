class Eligibility:
    def verify(self):
        age = int(input("Enter your Age: "))
        weight = float(input("Enter your Weight: "))
        if(age>=18 and age<= 65 and weight >= 45):
            print("Test 1 Passed!")
        else:
            return "stop"

    def disease(self):
        fever = input("Have Fever or Cold(Yes or No): ")
        diabete = input("Do you have Diabetes(Yes or No): ")
        heart = input("Any Heart Disease(Yes or No): ")
        blood_pressure = input("Have Normal Blood Pressure(Yes or No): ")
        haemoglobin = float(input("Haemoglobin Level(in gms): "))
        print("\nChecking Health Status....")
        if(fever.upper() == "NO" and diabete.upper() == "NO" and blood_pressure.upper() == "YES" and heart.upper() == "NO" and haemoglobin >= 12.5):
            print("You are Healthy for donation.")
        else:
            print("You are not Healthy for donation.")
    

e = Eligibility()
res = e.verify()
if(res == "stop"):
    print("Not Eligible for Further Process")
else:
    e.disease()