import bitboard as b

test_cases = [
        ("",0),
        ("0b0101010101010101001",174761),
        ("0xffffffffffffffff",18446744073709551615),
        ("0x10000000000000000",None),
        ("-1",None),
        ("[1]*65",None),
        ("\"0x2c10a3002094000\"",198451059889881088),
        ("0x2c10a3002094000",198451059889881088),
        ("\"-0o13010243000202240000\"",None),
        ("\"0o13010243000202240000\"",198451059889881088),
        ("0b0000001011000001000010100011000000000010000010010100000000000000",198451059889881088),
        ("\"0b0000001011000001000010100011000000000010000010010100000000000000\"",198451059889881088),
        ("\"0000000000000010100100000100000000001100010100001000001101000000\"",198451059889881088),
        ("['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0']",None),
        ("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]",198451059889881088)
]

def test(input1, expected_output):
    result = None
    print("----------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        if input1 == "":
            result = b.bitboard().bits
        else:
            get_in = eval(input1)
            result = b.bitboard(get_in).bits
    except Exception as error:
        print(error)

    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False
def main():
    passed = 0
    failed = 0 
    for case in test_cases:
        correct = test(*case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")
    print("===============================")
    print("Setting and Getting Bits")
    print("===============================")
    myboard = b.bitboard(0x2c10a3002094000)
    print(f"board before: {myboard}")
    print(f"index 17: {myboard[17]}")
    myboard[17] = 1
    print(f"changed value to: {myboard[17]}")
    print(f"board: {myboard}")
main()
