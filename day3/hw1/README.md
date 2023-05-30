```
def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1
```
```
def read_multi(line, index):
    token = {'type': 'MULTI'}
    return token, index + 1
```