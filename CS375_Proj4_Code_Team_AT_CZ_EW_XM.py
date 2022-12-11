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
    elif T == '':
        return len(S)
    elif S[len(S) - 1] == T[len(T) - 1]:
        return editDistance_rec(S[:len(S) - 2],T[:len(T) - 2]) 
    else:
        return 1 + min( editDistance_rec(S[:len(S) - 2],T[:len(T) - 2]), 
                        editDistance_rec(S[:len(S) - 2],T[:len(T) - 1]),
                        editDistance_rec(S[:len(S) - 1],T[:len(T) - 2]) )


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
    pass

