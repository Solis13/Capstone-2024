
def triangle_area(base,height):
    if base <0 or height <0:
        raise ValueError('Base and height must be 0 or positive')
    return base * height * 0.5
