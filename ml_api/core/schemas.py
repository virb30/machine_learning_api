from ninja import Schema


class Values(Schema):
    crim: float
    zn: float
    indus: float
    chas: float
    nox: float
    rm: float
    age: float
    dis: float
    rad: float
    tax: float
    ptratio: float
    b: float
    lstat: float


class Input(Schema):
    values: Values
