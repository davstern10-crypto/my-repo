import cmath
from py_compile import main

def solve_cubic(a, b, c, d):
    """
    Solves ax^3 + bx^2 + cx + d = 0 using Cardano's Method.
    Returns a tuple of 3 roots (real or complex).
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 for a cubic equation.")

    # Convert coefficients to reduced/depressed form: t^3 + p*t + q = 0
    # x = t - b / (3*a)
    b_a = b / a
    c_a = c / a
    d_a = d / a

    p = c_a - (b_a ** 2) / 3
    q = (2 * (b_a ** 3)) / 27 - (b_a * c_a) / 3 + d_a

    # Cardano's formula components
    discriminant = (q / 2) ** 2 + (p / 3) ** 3
    
    # Complex square root of discriminant
    sqrt_disc = cmath.sqrt(discriminant)

    # Cube roots u and v
    u = cmath.exp(cmath.log(-q / 2 + sqrt_disc) / 3) if (-q / 2 + sqrt_disc) != 0 else 0
    v = cmath.exp(cmath.log(-q / 2 - sqrt_disc) / 3) if (-q / 2 - sqrt_disc) != 0 else 0

    # Cube roots of unity
    w1 = complex(-0.5, cmath.sqrt(3) / 2)
    w2 = complex(-0.5, -cmath.sqrt(3) / 2)

    # Roots for depressed cubic variable 't'
    t1 = u + v
    t2 = u * w1 + v * w2
    t3 = u * w2 + v * w1

    # Shift back to find x = t - b / (3*a)
    shift = b_a / 3
    x1 = t1 - shift
    x2 = t2 - shift
    x3 = t3 - shift

    # Clean up small imaginary parts caused by floating-point precision
    return tuple(clean_complex(root) for root in (x1, x2, x3))


def clean_complex(val, tol=1e-10):
    """Removes negligible real/imaginary parts due to floating-point rounding."""
    real = val.real if abs(val.real) > tol else 0.0
    imag = val.imag if abs(val.imag) > tol else 0.0
    if imag == 0:
        return round(real, 6)
    return complex(round(real, 6), round(imag, 6))


# --- Interactive Command Line App ---
if __name__ == "__main__":
    print("=== Cubic Equation Solver (ax³ + bx² + cx + d = 0) ===")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        d = float(input("Enter coefficient d: "))

        roots = solve_cubic(a, b, c, d)

        print("\nThe solutions are:")
        for idx, root in enumerate(roots, start=1):
            print(f"  x{idx} = {root}")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    # Call main with 4 custom numbers (e.g., 1, 0, 0, -1)
    main()

