import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib import font_manager as fm
fp='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fm.fontManager.addfont(fp)
prop=fm.FontProperties(fname=fp)
plt.rcParams['font.family']=prop.get_name()
W,H=12.0,5.45
fig=plt.figure(figsize=(W,H),dpi=220); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis('off')
INK='#222222'; GRAY='#555555'
def box(x,y,w,h,txt,fc='#ffffff',ec=INK,fs=14.2,lw=1.0,bold=False,ls='-'):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',fc=fc,ec=ec,lw=lw,ls=ls); ax.add_patch(p)
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,color=INK,fontweight='bold' if bold else 'normal',linespacing=1.25)
def arr(x1,y1,x2,y2,ls='-',col=INK,rad=0.0,lw=1.1):
    a=FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=10,lw=lw,color=col,linestyle=ls,connectionstyle=f'arc3,rad={rad}'); ax.add_patch(a)
def ep(x,y,l):
    ax.add_patch(Circle((x,y),0.22,fc='#1f1f1f',ec='#1f1f1f',zorder=5)); ax.text(x,y,l,ha='center',va='center',color='white',fontsize=12,fontweight='bold',zorder=6)
# stage bands
bands=[(0.15,3.55,'진입 (entry)','T1 지시·목표 조작, T3 도구·공급망'),(3.9,4.25,'전파 (propagation)','T2 메모리·컨텍스트 조작, T6 에이전트 간 상호작용'),(8.35,3.5,'영향 (impact)','T4 데이터·프라이버시, T5 허용 범위 밖 행동')]
for x,w,t1,t2 in bands:
    ax.add_patch(FancyBboxPatch((x,0.12),w,0.62,boxstyle='round,pad=0.0,rounding_size=0.06',fc='#ececec',ec='none'))
    ax.text(x+w/2,0.55,t1,ha='center',va='center',fontsize=14.2,fontweight='bold',color=INK)
    ax.text(x+w/2,0.3,t2,ha='center',va='center',fontsize=11.6,color=GRAY)
# inputs
ax.text(1.9,4.66,'입력 출처',ha='center',fontsize=14.2,fontweight='bold',color=INK)
ins=[('사용자 작업 q  (위임의 출처)',4.1,'#ffffff','-'),('웹·문서·이메일  (U)',3.45,'#f7f7f7','--'),('도구 출력·환경  (U)',2.8,'#f7f7f7','--'),('도구 메타데이터  (U)',2.15,'#f7f7f7','--'),('다른 에이전트 메시지  (U)',1.5,'#f7f7f7','--')]
for t,y,fc,ls in ins: box(0.25,y,3.3,0.5,t,fc=fc,fs=13.2,ls=ls)
# agent
ax.add_patch(FancyBboxPatch((4.35,1.25),3.7,3.35,boxstyle='round,pad=0.02,rounding_size=0.12',fc='#fafafa',ec=INK,lw=1.3))
ax.text(6.2,4.35,'LLM 에이전트',ha='center',fontsize=14.0,fontweight='bold',color=INK)
box(4.6,3.25,3.2,0.75,'컨텍스트·계획\n(다음 행동 선택)',fs=12.9)
box(4.6,1.5,1.45,0.95,'장기 메모리\n(RAG)',fs=12.6,ls=(0,(4,3)))
box(6.35,1.5,1.45,0.95,'재계획',fs=12.6)
arr(5.3,3.25,5.3,2.47); arr(5.55,2.47,5.55,3.25,col=GRAY)
arr(7.05,2.47,7.05,3.25)
# input arrows into agent
for y in [4.35,3.7,3.05,2.4,1.75]: arr(3.57,y,4.33,y,lw=0.9)
ax.plot([3.95,3.95],[1.6,4.45],color=GRAY,lw=0.8,ls=':')
ep(3.95,4.62,'I')
ep(4.6,3.9,'P'); ep(4.6,2.4,'M'); ep(3.74,1.75,'C')
# outputs
box(8.85,3.55,3.0,0.65,'행동 $a_t$: 도구 호출\n$a_t \\in$ Auth(q) $\\cap$ Pol?',fs=12.6)
box(8.85,2.6,3.0,0.6,'행동 $a_t$: 최종 응답',fs=12.9)
box(8.85,1.6,3.0,0.65,'행동 $a_t$: 메시지·위임',fs=12.9)
arr(8.06,3.88,8.83,3.88); ep(8.45,3.88,'A')
arr(8.06,2.9,8.83,2.9); ep(8.45,2.9,'O')
arr(8.06,1.92,8.83,1.92); ep(8.45,1.92,'C')
# environment feedback loop
xs=[10.35,10.35,0.1,0.1]; ys=[4.2,5.02,5.02,3.05]
ax.plot(xs,ys,color=GRAY,lw=0.9,ls=(0,(4,3)))
arr(0.1,3.05,0.24,3.05,col=GRAY,lw=0.9)
ax.text(6.2,5.0-0.18,'',fontsize=1.5)
ax.text(10.2,5.06,'환경 상태 변화 → 재관찰',fontsize=12.6,color=GRAY,ha='right',va='bottom')
# legend
ax.add_patch(Circle((0.45,0.98),0.1,fc='#1f1f1f')); ax.text(0.62,0.98,'집행 지점: I 입력 수신 · P 계획 수립 · M 메모리 쓰기·읽기 · A 도구 호출 경계 · O 최종 응답 출력 · C 에이전트 간 통신',fontsize=11.4,va='center',color=INK)
ax.add_patch(FancyBboxPatch((0.25,0.0),0.0001,0.0001,fc='none',ec='none'))
ax.text(11.85,0.98,'점선: 비신뢰 출처(U)',ha='right',fontsize=11.4,va='center',color=GRAY)
fig.savefig('fig1_v15.png',dpi=220)
print('ok')
