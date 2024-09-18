def zeros():
    #returns all bits set 0
    return 0
def ones(n):
    #returns n number of bits, all set to 1
    return 2**n - 1
def nthbitone(k):
    #returns bits with all bits as 0 except the kth bit as 1, with k being 0 >= k >= 63 
    if k < 64:
        return 1 << k
    return 0
def nthbitzero(k):
    #returns all bits as 1 except the kth bit as 0, with k being 0 >= k >= 63
    if k < 64:
        return 0xffffffffffffffff ^ (1<<k)
    return 0xffffffffffffffff
mask_config = {'zs':  zeros,'os':ones,'nb':nthbitone,'nz':nthbitzero}
def mask(mode, *args):
   if mode in mask_config:
        return mask_config[mode](*args)
class bitboard:
    def __init__(self): 
        self.bits = 0
    
    def emptyboard(self):
        self.bits = mask('zs')

    def fullboard(self):
        self.bits = mask('os',64)

    def create(self, bits):
        if type(bits) == int:
            #set bits to bits as is
            assert(bits<=0xffffffffffffffff), "bitboard can contain at most 64 elements"
            self.bits = bits
        elif type(bits) == str:
            #the left most bit will be considered the most significant bit
            assert(len(bits)<=64), "bitboard can contain at most 64 elements"
            self.bits = eval(f"0b{bits}")
        elif type(bits) == list:
            #bit[0] will be the least significant bit
            assert(len(bits)<=64), "bitboard can contain at most 64 elements"
            value = 0
            for i in range(len(bits)):
                assert bits[i] == 1 or bits[i] == 0, f"Invalid Input: a bit can only be {int} assigned as 1 or 0, got {bits[i]!r},"
                value += 2**i if bits[i] == 1 else 0    
            self.bits = value

    def invert_bit(self, k:int):
        self.bits ^= mask('nb',k) 
        
    def set_bit(self, k:int):
        self.bits |= mask('nb',k)

    def clear_bit(self, k:int):
        self.bits &= mask('nz',k)

    def get_bit(self, k:int) -> int:
        return 1 & self.bits >> k
    def set_to(self, bit:int, value:int):
        if value == 1:
            self.set_bit(bit)
        elif value == 0:
            self.clear_bit(bit)

    def __str__(self) -> str:
        return bin(0xffffffffffffffff-~self.bits)[3:]
    def __repr__(self) -> str:
        return f"{type(self).__name__}[{self.__str__()}]"

a = bitboard()