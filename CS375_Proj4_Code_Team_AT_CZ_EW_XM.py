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
        return editDistance_rec(S[:-1],T[:-1]) 
    return 1 + min( editDistance_rec(S[:-1],T[:-1]), 
                    editDistance_rec(S[:-1],T),
                    editDistance_rec(S,T[:-1]) ) 



def editDistance_iter(S,T):
    '''
    TODO add docstring with I/O
    '''
    m = len(S)
    n = len(T)

    grid = []
    for i in range(m + 1): # rows: S, using m
        grid.append([])
        for j in range(n + 1): # columns: T, using n
            grid[i].append(0)  

    for i in range(1,m + 1): # base case for rows
        grid[i][0] = i  
    
    for j in range(1,n + 1): # base case for columns
        grid[0][j] = j

    for i in range(1, m + 1): # all but the first row / first column
        for j in range(1, n + 1): 
            if S[i - 1] == T[j - 1]: # if specified letters in S and T are the same
                grid[i][j] = grid[i - 1][j - 1] 
            else: # if specified letters in S and T are not the same
                grid[i][j] = 1 + min( 
                                grid[i - 1][j - 1],
                                grid[i - 1][j],
                                grid[i][j - 1]
                            ) 

    for i in range(m + 1): # printing out grid
        print(grid[i])  
    
    return grid[m][n]


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
    print(editDistance_rec("analysis", "algorithm"))


