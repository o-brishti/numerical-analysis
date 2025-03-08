import math

def newton_raphson(f, df, x0, max_iterations = 100, tol = 1e-5):

    x = x0
    for _ in range(max_iterations):

        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")

        h = -(fx / dfx)

        if abs(h) < tol:
            return x
            
        x += h

    raise RuntimeError(f"Newton-Raphson method didn't converge. Best estimate: {x}")

def bisection(a, b, f, max_iterations = 100, tol = 1e-5):

    if f(a) * f(b) >= 0:
        raise ValueError("Incorrect Endpoints: f(a) and f(b) must have opposite signs")

    if f(a) == 0:
        return a
        
    if f(b) == 0:
        return b 

    for _ in range(max_iterations):

        c = (a + b) / 2
        fc = f(c)

        if fc == 0 or abs(fc) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c

        else:
            a = c
    
    raise RuntimeError(f"Bisection method didn't converge. Best estimate: {(a + b) / 2}")
        
    
    
