import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib import font_manager as fm
fp = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; fm.fontManager.addfont(fp)
plt.rcParams['font.family'] = fm.FontProperties(fname=fp).get_name()
S = json.load(open(os.path.join(RAW, 'STATS10.json'))); P = S['prisma']; K = S['screen_kappa']['ALL']
W, H = 6.0, 2.53
fig = plt.figure(figsize=(W, H), dpi=600); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0.19, 0.19 + H); ax.axis('off')
INK = '#222222'
def box(x, y, w, h, t, fs=6.3):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.0,rounding_size=0.04', fc='white', ec=INK, lw=0.6))
    ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=fs, color=INK, linespacing=1.3)
def arr(pts):
    for (x1, y1), (x2, y2) in zip(pts[:-2], pts[1:-1]): ax.plot([x1, x2], [y1, y2], color=INK, lw=0.6)
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=6, lw=0.6, color=INK, shrinkA=0, shrinkB=0))
def band(y, h, t):
    ax.add_patch(FancyBboxPatch((0.05, y), 0.25, h, boxstyle='round,pad=0.0,rounding_size=0.04', fc='#e6e6e6', ec='none'))
    ax.text(0.175, y + h / 2, t, rotation=90, ha='center', va='center', fontsize=6.8, fontweight='bold', color=INK)
fmt = lambda n: f'{n:,}'
band(2.05, 0.65, '수집'); band(0.95, 1.05, '선별'); band(0.22, 0.62, '분류')
box(0.40, 2.10, 2.15, 0.55, '경로 1: 8개 학회 메타데이터 72,097편\n검색식 일치 1,204편: 기본 484, 확장 720')
box(2.70, 2.10, 1.40, 0.55, '경로 2: 보안 학회 4곳\n채택 목록 등 후보 85편')
box(4.25, 2.10, 1.70, 0.55, '경로 3: 선행 리뷰 2편의\n참고문헌 379편, 후보 13편')
box(0.40, 1.50, 2.15, 0.45, '제목·초록 선별 %s편\n실행 A·B 각각 판정, κ %.2f, PABAK %.2f' % (fmt(P['screened']), K['kappa'], K['pabak']))
arr([(1.475, 2.10), (1.475, 1.95)]); arr([(3.40, 2.10), (3.40, 2.03), (2.30, 2.03), (2.30, 1.95)])
r = P['both_exc_reasons']
box(2.70, 1.45, 1.40, 0.55, '두 실행 모두 제외 %s편\nX %d, E2 %d, E1 %d, E4 %d,\nE3 %d, E5 %d, E6 %d' % (fmt(P['both_exc']), r['X'], r['E2'], r['E1'], r['E4'], r['E3'], r['E5'], r['E6']), fs=6.0)
arr([(2.55, 1.725), (2.70, 1.725)])
box(0.40, 1.00, 2.15, 0.42, '다음 단계 %d편: 둘 다 포함 %d, 불일치 %d\n불일치는 조정 실행이 원문으로 확인' % (P['forwarded'], P['both_inc'], P['disagree']))
arr([(1.20, 1.50), (1.20, 1.42)])
e = P['elig_exc_reasons']
box(2.70, 1.02, 1.40, 0.36, '제외 %d편\nE2 %d, E1 %d, E4 %d' % (P['elig_excluded'], e['E2'], e['E1'], e['E4']), fs=6.0)
arr([(2.55, 1.20), (2.70, 1.20)])
box(4.25, 1.38, 1.70, 0.55, '후보 13편 판정\n두 실행 판정 일치 %d편\n포함 %d편, 제외 %d편' % (S['snowball']['passB_agree'], S['snowball']['inc'], 13 - S['snowball']['inc']), fs=6.0)
arr([(5.10, 2.10), (5.10, 1.93)])
pa = P['by_path']
box(0.40, 0.30, 2.15, 0.45, '분석 대상 %d편\n경로 1 %d편, 경로 2 %d편, 경로 3 %d편' % (P['total'], pa['V2'] + pa['V3'], pa['SEC'], P['snowball_inc']))
arr([(1.20, 1.00), (1.20, 0.75)])
arr([(5.10, 1.38), (5.10, 0.88), (2.10, 0.88), (2.10, 0.75)])
ax.text(3.60, 0.90, '포함 %d편' % S['snowball']['inc'], fontsize=6.0, color=INK, ha='center', va='bottom')
box(2.70, 0.30, 3.25, 0.45, '실행 A·B의 초록 기준 분류: 라벨 30개, κ %.2f–%.2f | 방어 %d편 원문 기준 분류: 원문 %d편\n다른 모델 점검: 선별 200편, 초록 기준 60편, 원문 기준 30편과 24편' % (S['rel_abs']['min'], S['rel_abs']['max'], S['Ndef'], 84))
arr([(2.55, 0.525), (2.70, 0.525)])
fig.savefig(os.path.join(RAW, '..', '..', 'fig2.png'), dpi=600); print('ok')
