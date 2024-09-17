class Bitboard:
    def __init__(self, bits_str): 
        self.bit_array = list(map(int , list(bits_str)))
        self.bits = eval(f"0b{bits_str}")  
    def zeros(self):
        self.bits, self.bit_array = self.mask(0,64)
    def ones(self):
        self.bits, self.bit_array = self.mask(1, 64)
    def mask(self,mask_to, n):
        if mask_to == 0:
            self.bits = 0b0
        else:
            self.bits = 2**n - 1
        self.bit_array = [mask_to]*n 
        return self.bits, self.bit_array
    def invert_bit(self,k):
        mask = 1 << k
        self.bits ^= mask  
        self.bit_array[k] ^=  1   