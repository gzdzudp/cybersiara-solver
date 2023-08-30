# cybersiara-solver

![alt text](https://github.com/gzdzudp/cybersiara-solver/blob/edf18dd49cce455fe2e57f3824fb5ac451e0f6e8/imglol.png)

An nn captcha requests based solver
if you want you can spam https://www.cybersiara.com/book-a-demo with the solver

usage:

```
from solver import CybersiaraSolver

if __name__ == "__main__":
    solver = CybersiaraSolver(url="https://www.cybersiara.com/book-a-demo" masterurlid="OXR2LVNvCuXykkZbB8KZIfh162sNT8S2")

    print(solver.solvecap().get("data"))
```
