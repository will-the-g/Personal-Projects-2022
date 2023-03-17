


x = "01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101"
Base64 = {
    0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22: 'W', 23:	'X', 24:'Y', 25:'Z', 
    26:'a', 27:'b', 28:'c', 29:'d', 30:'e', 31:'f', 32:'g', 33:'h', 34:'i', 35:'j', 36:'k', 37:'l', 38:'m', 39:'n', 40:'o', 41:'p', 42:'q',43:'r', 44:'s', 45:'t', 46:'u', 47:'v', 48:'w', 49:'x', 50:'y', 51:'z',
    52:	'0', 53:'1', 54:'2', 55:'3', 56:'4', 57:'5', 58:'6', 59:'7', 60:'8', 61:'9', 62:'+', 63:'/',
}
ReverseBase64 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,'T': 19, 'U': 20,
'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30,
'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40,
'p': 41, 'q': 42, 'r': 43, 's': 44,'t': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51,
 '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63}
Hexadecimal = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
Alphabet = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26, ' ': 100}
AlphabetReverse = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z', 0: 'z'}
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Morsecode = {"A":"._","N":"_.","B":"_...","O":"___",	 "C":"_._.","P":".__.",	 "D":"_..","Q":"__._",	 "E":".","R":"._.",	 "F":".._.","S":"...",	 "G":"__.","T":"_",	 "H":"....","U":".._",	 "I":"..","V":"..._",	 
 	"J":".___","W":".__","K":"_._","X":"_.._",	 "L":"._..","Y":"_.__",	 "M":"__","Z":"__..","1":".____","6":"_....",	 "2":"..___","7":"__...",	 "3":"...__","8":"___..",	 "4":"...._","9":"____.",	 "5":".....",
    "0":"_____"," ":"/","?":"..__..",";":"_._._.",	 ":":"___...","/":"_.._.",	 "-":"_...._","\'":".____.",	 "\"":"._.._.","(":"_.__.",")":"_.__._",	 "=":"_..._","+":"._._.",	 "*":"_.._", "@":".__._.",
    "Á":".__._","Ä":"._._", "É":".._..","Ñ":"__.__", "Ö":"___.","Ü":"..__" }
ReverseMorseCode = {'._': 'A', '_.': 'N', '_...': 'B', '___': 'O', '_._.': 'C', '.__.': 'P', '_..': 'D', '__._': 'Q', '.': 'E', '._.': 'R', '.._.': 'F', '...': 'S', '__.': 'G', '_': 'T', '....': 'H', '.._': 'U', '..': 'I', '..._': 'V', '.___': 'J', '.__': 'W', '_._': 'K', '_.._': '*', '._..': 'L', '_.__': 'Y', '__': 'M', '__..': 'Z', '.____': '1', '_....': '6', '..___': '2', '__...': '7', '...__': '3', '___..': '8', '...._': '4', '____.': '9', '.....': '5', '_____': '0', '/': ' ', '..__..': '?', '_._._.': ';', '___...': ':', '_.._.': '/', '_...._': '-', '.____.': "'", '._.._.': '"', '_.__.': '(', '_.__._': ')', '_..._': '=', '._._.': '+', '.__._.': '@', '.__._': 'Á', '._._': 'Ä', '.._..': 'É', '__.__': 'Ñ', '___.': 'Ö', '..__': 'Ü', '':''}

def decode_binary_string(s):
    y = ''
    for char in range(len(s)):
        if s[char] == "0" or s[char] == "1":
            y+=s[char]
    return ''.join(chr(int(y[i*8:i*8+8],2)) for i in range(len(y)//8))
s = '111001101100011011011110111001001110000011010010110111101101110'

def decode_base64_string(s):
    equal = 0
    if '=' in s:    
        s = s.replace('=','')
        equal += 1
    decimal = []
    for char in range(len(s)):
        decimal.append(ReverseBase64[s[char]])
    binary = []
    for num in range(len(decimal)):
        binary.append(bin(decimal[num]).replace('b', ''))
    for i in range(len(binary)):
        length = 8 - len(binary[i])
        for s in range(length):
            binary[i] = '0' + binary[i]
    output = ''.join(binary[t][2:] for t in range(len(binary)))
    return decode_binary_string(output)

def decode_hexadecimal_string(s):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    output = 0
    for char in range(len(s)):
        if s[char] not in numbers:
            num = Hexadecimal[s[char]]
            output += (num * (16 ** (len(s) - (char + 1))))
        else:
            output += (int(s[char]) * (16 ** (len(s) - (char + 1))))
    return decode_binary_string('0' + bin(output)[2:])

def ascii_addition(s, x):
    num = []
    for char in range(len(s)):
        num.append(ord(s[char]) + x)
    return ''.join(chr(num[number]) for number in range(len(num)))

def decode_ceaser_cihper(s, rotations):
    chunks = s.split(' ')
    outputChunks = []
    for chunk in range(len(chunks)):
        nums = []
        for char in range(len(chunks[chunk])):
            nums.append(Alphabet[chunks[chunk][char]])
        list1 = []
        for number in nums:
            list1.append(number + rotations)
        outputChunks.append(''.join(AlphabetReverse[list1[number1] % 26] for number1 in range(len(list1))))    
    return ' '.join(outputChunks[chunky] for chunky in range(len(outputChunks)))

def decode_atbash(s):
    chunks = s.split(' ')
    outputChunks = []
    for chunk in range(len(chunks)):
        nums = []
        for char in range(len(chunks[chunk])):
            nums.append(Alphabet[chunks[chunk][char]])
        print(nums)
        list1 = []
        outputChunks.append(''.join(alpha[0 - nums[number1]] for number1 in range(len(nums))))
    return ' '.join(outputChunks[chunky] for chunky in range(len(outputChunks)))

def decode_morsecode(s):
    s = s.replace('-', '_')
    chunks = s.split('/')
    output = []
    for chunk in range(len(chunks)):
        chunkychunks = chunks[chunk].split(' ')
        for chunkychunkychunks in range(len(chunkychunks)):
            output.append(ReverseMorseCode[chunkychunks[chunkychunkychunks]])
    return ''.join(output[char] for char in range(len(output)))


encryption = {'a':'g','b':'p','c':'m','d':'b','e':'q','f':'z','g':'u','h':'a','i':'r','j':'c','k':'h','l':'w','m':'o','n':'x','o':'f','p':'k','q':'v','r':'d','s':'j','t':'l','u':'y','v':'e','w':'s','x':'t','y':'i','z':'n','1':'7','2':'4','3':'5','4':'0','5':'1','6':'9','7':'8','8':'2','9':'3','0':'6'}
print(encryption.keys())
