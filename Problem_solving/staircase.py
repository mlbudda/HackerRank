# Staircase

def staircase(n):
    stairs = 1
    while n > 0:
        print((n-1)*' '+(stairs*'#'))
        n -= 1
        stairs += 1


staircase(6)
"""    
     #
    ##
   ###
  ####
 ##### 
###### 
"""