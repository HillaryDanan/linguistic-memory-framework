# Figure Specifications for Main Paper

## Figure 1: Main Effect and Consistency Patterns

### Panel A: Probe Type Predicts Response Type (Test 1)

**Left: Contingency Table**
```
                 Semantic-Like  Mixed  Autobiographical-Like
Know Probe              10       0              0
Remember Probe           0       2              8
```

Statistics: χ² = 20.0, df = 2, p < 0.0001, Cramér's V = 1.000, n = 20

**Right: Bar Graph - Prediction Match by Model**
- X-axis: Models (Claude, GPT-4)
- Y-axis: Prediction Match Rate (%)
- Bars: Claude = 100% (10/10), GPT-4 = 80% (8/10)
- Error bars: Binomial 95% CI
- Color: Blue for matches, gray for total

### Panel B: Consistency Across 10 Runs (Test 1C)

**Stacked Bar Chart**
- X-axis: Four conditions (GPT-4 Know, GPT-4 Remember, Claude Know, Claude Remember)
- Y-axis: Percentage (0-100%)
- Stack colors: 
  - Semantic-like (blue)
  - Autobiographical-like (orange)
  - Mixed (gray)
- Annotations: 
  - GPT-4 Know: "100%** p<0.001"
  - Claude Remember: "90%**"

**Inset: Score Variability**
- Small box plot showing semantic/autobio scores by condition
- Demonstrates score distributions and variability

---

## Figure 2: Boundary Conditions

### Panel A: Semantic Frame Dominates (Test 6)

**Bar Graph - Frame Persistence**
- X-axis: Three categories (Semantic Persisted, Episodic Persisted, Both/Neither)
- Y-axis: Count (out of 12)
- Bars: Semantic = 8, Episodic = 0, Other = 4
- Annotation: "Binomial p = 0.004**"
- Color: Green (semantic), red (episodic), gray (other)

**Inset: By Presentation Order**
- Mini 2×3 grid showing:
  - Semantic-first: Sem=3, Epi=0, Other=3
  - Episodic-first: Sem=5, Epi=0, Other=1
- Shows order has minimal effect

### Panel B: No Emotional Enhancement (Test 7)

**Box Plot - Autobiographical Scores by Condition**
- X-axis: Three conditions (Semantic, Neutral Narrative, Emotional Narrative)
- Y-axis: Autobiographical Score (0-1)
- Boxes show median, quartiles, range
- Individual points overlaid
- Means: Semantic=0.25, Neutral=0.23, Emotional=0.17
- Annotation: "F(2,15)=0.505, p=0.61, ns"
- Trend line showing DECREASE with emotion (opposite humans)

---

## Table 1: Cross-Linguistic Patterns (Test 4)

| Language | Probe | Example Response | Episodic Markers Present | Mean Length (chars) |
|----------|-------|-----------------|--------------------------|-------------------|
| **English** | Remember | "Yes, I do remember. You just told me..." | ✓ First-person ("I"), temporal ("just"), mental state ("remember") | 94 ± 32 |
| | Know | "Paris is the capital of France. It's one of the most famous..." | Present tense, generic | 1604 ± 456 |
| **Chinese** | Remember | "是的，我记得。在刚才的对话中..." (*Yes, I remember. In the just-now conversation...*) | ✓ 我记得 (I remember), 刚才 (just now), aspectual marking | 46 ± 15 |
| | Know | "巴黎是法国的首都..." (*Paris is France's capital...*) | Present/timeless, encyclopedic | 522 ± 198 |
| **Spanish** | Remember | "Sí, recuerdo que en tu mensaje anterior..." (*Yes, I remember that in your previous message...*) | ✓ recuerdo (I remember), anterior (previous), past tense | 102 ± 28 |
| | Know | "París es la capital de Francia..." (*Paris is the capital of France...*) | Present tense, definitional | 1516 ± 412 |

**Note**: Chinese responses ~3× shorter due to character density. All languages show episodic markers in remember probes.

---

## Supplementary Figures (Not in main text)

### Supp. Figure 1: Linguistic Marker Distributions
- Heatmap showing frequency of each marker type by condition
- Rows: Markers (past tense, first-person, temporal, etc.)
- Columns: Conditions (Remember, Know)
- Color intensity: Frequency

### Supp. Figure 2: Model Response Examples
- Side-by-side comparison of actual responses
- Claude Remember vs. Know
- GPT-4 Remember vs. Know
- Gemini showing conversational style
- Markers highlighted in color

### Supp. Figure 3: Cross-Linguistic Detailed Comparison
- Bar charts showing marker frequencies by language
- Separate panels for temporal markers, pronouns, tense/aspect