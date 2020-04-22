

"""
    glasstext.write algorithm
        plain text -> decimal -> binary -> whitespace

    glasstext.read algorithm
        whitespace -> binary -> decimal -> plain text

    from glasstext import glass
    glass(glass).read()
    glass(text,True).write()

    glass.read( text, rotate )
    glass.write( text, rotate )

    glasstext.read()
"""


class __glass:
    def __init__( self, rotate=False ):
        self.sep = chr(173)
        self.std = [" ", "\t"]
        if rotate: self.std = ["\t", " "]



    def _StrToDec( self, text ):
        # Convert string to decimal
        result = []
        for i in text:
            result.append(ord(i))

        return result



    def _DecToStr( self, decimals ):
        # convert decimal to string
        return ''.join(list(map(chr, decimals)))



    def _DecToBin( self, decimals ):
        # convert decimal to binary
        result = []
        for i in decimals:
            result.append(bin(i)[2:])

        return result



    def _BinToDec( self, binary ):
        # convert binary to decimal
        binary = int(binary)
        decimal = 0
        power = 0
        while binary > 0:
            decimal += 2 ** power * (binary % 10)
            binary //= 10
            power += 1
        
        return decimal



    def _BinToWspace( self, binary ):
        # convert binary to whitespace
        result = []
        for i in binary:
            i = i.replace('0', self.std[0])
            i = i.replace('1', self.std[1])
            result.append(i)

        return self.sep.join(result)



    def _WspaceToBin( self, wspace ):
        # convert whitespace to binary
        wspace = wspace.split(self.sep)
        result = []
        for i in wspace:
            i = i.replace(self.std[0], '0')
            i = i.replace(self.std[1], '1')
            result.append(i)

        return result


        

def read( glasstext, rotate=False ):
    """
    reading a glasstext into a plain text
    """
    # whitespace -> binary -> decimal -> plain text
    r = __glass( rotate=rotate )

    # uncomment the print function to see the algorithm
    binary = r._WspaceToBin( glasstext )
    #print(binary)
    decimal = list(map(r._BinToDec, binary))
    #print(decimal)
    plaintext = r._DecToStr( decimal )
    #print(plaintext)

    return plaintext

def write( text, rotate=False ):
    # plain text -> decimal -> binary -> whitespace
    r = __glass( rotate=rotate )

    decimal = r._StrToDec(text)
    #print(decimal)
    binary = r._DecToBin(decimal)
    #print(binary)
    whitespace = r._BinToWspace(binary)
    #print(whitespace)

    return whitespace



def load( filename, rotate=False ):
    # whitespace -> binary -> decimal -> plain text
    glasstext = open(filename, 'r').read()
    r = __glass( rotate=rotate )

    binary = r._WspaceToBin( glasstext )
    decimal = list(map(r._BinToDec, binary))
    plaintext = r._DecToStr( decimal )

    return plaintext



def dump( text, filename, rotate=False ):
    # plain text -> decimal -> binary -> whitespace
    f = open(filename, 'w')
    r = __glass( rotate=rotate )

    decimal = r._StrToDec(text)
    binary = r._DecToBin(decimal)
    whitespace = r._BinToWspace(binary)

    f.write(whitespace)

