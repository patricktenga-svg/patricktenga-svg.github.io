import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, ConnectionPatch
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(16, 10))
fig.patch.set_facecolor('white')

# === Correction : GridSpec avec 4 lignes au lieu de 3 ===
gs = gridspec.GridSpec(4, 4, figure=fig, height_ratios=[1.2, 1.5, 0.8, 0.6], hspace=0.3, wspace=0.3)

# ===== TITLE =====
ax_title = fig.add_subplot(gs[0, :])
ax_title.axis('off')
ax_title.text(0.5, 0.6, 'INGA II HYDROELECTRIC PLANT - DRC', fontsize=20, fontweight='bold', 
              ha='center', color='#1a5276', family='serif')
ax_title.text(0.5, 0.3, 'Multi‑Scenario Optimization of Hydropower, Irrigation & Ecology', 
              fontsize=14, ha='center', color='#2c3e50', style='italic')
ax_title.text(0.5, 0.05, 'How does the system perform under normal, dry and very dry inflows?', 
              fontsize=12, ha='center', color='#7f8c8d')

# ===== LEFT COLUMN: SCENARIOS =====
ax_scenarios = fig.add_subplot(gs[1, 0])
ax_scenarios.axis('off')
ax_scenarios.set_xlim(0, 1)
ax_scenarios.set_ylim(0, 1)

# Scenario boxes
scenarios = [
    {'name': 'NORMAL', 'color': '#2ecc71', 'inflow': '~42,000 m³/s', 'desc': 'Average Congo River'},
    {'name': 'DRY', 'color': '#f39c12', 'inflow': '~4,200 m³/s', 'desc': '10% of normal (drought)'},
    {'name': 'VERY DRY', 'color': '#e74c3c', 'inflow': '~2,100 m³/s', 'desc': '5% of normal (severe)'}
]

y_positions = [0.75, 0.45, 0.15]
for i, (scen, y) in enumerate(zip(scenarios, y_positions)):
    rect = FancyBboxPatch((0.05, y-0.12), 0.9, 0.22, boxstyle="round,pad=0.05",
                          facecolor=scen['color'], alpha=0.2, edgecolor=scen['color'], linewidth=2)
    ax_scenarios.add_patch(rect)
    ax_scenarios.text(0.5, y+0.05, scen['name'], fontsize=12, fontweight='bold', 
                     ha='center', color=scen['color'])
    ax_scenarios.text(0.5, y-0.02, scen['inflow'], fontsize=10, ha='center', color='#2c3e50')
    ax_scenarios.text(0.5, y-0.08, scen['desc'], fontsize=8, ha='center', color='#7f8c8d')

ax_scenarios.text(0.5, 0.96, '🌊 HYDROLOGICAL SCENARIOS', fontsize=11, fontweight='bold', 
                 ha='center', color='#1a5276')

# ===== CENTER COLUMN: DAM SCHEMATIC =====
ax_dam = fig.add_subplot(gs[1, 1])
ax_dam.axis('off')
ax_dam.set_xlim(0, 1)
ax_dam.set_ylim(0, 1)

# Reservoir
water = Rectangle((0.2, 0.55), 0.7, 0.35, facecolor='#3498db', alpha=0.6, edgecolor='#2980b9', linewidth=1)
ax_dam.add_patch(water)
# Dam wall
dam_wall = Rectangle((0.75, 0.2), 0.12, 0.35, facecolor='#95a5a6', edgecolor='#7f8c8d', linewidth=2)
ax_dam.add_patch(dam_wall)
# Turbine symbol
turbine = Circle((0.81, 0.25), 0.035, facecolor='#e74c3c', alpha=0.8)
ax_dam.add_patch(turbine)
# Water flow arrow
ax_dam.annotate('', xy=(0.75, 0.3), xytext=(0.93, 0.3),
               arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
# Labels
ax_dam.text(0.5, 0.95, '🏭 INGA II DAM', fontsize=11, fontweight='bold', ha='center', color='#1a5276')
ax_dam.text(0.5, 0.85, '1,280 MW Capacity', fontsize=9, ha='center', color='#2c3e50')
ax_dam.text(0.5, 0.78, '58 m Head', fontsize=9, ha='center', color='#2c3e50')
ax_dam.text(0.5, 0.71, '2,200 m³/s Intake', fontsize=9, ha='center', color='#2c3e50')
ax_dam.text(0.3, 0.48, 'Reservoir', fontsize=8, ha='center', color='#2980b9', style='italic')
ax_dam.text(0.87, 0.15, 'Turbine', fontsize=8, ha='center', color='#e74c3c')

# ===== RIGHT COLUMN: OBJECTIVES =====
ax_obj = fig.add_subplot(gs[1, 2])
ax_obj.axis('off')
ax_obj.set_xlim(0, 1)
ax_obj.set_ylim(0, 1)

objectives = [
    {'icon': '⚡', 'name': 'Hydropower', 'color': '#f1c40f', 'y': 0.75},
    {'icon': '💧', 'name': 'Irrigation', 'color': '#3498db', 'y': 0.5},
    {'icon': '🌿', 'name': 'Ecology', 'color': '#2ecc71', 'y': 0.25}
]

for obj in objectives:
    ax_obj.text(0.2, obj['y'], obj['icon'], fontsize=20, ha='center')
    ax_obj.text(0.4, obj['y'], obj['name'], fontsize=11, fontweight='bold', 
               ha='left', color=obj['color'])
    ax_obj.annotate('', xy=(0.85, obj['y']), xytext=(0.55, obj['y']),
                   arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, alpha=0.5))

ax_obj.text(0.5, 0.96, '🎯 OBJECTIVES', fontsize=11, fontweight='bold', ha='center', color='#1a5276')

# ===== BOTTOM: RESULTS COMPARISON =====
ax_results = fig.add_subplot(gs[2, :])
ax_results.axis('off')
ax_results.set_xlim(0, 1)
ax_results.set_ylim(0, 1)

# Results table
results_data = [
    ['', 'NORMAL', 'DRY', 'VERY DRY'],
    ['💡 Hydropower (MW)', '6,107', '5,995', '4,137'],
    ['💧 Irrigation Penalty', '0', '0', '0'],
    ['🌿 Ecological Penalty', '0', '0', '0'],
    ['📦 Final Storage (Mm³)', '21,232', '1,740', '530']
]

table = ax_results.table(cellText=results_data, loc='center', cellLoc='center',
                          colWidths=[0.22, 0.18, 0.18, 0.22])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.8)

# Color header row
for i, col in enumerate(results_data[0]):
    table[(0, i)].set_facecolor('#1a5276')
    table[(0, i)].set_text_props(color='white', fontweight='bold')

# Color cells
table[(1, 1)].set_facecolor('#d5f5e3')  # Normal
table[(1, 2)].set_facecolor('#fdebd0')  # Dry
table[(1, 3)].set_facecolor('#fadbd8')  # Very Dry

ax_results.text(0.5, 0.92, '📊 OPTIMIZATION RESULTS (Peak Policy)', fontsize=12, 
                fontweight='bold', ha='center', color='#1a5276')

# ===== CONNECTION ARROWS =====
# Scenario to Dam
arrow1 = ConnectionPatch(xyA=(0.98, 0.5), xyB=(0.02, 0.5), coordsA='axes fraction',
                         coordsB='axes fraction', axesA=ax_scenarios, axesB=ax_dam,
                         arrowstyle='->', color='#7f8c8d', lw=2, alpha=0.7)
fig.add_artist(arrow1)

# Dam to Objectives
arrow2 = ConnectionPatch(xyA=(0.98, 0.5), xyB=(0.02, 0.5), coordsA='axes fraction',
                         coordsB='axes fraction', axesA=ax_dam, axesB=ax_obj,
                         arrowstyle='->', color='#7f8c8d', lw=2, alpha=0.7)
fig.add_artist(arrow2)

# Objectives to Results
arrow3 = ConnectionPatch(xyA=(0.5, 0.02), xyB=(0.5, 0.98), coordsA='axes fraction',
                         coordsB='axes fraction', axesA=ax_obj, axesB=ax_results,
                         arrowstyle='->', color='#7f8c8d', lw=2, alpha=0.7)
fig.add_artist(arrow3)

# ===== BOTTOM SUMMARY =====
# Correction : utiliser gs[3, :] avec la grille 4x4
ax_summary = fig.add_subplot(gs[3, :])
ax_summary.axis('off')
ax_summary.set_xlim(0, 1)
ax_summary.set_ylim(0, 1)

summary_text = """CONCLUSION: Under normal flows, Inga II operates without constraints. During severe drought (5% inflow),
hydropower drops by 32% and reservoir storage collapses by 97.5%."""
ax_summary.text(0.5, 0.7, summary_text, fontsize=10, ha='center', color='#e74c3c',
               bbox=dict(boxstyle='round', facecolor='#fadbd8', alpha=0.5))

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#2ecc71', alpha=0.3, label='Normal (≥42,000 m³/s)'),
    mpatches.Patch(facecolor='#f39c12', alpha=0.3, label='Dry (≈4,200 m³/s)'),
    mpatches.Patch(facecolor='#e74c3c', alpha=0.3, label='Very Dry (≈2,100 m³/s)')
]
ax_summary.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=9)

plt.tight_layout()
plt.savefig('graphical_abstract_inga_ii.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("✅ Graphical abstract saved as 'graphical_abstract_inga_ii.png'")