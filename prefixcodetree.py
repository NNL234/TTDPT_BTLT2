import binascii

class Node(object):
    def __init__(self,codeword = '',symbol = None):
        self.codeword = codeword
        self.symbol = symbol

class PrefixCodeTree:
    def __init__(self):
        self.tree = {}

    def insert(self,codeword,symbol):
        index = 0
        for i in range(len(codeword)):
            index = index * 2 + codeword[i] + 1
        
        self.tree[str(index)] = Node(codeword,symbol)

    def find(self,codeword) :
        index = 0
        for i in range(len(codeword)):
            
                index = index * 2 + codeword[i] + 1
        for index_node in self.tree:
            if(index_node == str(index)):
                return self.tree[str(index)].symbol

        return None

    

    def decode(self,encodedData,datalen):
        binCode =bin(int(binascii.hexlify(encodedData).decode('utf8'),16))[2:]
        print(binCode)
        result =''
        current_start_index = 0
        length = 0
        current_codeword = []
        while(current_start_index+ length < datalen):
            while(self.find(current_codeword) == None):
                length +=1
                current_codeword = list_bits(binCode[current_start_index:current_start_index+ length])
            result += self.find(current_codeword)
            current_start_index = current_start_index+ length
            length = 0
            current_codeword =[]
        
        return result


def list_bits(codeword):
        result = []
        for i in range(len(codeword)):
            if codeword[i] == '0':
                result.append(0) 
            else :
                result.append(1)
        return result




