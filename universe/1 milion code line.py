with open("big_file.py", "w") as f:
    for i in range(1000000):
        f.write(f"print('Line {i}')\n")
