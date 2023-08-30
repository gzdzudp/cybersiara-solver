from solver import CybersiaraSolver

if __name__ == "__main__":
    solver = CybersiaraSolver(url="https://www.cybersiara.com/book-a-demo", masterurlid="OXR2LVNvCuXykkZbB8KZIfh162sNT8S2")
    print(solver.solvecap().get("data"))
