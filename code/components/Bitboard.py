def zeros():
    #returns all bits set 0
    return 0
def ones(n):
    #returns n number of bits, all set to 1
    return 2**n - 1
def nthbitone(k):
    #returns bits with all bits as 0 except the kth bit as 1, with k being 0 <= k <= 63 
    if k < 64:
        return 1 << k
    return 0
def nthbitzero(k):
    #returns all bits as 1 except the kth bit as 0, with k being 0 <= k <= 63
    if k < 64:
        return 0xffffffffffffffff ^ (1<<k)
    return 0xffffffffffffffff
mask_config = {'zs':  zeros,'os':ones,'nb':nthbitone,'nz':nthbitzero}
def mask(mode, *args):
   if mode in mask_config:
        return mask_config[mode](*args)
class bitboard:
    def __init__(self,bits=0): 
        self.make(bits)
    
    def emptyboard(self):
        self.bits = mask('zs')

    def fullboard(self):
        self.bits = mask('os',64)

    def make(self, bits):
        if type(bits) == int:
            #set bits to bits as is
            assert(bits<=0xffffffffffffffff), f"Invalid Input: {type(self).__name__} can contain at most 64 elements"
            self.bits = bits
        elif type(bits) == str:
            #the left most bit will be considered the most significant bit
            assert(len(bits)<=64), f"Invalid Input: {type(self).__name__} can contain at most 64 elements"
            self.bits = eval(f"0b{bits}")
        elif type(bits) == list:
            #bit[0] will be the least significant bit
            assert(len(bits)<=64), f"Invalid Input: {type(self).__name__} can contain at most 64 elements"
            value = 0
            for i in range(len(bits)):
                assert bits[i] == 1 or bits[i] == 0, f"Invalid Input: A bit can only be {int} assigned as 1 or 0, got {bits[i]!r},"
                value += 2**i if bits[i] == 1 else 0    
            self.bits = value
    def fill(self,start=None,end=None):
        start = 0 if start == None else start
        end = len(bin(self.bits)[2:]) if end == None else end
        return self.bits | 2**(end) - 2**(start)
    def invert_bit(self, k:int):
        self.bits ^= mask('nb',k) 
    def set_bit(self, k:int):
        self.bits |= mask('nb',k)
    def clear_bit(self, k:int):
        self.bits &= mask('nz',k)
    def __setitem__(self,index,data):
        assert(index < 64), f"IndexError: {type(self).__name__} assignment index out of range"
        self.bits = (self.bits & ~(data<<index)) | data<<index
    def __getitem__(self, index):
        assert(index < 64), f"IndexError: {type(self).__name__} index out of range"
        return 1 & (self.bits >> index)
    def __str__(self) -> str:
        return bin(0xffffffffffffffff-~self.bits)[3:]
    def __repr__(self) -> str:
        return f"{type(self).__name__}(Decimal:{self.bits},Hex:{hex(self.bits)},Binary:{self.__str__()})"