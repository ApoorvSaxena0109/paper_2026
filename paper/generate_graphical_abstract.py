#!/usr/bin/env python3
"""
Generate graphical abstract for:
"Geopolitical Oil Shocks, Sectoral Heterogeneity, and Aggregation Masking:
 Evidence from a Multi-Event Framework"

Design: Prof. Yang's flow structure + enriched with key conceptual findings.
- Big fonts, no regression tables
- Simple intuitive numbers only (percentages, Psi)
- Relationships and contrasts, not coefficients
- Supply vs Demand asymmetry (H4)
- Psi = 0.947 (~95%) — novel metric, not a regression stat

Elsevier: >=531 x 1328 px (h x w), PDF preferred, readable at 5x13 cm.
Output: 2656 x 1062 px at 300 DPI.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.font_manager as fm

# ── Font ──
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
# COLORS
# ══════════════════════════════════════════════════
C = {
    'blue':      '#2563EB',
    'ltblue':    '#93C5FD',
    'navy':      '#1A365D',
    'amber':     '#F59E0B',
    'dkamber':   '#92400E',
    'green':     '#16A34A',
    'dkgreen':   '#166534',
    'red':       '#DC2626',
    'dkred':     '#991B1B',
    'charcoal':  '#1F2937',
    'steel':     '#4B5563',
    'gray':      '#6B7280',
    'silver':    '#9CA3AF',
    'lightgray': '#F3F4F6',
    'mist':      '#E5E7EB',
    'white':     '#FFFFFF',
}

# ── White background ──
ax.add_patch(FancyBboxPatch((0, 0), 100, 40, boxstyle="square,pad=0",
             facecolor=C['white'], edgecolor='none'))

# ══════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════
ax.text(50, 38.0,
        'Do Aggregate Indices Mask Economic Disruptions?',
        ha='center', va='center', fontsize=14, fontweight='bold',
        color=C['charcoal'], fontfamily=FONT)

ax.text(50, 35.8,
        'Geopolitical Oil Shocks, Sectoral Heterogeneity, and Aggregation Masking: '
        'Evidence from a Multi-Event Framework',
        ha='center', va='center', fontsize=5.5, color=C['gray'],
        fontfamily=FONT, style='italic')

# ══════════════════════════════════════════════════
# BOX 1: OIL SHOCK (blue, left)
# ══════════════════════════════════════════════════
b1_x, b1_y, b1_w, b1_h = 2, 13, 18, 20
ax.add_patch(FancyBboxPatch((b1_x, b1_y), b1_w, b1_h,
             boxstyle="round,pad=0.4", facecolor=C['blue'],
             edgecolor='none'))

ax.text(b1_x + b1_w/2, b1_y + b1_h - 3, 'Oil Shock',
        ha='center', va='center', fontsize=15, fontweight='bold',
        color=C['white'], fontfamily=FONT)

# Divider line inside blue box
ax.plot([b1_x + 2, b1_x + b1_w - 2],
        [b1_y + b1_h - 5.5, b1_y + b1_h - 5.5],
        color=C['ltblue'], lw=0.6, alpha=0.5)

# Supply shocks
ax.text(b1_x + b1_w/2, b1_y + b1_h - 7.5, '4 Supply Shocks',
        ha='center', va='center', fontsize=8.5, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b1_x + b1_w/2, b1_y + b1_h - 9.5,
        'Hormuz \u2022 Russia\u2013Ukraine\nOPEC+ \u2022 Middle East',
        ha='center', va='center', fontsize=6, color=C['ltblue'],
        fontfamily=FONT, linespacing=1.5)

# Demand shock
ax.text(b1_x + b1_w/2, b1_y + 5.5, '1 Demand Shock',
        ha='center', va='center', fontsize=8.5, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b1_x + b1_w/2, b1_y + 3.5, 'COVID-19',
        ha='center', va='center', fontsize=6, color=C['ltblue'],
        fontfamily=FONT)

# Sample scope
ax.text(b1_x + b1_w/2, b1_y + 1.2, '34 ETFs  \u2022  2020\u20132026',
        ha='center', va='center', fontsize=5, color=C['ltblue'],
        fontfamily=FONT, alpha=0.8)

# ══════════════════════════════════════════════════
# ARROW: Box 1 → Box 2
# ══════════════════════════════════════════════════
ax.annotate('', xy=(24, b1_y + b1_h/2),
            xytext=(b1_x + b1_w + 0.5, b1_y + b1_h/2),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'],
                            lw=2.5, mutation_scale=20))

# ══════════════════════════════════════════════════
# BOX 2: SECTORAL RESPONSES (center)
# ══════════════════════════════════════════════════
b2_x, b2_y, b2_w, b2_h = 24.5, 13, 26, 20
ax.add_patch(FancyBboxPatch((b2_x, b2_y), b2_w, b2_h,
             boxstyle="round,pad=0.4", facecolor=C['white'],
             edgecolor=C['mist'], linewidth=1.5))

ax.text(b2_x + b2_w/2, b2_y + b2_h - 2.5, 'Sectoral Responses',
        ha='center', va='center', fontsize=13, fontweight='bold',
        color=C['charcoal'], fontfamily=FONT)

# ── Supply side: winners & losers ──
ax.text(b2_x + 2.5, b2_y + b2_h - 5.5, 'Supply shocks:',
        va='center', fontsize=7.5, color=C['steel'], fontfamily=FONT,
        style='italic')

ax.text(b2_x + 3, b2_y + b2_h - 8, '\u25B2',
        va='center', fontsize=12, color=C['red'], fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + b2_h - 8, 'High Oil Beta  \u2192  Winners',
        va='center', fontsize=9.5, fontweight='bold', color=C['red'],
        fontfamily=FONT)

ax.text(b2_x + 3, b2_y + b2_h - 10.5, '\u25BC',
        va='center', fontsize=12, color=C['blue'], fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + b2_h - 10.5, 'Low Oil Beta  \u2192  Losers',
        va='center', fontsize=9.5, fontweight='bold', color=C['blue'],
        fontfamily=FONT)

# Divider
ax.plot([b2_x + 2, b2_x + b2_w - 2],
        [b2_y + 5.5, b2_y + 5.5],
        color=C['mist'], lw=0.8)

# ── Demand side: all fall ──
ax.text(b2_x + 2.5, b2_y + 4, 'Demand shocks:',
        va='center', fontsize=7.5, color=C['steel'], fontfamily=FONT,
        style='italic')

ax.text(b2_x + 3, b2_y + 2, '\u25BC',
        va='center', fontsize=10, color=C['gray'], fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + 2, 'All sectors fall together',
        va='center', fontsize=9, fontweight='bold', color=C['gray'],
        fontfamily=FONT)


# ══════════════════════════════════════════════════
# ARROWS: Box 2 → Box 3a (top) and Box 2 → Box 3b (bottom)
# ══════════════════════════════════════════════════
# Arrow to Aggregate Index
ax.annotate('', xy=(57, 28),
            xytext=(b2_x + b2_w + 0.5, 28),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'],
                            lw=2.5, mutation_scale=20))

# Arrow to Reality
ax.annotate('', xy=(57, 18),
            xytext=(b2_x + b2_w + 0.5, 18),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'],
                            lw=2.5, mutation_scale=20))


# ══════════════════════════════════════════════════
# BOX 3a: AGGREGATE INDEX (amber, top right)
# ══════════════════════════════════════════════════
b3a_x, b3a_y, b3a_w, b3a_h = 57.5, 23, 24, 10
ax.add_patch(FancyBboxPatch((b3a_x, b3a_y), b3a_w, b3a_h,
             boxstyle="round,pad=0.4", facecolor=C['amber'],
             edgecolor='none'))

ax.text(b3a_x + b3a_w/2, b3a_y + b3a_h - 2.5, 'Aggregate Index',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b3a_x + b3a_w/2, b3a_y + b3a_h/2 - 1, 'S&P 500:  \u22121.81%',
        ha='center', va='center', fontsize=11, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b3a_x + b3a_w/2, b3a_y + 1.5, 'Looks calm',
        ha='center', va='center', fontsize=8, color=C['white'],
        fontfamily=FONT, alpha=0.85)


# ══════════════════════════════════════════════════
# "not equal" symbol between the two right boxes
# ══════════════════════════════════════════════════
ax.text(b3a_x + b3a_w/2, 22, '\u2260',
        ha='center', va='center', fontsize=18, fontweight='bold',
        color=C['dkred'], fontfamily=FONT)


# ══════════════════════════════════════════════════
# BOX 3b: REALITY (green, bottom right)
# ══════════════════════════════════════════════════
b3b_x, b3b_y, b3b_w, b3b_h = 57.5, 13, 24, 8
ax.add_patch(FancyBboxPatch((b3b_x, b3b_y), b3b_w, b3b_h,
             boxstyle="round,pad=0.4", facecolor=C['green'],
             edgecolor='none'))

ax.text(b3b_x + b3b_w/2, b3b_y + b3b_h - 2, 'Reality',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b3b_x + b3b_w/2, b3b_y + b3b_h/2 - 1, '59 pp sectoral range',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b3b_x + b3b_w/2, b3b_y + 1.3, '+42% to \u221217% across sectors',
        ha='center', va='center', fontsize=7, color=C['white'],
        fontfamily=FONT, alpha=0.85)

# ── Right-side brace label ──
# "~95% concealed" as the punchline next to the two boxes
ax.add_patch(FancyBboxPatch((83, 15), 16, 16,
             boxstyle="round,pad=0.3", facecolor=C['lightgray'],
             edgecolor=C['mist'], linewidth=0.8))

ax.text(91, 27, '~95%', ha='center', va='center',
        fontsize=16, fontweight='bold', color=C['dkred'], fontfamily=FONT)
ax.text(91, 24, 'of sectoral\ndisruption\nconcealed', ha='center', va='center',
        fontsize=7.5, color=C['steel'], fontfamily=FONT, linespacing=1.4)

ax.text(91, 19.5, '\u03A8 = 0.947', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C['charcoal'], fontfamily=FONT)
ax.text(91, 17.5, 'Aggregation\nMasking Index', ha='center', va='center',
        fontsize=6, color=C['gray'], fontfamily=FONT, linespacing=1.3)

# ══════════════════════════════════════════════════
# BOTTOM BAR
# ══════════════════════════════════════════════════
bar_y = 5.5
bar_h = 5.5
ax.add_patch(FancyBboxPatch((2, bar_y), 96, bar_h,
             boxstyle="round,pad=0.3", facecolor=C['lightgray'],
             edgecolor=C['mist'], linewidth=1))

ax.text(50, bar_y + bar_h/2 + 0.5,
        'Masking is significantly stronger during crises than non-event periods',
        ha='center', va='center', fontsize=9, fontweight='bold',
        color=C['charcoal'], fontfamily=FONT)
ax.text(50, bar_y + bar_h/2 - 1.5,
        'Index-level responses understate economically meaningful heterogeneity '
        'for investors and policymakers',
        ha='center', va='center', fontsize=6.5, color=C['steel'],
        fontfamily=FONT)

# ── Citation ──
ax.text(50, 2.5, 'Saxena & Yang (2026)  \u2022  '
        'College of Management, Yuan Ze University  \u2022  '
        'Research in International Business and Finance',
        ha='center', fontsize=4.5, color=C['silver'], fontfamily=FONT)

# ── Save ──
out_tiff = '/home/user/paper_2026/paper/graphical_abstract.tiff'
out_png = '/home/user/paper_2026/paper/graphical_abstract.png'
out_pdf = '/home/user/paper_2026/paper/graphical_abstract.pdf'

fig.savefig(out_tiff, dpi=DPI, bbox_inches='tight', pad_inches=0, format='tiff')
fig.savefig(out_png, dpi=DPI, bbox_inches='tight', pad_inches=0, format='png')
fig.savefig(out_pdf, dpi=DPI, bbox_inches='tight', pad_inches=0, format='pdf')

print(f"Saved all three formats")

from PIL import Image
img = Image.open(out_tiff)
w, h = img.size
print(f"Dimensions: {w} x {h} px | Ratio: {w/h:.2f} | Min met: {w>=1328 and h>=531}")
print(f"DPI: {DPI} | Font: {FONT}")

thumb = img.resize((500, 200), Image.LANCZOS)
thumb.save('/home/user/paper_2026/paper/graphical_abstract_thumbnail.png')
print("Thumbnail saved (500x200)")
