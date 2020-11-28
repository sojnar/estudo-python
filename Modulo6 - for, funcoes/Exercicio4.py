jose = 'entrou 6h'
def fatec():
    global jose
    jose = 'entrou 8h'
    print(jose)

print(jose)
fatec()
print(jose)