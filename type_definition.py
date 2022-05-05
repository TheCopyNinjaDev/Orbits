def type_definition(e: float) -> str:
    if e == 0:
        return "circular"
    elif 0 < e < 1:
        return "elliptical"
    elif e == 1:
        return "parabolic"
    elif 1 < e < float('inf'):
        return "hyperbolic"
    elif e == float('inf'):
        return "rectilinear"
    elif e <= 0:
        raise Exception("Incorrect value")


print(type_definition(0.4))