#!/usr/bin/env python3
"""
Generate graphical abstract for:
"Geopolitical Oil Shocks, Sectoral Heterogeneity, and Aggregation Masking:
 Evidence from a Multi-Event Framework"

Elsevier specs: >=531 x 1328 px (h x w), TIFF preferred, readable at 5x13 cm.
Output: 2656 x 1062 px (2x minimum) at 300 DPI.

Color scheme: Navy + Green (winners) + Red (losers/masking) + Gray. Four families only.
Font: Arial throughout (sans-serif fallback).
Text hierarchy: Navy bold (headers) → Charcoal (body) → Gray (annotations). Three tiers.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.font_manager as fm
import numpy as np

# ── Font: Liberation Sans (metric-compatible Arial substitute) ──
# Falls back to DejaVu Sans if unavailable
_candidates = ['Liberation Sans', 'Arial', 'Helvetica', 'DejaVu Sans']
FONT = 'sans-serif'
for _f in _candidates:
    try:
        _path = fm.findfont(fm.FontProperties(family=_f), fallback_to_default=False)
        if _path:
            FONT = _f
            break
    except:
        continue

# ── Dimensions ──
DPI = 300
W_in = 2656 / DPI
H_in = 1062 / DPI
fig = plt.figure(figsize=(W_in, H_in), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 100)
ax.set_ylim(0, 40)
ax.axis('off')

# ══════════════════════════════════════════════════
# COLOR PALETTE — 4 families only
# ══════════════════════════════════════════════════
C = {
    # Navy family (headers, authority)
    'navy':      '#1A365D',
    'dkblue':    '#1E3A5F',
    'teal':      '#2B6CB0',   # accent borders only

    # Green family (winners/positive)
    'dkgreen':   '#276749',
    'green':     '#38A169',
    'palegreen': '#C6F6D5',

    # Red family (losers/masking/warning)
    'dkred':     '#C53030',
    'red':       '#E53E3E',
    'palered':   '#FED7D7',

    # Neutral family
    'charcoal':  '#2D3748',
    'steel':     '#4A5568',
    'gray':      '#718096',
    'silver':    '#A0AEC0',
    'mist':      '#E2E8F0',
    'panelbg':   '#EDF2F7',
    'white':     '#FFFFFF',

    # Frame
    'bg':        '#1A365D',   # navy background
    'titlebg':   '#1E3A5F',
    'bottombg':  '#111D2E',
    'softblue':  '#90CDF4',
}

# ── Background ──
ax.add_patch(FancyBboxPatch((0, 0), 100, 40, boxstyle="square,pad=0",
             facecolor=C['bg'], edgecolor='none'))

# ══════════════════════════════════════════════════
# TITLE BAR
# ══════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0, 34.5), 100, 5.5, boxstyle="square,pad=0",
             facecolor=C['titlebg'], edgecolor='none'))

# Full paper title — two lines
ax.text(50, 38.2,
        'Geopolitical Oil Shocks, Sectoral Heterogeneity, and Aggregation Masking:',
        ha='center', va='center', fontsize=8.5, fontweight='bold', color='white',
        fontfamily=FONT)
ax.text(50, 36.8,
        'Evidence from a Multi-Event Framework',
        ha='center', va='center', fontsize=8.5, fontweight='bold', color='white',
        fontfamily=FONT)

# Take-home message — italic, smaller, differentiated
ax.text(50, 35.5,
        'Aggregate indices conceal ~95% of sectoral disruption — '
        'oil sensitivity predicts which sectors win and lose',
        ha='center', va='center', fontsize=5, color=C['softblue'],
        fontfamily=FONT, style='italic')

# ══════════════════════════════════════════════════
# BOTTOM CONCLUSION STRIP
# ══════════════════════════════════════════════════
ax.add_patch(FancyBboxPatch((0, 0), 100, 5.0, boxstyle="square,pad=0",
             facecolor=C['bottombg'], edgecolor='none'))
ax.text(50, 3.5,
        r'Oil sensitivity ($\beta_{oil}$) predicts sectoral winners and losers '
        r'across geopolitical shocks,',
        ha='center', fontsize=5.5, fontweight='bold', color=C['softblue'],
        fontfamily=FONT)
ax.text(50, 2.0,
        r'but cap-weighted indices conceal ~95% of this heterogeneity '
        r'($\Psi$ = 0.947)',
        ha='center', fontsize=5.5, fontweight='bold', color=C['softblue'],
        fontfamily=FONT)
ax.text(2, 0.6, 'Saxena & Yang (2026)', fontsize=3.5, color=C['silver'],
        fontfamily=FONT)
ax.text(50, 0.6, 'College of Management, Yuan Ze University, Taiwan',
        ha='center', fontsize=3.5, color=C['silver'], fontfamily=FONT)
ax.text(98, 0.6, 'Research in International Business and Finance',
        ha='right', fontsize=3.5, color=C['silver'], fontfamily=FONT,
        style='italic')

# ══════════════════════════════════════════════════
# PANEL HELPERS
# ══════════════════════════════════════════════════
panel_y0 = 5.5
panel_y1 = 34.0
hdr_h = 2.3

panels_x = [
    (1.0,  23.0),   # Stage 1
    (26.5, 49.5),   # Stage 2
    (53.0, 76.0),   # Stage 3
    (79.5, 99.0),   # Stage 4
]

def draw_panel(x0, x1, header_text, header_color):
    w, h = x1 - x0, panel_y1 - panel_y0
    ax.add_patch(FancyBboxPatch((x0, panel_y0), w, h,
                 boxstyle="round,pad=0.3", facecolor=C['white'],
                 edgecolor=C['mist'], linewidth=0.5))
    ax.add_patch(FancyBboxPatch((x0 + 0.15, panel_y1 - hdr_h), w - 0.3, hdr_h - 0.1,
                 boxstyle="round,pad=0.15", facecolor=header_color,
                 edgecolor='none'))
    ax.text((x0 + x1) / 2, panel_y1 - hdr_h / 2, header_text,
            ha='center', va='center', fontsize=6.5, fontweight='bold',
            color='white', fontfamily=FONT)

def draw_arrow(x_start, x_end, y):
    ax.annotate('', xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle='->', color=C['silver'],
                                lw=2.0, mutation_scale=13))

# ══════════════════════════════════════════════════
# STAGE 1: GEOPOLITICAL OIL SHOCK
# ══════════════════════════════════════════════════
x0, x1 = panels_x[0]
draw_panel(x0, x1, 'GEOPOLITICAL OIL SHOCK', C['navy'])
cx = (x0 + x1) / 2

# Price spike — clean red up-arrow with USO label (no barrel clutter)
arrow_x = cx - 1.5
arrow_by, arrow_ty = 25.0, 29.5
ax.annotate('', xy=(arrow_x, arrow_ty), xytext=(arrow_x, arrow_by),
            arrowprops=dict(arrowstyle='->', color=C['dkred'], lw=3.0,
                            mutation_scale=18))
ax.text(arrow_x + 1.5, 28.2, '+42.3%', fontsize=7.5, fontweight='bold',
        color=C['dkred'], fontfamily=FONT)
ax.text(arrow_x + 1.5, 26.8, 'USO (Oil ETF)', fontsize=4.5,
        color=C['steel'], fontfamily=FONT)
ax.text(arrow_x + 1.5, 25.6, 'Oil prices surged', fontsize=4.5,
        color=C['steel'], fontfamily=FONT)

# Event name — spaced below the arrow block
ax.text(cx, 23.5, 'Strait of Hormuz 2026', ha='center', fontsize=6.5,
        fontweight='bold', color=C['navy'], fontfamily=FONT)
ax.text(cx, 21.8, '~21% of global oil consumption\ntransits Hormuz',
        ha='center', fontsize=4.5, color=C['steel'], fontfamily=FONT,
        linespacing=1.3)

# Divider
ax.plot([x0 + 2, x1 - 2], [19.8, 19.8], color=C['mist'], lw=0.5)

# Validated across 5 events
ax.text(cx, 18.8, 'Validated Across 5 Events', ha='center', fontsize=5.5,
        fontweight='bold', color=C['navy'], fontfamily=FONT)

events = [
    ('Hormuz 2026',          'Supply', C['dkgreen']),
    ('Russia\u2013Ukraine 2022', 'Supply', C['dkgreen']),
    ('OPEC+ Cut 2022',       'Supply', C['dkgreen']),
    ('Middle East 2023',     'Supply', C['dkgreen']),
    ('COVID-19 2020',        'Demand', C['dkred']),
]
for i, (name, typ, col) in enumerate(events):
    yy = 17.3 - i * 2.0
    ax.plot(x0 + 2.5, yy, 'o', color=col, markersize=3.5)
    ax.text(x0 + 3.8, yy, name, fontsize=4, va='center', color=C['steel'],
            fontfamily=FONT)
    ax.text(x1 - 2, yy, typ, fontsize=4, va='center', ha='right',
            fontweight='bold', color=col, fontfamily=FONT)

# Arrow 1→2
draw_arrow(x1 + 0.3, panels_x[1][0] - 0.3, 20)

# ══════════════════════════════════════════════════
# STAGE 2: SECTORAL DIVERGENCE
# ══════════════════════════════════════════════════
x0, x1 = panels_x[1]
draw_panel(x0, x1, 'SECTORAL DIVERGENCE', C['navy'])
cx = (x0 + x1) / 2

# Scatter plot area — WHITE background (not gray)
px0, px1 = x0 + 3.0, x1 - 1.5
py0, py1 = 17.0, 29.5
mid_y = (py0 + py1) / 2

# No separate background box — draw directly on panel white
# Just a subtle border to frame the plot area
ax.add_patch(FancyBboxPatch((px0 - 0.8, py0 - 0.3), px1 - px0 + 1.6, py1 - py0 + 0.6,
             boxstyle="round,pad=0.15", facecolor='none',
             edgecolor=C['mist'], linewidth=0.3))

# Axes
ax.annotate('', xy=(px0, py1 + 0.2), xytext=(px0, py0 - 0.2),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'], lw=0.8))
ax.annotate('', xy=(px1 + 0.2, mid_y), xytext=(px0 - 0.2, mid_y),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'], lw=0.8))

# Axis labels — charcoal
ax.text(px0 - 1.8, (py0 + py1) / 2, 'CAR (%)', ha='center', va='center',
        fontsize=4, fontweight='bold', color=C['charcoal'],
        fontfamily=FONT, rotation=90)
ax.text((px0 + px1) / 2, py0 - 1.2, r'Oil Sensitivity ($\beta_{oil}$)',
        ha='center', fontsize=4, fontweight='bold', color=C['charcoal'],
        fontfamily=FONT)

# Zero label
ax.text(px0 - 0.6, mid_y, '0', fontsize=3.5, color=C['gray'],
        ha='center', va='center', fontfamily=FONT)

# Regression line — navy
ax.plot([px0 + 0.5, px1 - 0.5], [mid_y - 5.0, mid_y + 5.5],
        color=C['navy'], lw=1.8, zorder=3)

# Winners — only label extremes (USO)
win_data = [
    (px1 - 1.5, mid_y + 4.5, 'USO', True),
    (px1 - 3.0, mid_y + 3.2, 'XOP', False),
    (px1 - 4.0, mid_y + 2.5, 'FCG', False),
    (px1 - 4.8, mid_y + 1.8, '', False),
]
for wx, wy, wl, label_it in win_data:
    ax.plot(wx, wy, 'o', color=C['dkgreen'], markersize=4.5 if label_it else 3.5, zorder=4)
    if label_it:
        ax.text(wx + 0.5, wy + 0.4, wl, fontsize=4.5, fontweight='bold',
                color=C['dkgreen'], fontfamily=FONT, zorder=4)

# Middle sectors — gray
for mx, my in [(px0 + 5, mid_y + 0.3), (px0 + 6, mid_y - 0.3),
               (px0 + 7, mid_y + 0.6), (px0 + 8, mid_y + 0.1),
               (px0 + 4.5, mid_y - 0.5), (px0 + 5.5, mid_y + 0.9)]:
    ax.plot(mx, my, 'o', color=C['silver'], markersize=3, zorder=4)

# Losers — only label extremes (ITB)
lose_data = [
    (px0 + 1.5, mid_y - 4.2, 'ITB', True),
    (px0 + 2.5, mid_y - 3.5, '', False),
    (px0 + 1.0, mid_y - 3.7, '', False),
    (px0 + 3.2, mid_y - 2.5, '', False),
]
for lx, ly, ll, label_it in lose_data:
    ax.plot(lx, ly, 'o', color=C['dkred'], markersize=4.5 if label_it else 3.5, zorder=4)
    if label_it:
        ax.text(lx - 0.3, ly - 0.7, ll, fontsize=4.5, fontweight='bold',
                color=C['dkred'], ha='center', fontfamily=FONT, zorder=4)

# Key stat box
sy0, sy1 = 7.0, 15.5
ax.add_patch(FancyBboxPatch((x0 + 1.5, sy0), x1 - x0 - 3, sy1 - sy0,
             boxstyle="round,pad=0.25", facecolor=C['white'],
             edgecolor=C['navy'], linewidth=0.7))

ax.text(cx, 13.5, r'$\gamma_1$ = +20.18***', ha='center', fontsize=11,
        fontweight='bold', color=C['navy'], fontfamily=FONT)
ax.text(cx, 11.5, '1 s.d. oil sensitivity predicts\n18\u201321 pp higher CARs',
        ha='center', fontsize=4.5, color=C['steel'], fontfamily=FONT,
        linespacing=1.4)
ax.text(cx, 9.5, r'$R^2$ = 0.42  |  Bootstrap CI: [15.3, 31.6]',
        ha='center', fontsize=4, color=C['gray'], fontfamily=FONT)

# Dynamic persistence — key robustness finding
ax.text(cx, 8.0, 'Builds over time: +4.5 (t+1) \u2192 +25.1 (t+15)',
        ha='center', fontsize=4, color=C['gray'], fontfamily=FONT)

# Sample
ax.text(cx, 6.2, '34 US sector ETFs  |  11 GICS sectors + 23 sub-sectors',
        ha='center', fontsize=3.5, color=C['gray'], fontfamily=FONT)

# Arrow 2→3
draw_arrow(x1 + 0.3, panels_x[2][0] - 0.3, 20)

# ══════════════════════════════════════════════════
# STAGE 3: AGGREGATION MASKING
# ══════════════════════════════════════════════════
x0, x1 = panels_x[2]
draw_panel(x0, x1, 'AGGREGATION MASKING', C['dkred'])
cx = (x0 + x1) / 2

# Funnel: wide bars at top — green winners, red losers
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
        fontsize=5, fontweight='bold', color=C['dkgreen'], fontfamily=FONT)
ax.text(cx + bar_half/2, top_y + bar_h/2, '\u221216.6%', ha='center', va='center',
        fontsize=5, fontweight='bold', color=C['dkred'], fontfamily=FONT)

# Brace label
ax.text(cx, top_y + bar_h + 0.7, '59 pp sectoral range', ha='center',
        fontsize=4.5, fontweight='bold', color=C['charcoal'], fontfamily=FONT)

# Funnel lines — red dashed (warning color, not neutral gray)
nw = 3.5
ny = 22.0
nh = 1.6
ax.plot([cx - bar_half, cx - nw/2], [top_y, ny + nh], color=C['dkred'],
        lw=1.0, ls='--', alpha=0.6)
ax.plot([cx + bar_half, cx + nw/2], [top_y, ny + nh], color=C['dkred'],
        lw=1.0, ls='--', alpha=0.6)

# S&P 500 — WHITE box with RED border (warning, not gold)
# Use solid red border (FancyBboxPatch doesn't support dashed on rounded)
ax.add_patch(FancyBboxPatch((cx - nw/2, ny), nw, nh,
             boxstyle="round,pad=0.08", facecolor=C['white'],
             edgecolor=C['dkred'], linewidth=1.2))
ax.text(cx, ny + nh/2, '\u22121.81%', ha='center', va='center', fontsize=5.5,
        fontweight='bold', color=C['dkred'], fontfamily=FONT)
ax.text(cx, ny - 0.7, 'S&P 500', ha='center', fontsize=4.5,
        fontweight='bold', color=C['steel'], fontfamily=FONT)

# Psi metric box — palered with strong red border
psi_y0, psi_y1 = 11.0, 19.5
ax.add_patch(FancyBboxPatch((x0 + 1.5, psi_y0), x1 - x0 - 3, psi_y1 - psi_y0,
             boxstyle="round,pad=0.25", facecolor=C['palered'],
             edgecolor=C['dkred'], linewidth=0.8))

ax.text(x0 + 3.5, 18.0, '\u26A0', fontsize=7, color=C['dkred'], va='center')
ax.text(x0 + 5.5, 18.0, 'Novel Masking Index', fontsize=5, fontweight='bold',
        color=C['dkred'], va='center', fontfamily=FONT)

ax.text(cx, 15.8, r'$\Psi$ = 0.947', ha='center', fontsize=11,
        fontweight='bold', color=C['navy'], fontfamily=FONT)

# Proportion bar — STRONG red (not pastel) for concealed portion
pb_x0 = x0 + 2.5
pb_w = x1 - x0 - 5
pb_y = 13.0
pb_h = 1.2
# Red portion (95%) — strong, matches loser color
ax.add_patch(FancyBboxPatch((pb_x0, pb_y), pb_w * 0.94, pb_h,
             boxstyle="square,pad=0", facecolor=C['red'],
             edgecolor='none'))
# Navy portion (5%) — slightly wider for visibility at 300 DPI
ax.add_patch(FancyBboxPatch((pb_x0 + pb_w * 0.94, pb_y), pb_w * 0.06, pb_h,
             boxstyle="square,pad=0", facecolor=C['navy'],
             edgecolor='none'))
ax.text(pb_x0 + pb_w * 0.45, pb_y + pb_h/2, '~95% concealed', ha='center',
        va='center', fontsize=4.5, fontweight='bold', color='white',
        fontfamily=FONT)
ax.text(pb_x0 + pb_w * 0.97, pb_y + pb_h/2, '5%', ha='center',
        va='center', fontsize=3.5, fontweight='bold', color='white',
        fontfamily=FONT)

# Crisis vs Normal
ax.text(cx, 12.0, 'Crisis: 0.947  vs  Normal: 0.851', ha='center',
        fontsize=4.5, color=C['charcoal'], fontfamily=FONT)

# Bottom notes
ax.text(cx, 8.5, 'Masking is worst when\naccuracy matters most', ha='center',
        fontsize=4.5, fontweight='bold', color=C['steel'],
        fontfamily=FONT, linespacing=1.3)
ax.text(cx, 6.5, '72 placebo tests  |  5 events', ha='center',
        fontsize=3.5, color=C['gray'], fontfamily=FONT)

# Arrow 3→4
draw_arrow(x1 + 0.3, panels_x[3][0] - 0.3, 20)

# ══════════════════════════════════════════════════
# STAGE 4: IMPLICATIONS
# ══════════════════════════════════════════════════
x0, x1 = panels_x[3]
draw_panel(x0, x1, 'IMPLICATIONS', C['navy'])
cx = (x0 + x1) / 2

# Supply box — WHITE with green left-border accent
sy0 = 26.0
sh = 3.5
# White background
ax.add_patch(FancyBboxPatch((x0 + 1, sy0), x1 - x0 - 2, sh,
             boxstyle="round,pad=0.12", facecolor=C['white'],
             edgecolor=C['mist'], linewidth=0.4))
# Green left border accent
ax.add_patch(FancyBboxPatch((x0 + 1, sy0), 0.6, sh,
             boxstyle="square,pad=0", facecolor=C['dkgreen'],
             edgecolor='none'))
ax.text(x0 + 3, sy0 + 2.4, 'Supply Shocks', fontsize=5, fontweight='bold',
        color=C['dkgreen'], fontfamily=FONT)
ax.text(x0 + 3, sy0 + 1.2, r'$\gamma_1$ > 0  (4 events)', fontsize=4,
        color=C['steel'], fontfamily=FONT)

# Demand box — WHITE with red left-border accent
dy0 = 21.5
ax.add_patch(FancyBboxPatch((x0 + 1, dy0), x1 - x0 - 2, sh,
             boxstyle="round,pad=0.12", facecolor=C['white'],
             edgecolor=C['mist'], linewidth=0.4))
# Red left border accent
ax.add_patch(FancyBboxPatch((x0 + 1, dy0), 0.6, sh,
             boxstyle="square,pad=0", facecolor=C['dkred'],
             edgecolor='none'))
ax.text(x0 + 3, dy0 + 2.4, 'Demand Shocks', fontsize=5, fontweight='bold',
        color=C['dkred'], fontfamily=FONT)
ax.text(x0 + 3, dy0 + 1.2, r'$\gamma_1$ < 0  (COVID reversal)', fontsize=4,
        color=C['steel'], fontfamily=FONT)

# Interaction coefficient — strongest test statistic
ax.add_patch(FancyBboxPatch((x0 + 1, 19.0), x1 - x0 - 2, 2.0,
             boxstyle="round,pad=0.1", facecolor=C['white'],
             edgecolor=C['navy'], linewidth=0.5))
ax.text(cx, 20.0, r'$\beta_{oil}$ $\times$ Supply = +58.79***',
        ha='center', fontsize=4.5, fontweight='bold', color=C['navy'],
        fontfamily=FONT)
ax.text(cx, 19.3, 't = 5.22, strongest test',
        ha='center', fontsize=3.5, color=C['gray'], fontfamily=FONT)

# Who is affected — white cards with navy left-border accent
ax.text(cx, 17.6, 'Who Is Affected?', ha='center', fontsize=5.5,
        fontweight='bold', color=C['navy'], fontfamily=FONT)

stakeholders = [
    ('Policymakers', 'Index understates disruption'),
    ('Portfolio Managers', 'Benchmarks mislead'),
    ('Risk Managers', 'Index volatility uninformative'),
]
for i, (role, desc) in enumerate(stakeholders):
    yy = 15.8 - i * 2.5
    card_h = 1.8
    # White card
    ax.add_patch(FancyBboxPatch((x0 + 1.2, yy - 0.3), x1 - x0 - 2.4, card_h,
                 boxstyle="round,pad=0.1", facecolor=C['white'],
                 edgecolor=C['mist'], linewidth=0.3))
    # Navy left-border accent
    ax.add_patch(FancyBboxPatch((x0 + 1.2, yy - 0.3), 0.5, card_h,
                 boxstyle="square,pad=0", facecolor=C['navy'],
                 edgecolor='none'))
    ax.text(cx + 0.3, yy + 0.6, role, ha='center', fontsize=4.5,
            fontweight='bold', color=C['navy'], fontfamily=FONT)
    ax.text(cx + 0.3, yy, desc, ha='center', fontsize=3.5,
            color=C['steel'], fontfamily=FONT)

# ── Save ──
out_tiff = '/home/user/paper_2026/paper/graphical_abstract.tiff'
out_png = '/home/user/paper_2026/paper/graphical_abstract.png'
fig.savefig(out_tiff, dpi=DPI, bbox_inches='tight', pad_inches=0, format='tiff')
fig.savefig(out_png, dpi=DPI, bbox_inches='tight', pad_inches=0, format='png')

print(f"Saved: {out_tiff}")
print(f"Saved: {out_png}")

from PIL import Image
img = Image.open(out_tiff)
w, h = img.size
print(f"Dimensions: {w} x {h} pixels (w x h)")
print(f"Aspect ratio: {w/h:.2f} (target: {1328/531:.2f})")
print(f"Meets minimum: {'YES' if w >= 1328 and h >= 531 else 'NO'}")
print(f"DPI: {DPI}")
print(f"Font used: {FONT}")

# ── Thumbnail test: ScienceDirect preview ~500x200 px ──
thumb = img.resize((500, 200), Image.LANCZOS)
thumb_path = '/home/user/paper_2026/paper/graphical_abstract_thumbnail.png'
thumb.save(thumb_path)
print(f"Thumbnail saved: {thumb_path} (500x200 — check readability)")
