import decorator

@decorator.serious
def qualquer():
    return 'Qualquer função!'


x = qualquer()
print(x)