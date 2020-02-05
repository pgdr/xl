import pandas as pd


def read_excel_file(fname):
    return pd.read_excel(fname)


def read_column_headers(fname):
    df = read_excel_file(fname)
    return list(df.columns)


def read_column(fname, col):
    df = read_excel_file(fname)
    return list(df[col])


def main():
    import sys

    if len(sys.argv) < 2:
        exit("usage: xl fname.xls [col]")

    fname = sys.argv[1]
    if len(sys.argv) == 3:
        print("\n".join(read_column(fname, sys.argv[2])))
    else:
        print("\n".join(read_column_headers(fname)))
