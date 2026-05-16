# lets find out how much fix money do we spend in parlour per month



shutter_rent=12000
electricity_minimumCost=600
electricity_unit=int(input("Enter total electricity unit : "))
electricity_unitRate=13
total_electricity_bill=electricity_unit*electricity_unitRate
staff_salary=7000
flat_rent=4500
water_with_electricity=1000


Our_Total_fixed_cost=shutter_rent+electricity_minimumCost+total_electricity_bill+staff_salary+flat_rent+water_with_electricity

print(f"Our total fixed cost per month is {Our_Total_fixed_cost}.")