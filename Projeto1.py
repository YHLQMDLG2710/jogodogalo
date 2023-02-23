
def eh_tabuleiro(n):
    if isinstance(n,tuple) and len(n)==3:
        for i in range(3):
            if not isinstance(n[i],tuple) or not len(n[i])==3:
                return False
            for j in range(3):
                if not isinstance(n[i][j],int) or not n[i][j] in (1,-1,0):
                    return False
        return True
    else:
        return False
    
def eh_posicao(n):
    if isinstance(n,int) and n in (1,2,3,4,5,6,7,8,9):
        return True
    else:
        return False
    
def obter_coluna(tab,n):
    if not eh_tabuleiro(tab) or (not isinstance(n,int) or not n in (1,2,3)):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    else:
        return (tab[0][n-1],tab[1][n-1],tab[2][n-1])
    
def obter_linha(tab,n):
    if not eh_tabuleiro(tab) or (not isinstance(n,int) or not n in (1,2,3)):
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    else:
        return tab[n-1]   

def obter_diagonal(tab,n):
    if not eh_tabuleiro(tab) or (not isinstance(n,int) or not n in (1,2)):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    else:
        if (n==1):
            return (tab[0][0],tab[1][1],tab[2][2]) 
        else:
            return (tab[2][0],tab[1][1],tab[0][2]) 
        
def  tabuleiro_str(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')
    else:
        res=""
        for i in range(3):
            for j in range(3):
                res+=" "
                if tab[i][j]==1:
                    res+="X"
                if tab[i][j]==-1:
                    res+="O"
                if tab[i][j]==0:
                    res+=" "  
                res+=" "
                if j!=2:
                    res+="|"
            if i!= 2:
                res+="\n-----------\n"
        return res
                
def eh_posicao_livre(tab,n):
    if not eh_tabuleiro(tab) or (not isinstance(n,int) or not n in 
(1,2,3,4,5,6,7,8,9)):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    else:
        if n%3 ==0:
            return tab[(n//3)-1][2] ==0
        if n%3 ==1:
            return tab[(n//3)][0] ==0
        if n%3 ==2:
            return tab[(n//3)][1] ==0        
        
def obter_posicoes_livres(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    else:
        res=[]
        for i in range(3):
            for j in range(3):
                if tab[i][j] == 0:
                    if i==0:
                        res+=[j+1]
                    if i==1:
                        res+=[j+4]
                    if i==2:
                        res+=[j+7] 
        return tuple(res)
    
def jogador_ganhador(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')
    else:
        for i in range(3):
            c=obter_coluna(tab,i+1)
            l=obter_linha(tab,i+1)
            if c==(1,1,1) or l==(1,1,1):
                return 1;
            if c==(-1,-1,-1) or l==(-1,-1,-1):
                return -1;            
            
        for i in range(2):
            d=obter_diagonal(tab,i+1)
            if d==(1,1,1) :
                return 1;
            if d==(-1,-1,-1):
                return -1;            
        return 0
    
def marcar_posicao(tab, jog, n):
    if not eh_tabuleiro(tab) or not isinstance(n,int) or not eh_posicao_livre(tab,n) or not isinstance(jog,int) or not jog in (1,-1):   
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    else: 
        newtab= list(tab)
        for i in range(3):
            newtab[i]=list(tab[i])
        if n%3 ==0:
            newtab[(n//3)-1][2] =jog
        if n%3 ==1:
            newtab[(n//3)][0] =jog
        if n%3 ==2:
            newtab[(n//3)][1] =jog
        for i in range(3):
            newtab[i]=tuple(newtab[i])        
        return tuple(newtab)
    
def escolher_posicao_manual(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('escolher posicao manual: o argumento e invalido')
    else:
        n = eval(input("Turno do jogador. Escolha uma posicao livre: "))
        if not n in (1,2,3,4,5,6,7,8,9) or not eh_posicao_livre(tab,n):
            raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
        else:
            return n
        
def escolher_posicao_auto(tab, jog, mod):
    if not eh_tabuleiro(tab) or not isinstance(jog,int) or not jog in (1,-1) or not isinstance(mod,str) or not mod in ("basico","normal","perfeito"):
        raise ValueError('escolher posicao auto: algum dos argumentos e invalido')
    else:
        if mod=="basico":
            return mod_basico(tab)
        if mod=="normal":
            return mod_normal(tab,jog)
        if mod=="perfeito":
            return mod_perfeito(tab,jog)
        
def mod_basico(tab):
    ''' 5,7,8'''
    move=play5(tab)
    if move!=-1:
        return move
    else:
        move=play7(tab)
        if move != -1:
            return move
        else:
            move=play8(tab)
            if move != -1:
                return move   
            return -1
        
def mod_normal(tab,jog):
    ''' 1,2,5,6,7,8'''
    move=play1(tab,jog)
    if move!=-1:
        return move
    else:
        move=play2(tab,jog)
        if move != -1:
            return move
        else:
            move=play5(tab)
            if move != -1:
                return move   
            else:
                move=play6(tab,jog)
                if move != -1:
                    return move  
                else:
                    move=play7(tab)
                    if move != -1:
                        return move  
                    else:
                        move=play8(tab)
                        if move != -1:
                            return move   
                        else:
                            return -1
        
    
def mod_perfeito(tab,jog):
    ''' todos'''
    move=play1(tab,jog)
    if move!=-1:
        return move
    else:
        move=play2(tab,jog)
        if move != -1:
            return move
        else:
            move=play3(tab,jog)
            if move != -1:
                return move   
            else:
                move=play4(tab,jog)
                if move != -1:
                    return move  
                else:
                    move=play5(tab)
                    if move != -1:
                        return move  
                    else:
                        move=play6(tab,jog)
                        if move != -1:
                            return move   
                        else:
                            move=play7(tab)
                            if move != -1:
                                return move   
                            else:
                                move=play8(tab)
                                if move != -1:
                                    return move   
                                else:                                
                                    return -1    
            
def play1(tab,jog):
    for i in range(3):
        c=obter_coluna(tab,i+1)
        l=obter_linha(tab,i+1)
        if l==(jog,jog,0):
            return 3+3*i
        if l==(jog,0,jog):
            return 2+3*i
        if l==(0,jog,jog):
            return 1+3*i
        if c==(jog,jog,0):
            return 7+i
        if c==(jog,0,jog):
            return 4+i
        if c==(0,jog,jog):
            return 1+i        
    d1=obter_diagonal(tab,1)
    d2=obter_diagonal(tab,2)
    if d1==(jog,jog,0):
        return 9
    if d1==(jog,0,jog) or d2==(jog,0,jog):
        return 5
    if d1==(0,jog,jog):
        return 1
    if d2==(jog,jog,0):
        return 3
    if d2==(0,jog,jog):
        return 7 
    return -1
    

def play2(tab,jog):
    if jog==1:
        return play1(tab,-1)
    return play1(tab,1)

def play3(tab,jog):
    res=bifurcacoes(tab,jog)
    if res!=[]:
        return res[0]
    else:
        return -1
def bifurcacoes(tab,jog):
    res=[]
    livres=obter_posicoes_livres(tab)
    c1=obter_coluna(tab,1)
    l1=obter_linha(tab,1)
    c2=obter_coluna(tab,2)
    l2=obter_linha(tab,2)
    c3=obter_coluna(tab,3)
    l3=obter_linha(tab,3)    
    d1=obter_diagonal(tab,1)
    d2=obter_diagonal(tab,2)
    for i in livres:
        if i ==1 :
            if ((l1==(0,jog,0) or l1==(0,0,jog)) and (c1==(0,jog,0) or c1==(0,0,jog))):
                res+= [1]
            if ((l1==(0,jog,0) or l1==(0,0,jog)) and (d1==(0,jog,0) or d1==(0,0,jog))):
                res+= [1]
            if ((d1==(0,jog,0) or d1==(0,0,jog)) and (c1==(0,jog,0) or c1==(0,0,jog))):
                res+= [1]            
                
        if i==2 and ((l1==(jog,0,0) or l1==(0,0,jog)) and (c2==(0,jog,0) or c2==(0,0,jog))):
                res+= [2]  
                
        if i==3 :
            if ((l1==(0,jog,0) or l1==(jog,0,0)) and (c3==(0,jog,0) or c3==(0,0,jog))):
                res+= [3]  
            if (l1==(0,jog,0) or l1==(jog,0,0)) and ((d2==(0,jog,0) or d2==(jog,0,0))):
                res+=[3]
            if (c3==(0,jog,0) or c3==(0,0,jog)) and ((d2==(0,jog,0) or d2==(jog,0,0))):
                res+=[3]   
                
        if i==4 and ((l2==(0,jog,0) or l1==(0,0,jog)) and (c1==(0,jog,0) or c1==(0,0,jog))):
                res+= [4]
                
        if i==5 :
            #1
            if ((l2==(jog,0,0) or l2==(0,0,jog)) and (c2==(jog,0,0) or c2==(0,0,jog))):
                res+= [5]  
            #2
            if ((l2==(jog,0,0) or l2==(0,0,jog)) and (d1==(jog,0,0) or d1==(0,0,jog))):
                res+= [5]           
            #3
            if ((l2==(jog,0,0) or l2==(0,0,jog)) and (d2==(jog,0,0) or d2==(0,0,jog))):
                res+= [5]   
            #4
            if ((c2==(jog,0,0) or c2==(0,0,jog)) and (d1==(jog,0,0) or d1==(0,0,jog))):
                res+= [5]            
            if ((c2==(jog,0,0) or c2==(0,0,jog)) and (d2==(jog,0,0) or d2==(0,0,jog))):
                res+= [5]      
            if ((d1==(jog,0,0) or d1==(0,0,jog)) and (d2==(jog,0,0) or d2==(0,0,jog))):
                res+= [5]            
                    
        if i==6 and ((l2==(0,jog,0) or l1==(jog,0,0)) and (c3==(jog,0,0) or c3==(0,0,jog))):
                res+= [6]
        if i==7:
            if ((l3==(0,jog,0) or l3==(0,0,jog)) and (c1==(0,jog,0) or c1==(jog,0,0))):
                res+= [7]  
            if (l3==(0,jog,0) or l3==(0,0,jog)) and ((d2==(0,jog,0) or d2==(0,0,jog))):
                res+=[7]
            if (c1==(0,jog,0) or c1==(jog,0,0)) and ((d2==(0,jog,0) or d2==(0,0,jog))):
                res+=[7]             
        if i==8 and ((l3==(0,0,jog) or l1==(jog,0,0)) and (c2==(jog,0,0) or c2==(0,jog,0))):
                res+= [8]
        if i==9:
            if ((l3==(0,jog,0) or l3==(jog,0,0)) and (c3==(0,jog,0) or c3==(jog,0,0))):
                res+= [9]  
            if (l3==(0,jog,0) or l3==(jog,0,0)) and ((d1==(0,jog,0) or d1==(jog,0,0))):
                res+=[9]
            if (c3==(0,jog,0) or c3==(jog,0,0)) and ((d1==(0,jog,0) or d1==(jog,0,0))):
                res+=[9]              
    return res

def play4(tab,jog):
    res=[]
    if jog ==1:
        res=bifurcacoes(tab,-1)
        if len(res)==1:
            return res[0]
        else:
            mete=meter_dois(tab,jog)
            for i in mete:
                if not i in res:
                    return i
            return -1
            
    else:
        res=bifurcacoes(tab,1)
        if len(res)==1:
            return res[0]     
        else:
            mete=meter_dois(tab,jog)
            for i in mete:
                if not i in res:
                    return i
            return -1
        
def meter_dois(tab,jog):
    res=[]
    for i in range(3):
        l=obter_linha(tab,i+1)
        c=obter_coluna(tab,i+1)
        if l==(jog,0,0):
            res+=[3*i+2,3*1+3]
        if l==(0,jog,0):
            res+=[3*i+1,3*1+3]
        if l==(0,0,jog):
            res+=[3*i+2,3*1+1]        
        if c==(jog,0,0):
            res+=[4+i,7+i]
        if c==(0,jog,0):
            res+=[1+i,7+i]
        if c==(0,0,jog):
            res+=[4+i,1+i]
    d1= obter_diagonal(tab,1)
    d2= obter_diagonal(tab,2)
    if d1==(0,jog,0):
        res+=[1,9]
    if d2==(0,jog,0):
        res+=[3,7]
    if d1==(jog,0,0):
        res+=[5,9]
    if d2==(jog,0,0):
        res+=[5,3]
    if d1==(0,0,jog):
        res+=[1,5]
    if d2==(0,0,jog):        
        res+=[7,5]
    return res
        
        
def play5(tab):
    if eh_posicao_livre(tab,5):
        return 5
    else:
        return -1
    
def play6(tab,jog):
    d1=obter_diagonal(tab,1)
    d2=obter_diagonal(tab,2)
    if jog==1:
        if d1[0]==-1 and d1[2]==0:
            return 9
        if d1[0]==0 and d1[2]==-1:
            return 1;
        if d2[0]==-1 and d2[2]==0:
            return 3
        if d2[0]==0 and d2[2]==-1:
            return 7;        
    if jog==-1:
        if d1[0]==1 and d1[2]==0:
            return 9
        if d1[0]==0 and d1[2]==1:
            return 1; 
        if d2[0]==-1 and d2[2]==0:
            return 3
        if d2[0]==0 and d2[2]==-1:
            return 7;        
    return -1
        
def play7(tab):
    cantos=(1,3,7,9)
    for i in cantos:
        if eh_posicao_livre(tab,i):
            return i
    return -1

def play8(tab):
    lateral=(2,4,6,8)
    for i in lateral:
        if eh_posicao_livre(tab,i):
            return i
    return -1

def jogo_do_galo(str_jog,mod):
    if not isinstance(str_jog,str) or not str_jog in ('O','X') or not isinstance(mod, str) or not mod in ('basico','normal','perfeito'):
        raise ValueError('jogo do galo: algum dos argumentos e invalido')
    else:
        print("Bem-vindo ao JOGO DO GALO.")
        print("O jogador joga com '",str_jog,"'.")
        tab= ((0,0,0),(0,0,0),(0,0,0))
        while obter_posicoes_livres(tab) != ():
            if str_jog == 'O':
                pos= escolher_posicao_auto(tab,1,mod)
                new_tab= marcar_posicao(tab,1,pos)
                print("Turno do computador (",mod,")")
                print(tabuleiro_str(new_tab))
                tab=new_tab
                winner=jogador_ganhador(tab)
                if winner== 1:
                    return print("'X'")
                elif winner==-1:
                    return print("'O'")                
                if obter_posicoes_livres(tab) != ():
                    pos= escolher_posicao_manual(new_tab)
                    new_tab2= marcar_posicao(new_tab,-1,pos)
                    print(tabuleiro_str(new_tab2))
                    tab=new_tab2
                    winner=jogador_ganhador(tab)
                    if winner== 1:
                        return print("'X'") 
                    elif winner==-1:
                        return print("'O'")                    
            else:
                pos= escolher_posicao_manual(tab)
                new_tab= marcar_posicao(tab,1,pos)
                print(tabuleiro_str(new_tab))
                tab=new_tab
                winner=jogador_ganhador(tab)
                if winner== 1:
                    return print("'X'")
                elif winner==-1:
                    return print("'O'")                
                if obter_posicoes_livres(tab) != ():
                    pos= escolher_posicao_auto(tab,-1,mod)
                    new_tab2= marcar_posicao(new_tab,-1,pos)
                    print("Turno do computador (",mod,")")
                    print(tabuleiro_str(new_tab2))
                    tab=new_tab2   
                    winner=jogador_ganhador(tab)
                    if winner== 1:
                        return print("'X'")
                    elif winner==-1:
                        return print("'O'")                    
        winner=jogador_ganhador(tab)
        if winner== 1:
            print("'X'")
        elif winner==-1:
            print("'O'")
        else:
            print("'EMPATE'")
        
            