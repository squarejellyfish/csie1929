height = float(input())
weight = float(input())
height /= 100
bmi = weight / (height * height);

if (bmi < 18.5):
    print("{:.2f}".format(bmi));
    print("Underweight");
elif (bmi < 24):

    print("{:.2f}".format(bmi));
    print("Normal");
elif (bmi < 27):

    print("{:.2f}".format(bmi));
    print("Overweight");
elif (bmi < 30):

    print("{:.2f}".format(bmi));
    print("Obese Class I");
elif (bmi < 35):

    print("{:.2f}".format(bmi));
    print("Obese Class II");
else:
    print("{:.2f}".format(bmi));
    print("Obese Class III");

