from PIL import Image, ImageDraw, ImageFont
import sys
S='/tmp/claude-0/-home-user-ppc-v-cloud/f66bc35b-2c27-5e8d-a548-c85f38447dac/scratchpad/'
NAVY=(22,35,54); TEAL=(92,226,227); WHITE=(255,255,255); LIGHT=(110,160,210)
F='/usr/share/fonts/opentype/inter/Inter-'
def f(w,s): return ImageFont.truetype(F+w+'.otf',s)
tisa=Image.open(S+'img/tisa_full.jpg').convert('RGB')
logo=tisa.crop((36,48,470,172))
photos={'tisa':tisa.crop((548,236,1076,972)),
        'brigitte':Image.open(S+'img/brigitte_full.jpg').convert('RGB').crop((430,180,776,752))}
def dots(d,x,y,cols,rows,gap=36,r=4):
    for i in range(cols):
        for j in range(rows): d.ellipse((x+i*gap-r,y+j*gap-r,x+i*gap+r,y+j*gap+r),fill=WHITE)
def fit(img,w,h):
    sw,sh=img.size;sc=max(w/sw,h/sh);img=img.resize((int(sw*sc)+1,int(sh*sc)+1),Image.LANCZOS)
    l=(img.width-w)//2;t=0 if img.height>h else 0;return img.crop((l,t,l+w,t+h))
def text(d,xy,lines,font,fill,lh):
    x,y=xy
    for ln in lines: d.text((x,y),ln,font=font,fill=fill);y+=lh
    return y
def square(doc,name):
    W=H=1080;im=Image.new('RGB',(W,H),NAVY);d=ImageDraw.Draw(im)
    d.polygon([(1080,600),(1080,1080),(560,1080)],fill=WHITE)
    dots(d,975,22,3,5); dots(d,290,900,7,3)
    im.paste(logo,(36,48))
    # photo frame
    px,py,pw,ph=600,250,440,600
    d.rectangle((px-50,py-40,px+pw-60,py+ph-80),outline=LIGHT,width=2)
    im.paste(fit(photos[doc],pw,ph),(px,py)); d.rectangle((px,py,px+pw-1,py+ph-1),outline=TEAL,width=6)
    y=text(d,(40,225),['Gap Free*','New Patient','Visit'],f('Bold',66),WHITE,76)
    y+=18; d.text((40,y),'with '+name,font=f('Medium',34),fill=TEAL); y+=64
    for b in ['Exam, scale & clean','X-rays (if required)','Fluoride treatment','Oral health plan']:
        d.ellipse((44,y+12,58,y+26),fill=TEAL); d.text((74,y),b,font=f('Regular',32),fill=WHITE); y+=50
    y+=14; text(d,(40,y),["Use your extras before","the year's out."],f('SemiBold',34),WHITE,44)
    d.text((40,1022),'*New patients with 60%+ dental extras cover. T&Cs apply.',font=f('Regular',17),fill=(190,200,215))
    d.text((640,1010),'www.kddental.com.au',font=f('Medium',34),fill=NAVY)
    return im
def story(doc,name):
    W,H=1080,1920;im=Image.new('RGB',(W,H),NAVY);d=ImageDraw.Draw(im)
    d.polygon([(1080,1640),(1080,1920),(780,1920)],fill=WHITE)
    dots(d,975,300,3,5); dots(d,80,1560,6,3)
    im.paste(logo,(323,250))   # keep top ~14% clear for the Stories UI
    y=text(d,(80,440),['Gap Free* New','Patient Visit'],f('Bold',84),WHITE,98)
    d.text((80,y+16),'with '+name,font=f('Medium',42),fill=TEAL)
    px,py,pw,ph=80,760,440,600
    im.paste(fit(photos[doc],pw,ph),(px,py)); d.rectangle((px,py,px+pw-1,py+ph-1),outline=TEAL,width=6)
    y=800
    for b in ['Exam, scale','& clean','X-rays (if req.)','Fluoride','Oral health plan']:
        if b in ('& clean',): d.text((598,y-14),b,font=f('Regular',36),fill=WHITE); y+=46; continue
        d.ellipse((560,y+14,576,y+30),fill=TEAL); d.text((598,y),b,font=f('Regular',36),fill=WHITE); y+=62
    text(d,(560,y+30),["Use your extras","before the year's","out."],f('SemiBold',40),WHITE,52)
    d.text((80,1410),'*New patients with 60%+ dental extras cover. T&Cs apply.',font=f('Regular',24),fill=(190,200,215))
    d.text((80,1460),'www.kddental.com.au',font=f('SemiBold',40),fill=TEAL)
    return im
for doc,name in [('tisa','Dr Tisa Kolarov'),('brigitte',"Dr Brigitte O'Brien")]:
    square(doc,name).save(S+f'out/pp5006_gapfree_{doc}_1x1.png')
    story(doc,name).save(S+f'out/pp5006_gapfree_{doc}_9x16.png')
