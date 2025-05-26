
### bmi calculator

def bmi_calc():
  weight = float(input("enter your weight in kilogram."))
  height = float(input("enter your height in meter."))
  bmi = weight/(height**2)
  def am_i_good(bmi):
    if bmi<18.5:
      return "underweight"
    elif 18.5<bmi<25.5:
      return "moderate"
    else:
      return "overweight"  
  return f"My weight is: {weight}kg \n My height is: {height}m \n My BMI is: {bmi} \n I am {am_i_good(bmi)}"
print(bmi_calc())

### basic calculator function

def calc(x,y,z):
  if z == "*":
    return int(x*y)
  elif z=="/":
    return int(x/y)
  elif z =="+":
    return int(x+y)
  elif z == "-":
    return int(x-y)
print(calc(float(input("enter first number")), float(input("enter second number")),input("enter type of operation")))