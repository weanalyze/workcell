from workcell.core import get_callable
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("workcell_path", help="The path to the workcell.")
    args = parser.parse_args()
    func = get_callable(args.workcell_path)
    print("function name: ", func.__name__)