
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--radio', help='Provide the radius of a circle as --radio x', required=True, type=int)
args = parser.parse_args()

r= args.radio
pi = 3.14159265359
area = pi * r**2
circumference = 2 * pi * r

print("If the radius of your circle is",args.radio,"the circle will have:")
print("Area:", area)
print("Circumference:", circumference)