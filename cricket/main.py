def batscore(d):
    name=d.get('name')
    runs=d.get('runs')
    balls=d.get('balls')
    four=d.get('4')
    six=d.get('6')
    batscore=int(runs/2)
    if runs>=50:
        batscore=batscore+5
    if runs>=100:
        batscore=batscore+10
    
    sr=runs*100/balls
    if sr>80 and sr<100:
        batscore=batscore+2
    if sr>100:
            batscore=batscore+4
    batscore=batscore+four
    batscore=batscore+2*six
    return{'name': name,'batscore': batscore}

def ballscore(d):
    name=d.get('name')
    runs=d.get('runs')
    balls=d.get('overs')
    wkt=d.get('wkts')
    ballscore=int(wkt*10)
    if wkt>=3:
        ballscore=ballscore+5
    if wkt>=5:
        ballscore=ballscore+10
    er=runs/balls
    if er>3.5 and er<4.5:
        ballscore=ballscore+4
    if er>2 and er<3.5:
        ballscore=ballscore+7
    if er<2:
        ballscore=ballscore+10
    return{'name': name,'ballscore': ballscore}
    
    
