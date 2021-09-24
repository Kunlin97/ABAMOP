import pandas as pd
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable,GLPK

df = pd.read_excel('DEA Formulation.xlsx', header=0)

#print(df)


def efficiency_score(branch):

    L=branch[1]
    D=branch[2]
    E=branch[3]
    F=branch[4]


    oD = LpVariable(name="oD", lowBound=0)
    oL = LpVariable(name="oL", lowBound=0)
    iE = LpVariable(name="iE", lowBound=0)
    iF = LpVariable(name="iF", lowBound=0)

    # Add the constraints to the model
    model = LpProblem(name="DEA_Formulation", sense=LpMaximize)
    for index, row in df.iterrows():
        model +=  (row[1]*oL+row[2]*oD-row[3]*iE-row[4]*iF <=0, 'constraint.{i}'.format(i=index))
    model += ((E*iE+F*iF) == 1, "input_scaling")
    # Add the objective function to the model
    obj_func = L*oL+D*oD
    model += obj_func

    # Solve the problem
    model.solve()

    #print(pulp.LpStatus[model.status])

    for variable in model.variables():
        # print('{name}={value}'.format(name=variable.name, value=variable.varValue)) # print the optimal values of all variables
        # find optimal var values used to calculate optimized objective function value.
        if variable.name=='oL':
            oLo=variable.varValue
        if variable.name=='oD':
            oDo=variable.varValue
    return L*oLo+D*oDo # return the value of the objective function

#branch= pd.array(df.loc[1])
#print('Branch:',branch)
#efficiency_score(branch)

result=df.apply(efficiency_score, axis=1)
print(result)