import numpy as np

# Create matrix of 
def txtMat(textLST, q, freqLST):
    numfreq = []
    if freqLST == None:
        freqLST =  []
        for i in textLST:
            sen = list(set(i.split()))
            freqLST.extend([k for k in sen if k not in freqLST])
        freqLST = sorted(freqLST, key=lambda v: v.upper())
    for z in textLST:
        sen = [(z.split()).count(j) for j in freqLST]
        numfreq.append(sen)
    q = np.transpose(np.array([(q.split()).count(h) for h in freqLST]))
    return((np.array(numfreq).T),q)
                
                
def rankapprox(rank,mat):
    U, S, Vt = np.linalg.svd(mat[0])
    # rank-2 approximation
    Um=np.matrix(U[:, :rank])
    Sm=np.diag(S[:rank])
    Vm=np.matrix(Vt[:rank, :])
    return([Um,Sm,Vm])

def analysis(q,r,ts):
    coords = np.transpose(q) * (r[0] * np.linalg.inv(r[1]))
    tstlst = []
    for i in range(ts):
        test = np.dot(coords,r[2][:,i])/(np.linalg.norm(coords,2) * np.linalg.norm(r[2][:,i], 2))
        tstlst.append(test[0,0])
    return(tstlst)
        
    
    












