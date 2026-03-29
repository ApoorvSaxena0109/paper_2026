#!/usr/bin/env python3
"""
Generate graphical abstract for:
"Geopolitical Oil Shocks, Sectoral Heterogeneity, and Aggregation Masking:
 Evidence from a Multi-Event Framework"

Redesigned per Prof. Yang's feedback:
- Much larger fonts
- No detailed regression statistics
- Focus on relationships, simple intuitive numbers
- Simple conceptual flow: Oil Shock → Sectoral Responses → Aggregate vs Reality
- Bottom bar: Aggregation Masking Index

Elsevier specs: >=531 x 1328 px (h x w), PDF preferred, readable at 5x13 cm.
Output: 2656 x 1062 px (2x minimum) at 300 DPI.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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
# COLORS — clean, matching Prof. Yang's sketch
# ══════════════════════════════════════════════════
C = {
    'blue':      '#2563EB',   # Oil shock box (like Yang's sketch)
    'dkblue':    '#1E3A5F',
    'navy':      '#1A365D',
    'amber':     '#F59E0B',   # Aggregate index (like Yang's gold)
    'dkamber':   '#92400E',
    'green':     '#16A34A',   # Reality box (like Yang's green)
    'dkgreen':   '#166534',
    'red':       '#DC2626',   # High oil beta / warning
    'dkred':     '#991B1B',
    'charcoal':  '#1F2937',
    'steel':     '#4B5563',
    'gray':      '#6B7280',
    'silver':    '#9CA3AF',
    'lightgray': '#F3F4F6',
    'mist':      '#E5E7EB',
    'white':     '#FFFFFF',
}

# ── White background (clean, like Yang's sketch) ──
ax.add_patch(FancyBboxPatch((0, 0), 100, 40, boxstyle="square,pad=0",
             facecolor=C['white'], edgecolor='none'))

# ══════════════════════════════════════════════════
# TITLE — Big question (like Yang's sketch)
# ══════════════════════════════════════════════════
ax.text(50, 37.5,
        'Do Aggregate Indices Mask Economic Disruptions?',
        ha='center', va='center', fontsize=14, fontweight='bold',
        color=C['charcoal'], fontfamily=FONT)

# Subtitle — paper title
ax.text(50, 35.5,
        'Geopolitical Oil Shocks, Sectoral Heterogeneity, and Aggregation Masking: '
        'Evidence from a Multi-Event Framework',
        ha='center', va='center', fontsize=6, color=C['gray'],
        fontfamily=FONT, style='italic')

# ══════════════════════════════════════════════════
# FLOW: Three main boxes + split to two outcomes
# Layout follows Yang's sketch exactly
# ══════════════════════════════════════════════════

# ── BOX 1: OIL SHOCK (blue, left) ──
b1_x, b1_y, b1_w, b1_h = 3, 16, 18, 14
ax.add_patch(FancyBboxPatch((b1_x, b1_y), b1_w, b1_h,
             boxstyle="round,pad=0.4", facecolor=C['blue'],
             edgecolor='none'))

ax.text(b1_x + b1_w/2, b1_y + b1_h - 3, 'Oil Shock',
        ha='center', va='center', fontsize=14, fontweight='bold',
        color=C['white'], fontfamily=FONT)

ax.text(b1_x + b1_w/2, b1_y + b1_h/2 - 1.5, '5 Geopolitical Events',
        ha='center', va='center', fontsize=9, color=C['white'],
        fontfamily=FONT)

ax.text(b1_x + b1_w/2, b1_y + 3, 'Hormuz, Russia\u2013Ukraine,\nOPEC+, Middle East, COVID',
        ha='center', va='center', fontsize=6.5, color='#B3D4FF',
        fontfamily=FONT, linespacing=1.5)

# ── BOX 2: SECTORAL RESPONSES (white/outlined, center) ──
b2_x, b2_y, b2_w, b2_h = 28, 14, 24, 18
ax.add_patch(FancyBboxPatch((b2_x, b2_y), b2_w, b2_h,
             boxstyle="round,pad=0.4", facecolor=C['white'],
             edgecolor=C['mist'], linewidth=1.5))

ax.text(b2_x + b2_w/2, b2_y + b2_h - 2.5, 'Sectoral Responses',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color=C['charcoal'], fontfamily=FONT)

# Red triangle up + High Oil Beta
ax.text(b2_x + 3, b2_y + b2_h/2 + 2.5, '\u25B2',
        va='center', fontsize=11, color=C['red'], fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + b2_h/2 + 2.5, 'High Oil Beta',
        va='center', fontsize=10, fontweight='bold', color=C['red'],
        fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + b2_h/2 + 0.5, 'Large Returns',
        va='center', fontsize=9, fontweight='bold', color=C['red'],
        fontfamily=FONT)

# Blue triangle down + Low Oil Beta
ax.text(b2_x + 3, b2_y + 4, '\u25BC',
        va='center', fontsize=11, color=C['blue'], fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + 4, 'Low Oil Beta',
        va='center', fontsize=10, fontweight='bold', color=C['blue'],
        fontfamily=FONT)
ax.text(b2_x + 5.5, b2_y + 2, 'Small / Opposite',
        va='center', fontsize=9, fontweight='bold', color=C['blue'],
        fontfamily=FONT)

# ── ARROW: Box 1 → Box 2 ──
ax.annotate('', xy=(b2_x - 0.5, b1_y + b1_h/2 + 1),
            xytext=(b1_x + b1_w + 0.5, b1_y + b1_h/2 + 1),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'],
                            lw=2.5, mutation_scale=20))

# ── BOX 3a: AGGREGATE INDEX (amber/gold, top right) ──
b3a_x, b3a_y, b3a_w, b3a_h = 60, 23, 22, 9
ax.add_patch(FancyBboxPatch((b3a_x, b3a_y), b3a_w, b3a_h,
             boxstyle="round,pad=0.4", facecolor=C['amber'],
             edgecolor='none'))

ax.text(b3a_x + b3a_w/2, b3a_y + b3a_h - 2.5, 'Aggregate Index',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b3a_x + b3a_w/2, b3a_y + 2.5, 'Small Response',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=C['white'], fontfamily=FONT)

# ── BOX 3b: REALITY (green, bottom right) ──
b3b_x, b3b_y, b3b_w, b3b_h = 60, 12, 22, 9
ax.add_patch(FancyBboxPatch((b3b_x, b3b_y), b3b_w, b3b_h,
             boxstyle="round,pad=0.4", facecolor=C['green'],
             edgecolor='none'))

ax.text(b3b_x + b3b_w/2, b3b_y + b3b_h - 2.5, 'Reality',
        ha='center', va='center', fontsize=12, fontweight='bold',
        color=C['white'], fontfamily=FONT)
ax.text(b3b_x + b3b_w/2, b3b_y + 2.5, 'Large Dispersion',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=C['white'], fontfamily=FONT)

# ── ARROWS: Box 2 → Box 3a (up-right) and Box 2 → Box 3b (down-right) ──
# Arrow to Aggregate Index (top)
ax.annotate('', xy=(b3a_x - 0.5, b3a_y + b3a_h/2),
            xytext=(b2_x + b2_w + 0.5, b2_y + b2_h - 4),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'],
                            lw=2.5, mutation_scale=20))

# Arrow to Reality (bottom)
ax.annotate('', xy=(b3b_x - 0.5, b3b_y + b3b_h/2),
            xytext=(b2_x + b2_w + 0.5, b2_y + 4),
            arrowprops=dict(arrowstyle='->', color=C['charcoal'],
                            lw=2.5, mutation_scale=20))

# Right-side labels with intuitive contrast
ax.text(b3a_x + b3a_w/2, b3a_y - 1.2, 'S&P 500: \u22121.81%',
        ha='center', fontsize=7, color=C['dkamber'], fontfamily=FONT,
        fontweight='bold')

ax.text(b3b_x + b3b_w/2, b3b_y - 1.2, 'Sectoral range: 59 pp',
        ha='center', fontsize=7, color=C['dkgreen'], fontfamily=FONT,
        fontweight='bold')

# ══════════════════════════════════════════════════
# BOTTOM BAR: Aggregation Masking Index
# ══════════════════════════════════════════════════
bar_y = 3.5
bar_h = 4.5
ax.add_patch(FancyBboxPatch((3, bar_y), 94, bar_h,
             boxstyle="round,pad=0.3", facecolor=C['lightgray'],
             edgecolor=C['mist'], linewidth=1))

ax.text(50, bar_y + bar_h/2,
        'Aggregation Masking Index (\u03A8): Crisis > Non-event',
        ha='center', va='center', fontsize=10, fontweight='bold',
        color=C['charcoal'], fontfamily=FONT)

# ── Citation line ──
ax.text(50, 1.0, 'Saxena & Yang (2026)  |  Research in International Business and Finance',
        ha='center', fontsize=5, color=C['silver'], fontfamily=FONT)

# ── Save ──
out_tiff = '/home/user/paper_2026/paper/graphical_abstract.tiff'
out_png = '/home/user/paper_2026/paper/graphical_abstract.png'
out_pdf = '/home/user/paper_2026/paper/graphical_abstract.pdf'

fig.savefig(out_tiff, dpi=DPI, bbox_inches='tight', pad_inches=0, format='tiff')
fig.savefig(out_png, dpi=DPI, bbox_inches='tight', pad_inches=0, format='png')
fig.savefig(out_pdf, dpi=DPI, bbox_inches='tight', pad_inches=0, format='pdf')

print(f"Saved: {out_tiff}")
print(f"Saved: {out_png}")
print(f"Saved: {out_pdf}")

from PIL import Image
img = Image.open(out_tiff)
w, h = img.size
print(f"Dimensions: {w} x {h} pixels (w x h)")
print(f"Aspect ratio: {w/h:.2f} (target: {1328/531:.2f})")
print(f"Meets minimum: {'YES' if w >= 1328 and h >= 531 else 'NO'}")
print(f"DPI: {DPI}")
print(f"Font: {FONT}")

# Thumbnail test
thumb = img.resize((500, 200), Image.LANCZOS)
thumb.save('/home/user/paper_2026/paper/graphical_abstract_thumbnail.png')
print("Thumbnail saved (500x200)")
