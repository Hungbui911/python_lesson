#Tính năm 
#Cách 1
can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
chi = [ "THAN", "DAU", "TUAT", "HOI", "TI", "SUU", "DAN", "MAO", "THIN", "TY", "NGO", "MUI"]

year = int(input())
can_index = int(str(year)[-1:])
chi_index = year % 12
print(can[can_index] , chi[chi_index])

#Cách 2
can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
chi = ["TI", "SUU", "DAN", "MAO", "THIN", "TY", "NGO", "MUI", "THAN", "DAU", "TUAT", "HOI"]

year = int(input())
can_index = year  % 10
chi_index = year  % 12
print(can[can_index] + " " + chi[chi_index])

#Cách 3
can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
chi = ["TI", "SUU", "DAN", "MAO", "THIN", "TY", "NGO", "MUI", "THAN", "DAU", "TUAT", "HOI"]

while True:
    year = int(input("Nhập năm dương lịch (từ 1900 đến 10000): "))
    if 1900 <= year <= 10000:
        break
    print("Vui lòng nhập năm trong khoảng từ 1900 đến 10000.")

can_index = (year - 1900) % 10  
chi_index = (year - 1900) % 12  

print(f"{can[can_index]} {chi[chi_index]}")

#Cách 4
can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
chi = ["TI", "SUU", "DAN", "MAO", "THIN", "TY", "NGO", "MUI", "THAN", "DAU", "TUAT", "HOI"]

while True:
    year = int(input("Nhập năm dương lịch (từ 1900 đến 10000): "))
    if 1900 <= year <= 10000:
        break
    print("Vui lòng nhập năm trong khoảng từ 1900 đến 10000.")

print(f"{year} {can[(year - 1900) % 10]} {chi[(year - 1900) % 12]}")

#Cách 5
can = {0: "CANH", 1: "TAN", 2: "NHAM", 3: "QUY", 4: "GIAP", 5: "AT", 6: "BINH", 7: "DINH", 8: "MAU", 9: "KY"}
chi = {0: "TI", 1: "SUU", 2: "DAN", 3: "MAO", 4: "THIN", 5: "TY", 6: "NGO", 7: "MUI", 8: "THAN", 9: "DAU", 10: "TUAT", 11: "HOI"}

year = int(input())

can_index = (year - 1900) % 10
chi_index = (year - 1900) % 12

can_value = can.get(can_index, "")
chi_value = chi.get(chi_index, "")

print(f"{can_value} {chi_value}")

#Cách 6
def get_can_chi(year):
    can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
    chi = ["TI", "SUU", "DAN", "MAO", "THIN", "TY", "NGO", "MUI", "THAN", "DAU", "TUAT", "HOI"]
    
    can_index = (year - 1900) % 10  
    chi_index = (year - 1900) % 12  
    
    return f"{can[can_index]} {chi[chi_index]}"

print(f"{get_can_chi(year)}")

#Cách 7
year = int(input(""))
def get_can_chi(year):
    can = {0: "CANH", 1: "TAN", 2: "NHAM", 3: "QUY", 4: "GIAP", 5: "AT", 6: "BINH", 7: "DINH", 8: "MAU", 9: "KY"}
    chi = {0: "TI", 1: "SUU", 2: "DAN", 3: "MAO", 4: "THIN", 5: "TY", 6: "NGO", 7: "MUI", 8: "THAN", 9: "DAU", 10: "TUAT", 11: "HOI"}
    
    can_index = (year - 1900) % 10  
    chi_index = (year - 1900) % 12  
    
    can_value = can.get(can_index, "")
    chi_value = chi.get(chi_index, "")

    return f"{can_value} {chi_value}"

print(f"{get_can_chi(year)}")
