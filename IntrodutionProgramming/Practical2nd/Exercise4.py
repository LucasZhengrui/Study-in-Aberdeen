# Type yearly salary, and then showing your monthly income after and before taxing (20%)

yearlysalary = int(input("Please input your yearly income: "))
print("Your monthly income before taxing(20%): ")
print(yearlysalary/12)
print("Your monthly income after taxing(20%): ")
print(yearlysalary/12 - yearlysalary/12*0.2)
