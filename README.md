# Block scoping in python
Just to be clear, I made this as a joke.

```python
import block_scoping as bs

def main():
    x = 7
    with bs():
        y = x + 4
        print(f'y: {y}') # y: 11
        x -= 3

    print('x: {x}') # x: 4
    print('y: {y}') # UnboundLocalError

main()
```
