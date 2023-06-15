class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # encoded = [f'{len(s):04d}'+s for s in strs]
        # return ''.join(encoded)
        encoded = ''.join([f'{len(s):04d}{s}' for s in strs])
        return encoded
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        max_len = len(s)
        i = 0
        while i < max_len:
            str_len = int(s[i:i+4])
            i += 4
            result.append(s[i:i+str_len])
            i += str_len
        return result
        
        # res = []
        # i = 0
        # while i < len(s):
        #     num_c = int(s[i:i+4])
        #     i += 4
        #     res.append(s[i:i+num_c])
        #     i += num_c
        #     return ''.join(res)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))