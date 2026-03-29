#!/usr/bin/env python3
"""
Generate graphical abstract for:
"Geopolitical Oil Shocks and Sectoral Heterogeneity:
 Evidence on Market Transmission and Aggregation Masking"

Output: Proportional to 531 x 1328 pixels (h x w) at high res.
Elsevier specs: 531 x 1328 px minimum, TIFF preferred, readable at 5 x 13 cm.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ── Dimensions: 2656 x 1062 px (2x Elsevier min) at 300 DPI ──
DPI = 300
W_in = 2656 / DPI   # ~8.85 in
H_in = 1062 / DPI   # ~3.54 in
fig = plt.figure(figsize=(W_in, H_in), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 40)
ax.axis('off')
fig.patch.set_facecolor('#0F3D4A')

# ── Colors ──
C = {
    'bg':       '#0F3D4A',
    'titlebg':  '#1A6B7A',
    'navy':     '#1A365D',
    'dkblue':   '#1E3A5F',
    'blue':     '#3182CE',
    'softblue': '#90CDF4',
    'paleblue': '#D6EFFF',
    'dkgreen':  '#1C6B3A',
    'green':    '#38A169',
    'softgreen':'#68D391',
    'palegreen':'#C6F6D5',
    'dkred':    '#9B2C2C',
    'red':      '#E53E3E',
    'softred':  '#FC8181',
    'palered':  '#FED7D7',
    'amber':    '#D69E2E',
    'dkamber':  '#744210',
    'paleamber':'#FEFCBF',
    'charcoal': '#2D3748',
    'steel':    '#4A5568',
    'gray':     '#718096',
    'silver':   '#A0AEC0',
    'mist':     '#E2E8F0',
    'white':    '#FFFFFF',
    'panelbg':  '#EDF2F7',
    'bottombg': '#1A2332',
}

# ── Background ──
ax.add_patch(FancyBboxPatch((0, 0), 100, 40, boxstyle="square,pad=0",
             facecolor=C['bg'], edgecolor='none'))

# ═══════════════════════════════════════
# TITLE BAR
# ═══════════════════════════════════════
ax.add_patch(FancyBboxPatch((0, 35.0), 100, 5.0, boxstyle="square,pad=0",
             facecolor=C['titlebg'], edgecolor='none'))
ax.text(50, 38.0, 'Geopolitical Oil Shocks and Sectoral Heterogeneity',
        ha='center', va='center', fontsize=9, fontweight='bold', color='white',
        fontfamily='sans-serif')
ax.text(50, 36.2,
        'Aggregate indices conceal ~95% of sectoral disruption — '
        'oil sensitivity predicts which sectors win and lose',
        ha='center', va='center', fontsize=5.5, color=C['softblue'],
        fontfamily='sans-serif', style='italic')

# ═══════════════════════════════════════
# BOTTOM STRIP
# ═══════════════════════════════════════
ax.add_patch(FancyBboxPatch((0, 0), 100, 5.0, boxstyle="square,pad=0",
             facecolor=C['bottombg'], edgecolor='none'))
ax.text(50, 3.5,
        r'Oil sensitivity ($\beta_{oil}$) predicts sectoral winners and losers '
        r'across geopolitical shocks,',
        ha='center', fontsize=5.5, fontweight='bold', color=C['softblue'],
        fontfamily='sans-serif')
ax.text(50, 2.0,
        r'but cap-weighted indices conceal ~95% of this heterogeneity '
        r'($\Psi$ = 0.947)',
        ha='center', fontsize=5.5, fontweight='bold', color=C['softblue'],
        fontfamily='sans-serif')
ax.text(2, 0.6, 'Saxena & Yang (2026)', fontsize=3.5, color=C['silver'],
        fontfamily='sans-serif')
ax.text(50, 0.6, 'College of Management, Yuan Ze University, Taiwan',
        ha='center', fontsize=3.5, color=C['silver'], fontfamily='sans-serif')
ax.text(98, 0.6, 'Research in International Business and Finance',
        ha='right', fontsize=3.5, color=C['silver'], fontfamily='sans-serif',
        style='italic')

# ═══════════════════════════════════════
# PANELS
# ═══════════════════════════════════════
panel_y0 = 5.5
panel_y1 = 34.5
hdr_h = 2.5

panels_x = [
    (1.0,  23.0),   # Stage 1: Shock
    (26.5, 49.5),   # Stage 2: Divergence
    (53.0, 76.0),   # Stage 3: Masking
    (79.5, 99.0),   # Stage 4: Implications
]

def draw_panel(x0, x1, header_text, header_color):
    w = x1 - x0
    h = panel_y1 - panel_y0
    ax.add_patch(FancyBboxPatch((x0, panel_y0), w, h,
                 boxstyle="round,pad=0.3", facecolor=C['white'],
                 edgecolor=C['mist'], linewidth=0.5))
    ax.add_patch(FancyBboxPatch((x0 + 0.15, panel_y1 - hdr_h), w - 0.3, hdr_h,
                 boxstyle="round,pad=0.15", facecolor=header_color,
                 edgecolor='none'))
    ax.text((x0 + x1) / 2, panel_y1 - hdr_h / 2, header_text,
            ha='center', va='center', fontsize=6.5, fontweight='bold',
            color='white', fontfamily='sans-serif')

def draw_arrow(x_start, x_end, y):
    ax.annotate('', xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle='->', color=C['softblue'],
                                lw=2.2, mutation_scale=14))

# ═══════════════════════════════════════
# STAGE 1: THE SHOCK
# ═══════════════════════════════════════
x0, x1 = panels_x[0]
draw_panel(x0, x1, 'GEOPOLITICAL OIL SHOCK', C['dkblue'])
cx = (x0 + x1) / 2

# Oil barrel
bw, bh = 3.5, 4.0
bx, by = cx - bw/2, 23.5
ax.add_patch(FancyBboxPatch((bx, by), bw, bh,
             boxstyle="round,pad=0.12", facecolor=C['dkamber'],
             edgecolor=C['charcoal'], linewidth=1))
for yb in [by + 1.2, by + 2.8]:
    ax.plot([bx + 0.3, bx + bw - 0.3], [yb, yb], color=C['charcoal'], lw=1.2)

# Price spike arrow
ax.annotate('', xy=(bx + bw + 2.0, by + bh - 0.3), xytext=(bx + bw + 2.0, by + 0.3),
            arrowprops=dict(arrowstyle='->', color=C['red'], lw=2.2,
                            mutation_scale=14))
ax.text(bx + bw + 3.0, by + 2.8, '+42%', fontsize=6.5, fontweight='bold',
        color=C['red'], fontfamily='sans-serif')
ax.text(bx + bw + 3.0, by + 1.5, 'WTI', fontsize=4.5, color=C['steel'],
        fontfamily='sans-serif')

# Event name
ax.text(cx, 22.0, 'Strait of Hormuz 2026', ha='center', fontsize=6.5,
        fontweight='bold', color=C['charcoal'], fontfamily='sans-serif')
ax.text(cx, 20.5, '21% of global oil transit disrupted', ha='center',
        fontsize=5, color=C['steel'], fontfamily='sans-serif')

# Divider
ax.plot([x0 + 2, x1 - 2], [19.0, 19.0], color=C['mist'], lw=0.6)

# 5 events
ax.text(cx, 17.8, 'Validated Across 5 Events', ha='center', fontsize=5.5,
        fontweight='bold', color=C['navy'], fontfamily='sans-serif')

events = [
    ('Hormuz 2026', 'Supply', C['dkgreen']),
    ('Russia–Ukraine 2022', 'Supply', C['dkgreen']),
    ('OPEC+ Cut 2022', 'Supply', C['dkgreen']),
    ('Middle East 2023', 'Supply', C['dkgreen']),
    ('COVID-19 2020', 'Demand', C['dkred']),
]
for i, (name, typ, col) in enumerate(events):
    yy = 16.5 - i * 2.0
    ax.plot(x0 + 2.5, yy, 'o', color=col, markersize=3.5)
    ax.text(x0 + 3.8, yy, name, fontsize=4, va='center', color=C['steel'],
            fontfamily='sans-serif')
    ax.text(x1 - 2, yy, typ, fontsize=4, va='center', ha='right',
            fontweight='bold', color=col, fontfamily='sans-serif')

# Arrow 1→2
draw_arrow(x1 + 0.3, panels_x[1][0] - 0.3, 20)

# ═══════════════════════════════════════
# STAGE 2: SECTORAL DIVERGENCE
# ═══════════════════════════════════════
x0, x1 = panels_x[1]
draw_panel(x0, x1, 'SECTORAL DIVERGENCE', C['dkblue'])
cx = (x0 + x1) / 2

# Scatter plot area
px0, px1 = x0 + 3.0, x1 - 1.5
py0, py1 = 16.5, 29.5
mid_y = (py0 + py1) / 2

ax.add_patch(FancyBboxPatch((px0 - 0.8, py0 - 0.3), px1 - px0 + 1.6, py1 - py0 + 0.6,
             boxstyle="round,pad=0.15", facecolor=C['panelbg'],
             edgecolor=C['mist'], linewidth=0.4))

# Axes
ax.annotate('', xy=(px0, py1 + 0.2), xytext=(px0, py0 - 0.2),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'], lw=0.8))
ax.annotate('', xy=(px1 + 0.2, mid_y), xytext=(px0 - 0.2, mid_y),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'], lw=0.8))

ax.text(px0 - 1.8, (py0 + py1) / 2, 'CAR (%)', ha='center', va='center',
        fontsize=4, fontweight='bold', color=C['charcoal'],
        fontfamily='sans-serif', rotation=90)
ax.text((px0 + px1) / 2, py0 - 1.2, r'Oil Sensitivity ($\beta_{oil}$)',
        ha='center', fontsize=4, fontweight='bold', color=C['charcoal'],
        fontfamily='sans-serif')

# Zero label
ax.text(px0 - 0.6, mid_y, '0', fontsize=3.5, color=C['gray'],
        ha='center', va='center')

# Regression line
ax.plot([px0 + 0.5, px1 - 0.5], [mid_y - 5.0, mid_y + 5.5],
        color=C['navy'], lw=1.8, zorder=3)

# Winners
for wx, wy, wl in [(px1 - 1.5, mid_y + 4.5, 'USO'),
                     (px1 - 3.0, mid_y + 3.2, 'XOP'),
                     (px1 - 4.0, mid_y + 2.5, 'FCG')]:
    ax.plot(wx, wy, 'o', color=C['dkgreen'], markersize=4, zorder=4)
    ax.text(wx + 0.4, wy + 0.3, wl, fontsize=3.5, fontweight='bold',
            color=C['dkgreen'], fontfamily='sans-serif', zorder=4)

# Middle
for mx, my in [(px0 + 5, mid_y + 0.3), (px0 + 6, mid_y - 0.3),
               (px0 + 7, mid_y + 0.6), (px0 + 8, mid_y + 0.1),
               (px0 + 4.5, mid_y - 0.5)]:
    ax.plot(mx, my, 'o', color=C['silver'], markersize=2.8, zorder=4)

# Losers
for lx, ly, ll in [(px0 + 1.5, mid_y - 4.2, 'ITB'),
                     (px0 + 2.5, mid_y - 3.5, 'XHB'),
                     (px0 + 1.0, mid_y - 3.7, 'JETS')]:
    ax.plot(lx, ly, 'o', color=C['dkred'], markersize=4, zorder=4)
    ax.text(lx - 0.2, ly - 0.6, ll, fontsize=3.5, fontweight='bold',
            color=C['dkred'], ha='center', fontfamily='sans-serif', zorder=4)

# Key stat box
sy0 = 7.0
sy1 = 14.5
ax.add_patch(FancyBboxPatch((x0 + 1.5, sy0), x1 - x0 - 3, sy1 - sy0,
             boxstyle="round,pad=0.25", facecolor=C['paleblue'],
             edgecolor=C['navy'], linewidth=0.7))

ax.text(cx, 12.5, r'$\gamma_1$ = +20.18***', ha='center', fontsize=10,
        fontweight='bold', color=C['navy'], fontfamily='sans-serif')
ax.text(cx, 10.3, '1 s.d. oil sensitivity predicts\n18–21 pp higher CARs',
        ha='center', fontsize=4.5, color=C['steel'], fontfamily='sans-serif',
        linespacing=1.4)
ax.text(cx, 8.2, r'$R^2$ = 0.42  |  Bootstrap CI: [15.3, 31.6]',
        ha='center', fontsize=4, color=C['gray'], fontfamily='sans-serif')

# Sample
ax.text(cx, 6.2, '34 US sector ETFs  |  11 GICS sectors + 23 sub-sectors',
        ha='center', fontsize=3.5, color=C['gray'], fontfamily='sans-serif')

# Arrow 2→3
draw_arrow(x1 + 0.3, panels_x[2][0] - 0.3, 20)

# ═══════════════════════════════════════
# STAGE 3: AGGREGATION MASKING
# ═══════════════════════════════════════
x0, x1 = panels_x[2]
draw_panel(x0, x1, 'AGGREGATION MASKING', C['dkred'])
cx = (x0 + x1) / 2

# Funnel: wide bars at top
bar_half = 9.0
top_y = 27.0
bar_h = 2.0

ax.add_patch(FancyBboxPatch((cx - bar_half, top_y), bar_half - 0.15, bar_h,
             boxstyle="round,pad=0.08", facecolor=C['palegreen'],
             edgecolor=C['dkgreen'], linewidth=0.4))
ax.add_patch(FancyBboxPatch((cx + 0.15, top_y), bar_half - 0.15, bar_h,
             boxstyle="round,pad=0.08", facecolor=C['palered'],
             edgecolor=C['dkred'], linewidth=0.4))
ax.text(cx - bar_half/2, top_y + bar_h/2, '+42.3%', ha='center', va='center',
        fontsize=5, fontweight='bold', color=C['dkgreen'], fontfamily='sans-serif')
ax.text(cx + bar_half/2, top_y + bar_h/2, '−16.6%', ha='center', va='center',
        fontsize=5, fontweight='bold', color=C['dkred'], fontfamily='sans-serif')

# Brace label
ax.text(cx, top_y + bar_h + 0.7, '59 pp sectoral range', ha='center',
        fontsize=4.5, fontweight='bold', color=C['charcoal'],
        fontfamily='sans-serif')

# Funnel lines
nw = 3.5
ny = 22.0
nh = 1.6
ax.plot([cx - bar_half, cx - nw/2], [top_y, ny + nh], color=C['steel'],
        lw=1.2, ls='--')
ax.plot([cx + bar_half, cx + nw/2], [top_y, ny + nh], color=C['steel'],
        lw=1.2, ls='--')

# Narrow bar: S&P 500
ax.add_patch(FancyBboxPatch((cx - nw/2, ny), nw, nh,
             boxstyle="round,pad=0.08", facecolor=C['paleamber'],
             edgecolor=C['amber'], linewidth=0.8))
ax.text(cx, ny + nh/2, '−1.81%', ha='center', va='center', fontsize=5.5,
        fontweight='bold', color=C['dkamber'], fontfamily='sans-serif')
ax.text(cx, ny - 0.7, 'S&P 500', ha='center', fontsize=4.5, color=C['steel'],
        fontfamily='sans-serif')

# Psi box
psi_y0 = 11.0
psi_y1 = 19.5
ax.add_patch(FancyBboxPatch((x0 + 1.5, psi_y0), x1 - x0 - 3, psi_y1 - psi_y0,
             boxstyle="round,pad=0.25", facecolor=C['palered'],
             edgecolor=C['red'], linewidth=0.8))

ax.text(x0 + 3.5, 18.0, '\u26A0', fontsize=7, color=C['red'], va='center')
ax.text(x0 + 5.5, 18.0, 'Novel Masking Index', fontsize=5, fontweight='bold',
        color=C['dkred'], va='center', fontfamily='sans-serif')

ax.text(cx, 15.8, r'$\Psi$ = 0.947', ha='center', fontsize=11,
        fontweight='bold', color=C['navy'], fontfamily='sans-serif')

# Proportion bar
pb_x0 = x0 + 2.5
pb_w = x1 - x0 - 5
pb_y = 12.5
pb_h = 1.0
ax.add_patch(FancyBboxPatch((pb_x0, pb_y), pb_w * 0.947, pb_h,
             boxstyle="square,pad=0", facecolor=C['softred'],
             edgecolor='none'))
ax.add_patch(FancyBboxPatch((pb_x0 + pb_w * 0.947, pb_y), pb_w * 0.053, pb_h,
             boxstyle="square,pad=0", facecolor=C['navy'],
             edgecolor='none'))
ax.text(pb_x0 + pb_w * 0.45, pb_y + pb_h/2, '~95% concealed', ha='center',
        va='center', fontsize=4, fontweight='bold', color='white',
        fontfamily='sans-serif')
ax.text(pb_x0 + pb_w * 0.975, pb_y + pb_h/2, '5%', ha='center',
        va='center', fontsize=3, fontweight='bold', color='white',
        fontfamily='sans-serif')

ax.text(cx, 11.5, 'Crisis: 0.947  vs  Normal: 0.851', ha='center',
        fontsize=4.5, color=C['charcoal'], fontfamily='sans-serif')

# Bottom notes
ax.text(cx, 8.5, 'Masking is worst when\naccuracy matters most', ha='center',
        fontsize=4.5, fontweight='bold', color=C['steel'],
        fontfamily='sans-serif', linespacing=1.3)
ax.text(cx, 6.5, '72 placebo tests  |  5 events', ha='center',
        fontsize=3.5, color=C['gray'], fontfamily='sans-serif')

# Arrow 3→4
draw_arrow(x1 + 0.3, panels_x[3][0] - 0.3, 20)

# ═══════════════════════════════════════
# STAGE 4: IMPLICATIONS
# ═══════════════════════════════════════
x0, x1 = panels_x[3]
draw_panel(x0, x1, 'IMPLICATIONS', C['titlebg'])
cx = (x0 + x1) / 2

# Supply box
sy0 = 25.0
sh = 3.8
ax.add_patch(FancyBboxPatch((x0 + 1, sy0), x1 - x0 - 2, sh,
             boxstyle="round,pad=0.15", facecolor=C['palegreen'],
             edgecolor=C['dkgreen'], linewidth=0.5))
ax.annotate('', xy=(x0 + 2.8, sy0 + sh - 0.5), xytext=(x0 + 2.8, sy0 + 0.5),
            arrowprops=dict(arrowstyle='->', color=C['dkgreen'], lw=1.8,
                            mutation_scale=11))
ax.text(x0 + 4.2, sy0 + 2.8, 'Supply Shocks', fontsize=5, fontweight='bold',
        color=C['dkgreen'], fontfamily='sans-serif')
ax.text(x0 + 4.2, sy0 + 1.5, r'$\gamma_1$ > 0  (4 events)', fontsize=4,
        color=C['steel'], fontfamily='sans-serif')

# Demand box
dy0 = 20.0
ax.add_patch(FancyBboxPatch((x0 + 1, dy0), x1 - x0 - 2, sh,
             boxstyle="round,pad=0.15", facecolor=C['palered'],
             edgecolor=C['dkred'], linewidth=0.5))
ax.annotate('', xy=(x0 + 2.8, dy0 + 0.5), xytext=(x0 + 2.8, dy0 + sh - 0.5),
            arrowprops=dict(arrowstyle='->', color=C['dkred'], lw=1.8,
                            mutation_scale=11))
ax.text(x0 + 4.2, dy0 + 2.6, 'Demand Shocks', fontsize=5, fontweight='bold',
        color=C['dkred'], fontfamily='sans-serif')
ax.text(x0 + 4.2, dy0 + 1.3, r'$\gamma_1$ < 0  (COVID flip)', fontsize=4,
        color=C['steel'], fontfamily='sans-serif')

# Who is affected
ax.text(cx, 18.2, 'Who Is Affected?', ha='center', fontsize=5.5,
        fontweight='bold', color=C['navy'], fontfamily='sans-serif')

stakeholders = [
    ('Policymakers', 'Index understates disruption'),
    ('Portfolio Mgrs', 'Benchmarks mislead'),
    ('Risk Managers', 'Index vol. uninformative'),
]
for i, (role, desc) in enumerate(stakeholders):
    yy = 16.0 - i * 2.8
    ax.add_patch(FancyBboxPatch((x0 + 1.2, yy - 0.5), x1 - x0 - 2.4, 2.2,
                 boxstyle="round,pad=0.12", facecolor=C['paleblue'],
                 edgecolor=C['mist'], linewidth=0.3))
    ax.text(cx, yy + 0.6, role, ha='center', fontsize=4.5, fontweight='bold',
            color=C['dkblue'], fontfamily='sans-serif')
    ax.text(cx, yy - 0.1, desc, ha='center', fontsize=3.5,
            color=C['steel'], fontfamily='sans-serif')

# Bottom note
ax.text(cx, 6.8, 'Index movements understate\ntrue economic disruption',
        ha='center', fontsize=4, fontweight='bold', color=C['steel'],
        fontfamily='sans-serif', linespacing=1.3)

# ── Save ──
out_tiff = '/home/user/paper_2026/paper/graphical_abstract.tiff'
out_png = '/home/user/paper_2026/paper/graphical_abstract.png'
fig.savefig(out_tiff, dpi=DPI, bbox_inches='tight', pad_inches=0, format='tiff')
fig.savefig(out_png, dpi=DPI, bbox_inches='tight', pad_inches=0, format='png')

print(f"Saved: {out_tiff}")
print(f"Saved: {out_png}")

from PIL import Image
img = Image.open(out_tiff)
print(f"Dimensions: {img.size[0]} x {img.size[1]} pixels (w x h)")
ratio = img.size[0] / img.size[1]
print(f"Aspect ratio: {ratio:.2f} (target: {1328/531:.2f})")
