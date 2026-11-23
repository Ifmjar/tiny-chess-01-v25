import base64,json,lzma,os,urllib.request as u,zlib
D=os.path.dirname(os.path.abspath(__file__))
BK=json.loads(zlib.decompress(base64.b85decode(open(os.path.join(D,'book.b85')).read())))
E={}
exec(lzma.decompress(base64.b85decode(open(os.path.join(D,'engine.b85')).read())).decode(),E)
U=os.environ['MAKEFUN_ENV_URL']
def P(p,b):
	try:
		q=u.Request(U+p,json.dumps(b).encode(),headers={'Content-Type':'application/json'})
		with u.urlopen(q,timeout=30)as r:return json.load(r)
	except Exception:return{'error':1}
def BM(g):
	L=BK.get(g['opening']['id']+g['opponent']+g['colour'][0])
	if not L:return None
	i=(len(g['moves'])-8)//2
	if i<len(L)and L[i]in g.get('legal_moves',[]):return L[i]
	return None
while 1:
	g=None
	for _ in range(3):
		g=P('/game',{})
		if not g.get('error'):break
	if g.get('status')=='done'or g.get('error'):break
	E['GH'].clear()
	while g.get('status')=='your_move':
		E['F'](g['fen']);E['GH'].add(E['H'])
		r=P('/move',{'game':g['game'],'move':BM(g)or E['CH']()})
		if r.get('error')and g.get('legal_moves'):r=P('/move',{'game':g['game'],'move':g['legal_moves'][0]})
		g=r
