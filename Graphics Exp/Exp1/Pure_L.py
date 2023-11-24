I = lambda x:x
K = lambda x : lambda y:x
S = lambda x:lambda y:lambda z: (x(z))(y(z))

TRUE = K 
FALSE = K(I)