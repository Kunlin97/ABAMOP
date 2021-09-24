from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="Utility Company", sense=LpMinimize)

# Initialize the decision variables
XA = LpVariable(name="XA", lowBound=0,)
XB = LpVariable(name="XB", lowBound=0,)

# Add the constraints to the model
model += (10*XA >= 4000, "demand_active")
model += (XB >= 50, "demand_inactive")
model += (XA +XB <= 10*24*7, "time_constraint")

# Add the objective function to the model
obj_func = (7575-3*XA-2.5*XB-2*(XA+XB-40*10))/7575 + (XA+XB-40*10-50)/50
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")