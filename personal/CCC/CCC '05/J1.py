day = float(input())
evening = float(input())
night = float(input())
plan_a = day - 100
plan_b = day- 250

if plan_a <= 0:
    plan_a = 0.15*evening + 0.2*night
else:
    plan_a = plan_a*0.25 + 0.15*evening + 0.2*night

if plan_b <= 0:
    plan_b = 0.35*evening + 0.25*night
else:
    plan_b = plan_b*0.45 + 0.35*evening + 0.25*night

print(f"Plan A costs {round(plan_a,2)}")
print(f"Plan B costs {round(plan_b,2)}")
if plan_a == plan_b: print("Plan A and B are the same price.")
elif plan_a < plan_b: print("Plan A is cheapest.")
elif plan_a > plan_b: print("Plan B is cheapest.")