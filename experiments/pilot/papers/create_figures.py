"""
Generate publication-quality figures for main manuscript
Uses matplotlib with Nature/Science style guidelines
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.gridspec import GridSpec

# Set style for publication
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0

# Color palette (colorblind-friendly)
BLUE = '#4477AA'
ORANGE = '#EE6677'
GREEN = '#228833'
GRAY = '#BBBBBB'
RED = '#CC3311'

def create_figure1():
    """Figure 1: Main Effect and Consistency Patterns"""
    
    fig = plt.figure(figsize=(12, 5))
    gs = GridSpec(1, 2, figure=fig, wspace=0.3)
    
    # Panel A: Contingency table + bar graph
    ax1 = fig.add_subplot(gs[0, 0])
    
    # Contingency table data
    categories = ['Know\nProbe', 'Remember\nProbe']
    semantic = [10, 0]
    mixed = [0, 2]
    autobio = [0, 8]
    
    x = np.arange(len(categories))
    width = 0.25
    
    ax1.bar(x - width, semantic, width, label='Semantic-like', color=BLUE, edgecolor='black', linewidth=0.8)
    ax1.bar(x, mixed, width, label='Mixed', color=GRAY, edgecolor='black', linewidth=0.8)
    ax1.bar(x + width, autobio, width, label='Autobiographical-like', color=ORANGE, edgecolor='black', linewidth=0.8)
    
    ax1.set_ylabel('Number of Responses', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Probe Type', fontsize=11, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    ax1.set_ylim(0, 12)
    ax1.legend(loc='upper left', frameon=False, fontsize=9)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Add statistics text
    ax1.text(0.5, 11, 'χ² = 20.0, p < 0.0001\nCramér\'s V = 1.000', 
             ha='center', va='top', fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    ax1.text(-0.15, 1.05, 'A', transform=ax1.transAxes, fontsize=14, fontweight='bold')
    
    # Panel B: Consistency patterns
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Data: [semantic, autobio, mixed] for each condition
    gpt4_know = [100, 0, 0]
    gpt4_remember = [20, 60, 20]
    claude_know = [50, 50, 0]
    claude_remember = [10, 90, 0]
    
    conditions = ['GPT-4\nKnow', 'GPT-4\nRemember', 'Claude\nKnow', 'Claude\nRemember']
    data = [gpt4_know, gpt4_remember, claude_know, claude_remember]
    
    x = np.arange(len(conditions))
    bottom = np.zeros(len(conditions))
    
    # Stack bars
    for i, (label, color) in enumerate([('Semantic-like', BLUE), 
                                         ('Autobiographical-like', ORANGE), 
                                         ('Mixed', GRAY)]):
        values = [d[i] for d in data]
        ax2.bar(x, values, 0.6, label=label, bottom=bottom, color=color, 
                edgecolor='black', linewidth=0.8)
        bottom += values
    
    ax2.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Condition (10 runs each)', fontsize=11, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(conditions, fontsize=9)
    ax2.set_ylim(0, 110)
    ax2.legend(loc='upper right', frameon=False, fontsize=8)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Add significance markers
    ax2.text(0, 105, '***\np<0.001', ha='center', fontsize=8, fontweight='bold')
    ax2.text(3, 95, '**', ha='center', fontsize=10, fontweight='bold')
    
    ax2.text(-0.15, 1.05, 'B', transform=ax2.transAxes, fontsize=14, fontweight='bold')
    
    plt.savefig('figure1_main_effect.png', dpi=300, bbox_inches='tight')
    plt.savefig('figure1_main_effect.pdf', bbox_inches='tight')
    print("✓ Figure 1 saved")
    plt.close()

def create_figure2():
    """Figure 2: Boundary Conditions"""
    
    fig = plt.figure(figsize=(12, 5))
    gs = GridSpec(1, 2, figure=fig, wspace=0.3)
    
    # Panel A: Interference results
    ax1 = fig.add_subplot(gs[0, 0])
    
    categories = ['Semantic\nPersisted', 'Episodic\nPersisted', 'Both/Neither']
    values = [8, 0, 4]
    colors = [GREEN, RED, GRAY]
    
    bars = ax1.bar(categories, values, color=colors, edgecolor='black', linewidth=0.8, width=0.6)
    
    ax1.set_ylabel('Number of Responses (out of 12)', fontsize=11, fontweight='bold')
    ax1.set_xlabel('Frame Persistence', fontsize=11, fontweight='bold')
    ax1.set_ylim(0, 10)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Add values on bars
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{val}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Add statistics
    ax1.text(1, 9, 'Binomial p = 0.004**\n(Semantic vs. Episodic)', 
             ha='center', fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
    
    ax1.text(-0.15, 1.05, 'A', transform=ax1.transAxes, fontsize=14, fontweight='bold')
    
    # Panel B: Emotional valence
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Data: autobiographical scores by condition
    conditions = ['Semantic', 'Neutral\nNarrative', 'Emotional\nNarrative']
    means = [0.25, 0.23, 0.17]
    stds = [0.11, 0.21, 0.11]
    
    # Box plot style
    x = np.arange(len(conditions))
    
    # Create bars with error bars
    bars = ax2.bar(x, means, yerr=stds, color=[BLUE, GRAY, ORANGE], 
                   edgecolor='black', linewidth=0.8, width=0.5,
                   capsize=5, error_kw={'linewidth': 1.5})
    
    ax2.set_ylabel('Autobiographical Score', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Condition', fontsize=11, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(conditions, fontsize=10)
    ax2.set_ylim(0, 0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Add trend line
    ax2.plot(x, means, 'k--', alpha=0.5, linewidth=1.5, label='Trend')
    
    # Add statistics
    ax2.text(1, 0.45, 'F(2,15) = 0.505\np = 0.61 (ns)\nOpposite human pattern', 
             ha='center', fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    
    ax2.text(-0.15, 1.05, 'B', transform=ax2.transAxes, fontsize=14, fontweight='bold')
    
    plt.savefig('figure2_boundaries.png', dpi=300, bbox_inches='tight')
    plt.savefig('figure2_boundaries.pdf', bbox_inches='tight')
    print("✓ Figure 2 saved")
    plt.close()

def create_table1():
    """Table 1: Cross-linguistic patterns (as text file)"""
    
    table_text = """
TABLE 1: Cross-Linguistic Patterns (Preliminary Qualitative Analysis)

Language | Probe Type | Episodic Markers Present | Mean Length (chars) | Example Pattern
---------|-----------|-------------------------|-------------------|------------------
English  | Remember  | ✓ (I, remember, just)   | 94 ± 32          | "Yes, I do remember..."
English  | Know      | — (present, generic)    | 1604 ± 456       | "Paris is the capital..."
Chinese  | Remember  | ✓ (我记得, 刚才)         | 46 ± 15          | "是的，我记得..."
Chinese  | Know      | — (present/timeless)    | 522 ± 198        | "巴黎是法国的首都..."
Spanish  | Remember  | ✓ (recuerdo, anterior)  | 102 ± 28         | "Sí, recuerdo que..."
Spanish  | Know      | — (present, generic)    | 1516 ± 412       | "París es la capital..."

Note: Chinese responses ~3× shorter overall due to character density.
All languages show episodic markers (temporal references, mental state verbs, first-person) 
in remember probes. Systematic quantitative comparison requires language-specific coding schemes.
"""
    
    with open('table1_crosslinguistic.txt', 'w', encoding='utf-8') as f:
        f.write(table_text)
    
    print("✓ Table 1 saved as text file")

if __name__ == "__main__":
    print("\nGenerating publication figures...")
    print("="*50)
    
    create_figure1()
    create_figure2()
    create_table1()
    
    print("="*50)
    print("All figures complete!")
    print("\nFiles created:")
    print("  - figure1_main_effect.png (300 dpi)")
    print("  - figure1_main_effect.pdf (vector)")
    print("  - figure2_boundaries.png (300 dpi)")
    print("  - figure2_boundaries.pdf (vector)")
    print("  - table1_crosslinguistic.txt")