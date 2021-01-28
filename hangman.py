"""
╦ ╦┌─┐┌┐┌┌─┐┌┬┐┌─┐┌┐┌
╠═╣├─┤││││ ┬│││├─┤│││
╩ ╩┴ ┴┘└┘└─┘┴ ┴┴ ┴┘└┘
"""

# initializing hangman
hm = []

def hangman(n):
    '''
    Returns hangman, taken n - the number of wrong answers
    n is the number of times the answer was wrong
    '''
    global hm
    
    # col
    c = 9
    # face
    if n == 0:
        hm = [['' for i in range(9) ] for j in range(9)]
    if n == 1:
        hm[0][c//2] = "_"
        hm[1][c//2-1:c//2+1] = ["/", " ", "\\"]
        hm[2][c//2-1:c//2+1] = ["\\", "_", "/"]
    if n == 2:
        hm[3][c//2] = "|"
        hm[4][c//2] = "|"
        hm[5][c//2] = "|"
    if n == 3:
        hm[4][c//2-1] = "/"
        hm[5][c//2-2] = "/"
        hm[4][c//2+1] = " "
        hm[5][c//2+2] = " "
    if n == 4:
        hm[4][c//2+1] = "\\"
        hm[5][c//2+2] = "\\"
    if n == 5:
        hm[6][c//2-1] = "/"
        hm[7][c//2-2] = "/"
    if n == 6:
        hm[6][c//2] = "\\"
        hm[7][c//2+1] = "\\"
    
    return hm




    
