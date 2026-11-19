import json,os,urllib.request as u
G=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0);H1=(0,0,1,1,2,4,0)
PT=["UUUU}}}}__isZZ_nUUUiZPKUZ__AUUUU","#-77-AUU7U_d7Zdi7Udi7Z_d-AUZ#-77","AKKKKUUUKUZ_KZZ_KU__K___KZUUAKKK","UUUUZ___PUUUPUUUPUUUPUUUPUUUUUUZ","AKKPKUUUKUZZPUZZUUZZKZZZKUZUAKKP","7--#7--#7--#7--#A77-KAAAiiUUis_U","UUUU}}}}ssssiiii____ZZZZUUUUUUUU","#-7A7AKU7Kis7Ks}7Ks}7Kis77UU#777"]
KN=(33,18,-14,-31,-33,-18,14,31);KG=(1,15,16,17,-1,-15,-16,-17);DG=(15,17,-15,-17);OR=(1,16,-1,-16)
CK=((4,6,7,1,(5,6),(4,5,6)),(4,2,0,2,(3,2,1),(4,3,2)),(116,118,119,4,(117,118),(116,117,118)),(116,114,112,8,(115,114,113),(116,115,114)))
M=100000;N=0;L=25000
B=[0]*128;W=1;C=0;E=-1;H=0;K=0;KS=[4,116];CN=[0]*13;NP=0;NM=0;RQ=0;U=[];T={};KL=[[0,0] for _ in range(64)];HS=[0]*1664;HC={}
x=88172645463325252;Z=[]
for _ in range(1690):
 x=(x*6364136223846793005+1)&(1<<64)-1;Z.append(x)
ZS=Z[1689]
def at(s,b):
 for o in ((15,17) if b>0 else (-15,-17)):
  q=s-o
  if not q&136 and B[q]==b:return 1
 for o in KN:
  q=s+o
  if not q&136 and B[q]==b*2:return 1
 for o in KG:
  q=s+o
  if not q&136 and B[q]==b*6:return 1
 for o in DG:
  q=s+o
  while not q&136:
   c=B[q]
   if c:
    if c==b*3 or c==b*5:return 1
    break
   q+=o
 for o in OR:
  q=s+o
  while not q&136:
   c=B[q]
   if c:
    if c==b*4 or c==b*5:return 1
    break
   q+=o
 return 0
def pv(i,s):
 r=s>>4;f=7-(s&7) if (s&7)>3 else s&7
 return ord(PT[i][(7-r)*4+f])-85
def ev():
 mg=eg=ph=0;wb=bb=0
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p:continue
  t=p if p>0 else -p;q=s if p>0 else s^112;g=1 if p>0 else -1
  mg+=g*(V[t]+pv(t-1,q));eg+=g*(V[t]+pv(6 if t==1 else 7 if t==6 else t-1,q));ph+=H1[t]
  if t==3:
   if p>0:wb+=1
   else:bb+=1
 mg+=30*(wb>1)-30*(bb>1);eg+=50*(wb>1)-50*(bb>1)
 s=(mg*ph+eg*(24-ph))//24
 return s+10 if W>0 else -s+10
def gen(cp=0):
 ms=[]
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or (p>0)!=(W>0):continue
  t=p if p>0 else -p
  if t==1:
   d=16*W;lr=7 if W>0 else 0;hr=1 if W>0 else 6;o=s+d
   if not cp and not B[o]:
    if o>>4==lr:
     for pr in (5,4,3,2):ms.append(s|o<<7|pr<<14)
    else:
     ms.append(s|o<<7)
     if (s>>4)==hr and not B[s+d*2]:ms.append(s|(s+d*2)<<7)
   for o in (s+d-1,s+d+1):
    if o&136:continue
    c=B[o]
    if c and (c>0)!=(W>0):
     if o>>4==lr:
      for pr in (5,4,3,2):ms.append(s|o<<7|pr<<14)
     else:ms.append(s|o<<7)
    elif o==E:ms.append(s|o<<7)
  elif t==2 or t==6:
   for o in (KN if t==2 else KG):
    q=s+o
    if q&136:continue
    c=B[q]
    if (not cp and not c) or (c and (c>0)!=(W>0)):ms.append(s|q<<7)
   if t==6:
    for kf,kt,rf,bit,em,sa in CK:
     if s==kf and C&bit and B[rf]==(4 if kf<16 else -4) and not any(B[q] for q in em) and not any(at(q,-W) for q in sa):ms.append(kf|kt<<7)
  else:
   for o in (DG if t==3 else OR if t==4 else DG+OR):
    q=s+o
    while not q&136:
     c=B[q]
     if not c:
      if not cp:ms.append(s|q<<7)
     else:
      if (c>0)!=(W>0):ms.append(s|q<<7)
      break
     q+=o
 return ms
def make(m):
 global W,C,E,H,K,NP,NM,RQ
 f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];c=B[t];cs=-1
 if abs(p)==1 and t==E and not c:cs=t-16*W;c=B[cs];B[cs]=0
 U.append((m,c,cs,C,E,H,K,NP,NM,RQ))
 K^=Z[(p+6)*128+f]^Z[((pr*W if pr else p)+6)*128+t]
 if c:K^=Z[(c+6)*128+(cs if cs>=0 else t)]
 B[t]=pr*W if pr else p;B[f]=0
 if abs(p)==6:
  KS[0 if W>0 else 1]=t
  if abs(t-f)==2:
   if t>f:B[t-1]=B[t+1];B[t+1]=0
   else:B[t+1]=B[t-2];B[t-2]=0
 nc=C
 if abs(p)==6:nc&=12 if W>0 else 3
 if f==0 or t==0:nc&=~2
 if f==7 or t==7:nc&=~1
 if f==112 or t==112:nc&=~8
 if f==119 or t==119:nc&=~4
 if nc!=C:K^=Z[1664+C]^Z[1664+nc];C=nc
 ne=f+16*W if abs(p)==1 and abs(t-f)==32 else -1
 if ne!=E:K^=Z[1680+((E&7) if E>=0 else 8)]^Z[1680+((ne&7) if ne>=0 else 8)];E=ne
 H=0 if abs(p)==1 or c else H+1
 if c:
  CN[c+6]-=1
  if abs(c)==1:NP-=1
  else:NM-=1;RQ-=abs(c)>3
 if pr:CN[p+6]-=1;CN[pr*W+6]+=1;NP-=1;NM+=1;RQ+=pr>3
 W=-W;K^=ZS
def unmake():
 global W,C,E,H,K,NP,NM,RQ
 m,c,cs,C,E,H,K,NP,NM,RQ=U.pop()
 f=m&127;t=(m>>7)&127;pr=m>>14;mv=-W;p=B[t]
 B[f]=mv if pr else p;B[t]=0
 if c:B[cs if cs>=0 else t]=c
 if abs(p)==6:
  KS[0 if mv>0 else 1]=f
  if abs(t-f)==2:
   if t>f:B[t+1]=B[t-1];B[t-1]=0
   else:B[t-2]=B[t+1];B[t+1]=0
 if c:CN[c+6]+=1
 if pr:CN[mv+6]+=1;CN[pr*mv+6]-=1
 W=-W
def legal(m):
 make(m);r=not at(KS[0 if W<0 else 1],W);unmake();return r
def ordr(ms,tm,pl):
 def sc(m):
  if m==tm:return 20000
  f=m&127;t=(m>>7)&127;c=B[t]
  if c or (abs(B[f])==1 and t==E):return 10000+V[abs(c)]*10-V[abs(B[f])]
  if m==KL[pl][0]:return 9000
  if m==KL[pl][1]:return 8000
  return HS[(B[f]+6)*128+t]
 ms.sort(key=sc,reverse=True);return ms
class TO(Exception):pass
def Q(a,b,pl):
 global N
 N+=1
 if N>L:raise TO
 if H>=100 or (NP==0 and RQ==0 and NM<=1):return 0
 ck=at(KS[0 if W>0 else 1],-W)
 if not ck:
  st=ev()
  if st>=b:return b
  if st>a:a=st
 ms=gen(1) if not ck else gen()
 om=ordr(ms,0,pl);fd=0
 for m in om:
  make(m)
  if at(KS[0 if W<0 else 1],W):unmake();continue
  fd=1;s=-Q(-b,-a,pl+1);unmake()
  if s>a:a=s
  if a>=b:break
 if ck and not fd:return -M+pl
 return a
def S(d,a,b,pl):
 global N
 N+=1
 if N>L:raise TO
 if H>=100 or (NP==0 and RQ==0 and NM<=1) or HC.get(K,0)>=2:return 0
 e=T.get(K);tm=0
 if e and e[0]>=d:
  if e[1]==0:return e[2]
  if e[1]==1 and e[2]>=b:return e[2]
  if e[1]==2 and e[2]<=a:return e[2]
  tm=e[3]
 ck=at(KS[0 if W>0 else 1],-W)
 if ck:d+=1
 if d<=0:return Q(a,b,pl)
 ms=gen()
 if not ms:return -M+pl if ck else 0
 om=ordr(ms,tm,pl);best=-M;bm=0;a0=a
 for m in om:
  f=m&127;t=(m>>7)&127;cap=B[t] or (abs(B[f])==1 and t==E)
  make(m)
  if at(KS[0 if W<0 else 1],W):unmake();continue
  s=-S(d-1,-b,-a,pl+1);unmake()
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if not cap:
    KL[pl][1]=KL[pl][0];KL[pl][0]=m;HS[(B[f]+6)*128+t]+=d*d
   break
 if best==-M:return -M+pl if ck else 0
 if abs(best)<M-1000:T[K]=(d,0 if a0<best<b else 1 if best>=b else 2,best,bm)
 if len(T)>262144:T.clear()
 return best
def root():
 global N
 ms=[m for m in gen() if legal(m)]
 if len(ms)==1:return ms[0]
 bm=ms[0];N=0
 for d in range(1,64):
  try:
   om=ordr(ms,bm,0);a=-M-1;b=M+1;bb=bm
   for m in om:
    make(m);s=-S(d-1,-b,-a,1);unmake()
    if s>a:a=s;bb=m
   bm=bb;ms=om
  except TO:break
 return bm
def pf(f):
 global B,W,C,E,H,K,KS,CN,NP,NM,RQ,U
 p=f.split();B=[0]*128;W=1 if p[1]=='w' else -1;C=0;E=-1;H=int(p[4]);CN=[0]*13;NP=0;NM=0;RQ=0;KS=[4,116];K=0;U=[]
 for r,row in enumerate(p[0].split('/')):
  x=0
  for ch in row:
   if ch.isdigit():x+=int(ch)
   else:
    t='PNBRQK'.index(ch.upper())+1;v=t if ch.isupper() else -t;sq=(7-r)*16+x;B[sq]=v;x+=1
    if t==6:KS[0 if v>0 else 1]=sq
    CN[v+6]+=1
    if t==1:NP+=1
    elif t!=6:NM+=1;RQ+=t>3
 for i,ch in enumerate('KQkq'):
  if ch in p[2]:C|=1<<i
 if p[3]!='-':E=(int(p[3][1])-1)*16+ord(p[3][0])-97
 for s in range(128):
  v=B[s]
  if v:K^=Z[(v+6)*128+s]
 K^=Z[1664+C]^Z[1680+((E&7) if E>=0 else 8)]^(ZS if W<0 else 0)
def best(g):
 global HC
 pf(g['start_fen']);HK=[K]
 for u in g['moves']:make((ord(u[1])-49)*16+ord(u[0])-97|((ord(u[3])-49)*16+ord(u[2])-97)<<7|((('nbrq'.index(u[4])+2)<<14) if len(u)==5 else 0));HK.append(K)
 HC={}
 for k in HK:HC[k]=HC.get(k,0)+1
 m=root();f=m&127;t=(m>>7)&127;pr=m>>14
 return 'abcdefgh'[f&7]+str((f>>4)+1)+'abcdefgh'[t&7]+str((t>>4)+1)+('nbrq'[pr-2] if pr else '')
def post(p,b):
 r=u.Request(G+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 with u.urlopen(r) as x:return json.load(x)
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  try:g=post('/move',{'game':g['game'],'move':best(g)})
  except Exception:g=post('/move',{'game':g['game'],'move':g['legal_moves'][0]})
