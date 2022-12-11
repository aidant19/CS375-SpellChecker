'''
CS375 Project 4
Aidan Tokarski, Cynthia Zafris,
Eda Wright, Xavier Markowitz

This program explores different edit distance algorithms
and a spell spell checker. 

Usage:
#TODO add usage for each example


'''



def editDistance_rec(S,T):
    '''
    TODO add docstring with I/O
    '''
    if S == '':
        return len(T) 
    if T == '':
        return len(S)
    if S[-1] == T[-1]:
        return editDistance_rec(S[:-2],T[:-2]) 
    return 1 + min( editDistance_rec(S[:-2],T[:-2]), 
                    editDistance_rec(S[:-2],T[:-1]),
                    editDistance_rec(S[:-1],T[:-2]) ) 


def editDistance_iter(S,T):
    '''
    TODO add docstring with I/O
    '''
    pass


def spellCheck(T, D):
    '''
    Input: A sting of text T to be spell checked. A dictionary D of correctly spelled words.

    Output: For every word w in T that does not occour in D, 5 words in D with minimal edit distance.
    These will be returned as a dictionary with the w as the key and the value a list of spelling suggestions.
    '''
    out = {} #Output dictionary
    words = T.lower().split() 
    for word in words:
        if word not in D:
            out[word] = findSuggestions(word, D)
    return out


def findSuggestions(word, D):
    '''
    Input: A mispelled word, a dictionary of ccorrectly spelled words D

    Output: Returns a list of 5 words from D with the closest edit distance to word. If there is a tie, the word
    that appears in D first is valued closer to the word.
    '''
    out = [] #Output list
    editDistances = [1e10, 1e10, 1e10, 1e10, 1e10] #keeps track of the 5 smallest edit distances so far
    for d in D:
        editDistance = editDistance_iter(d, word)
        k = 5 #index where new word should be inserted
        while k > 0 or editDistance < editDistances[k-1]:
            k -= 1 #d belongs higher in the list
        #Inserting d and edit distance into their lists
        out.insert(k, d)
        editDistance.insert(k, editDistance)
        #Trimming list to sill be 5 long
        out = out[:5]
        editDistances = editDistance[:5]
    return out





if __name__ == "__main__":
    print(editDistance_rec("analysis", "algotithms"))

