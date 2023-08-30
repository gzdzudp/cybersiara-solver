# cybersiara-solver

![alt text](https://github.com/gzdzudp/cybersiara-solver/blob/edf18dd49cce455fe2e57f3824fb5ac451e0f6e8/imglol.png)

# An nn captcha requests based solver
if you want you can spam https://www.cybersiara.com/book-a-demo with this funny solver

usage:

```
from solver import CybersiaraSolver

if __name__ == "__main__":
    solver = CybersiaraSolver(url="https://www.cybersiara.com/book-a-demo", masterurlid="OXR2LVNvCuXykkZbB8KZIfh162sNT8S2")
    print(solver.solvecap().get("data"))
```

# WARNING!

this code can be shit because i am bad dev. 

Dont bully me pls

# FUN FACT

they didnt add any obf for their .js backend files
