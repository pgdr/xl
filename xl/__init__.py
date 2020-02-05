import pandas as pd
def read_excel(fname):
    df = pd.read_excel(fname)
    return '\n'.join(list(df.columns))

def main():
    import sys
    fname = sys.argv[1]
    print(read_excel(fname))
