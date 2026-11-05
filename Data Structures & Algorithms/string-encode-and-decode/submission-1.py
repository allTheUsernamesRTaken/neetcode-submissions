class Solution:

    def encode(self, strs: List[str]) -> str:
        output=[]#separate each by ; no need for starting even
        #so "ab;",";l"  can be 3;ab;2;;l //note ; doesnt cause problems cuz nums are continuous
        for chunk in strs:
            output.append(str(len(chunk))+";") 
            output.append(chunk)
        output = "".join(output)
        return output



    def decode(self, s: str) -> List[str]:
        output = []
        index = 0
        curlen = []
        temp = []
        #2;34    length = 2, i=1, [2,3]
        #"4;neet4;code4;love3;you"
        #  1[2:7]
        while(index<len(s)):
            char = s[index]
            if(char ==";"):
                length = int("".join(curlen))
                curlen = []
                output.append(s[index+1:index+length+1])
                index +=length+1
            else:
                curlen.append(char)
                index+=1
        return output