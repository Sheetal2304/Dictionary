#Ek program likhiye jo ki nested dictionary me se
#  first key or value ko remove kare.
'''Dic= {
    #1: 'NAVGURUKUL',
    # 2: 'IN',  
  	# 3:
    #   { 'B' : 'To',
    #     'C' : 'DHARAMSALA'
    #    }
    # }'''
    
Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
Dic[3].pop('A')
print(Dic)

