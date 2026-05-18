class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "%" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # print(s)
        res = []
        pointer = 0
        while pointer < len(s):
            text_begin = pointer
            while s[text_begin] != "%":
                text_begin += 1
            length = int(s[pointer:text_begin])
            text = s[text_begin+1:text_begin+length+1]
            res.append(text)
            pointer = text_begin+length+1
        return res