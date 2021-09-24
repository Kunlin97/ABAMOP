from pulp import LpMinimize, LpProblem, LpStatus, LpVariable

# Create the model
model = LpProblem(name="Susan Lovett", sense=LpMinimize)

# Initialize the decision variables
X1 = LpVariable(name="X1", lowBound=0, cat='Integer')
X2 = LpVariable(name="X2", lowBound=0, cat='Integer')
X3 = LpVariable(name="X3", lowBound=0, cat='Integer')
X4 = LpVariable(name="X4", lowBound=0, cat='Integer')
X5 = LpVariable(name="X5", lowBound=0, cat='Integer')
X6 = LpVariable(name="X6", lowBound=0, cat='Integer')
dD1 = LpVariable(name="dD1", lowBound=0)
dD2 = LpVariable(name="dD2", lowBound=0)
dC1 = LpVariable(name="dC1", lowBound=0)
dC2 = LpVariable(name="dC2", lowBound=0)
dL1 = LpVariable(name="dL1", lowBound=0)
dL2 = LpVariable(name="dL2", lowBound=0)
dF1 = LpVariable(name="dF1", lowBound=0)
dF2 = LpVariable(name="dF2", lowBound=0)

# Add the constraints to the model
model += (X1+X2+X3+X4+X5+X6+dD1-dD2 == 50000, "demand_constraint")
model += (3*X1+3.5*X2+4*X3+4.5*X4+5*X5+6*X6+dC1-dC2 == 250000, "cost_constraint")
model += (0.25*X1+0.3*X2+0.15*X3+0.2*X4+0.4*X5+0.05*X6+dL1-dL2 == 0, "late_constraint")
model += (0.4*X1+0.35*X2+0.3*X3+0.25*X4+0.2*X5+0.05*X6+dF1-dF2 == 0, "defect_constraint")

# Add the objective function to the model
obj_func = dD1+dD2+dC1+dC2+dL1+dL2+dF1+dF2
model += obj_func

# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")

print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
