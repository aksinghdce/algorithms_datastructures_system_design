import operator
from collections import OrderedDict
class LongestSWR():
    '''Return the longest substring without repeating characters'''
    def __init__(self, inputstr:str):
        '''Initialize the input string'''
        self.input = list(inputstr)
    def answer(self):
        '''Returns lnogest substring without repeating character from self.input'''
        s = self.input
        if len(s) <= 1:
            return len(s)
        results_dict:OrderedDict = OrderedDict()
        char_count:int = 0
        substr_list:list = list()
        #slide a window from left to right
        i:int = 0
        j:int = i
        iter_count:int = 0
        while i <= j and j < len(s) and iter_count < len(s):
            if s[j] not in s[i:j]:
                char_count += 1
            else:
                results_dict[str(s[i:j])] = char_count
                #two possible cases at this stage. Case 1: s[i] == s[j], Case 2: s[j-1] == s[j]
                if s[i] == s[j]:
                    i += 1
                    j -= 1 #because j will be incremented at the end of the loop
                    char_count -= 1 #because i got incremented
                if s[j-1] == s[j]:
                    i = j
                    char_count = 1
            j += 1
            iter_count += 1
        results_dict[str(s[i:j])] = char_count
        sorted_results = sorted(results_dict.items(), key=lambda x:x[1])
        return sorted_results[-1][1] if len(sorted_results) > 0 else 0

if __name__ == '__main__':
    #lswr = LongestSWR("dvdf")
    #lswr = LongestSWR(" ")
    #lswr = LongestSWR("pwwkew")
    lswr = LongestSWR("bbbbb")
    print(lswr.answer())