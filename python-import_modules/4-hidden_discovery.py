#!/usr/bin/python3
import hidden_4

def main():
    pyc_path = "./hidden_4.pyc"

    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)

    hidden_4 = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(hidden_4)

    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()
