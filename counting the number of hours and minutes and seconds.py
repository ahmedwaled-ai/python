seconds=int(input("please enter the number of seconds: "))
hours=seconds//3600
minutes=(seconds%3600)//60
total_seconds=seconds%60
print("the total time is:", hours,"hours and",minutes,)

