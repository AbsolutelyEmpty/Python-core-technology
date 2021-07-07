print("Please input your score:")
score = int(input())
if score >= 90 and score <= 100:
    print("Your level is A.")
elif score >= 80:
    print("Your level is B.")
elif score >= 60:
    print("Your level is C.")
else:
    print("Your level is D.")
