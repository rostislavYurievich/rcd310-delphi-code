import sys
def getCode(data):
    return str(hex(data ^ 0x65656565))[2::2].zfill(4)


if __name__ == "__main__":
    _bytes =0
    if len(sys.argv)!=2:
        print("USAGE:\npython rcd310.py BINARY_DUMP_FILE")
        exit(1)
    with open(sys.argv[1], "rb") as f:
        f.seek(160,1)
        _bytes =f.read(4)
    _hex = int(_bytes.hex(),16)
    print(getCode(_hex))
