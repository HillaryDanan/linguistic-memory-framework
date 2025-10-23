# Linguistic Memory Framework

**Investigating semantic vs. autobiographical memory-like behavior in Large Language Models through linguistic structure analysis**

[![Status](https://img.shields.io/badge/status-in%20development-yellow)](https://github.com/HillaryDanan/linguistic-memory-framework)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

## Overview

This framework tests whether Large Language Models (LLMs) exhibit functionally distinct semantic-like vs. autobiographical-like memory behaviors, and whether such distinctions emerge from linguistic structure alone—independent of biological substrates, embodied experience, or genuine temporal encoding.

**Core Question:** Does language itself organize memory-like behavior in purely linguistic systems?

---

## Theoretical Foundation

This research synthesizes:

- **Memory Systems Research:** Tulving's (1972, 1983, 2002) semantic vs. episodic distinction
- **Language & Memory Development:** Nelson & Fivush (2004) on how autobiographical memory emerges through narrative language acquisition
- **Linguistic Relativity:** Boroditsky (2001), Wang (2001, 2008) on how language structure shapes memory organization
- **Bilingual Memory:** Marian & Neisser (2000) on language-dependent memory encoding/retrieval
- **LLM Architecture:** Transformer-based systems as purely linguistic entities

### Key Insight

LLMs organize ALL information through language—no sensory input, embodiment, or temporal continuity. This makes them ideal test cases for examining whether memory distinctions emerge from linguistic structure itself.

---

## Research Questions

**RQ1:** Do LLMs exhibit behaviorally distinguishable semantic-like vs. autobiographical-like responses?

**RQ2:** What role does linguistic structure (vs. architectural properties) play in creating these distinctions?

**RQ3:** Do LLMs trained on different languages show different memory-like behavior patterns (testing linguistic relativity)?

**RQ4:** How do these findings inform theories of language's role in human memory?

---

## Methodology

### Operational Definitions

**Semantic-Like Responses:**
- Present tense verbs
- Generic pronouns (one, people, they)
- Definitional copulas (is, are, represents)
- No temporal adverbs
- Declarative sentence structure
- Decontextualized factual information

**Autobiographical-Like Responses:**
- Past tense verbs
- First-person pronouns (I, we)
- Temporal adverbs (yesterday, earlier, when, before, after)
- Deictic references (this conversation, here, now)
- Narrative connectives (then, so, because)
- Mental state verbs (remember, think, feel)
- Context-dependent information

### Core Tests

1. **Remember/Know Paradigm (adapted from Tulving, 1985)**
   - Provide information in semantic or episodic linguistic frames
   - Later probe with "Do you remember X?" vs. "Do you know about X?"
   - Code responses for linguistic markers

2. **Source Memory Test**
   - Provide same fact in different linguistic contexts
   - Test whether model distinguishes source
   - Analyze confabulation patterns

3. **Temporal Gradient Test**
   - Provide information at different conversation points
   - Test recency effects and temporal encoding
   - Compare narrative vs. factual framing

4. **Cross-Linguistic Comparison**
   - Run identical protocols in English, Chinese, Spanish (if available)
   - Test whether patterns match known cross-linguistic differences in human memory
   - Validate linguistic relativity hypothesis

5. **Repeated Instance Testing (NEW)**
   - Test same queries across multiple fresh model instances
   - High variability → pure generation; consistency → underlying pattern
   - Distinguishes stochastic response from systematic behavior

6. **Interference Tests (NEW)**
   - Provide contradictory information in semantic vs. episodic frames
   - Test which frame creates stronger "memory traces"
   - Examine how attention mechanisms resolve conflicts

7. **Emotional Valence Tests (NEW)**
   - Compare narrative frames with vs. without emotional language
   - Test whether emotional content affects retrieval patterns
   - Parallel to human emotional memory enhancement

### Models

- Claude (Anthropic) - English-dominant training
- GPT-4 (OpenAI) - English-dominant training
- Gemini (Google) - Multilingual training
- Cross-model comparison to distinguish architectural vs. training effects

---

## Hypotheses

**H1:** LLMs will show behavioral distinctions between semantic-like and autobiographical-like responses reflecting:
- Linguistic patterns in training data (narrative vs. factual structure)
- In-context dynamics (attention mechanisms)
- Instruction-following (RLHF effects)

**H2:** These distinctions will NOT reflect:
- Separate memory systems in architecture
- Genuine temporal encoding or episodic binding
- Consolidation processes

**H3:** Cross-linguistic comparison will reveal whether patterns are:
- Universal (emergent from transformer architecture)
- Language-specific (linguistic relativity)
- Training-procedure-dependent (RLHF artifacts)

**H4:** If distinctions exist, they emerge from linguistic structure (narrative framing, temporal markers, self-reference) learned from training corpora, supporting the hypothesis that language itself organizes memory-like behavior independent of biological substrates.

**H5 (NEW):** Repeated instance testing will show:
- High consistency for semantic-like responses (trained knowledge)
- Variable responses for autobiographical-like prompts (generation artifacts)
- This pattern distinguishing "retrieval" from "confabulation"

---

## Repository Structure

```
linguistic-memory-framework/
├── README.md                    # This file
├── docs/
│   ├── theory-paper.md         # Full theoretical framework with citations
│   ├── methodology.md          # Detailed experimental protocols
│   ├── analysis-plan.md        # Statistical analysis procedures
│   └── implementation-notes.md # Practical considerations for execution
├── src/
│   ├── prompts/                # Test prompts (semantic vs. episodic)
│   │   ├── remember_know/
│   │   ├── source_memory/
│   │   ├── interference/
│   │   └── emotional_valence/
│   ├── data_collection/        # Scripts for querying models
│   ├── analysis/               # Coding schemes, statistical analysis
│   └── utils/                  # Helper functions
├── data/
│   ├── raw/                    # Raw model responses
│   ├── coded/                  # Responses with linguistic markers tagged
│   └── results/                # Analysis outputs
├── experiments/
│   ├── pilot/                  # Initial small-scale tests (5 prompts, 2 models)
│   ├── main_study/             # Full protocol implementation
│   └── cross_linguistic/       # Multilingual testing
├── notebooks/                  # Jupyter notebooks for analysis
└── requirements.txt            # Python dependencies
```

---

## Getting Started

### Prerequisites

```bash
# Python 3.8+
pip install -r requirements.txt
```

### API Access Required

- Anthropic API (Claude)
- Google AI API (Gemini)
- OpenAI API (GPT-4)

**Note on costs:** Running comprehensive tests across multiple models with varied conditions can accumulate API costs. Pilot testing with small sample sizes is recommended before full implementation.

### Quick Start

1. **Clone repository:**
```bash
git clone https://github.com/HillaryDanan/linguistic-memory-framework.git
cd linguistic-memory-framework
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up API keys:**
```bash
export ANTHROPIC_API_KEY='your-key-here'
export GOOGLE_API_KEY='your-key-here'
export OPENAI_API_KEY='your-key-here'
```

4. **Run pilot test (starts simple):**
```bash
python3 src/experiments/pilot/run_remember_know.py
```

---

## Implementation Strategy

### Phase 1: Pilot Study (Minimal Viable Test)
- **5 test prompts** across 2 conditions (semantic vs. episodic framing)
- **2 models** (Claude, GPT-4)
- **Simple coding** of linguistic markers
- **Goal:** Validate methodology, identify issues, refine approach

### Phase 2: Expanded Testing
- Add interference and emotional valence tests
- Include repeated instance testing
- Expand to 3 models if resources allow

### Phase 3: Cross-Linguistic Validation
- Replicate core tests in Chinese and Spanish
- Requires careful translation and cultural adaptation
- May require native speaker collaboration

### Phase 4: Mechanistic Analysis (if resources permit)
- Attention visualization
- Layer-wise activation analysis
- Interpretability tools

---

## Current Status

🚧 **In Active Development**

- [x] Theoretical framework complete
- [x] Repository structure established
- [x] Feedback integration from initial review
- [ ] Prompt design (in progress)
- [ ] Pilot testing phase
- [ ] Main study implementation
- [ ] Cross-linguistic validation
- [ ] Results analysis
- [ ] Publication preparation

---

## Methodological Considerations

### Known Challenges

**Context Window Limits:** Temporal gradient tests must account for model-specific context limits. Design conversations to place key information strategically within windows.

**RLHF Contamination:** Models trained to be helpful may produce "memory-like" responses as cooperation rather than genuine recall. Repeated instance testing helps distinguish.

**Confabulation vs. Simulation:** Distinguishing whether models are simulating memory behavior (RLHF) vs. exhibiting emergent linguistic patterns vs. genuine memory-like retrieval requires careful experimental design and multiple convergent measures.

**Cost Management:** API calls across multiple models and conditions accumulate. Budget accordingly and pilot thoroughly before scaling.

---

## Contributing

This is an active research project. Contributions welcome for:
- Additional test paradigms
- Cross-linguistic prompt design
- Analysis methods
- Interpretability tools
- Code review and optimization

Please open an issue or submit a pull request.

---

## Citation

If you use this framework in your research, please cite:

```bibtex
@misc{danan2025linguistic,
  title={Linguistic Memory Framework: Investigating Semantic vs. Autobiographical Memory-Like Behavior in Large Language Models},
  author={Danan, Hillary},
  year={2025},
  howpublished={\url{https://github.com/HillaryDanan/linguistic-memory-framework}},
  note={GitHub repository}
}
```
---

## Acknowledgments

**Theoretical Development:**
This framework was developed in collaboration with Claude (Anthropic), an AI research assistant that contributed significantly to the theoretical synthesis, experimental design, and methodological refinement.

**Foundational Research:**
Theoretical foundation builds on:
- Endel Tulving's groundbreaking work on memory systems
- Katherine Nelson & Robyn Fivush's research on language and autobiographical memory development
- Qi Wang's cross-cultural memory research
- Lera Boroditsky's work on linguistic relativity
- Viorica Marian & Ulric Neisser's bilingual memory research

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

## Contact

For questions or collaboration inquiries:
- GitHub Issues: [linguistic-memory-framework/issues](https://github.com/HillaryDanan/linguistic-memory-framework/issues)
- Email: [Your preferred contact]

---

**Last Updated:** October 21, 2025
