# really quick inference in two node graph. To check everything is working.

import opengm
gm = opengm.gm( [2,2] )

pottsFunction = opengm.pottsFunction([2,2],0.0,1.0)
pottsFunctionId = gm.addFunction(pottsFunction)
gm.addFactor(pottsFunctionId,[0,1])

Inf  = opengm.inference.BeliefPropagation
parameter = opengm.InfParam(steps=1000,damping=0.9,convergenceBound=0.001)
inf2 = Inf(gm,parameter=parameter)

inf2.infer()