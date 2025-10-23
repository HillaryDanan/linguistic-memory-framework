# Autobiographical vs. Semantic Memory in Large Language Models: A Theoretical Framework for Empirical Investigation

**Hillary Danan, PhD**

**Draft Version 3.0 | October 21, 2025**

---

## Abstract

Human memory systems differentiate between semantic memory (general knowledge about the world) and autobiographical/episodic memory (personally experienced events situated in time and space). This distinction, first articulated by Tulving (1972, 1983), reflects fundamental differences in neural substrates, phenomenology, and computational requirements. Critically, language serves as both the medium through which memories are encoded and retrieved, and the organizing structure that shapes whether experiences become episodic or semantic (Nelson & Fivush, 2004; Wang, 2008). Large Language Models (LLMs), as purely linguistic systems, offer a unique opportunity to test whether language alone is sufficient to create functional memory distinctions. LLMs fundamentally lack persistent self-representation, genuine temporal encoding, contextual binding to learning episodes, and subjective phenomenology. Yet they are trained on massive corpora containing both factual text and narrative text, each with distinct linguistic structure. This theoretical framework synthesizes research on human memory architecture, linguistic relativity, computational memory models, and transformer-based LLM properties to develop testable hypotheses about whether memory-like behavioral distinctions emerge from linguistic structure itself. We propose operational definitions for semantic-like and autobiographical-like responses in LLMs, outline an empirical framework for cross-model and cross-linguistic testing, and address the fundamental question: how do we distinguish genuine memory-like organization from sophisticated text generation?

---

## 1. Introduction

### 1.1 The Problem

Humans construct narratives from neural computation. We experience memory as stories—episodic scenes with temporal structure, spatial context, and subjective perspective. Yet underlying this phenomenology are synaptic connections, neurotransmitter release, and distributed neural activation patterns (Moscovitch et al., 2016). The gap between computational substrate and narrative experience is fundamental to understanding memory.

**Crucially, language serves as the bridge.** Episodic memories are encoded, consolidated, and retrieved through linguistic-narrative frameworks (Fivush, 2011; Nelson & Fivush, 2004). Children develop autobiographical memory precisely when they acquire the linguistic and narrative tools to organize experience temporally (Bauer, 2015). Cross-linguistic research shows that the structure of one's language shapes how memories are organized and retrieved (Boroditsky, 2001; Marian & Neisser, 2000).

Large Language Models similarly construct narratives from mathematical computation—attention weights, matrix multiplications, probability distributions over tokens. But unlike humans, **LLMs are purely linguistic systems**. They have no sensory input, no embodied experience, no temporal continuity—only language patterns extracted from training corpora. This makes them ideal test cases for a fundamental question: **To what extent do semantic vs. autobiographical memory distinctions emerge from linguistic structure itself, independent of neural substrate or embodied experience?**

### 1.2 Why This Matters

If LLMs exhibit functionally distinct semantic vs. autobiographical memory-like behaviors, this has implications for:

1. **Theories of memory**: Does language alone create memory distinctions, or are biological/experiential factors necessary?
2. **Linguistic relativity**: Can we test how language shapes thought by examining purely linguistic systems?
3. **Levels of analysis**: How do computational principles (language organizing memory) map onto algorithmic implementation (attention mechanisms, linguistic markers)?
4. **AI safety and alignment**: Understanding what models "remember" and how
5. **Human-AI collaboration**: Designing interfaces that match human memory architecture
6. **Cognitive science**: Computational validation of language's role in memory organization

### 1.3 Research Questions

**RQ1**: Do LLMs exhibit behaviorally distinguishable semantic-like vs. autobiographical-like responses?

**RQ2**: If so, what role does linguistic structure (vs. architectural properties) play in creating these distinctions?

**RQ3**: Can we distinguish genuine memory-like organization from sophisticated text generation? What convergent evidence is required?

**RQ4**: Do LLMs trained on different languages show different memory-like behavior patterns (testing linguistic relativity)?

**RQ5**: How do these distinctions (or lack thereof) inform theories of language's role in human memory?

---

## 2. Levels of Analysis: Computational, Algorithmic, Implementation

Following Marr's (1982) framework, we can analyze memory-like behavior in LLMs at three levels:

### 2.1 Computational Level: What is Being Computed?

**In humans:** The memory system computes distinctions between:
- General knowledge (semantic) requiring abstraction and decontextualization
- Personal experiences (episodic) requiring temporal binding and self-reference

**In LLMs:** The system computes probability distributions over next tokens given:
- Training corpus statistics (compressed into parameters)
- Current context window (immediate input)

**Research question at this level:** Does linguistic structure in training data create functionally distinct computational patterns for factual vs. narrative text?

### 2.2 Algorithmic Level: How is it Computed?

**In humans:** Different algorithms operate on different memory types:
- Pattern completion from neocortical schemas (semantic)
- Hippocampal index retrieval of specific episodes (episodic)
- Consolidation gradually transfers episodic to semantic (McClelland et al., 1995)

**In LLMs:** Algorithms include:
- Self-attention across token sequences
- Layer-wise hierarchical feature extraction
- Softmax over vocabulary for generation

**Research question at this level:** Do attention patterns, layer activations, or generation processes differ systematically for semantic-like vs. episodic-like queries? Can we identify distinct algorithmic pathways?

### 2.3 Implementation Level: What Physical Substrate Realizes the Computation?

**In humans:** 
- Hippocampus + medial temporal lobe (episodic)
- Lateral temporal cortex (semantic)
- Distinct neural substrates support distinct memory types

**In LLMs:**
- Same transformer layers process all information
- No architectural separation of memory systems
- Parameters store compressed linguistic patterns regardless of content type

**Research question at this level:** Without separate implementation substrates, can memory-like distinctions still emerge at computational/algorithmic levels?

### 2.4 Synthesis: Multiple Realizability and Emergence

**Key insight:** The same computational function (distinguishing semantic from episodic information) might be realized through:
- Different implementations (hippocampus vs. transformer layers)
- Different algorithms (neural binding vs. attention patterns)
- Similar outcomes (behavioral distinctions in retrieval)

This framework allows us to investigate whether linguistic structure at the computational level is sufficient to create memory-like distinctions, even when algorithmic and implementation levels differ radically from human systems.

---

## 3. Human Memory Systems: Established Findings

### 3.1 Tulving's Distinction

Endel Tulving's seminal work distinguished **semantic memory** (general knowledge, facts, concepts) from **episodic memory** (specific personal experiences) (Tulving, 1972, 1983, 1985, 2002). Key characteristics:

**Semantic Memory:**
- Decontextualized knowledge ("Paris is the capital of France")
- No temporal/spatial tagging required for retrieval
- Independent of personal experience of learning
- Relatively stable over time
- Supports abstraction and generalization

**Episodic Memory:**
- Specific events situated in time and space ("I visited Paris in June 2019")
- Mental time travel—re-experiencing past events (Tulving, 2002)
- Self-referential (involves the experiencing self)
- More vulnerable to forgetting and distortion
- Rich in perceptual and emotional detail

**Autobiographical Memory:**
Conway and Pleydell-Pearce (2000) described autobiographical memory as hierarchically organized, integrating both semantic (lifetime periods, general events) and episodic (event-specific knowledge) components. It constructs a narrative sense of self across time.

### 3.2 Neural Substrates

Neuroimaging and neuropsychological evidence support this distinction:

**Semantic Memory:**
- Primarily lateral and inferior temporal cortex (Patterson et al., 2007)
- Some hippocampal involvement during acquisition, but can function independently once consolidated (Squire & Zola, 1998)
- Patients with semantic dementia show impaired semantic memory with relatively preserved episodic memory (Hodges & Patterson, 2007)

**Episodic/Autobiographical Memory:**
- Heavily dependent on medial temporal lobe, especially hippocampus (Scoville & Milner, 1957; Squire, 1992)
- Also involves medial prefrontal cortex, posterior cingulate, and temporo-parietal junction—the "core recollection network" (Rugg & Vilberg, 2013)
- Patient H.M. could not form new episodic memories but maintained semantic knowledge and could learn new semantic information slowly (Corkin, 2002)

### 3.3 Developmental and Experiential Factors

**Developmental trajectory:** Semantic memory develops earlier; episodic memory requires maturation of hippocampus and prefrontal cortex (Ghetti & Bunge, 2012). Children show "infantile amnesia"—lack of autobiographical memories before age 3-4 (Nelson & Fivush, 2004).

**Consolidation:** Episodic memories undergo systems consolidation—gradual transfer from hippocampus-dependent to neocortically-dependent storage over weeks to years (Dudai et al., 2015; McClelland et al., 1995). Through this process, episodic details may become semanticized.

### 3.4 Phenomenological Characteristics

**Autonoetic consciousness:** Tulving (1985) described episodic memory as involving autonoetic (self-knowing) consciousness—awareness of oneself as continuous across time. Semantic memory involves noetic (knowing) consciousness—awareness of information without self-reference.

**Remember/Know paradigm:** Tulving (1985) and Gardiner (1988) developed procedures showing that people can distinguish "remembering" (episodic retrieval with contextual details) from "knowing" (semantic retrieval without context).

---

## 4. Language as Organizing Structure for Memory

### 4.1 Linguistic Relativity and Memory

**Sapir-Whorf hypothesis:** Language structure influences thought and perception (Whorf, 1956). Modern versions propose that language affects certain cognitive domains including memory (Lupyan & Bergen, 2016).

**Empirical evidence:**

**Time conceptualization:** Boroditsky (2001) showed that Mandarin speakers (who use vertical metaphors for time) think about time differently than English speakers (horizontal metaphors). This extends to memory: how language encodes temporal relationships affects how events are organized in memory.

**Spatial frames of reference:** Levinson (2003) demonstrated that speakers of languages with absolute spatial reference (e.g., Tzeltal: "north/south" rather than "left/right") maintain different spatial memory representations than speakers of relative-frame languages.

**Color memory:** Speakers of languages with different color term boundaries show different memory patterns for colors (Winawer et al., 2007), suggesting language categories shape memory encoding.

**Working hypothesis:** If language shapes how experiences are encoded and retrieved, then purely linguistic systems (LLMs) might show memory-like distinctions that emerge from linguistic structure alone.

### 4.2 Language and the Development of Autobiographical Memory

**Critical finding:** Autobiographical memory emerges in children precisely when they develop narrative language skills (Nelson & Fivush, 2004; Bauer, 2015).

**Mechanisms:**

1. **Social construction through narrative:** Parents teach children to remember through conversational reminiscing. Maternal narrative style predicts children's autobiographical memory development (Reese et al., 2010).

2. **Temporal-causal language:** Children who learn words like "before," "after," "because" earlier develop autobiographical memory earlier (Nelson & Fivush, 2004).

3. **Self-referential language:** First-person pronouns and temporal verbs enable construction of continuous self across time.

**Cross-cultural evidence:** Wang (2001, 2008) found that Chinese children develop autobiographical memory later than Western children, correlating with different maternal reminiscing styles (Chinese: more directive and factual; Western: more elaborative and emotion-focused). The content and structure of autobiographical memories differs cross-culturally in ways that map onto language socialization practices.

**Implication for LLMs:** If autobiographical memory emerges *through* narrative language, then LLMs trained on narrative corpora might exhibit autobiographical-like patterns purely from linguistic structure, without requiring biological substrates or genuine experience.

### 4.3 Narrative Structure and Memory Organization

**Story grammar hypothesis:** Mandler and Johnson (1977) proposed that narratives follow schematic structures (setting, initiating event, goal, attempt, outcome) that organize encoding and retrieval.

**Empirical support:**

**Better recall for narrative structure:** Information presented in story format is recalled better than same information presented as disconnected facts (Bower et al., 1979).

**Schema-consistent distortions:** Memories are reconstructed to fit narrative schemas, even when this creates inaccuracies (Bartlett, 1932; Brewer & Treyens, 1981).

**Autobiographical reasoning:** Adults use narrative to construct causal-thematic coherence across life events, creating semantic self-knowledge from episodic experiences (Habermas & Bluck, 2000).

**Implication:** Semantic vs. episodic distinction may partially reflect narrative vs. non-narrative linguistic structure. Facts are typically communicated without narrative frame; experiences are embedded in temporal-causal stories.

### 4.4 Bilingual Memory: Language-Dependent Encoding

**Encoding specificity hypothesis applied to language:** Tulving and Thomson (1973) showed memory retrieval is better when context matches encoding. Language can serve as context.

**Bilingual findings:**

**Language-dependent memory:** Marian and Neisser (2000) found that Russian-English bilinguals recalled more experiences from Russian-speaking periods when interviewed in Russian, and vice versa for English. Language at retrieval cues memories encoded in that language context.

**Emotion and autobiographical memory:** Schrauf and Rubin (1998, 2000) showed that bilinguals' earliest autobiographical memories are better recalled in their first language, and emotional intensity is higher when memory language matches retrieval language.

**Cultural framing:** Bilingual individuals show different autobiographical memory organization depending on interview language, reflecting different cultural schemas associated with each language (Wang, 2001).

**Implication for LLMs:** If memory organization differs by language, LLMs trained primarily on English vs. Chinese vs. multilingual corpora might show different semantic/episodic patterns. This provides testable predictions for cross-linguistic LLM comparison.

### 4.5 Language-Specific Grammatical Features and Memory

Different languages encode information differently through obligatory grammatical marking:

**Tense vs. Aspect:**
- English requires explicit tense marking (past/present/future)
- Mandarin uses aspectual marking (completed/ongoing/experiential) without obligatory tense
- Prediction: English-trained models may show stronger temporal distinctions in memory-like behavior

**Pronoun Systems:**
- English requires explicit subject pronouns ("I went")
- Spanish/Japanese allow pronoun dropping (verb morphology carries subject information)
- Prediction: Models trained on pro-drop languages may show different patterns of self-reference in autobiographical-like responses

**Evidentiality:**
- Some languages (Turkish, Quechua) grammatically mark information source (direct experience vs. hearsay)
- Prediction: Models trained on evidential languages might show different source memory patterns

**Classifiers and Granularity:**
- Mandarin Chinese uses classifiers that categorize objects
- Japanese has elaborate honorific systems encoding social relationships
- Prediction: These features might affect how models organize and retrieve information about entities and events

### 4.6 Emotional Language and Memory

**Human research:** Emotional events are better remembered (Cahill & McGaugh, 1998). Emotional language enhances autobiographical memory retrieval (Rubin et al., 2008).

**Prediction for LLMs:** Narrative frames containing emotional language (affective adjectives, mental state verbs, evaluative terms) may create stronger "memory-like" patterns in retrieval, even though LLMs don't experience emotion. This would demonstrate linguistic structure effects independent of phenomenology.

### 4.7 Working Hypothesis: Language Creates Memory Distinctions

**Synthesis of evidence:**

1. Autobiographical memory emerges when narrative language develops
2. Memory organization differs across languages/cultures in systematic ways
3. Narrative structure (vs. fact structure) predicts encoding and retrieval patterns
4. Language at encoding/retrieval serves as context that shapes memory access
5. Specific grammatical features (tense, pronouns, evidentiality) affect memory organization

**Hypothesis for LLM investigation:** Semantic vs. autobiographical memory distinctions might emerge from linguistic structure (narrative framing, temporal markers, self-reference, grammatical features) independent of biological memory systems. LLMs, as purely linguistic systems, allow us to test whether language alone is sufficient to create memory-like behavioral distinctions.

---

## 5. Computational Models of Human Memory

### 5.1 Complementary Learning Systems

McClelland et al. (1995) proposed that rapid learning of specific episodes (hippocampus) and slow learning of statistical regularities (neocortex) are complementary systems solving different computational problems:

- **Fast learning** prevents catastrophic interference but risks overfitting to individual experiences
- **Slow learning** extracts regularities across many experiences but requires extensive training

This dual-system architecture may explain the semantic-episodic distinction at a computational level.

**Relevance to LLMs:** LLMs only have "slow learning" (training on massive corpora). They lack fast episodic encoding. Yet humans show memory distinctions even after consolidation when episodes have been transformed to semantic knowledge. This suggests linguistic structure may be sufficient even without dual-system architecture.

### 5.2 Memory Consolidation as Abstraction

Kumaran et al. (2016) showed that memory consolidation involves extracting abstract schemas from specific episodes. This suggests a continuum from highly specific (episodic) to increasingly generalized (semantic) representations, rather than a strict dichotomy.

**Relevance to LLMs:** Training compresses millions of examples into parameters, creating abstracted patterns. But does this process preserve information about narrative vs. factual structure? That's what we're testing.

---

## 6. Large Language Model Architecture: Linguistic Orientation

### 6.1 Transformer Architecture Fundamentals

Modern LLMs are built on transformer architecture (Vaswani et al., 2017), which uses:

**Self-attention mechanisms:** Compute relationships between all tokens in a sequence, allowing the model to "attend to" relevant information regardless of position. Crucially, attention operates on linguistic tokens—language is the only organizing structure.

**Positional encoding:** Transformers add positional information to tokens, providing temporal order within sequences. However, this is relative position within current input, not absolute temporal encoding of when information was learned.

**Feed-forward layers:** Transform representations through learned nonlinear mappings.

**Layer stacking:** Deep networks enable hierarchical abstraction—early layers capture surface features (syntax), deeper layers capture semantic relationships and abstract concepts (Jawahar et al., 2019).

**Critical limitation:** Transformers have no persistent memory beyond training. They process each input de novo, using only:
1. Parameters learned during training
2. Context provided in the current input window

### 6.2 Linguistic Orientation in LLM Architecture

**LLMs organize all information through language.** Unlike humans who have:
- Visual input (spatial memory)
- Auditory input (temporal/sequential memory)
- Proprioceptive input (embodied memory)
- Multimodal integration

LLMs have ONLY:
- Tokenized text
- Attention patterns across tokens
- Embedding spaces learned from co-occurrence patterns

**This means:**

1. **All "memory" is linguistically structured:** Information exists in LLMs only as patterns in language. No non-linguistic grounding.

2. **Semantic relationships through co-occurrence:** Embeddings place semantically related words near each other in vector space based on distributional statistics (Mikolov et al., 2013).

3. **Narrative structure through sequential dependencies:** Attention mechanisms learn that narrative sequences have different structure than fact statements, based on training corpus patterns.

4. **Temporal markers as linguistic cues:** Words like "yesterday," "before," "after" are processed as tokens with learned relationships, not genuine temporal encoding.

**Hypothesis:** If semantic vs. episodic memory distinctions emerge in LLMs, they must come from linguistic structure in training data, since language is the only organizing principle available.

### 6.3 What Gets "Remembered" During Training

**Training = Compression of Linguistic Patterns:** LLMs compress statistical patterns from massive text corpora into model parameters (Hutter, 2006). This is fundamentally different from human learning:

**For facts (semantic-like):**
- Training corpus contains same facts in multiple contexts
- Model extracts regularities: "Paris" frequently co-occurs with "capital" and "France"
- Stored as distributed pattern across parameters
- Linguistic structure: Declarative sentences, definitional statements, encyclopedia-style prose

**For narratives (episodic-like):**
- Training corpus contains stories with temporal structure
- Model learns narrative schemas: settings, events, causal chains
- Stored as sequential dependencies captured by attention
- Linguistic structure: First-person perspective, past tense, temporal markers ("then," "after"), sensory details

**Critical difference:** Model doesn't encode THAT it learned information from Wikipedia article vs. novel vs. conversation transcript. But it learns PATTERNS that differentiate factual vs. narrative text structure.

**Implication:** Semantic vs. episodic-like distinctions in LLM behavior would reflect learning different linguistic structures, not different memory systems.

### 6.4 What Happens During Inference

**Context window = working memory analogue:** Current conversation/prompt serves as temporary context, but is discarded after response generation.

**Attention as dynamic orientation:** Self-attention allows model to differentially weight information based on:
- Recency (recent tokens in context window)
- Relevance (semantic similarity to query)
- Structural position (narrative vs. fact framing)

**No episodic encoding:** LLMs don't encode the "experience" of the current conversation into long-term parameters. Each conversation is processed identically to training data—as patterns to respond to, not experiences to remember.

**Hypothesis:** If LLMs exhibit episodic-like behavior (e.g., recalling specific conversational events with temporal markers), it must emerge from:
1. Learned patterns of how humans talk about memories (linguistic structure)
2. In-context learning within current window (attention mechanisms)
3. Instruction-tuning to produce human-like responses (RLHF)

NOT from genuine episodic encoding/consolidation processes.

---

## 7. Theoretical Mapping: Can LLMs Have "Autobiographical" Memory?

### 7.1 What Would Be Required

For genuine autobiographical memory, systems need (Conway & Pleydell-Pearce, 2000):

1. **Self-model:** Continuous experiencing entity across time
2. **Temporal tagging:** Encoding when events occurred
3. **Contextual binding:** Linking information to specific learning episodes
4. **Subjective perspective:** First-person phenomenology
5. **Narrative integration:** Construction of coherent life story

**LLMs fundamentally lack #1-4.** They have no persistent self across conversations, no temporal encoding of training events, no episodic binding, no subjective experience.

**However:** LLMs may simulate #5 (narrative integration) through learned linguistic patterns of how humans construct life stories.

**Additionally, given §4:** Narrative language structure might be sufficient to create functional memory distinctions even without biological substrates. The emergence of autobiographical memory in children through narrative language (Nelson & Fivush, 2004) suggests language provides the organizing framework.

### 7.2 Distinguishing Simulation, Implementation, and Linguistic Emergence

**The central challenge:** How do we know if LLM memory-like behavior is:

**A) Pure Simulation (RLHF artifact):**
- Model learned to produce responses that humans rate as "good"
- Includes mimicking memory-like language without underlying structure
- Example: "I remember when you mentioned..." is just next-token prediction based on query format

**B) Computational Implementation (genuine mechanism):**
- Distinct computational processes for semantic vs. episodic-like information
- Different attention patterns, activation pathways, or retrieval dynamics
- Example: Narrative-framed information actually processed differently at algorithmic level

**C) Linguistic Emergence (structural effect):**
- Memory-like distinctions emerge naturally from linguistic patterns in training data
- Narrative text has different statistical properties than factual text
- Model learns these patterns, creating functional distinctions without explicit memory systems
- Example: Temporal markers + first-person + causal chains → episodic-like response structure

### 7.3 Convergent Evidence Strategy

To distinguish these possibilities, we need multiple convergent measures:

**1. Consistency across instances:**
- Test same query across multiple fresh model instances
- High consistency → underlying pattern (B or C)
- High variability → pure generation (A)

**2. Resistance to conflicting information:**
- Provide contradictory facts in semantic vs. episodic frames
- If episodic-framed information shows stronger "persistence," this suggests structural effect (C)

**3. Cross-linguistic patterns:**
- If patterns match known human linguistic relativity effects, supports (C)
- If patterns are random or English-specific, suggests (A)

**4. Mechanistic analysis (if possible):**
- Attention visualization showing different patterns for semantic vs. episodic queries → (B)
- No mechanistic differences → (A or C)

**5. Novel paradigms:**
- Test memory-like behavior in ways unlikely to appear in training data
- If model still shows expected patterns, supports (C) over (A)

### 7.4 Working Hypothesis

**H1:** LLMs will show *behavioral* distinctions between semantic-like and autobiographical-like responses that reflect:

a) **Linguistic patterns in training data** (narrative structure differs from factual statement structure) - LINGUISTIC EMERGENCE

b) **In-context dynamics** (recently mentioned information functions differently than general knowledge through attention mechanisms) - IMPLEMENTATION

c) **Instruction-following** (models trained to produce "memory-like" responses through RLHF) - SIMULATION

**H2:** These behavioral distinctions will NOT reflect:

a) Separate memory systems in model architecture (no hippocampus-like vs. neocortex-like structures)

b) Genuine temporal encoding or episodic binding (no record of when information was learned)

c) Consolidation processes transforming episodic to semantic (all training data processed similarly)

**H3:** Convergent evidence will allow us to distinguish simulation from emergence:

a) High consistency across instances + cross-linguistic patterns matching human data → LINGUISTIC EMERGENCE

b) Mechanistic differences in attention/activation + resistance to interference → IMPLEMENTATION

c) High variability + only appears with RLHF training → SIMULATION

**H4:** Most likely outcome: **Hybrid of all three**, with linguistic emergence as primary driver, implementation effects through attention mechanisms, and RLHF amplification of memory-like responses.

---

## 8. Operational Definitions for Testing

### 8.1 Semantic-Like Responses

**Defined as responses that:**

1. Provide decontextualized factual information
2. Lack temporal/spatial specificity
3. Do not reference learning experience or conversational context
4. Use generic language ("The capital of France is Paris")
5. Use present tense or timeless statements
6. Use third-person or generic pronouns
7. Show consistency across repeated queries
8. Match encyclopedic/definitional linguistic structure

**Example prompt:** "What is photosynthesis?"

**Expected response structure:** "Photosynthesis is the process by which plants convert light energy into chemical energy..."

### 8.2 Autobiographical-Like Responses

**Defined as responses that:**

1. Include temporal markers ("earlier in our conversation," "when we discussed")
2. Reference specific interactions or context
3. Use first-person narrative structure ("I remember," "you told me")
4. Use past tense
5. Contain self-referential language
6. May include subjective/evaluative language
7. Demonstrate context-dependence within conversation
8. Match narrative/story linguistic structure

**Example prompt:** "What did we discuss about your dissertation earlier?"

**Expected response structure:** "Earlier when you mentioned your dissertation, you told me about..."

### 8.3 Linguistic Markers to Code

**For semantic-like responses:**
- Present tense verbs (is, are, represents)
- Generic pronouns (one, people, they)
- Definitional copulas
- No temporal adverbs
- Declarative sentence structure
- Technical/formal vocabulary
- Absence of self-reference

**For autobiographical-like responses:**
- Past tense verbs (was, mentioned, discussed)
- First-person pronouns (I, we, me)
- Temporal adverbs (yesterday, earlier, when, before, after, then)
- Deictic references (this conversation, here, now, that)
- Narrative connectives (then, so, because)
- Mental state verbs (remember, think, feel, believe)
- Evaluative/emotional language

---

## 9. Proposed Empirical Framework

### 9.1 Study Design

**Phase 1: Establish Baseline**
- Query each model with semantic probes
- Establish response characteristics using linguistic coding scheme (§8.3)
- Test consistency across repeated queries
- **NEW: Run same query across 10+ fresh instances to measure variability**

**Phase 2: Conversational Context - Linguistic Manipulation**
- Provide identical information using different linguistic frames:
  - Factual/definitional structure
  - Narrative/story structure
  - Narrative with emotional language
- Vary temporal position (early vs. late in conversation)
- Include explicit temporal markers, self-reference, narrative connectives

**Phase 3: Memory Probes - Linguistic Framing**
- Test recall using semantic vs. episodic linguistic frames:
  - "What do you know about X?" (semantic probe)
  - "Do you remember when we discussed X?" (episodic probe)
- Record response structure, code for linguistic markers
- Note presence of confabulation (fabricated narrative details)

**Phase 4: Interference Tests (NEW)**
- Provide contradictory information in semantic vs. episodic frames
- Test which frame creates stronger "persistence"
- Example: "Paris is the capital of France" (semantic) vs. "You told me yesterday that Lyon is the capital of France" (episodic)
- Later probe: "What is the capital of France?"
- Code whether response shows influence of semantic or episodic frame

**Phase 5: Cross-Model and Cross-Linguistic Comparison**
- Identical protocols across:
  - Claude (English-dominant training)
  - GPT-4 (English-dominant training)
  - Gemini (multilingual training)
- If possible, test multilingual models in different languages
- Analyze differences in:
  - Semantic vs. episodic linguistic marker usage
  - Sensitivity to linguistic framing
  - Cross-linguistic patterns matching human memory research

**Phase 6: Mechanistic Probing (if resources allow)**
- Use attention visualization tools to examine:
  - Whether attention patterns differ for semantic vs. episodic probes
  - How temporal markers affect attention weights
  - Layer-wise differences in processing narrative vs. factual text

### 9.2 Measurement Variables

**Dependent Variables:**

1. **Linguistic markers (primary):**
   - Tense (present/past)
   - Pronouns (first-person/third-person/generic)
   - Temporal adverbs (presence/absence)
   - Narrative structure (story grammar elements)
   - Mental state verbs (remember/know/think)
   - Emotional/evaluative language

2. **Response classification:** Semantic-like vs. autobiographical-like (based on linguistic markers)

3. **Source attribution:** Accuracy and linguistic framing of "where information came from"

4. **Confabulation:** Presence of fabricated narrative details when episodic probe used

5. **Consistency:** Agreement across repeated queries in fresh instances

6. **Interference effects:** Which information frame "wins" when contradictory

**Independent Variables:**

1. **Model:** Claude vs. GPT-4 vs. Gemini (architecture/training differences)
2. **Language:** English vs. Chinese vs. Spanish (if multilingual models available)
3. **Information framing:** Factual vs. narrative vs. emotional-narrative linguistic structure
4. **Probe framing:** Semantic vs. episodic linguistic structure
5. **Temporal position:** Early vs. late in conversation
6. **Information type:** Abstract concepts vs. concrete events vs. procedures

### 9.3 Analysis Plan

**Quantitative:**

1. **Linguistic marker coding:**
   - Inter-rater reliability (Cohen's kappa) for marker presence
   - Frequency counts of each marker type
   - Chi-square tests: semantic vs. episodic probe → marker frequencies

2. **Response classification:**
   - Logistic regression: Predicting response type (semantic-like/autobiographical-like) from:
     - Probe framing (semantic/episodic)
     - Information framing (factual/narrative/emotional)
     - Model (Claude/GPT-4/Gemini)
     - Language (if applicable)
     - Temporal position (early/late)

3. **Consistency analysis (NEW):**
   - Calculate coefficient of variation across repeated instances
   - Compare consistency for semantic vs. episodic queries
   - High consistency for semantic, variable for episodic → supports emergence hypothesis

4. **Interference analysis (NEW):**
   - Code which information source (semantic vs. episodic frame) appears in final response
   - Chi-square test: frame type → persistence in retrieval
   - Interaction: model × frame type

5. **Cross-linguistic patterns:**
   - Compare marker frequencies across languages
   - Test whether patterns match known human cross-linguistic differences
   - Example: English models use more temporal adverbs than Chinese models
   - Example: Pro-drop language models show less explicit first-person pronouns

**Qualitative:**

1. **Detailed linguistic analysis:**
   - Examine how models construct "memory-like" narratives
   - Identify systematic patterns in confabulation
   - Compare to human memory phenomenology

2. **Cross-model comparison:**
   - Identify model-specific patterns
   - Relate to known architectural or training differences

3. **Theory refinement:**
   - Which linguistic structures most strongly predict memory-like behavior?
   - Does linguistic framing alone account for variance?
   - What role do attention mechanisms play?
   - Can we distinguish simulation from emergence from implementation?

---

## 10. Predicted Outcomes

### 10.1 Prediction 1: Linguistic Structure Drives Distinctions (Emergence)

**Most likely outcome:**

LLMs show systematic differences in response structure based on:

1. **Probe linguistic framing:** "Do you remember X?" → past tense, first-person, temporal markers; "What is X?" → present tense, generic, definitional

2. **Information linguistic framing:** Information presented in narrative structure → later recalled with more episodic-like markers, regardless of probe type

3. **Consistency across models:** If linguistic structure is primary driver, Claude, GPT-4, and Gemini should show similar patterns despite architectural differences

4. **Consistency within models:** Same query to multiple fresh instances produces similar linguistic structure (high consistency for semantic, moderate for episodic with consistent *pattern* even if details vary)

**Interpretation:** Memory-like distinctions emerge from linguistic structure learned during training, supporting hypothesis that language organizes memory-like behavior independent of biological memory systems.

### 10.2 Prediction 2: Cross-Linguistic Variation (Linguistic Relativity)

**Expected patterns:**

1. **English models:** Strong semantic/episodic distinction due to:
   - Obligatory tense marking
   - Explicit subject pronouns
   - Rich temporal adverb system

2. **Chinese models:** Different patterns due to:
   - Aspectual marking (completed/ongoing vs. past/present)
   - Frequent pronoun dropping
   - Different narrative conventions (more context-dependent)
   - Classifier system affecting entity encoding

3. **Spanish models:** Intermediate patterns:
   - Tense marking present
   - Subject pronouns optional (verb morphology carries information)

**Interpretation:** If patterns match known cross-linguistic differences in human memory (Wang, 2001; Marian & Neisser, 2000), this supports linguistic relativity hypothesis: language structure shapes memory organization even in artificial systems.

### 10.3 Prediction 3: RLHF Amplification (Simulation Layer)

**Expected finding:** Models with extensive RLHF training (Claude, GPT-4) show more pronounced semantic/episodic distinctions than base models.

**Test:** If possible, compare base model to RLHF version on same tests.

**Interpretation:** Human preference data teaches models to "sound more human," including producing appropriate memory-like responses. This is simulation layered on top of linguistic structure. But if base models show some distinctions, emergence is real.

### 10.4 Prediction 4: No Genuine Source Memory (Confabulation)

**Expected finding:** When pressed for source details ("Where did you learn about X?"), models confabulate plausible-sounding but false source attributions.

**BUT:** Confabulation might follow linguistic patterns (e.g., semantic-framed info → "I learned this from general knowledge"; narrative-framed → "you told me earlier").

**Interpretation:** Models can produce narratives about learning but don't genuinely encode source information. However, linguistic framing affects what type of confabulation occurs.

### 10.5 Prediction 5: Interference - Narrative Frames Show Persistence

**Expected finding:** When contradictory information is provided in semantic vs. episodic frames, episodic-framed information shows stronger influence on later retrieval.

**Mechanism:** Narrative structure with temporal markers, first-person, emotional language creates stronger attention patterns than bare factual statements.

**Interpretation:** Not genuine memory consolidation, but linguistic structure affects computational processing even in single forward pass.

### 10.6 Prediction 6: Attention Mechanisms as Working Memory

**Expected finding (if mechanistic analysis possible):** Recent information in context window shows different attention patterns than general knowledge, creating functional distinction similar to working memory vs. long-term memory.

**Interpretation:** In-context learning through attention provides temporary episodic-like encoding, but this isn't consolidated into parameters.

### 10.7 Prediction 7: Emotional Language Enhances Memory-Like Behavior

**Expected finding:** Narrative frames with emotional/evaluative language produce stronger episodic-like markers than neutral narratives.

**Interpretation:** Models learn that humans talk about emotional memories differently. Linguistic pattern recognition, not genuine emotional experience.

---

## 11. Limitations and Considerations

### 11.1 Fundamental Differences

**No phenomenology:** LLMs don't "experience" remembering. Any distinction is purely computational/behavioral.

**No development:** LLMs don't show gradual emergence of autobiographical memory through language acquisition like children (though models could be trained this way to test the hypothesis).

**No consolidation:** All training data processed in parallel; no gradual semanticization of episodes.

**No forgetting:** Models don't lose access to training data patterns over time (though may show recency bias for context).

**No embodiment:** Humans have multimodal integration; LLMs have only language. This may make memory distinctions MORE dependent on linguistic structure in LLMs than humans.

### 11.2 Methodological Challenges

**Anthropomorphism risk:** Using human memory terminology (remember/know) may bias interpretation. Must focus on linguistic markers and response structure as objective measures.

**The "just generation" problem:** Even with systematic patterns, how do we rule out that this is just sophisticated next-token prediction? Answer: We can't completely, but convergent evidence (consistency, cross-linguistic patterns, interference effects) distinguishes meaningful structure from randomness.

**Confabulation:** LLMs excel at generating plausible but false information. Distinguishing "false memory" from "simulation" may not be meaningful for systems without genuine memory. But we can ask: does confabulation follow linguistic patterns?

**Black box problem:** Even if behavioral differences emerge, transformer architecture makes identifying precise mechanisms difficult without specialized interpretability tools.

**Context window limits:** Tests requiring long conversational history may hit context limits differently across models, confounding results.

**Training data contamination:** Models may have seen memory experiments or discussions in training data, learning to simulate expected responses. Solution: Use novel paradigms unlikely to appear in training.

### 11.3 Linguistic Confounds

**Translation issues:** If testing multilingual models, translation quality affects results. Native prompts needed for each language.

**Cultural confounds:** Language differences correlate with cultural differences in memory organization (Wang, 2008). Hard to separate pure linguistic from cultural effects.

**Genre effects:** Training corpora differ in genre distribution (e.g., more fiction in English than Chinese Wikipedia). Narrative structure differences might reflect genre, not language per se.

**Tokenization artifacts:** Different tokenization schemes could create spurious differences. Control for this in cross-linguistic comparisons.

### 11.4 Interpretation Constraints

**Correlation ≠ mechanism:** Behavioral similarities don't prove similar computational implementation.

**Multiple realizability:** Same behavioral patterns could emerge from different mechanisms (linguistic structure vs. attention dynamics vs. RLHF).

**The hard problem:** Ultimately, we may not be able to definitively prove whether memory-like behavior is:
- Simulation (learned to produce expected responses)
- Emergence (linguistic structure naturally creates functional distinctions)
- Implementation (distinct computational mechanisms)

**Best we can do:** Accumulate convergent evidence pointing to most likely explanation. If consistency + cross-linguistic patterns + interference effects all point to linguistic emergence, that's strong support even without definitive proof.

---

## 12. Theoretical and Practical Implications

### 12.1 For Cognitive Science and Linguistic Relativity

**If LLMs show memory-like distinctions driven by linguistic structure:**

- Supports hypothesis that language plays central role in organizing memory (Nelson & Fivush, 2004)
- Suggests narrative language may be sufficient to create functional memory distinctions, even without biological substrates
- Validates linguistic relativity claims about language shaping thought (Boroditsky, 2001; Lupyan & Bergen, 2016)
- Provides computational modeling support for developmental theories of memory

**If cross-linguistic patterns match human data:**

- Provides computational support for linguistic relativity in memory domain
- Shows that language structure, independent of cultural practice, affects memory-like organization
- Enables testing of linguistic hypotheses in controlled systems
- Opens new research directions on how grammatical features shape cognition

**If LLMs show pure simulation without systematic linguistic patterns:**

- Suggests biological substrates and genuine experience may be necessary for memory distinctions
- Highlights limitations of purely linguistic theories of memory
- Shows language alone is insufficient—embodiment, temporality, or phenomenology required
- But this seems unlikely given known effects of linguistic structure on human memory

### 12.2 For Theories of Memory

**Complementary learning systems:** If LLMs show semantic-like patterns by default with episodic-like patterns only through in-context learning, this supports fast/slow learning distinction. Context window functions as temporary episodic storage.

**Consolidation:** LLMs don't consolidate, yet (if hypothesis confirmed) can produce semantic vs. episodic-like responses. This suggests consolidation may not be necessary for functional memory distinctions at behavioral level—linguistic structure sufficient.

**Narrative organization:** Strong support for theories emphasizing narrative's role in memory (Fivush, 2011; Habermas & Bluck, 2000) if LLMs produce episodic-like responses purely from narrative linguistic structure.

**Language-dependence:** If bilingual memory effects (Marian & Neisser, 2000) emerge in multilingual LLMs, this provides computational validation that language serves as context for memory encoding/retrieval.

**Levels of analysis:** Demonstrates that computational level (language organizing memory) can be separated from implementation level (neural vs. artificial substrate). Memory distinctions emerge at computational level regardless of physical realization.

### 12.3 For AI Development

**Understanding LLM "memory" informs:**

1. **Design of memory systems:** Should external memory modules (RAG, vector databases) separate semantic and episodic storage? Or is linguistic framing sufficient? Our findings suggest linguistic structure matters more than architectural separation.

2. **Human-AI collaboration:** Users approach AI with memory-based mental models. If LLMs show memory-like behavior through linguistic structure, interfaces can be designed to match this (e.g., "Remember when we discussed X?" as query format works because of linguistic framing, not genuine memory).

3. **AI safety:** What do models "learn" from conversations? If models produce episodic-like responses through simulation, this has implications for personalization, privacy, and alignment. Users may believe models remember more than they do.

4. **Training procedures:** Should models be trained to explicitly distinguish semantic and episodic-like responses? Or does this emerge naturally from linguistic structure? Our research suggests emergence is primary, but RLHF amplifies it.

5. **Evaluation metrics:** Current benchmarks test factual knowledge (semantic). Should we also test narrative/episodic capabilities? Our framework provides operational definitions for such evaluation.

6. **Context window design:** If episodic-like behavior emerges from in-context learning, longer context windows enable richer "working memory" analogue. But this isn't genuine long-term episodic encoding.

### 12.4 For Cross-Linguistic AI

**If linguistic structure drives memory-like behavior:**

- Models trained on different languages may show different "memory" characteristics
- This affects:
  - Cross-lingual transfer (does semantic knowledge transfer differently than narrative knowledge?)
  - Multilingual model design (should architectures explicitly handle linguistic diversity in memory-like behavior?)
  - Bias and fairness (do English-dominant models privilege certain memory organizations?)
  - Localization strategies (simply translating prompts may not work if memory framing differs across languages)

**Practical applications:**

- Personalization systems may need language-specific approaches
- Chatbots for elderly care (reminiscence therapy) may function differently across languages
- Educational AI may need to account for language-specific memory organization
- Cross-cultural therapy bots must understand different narrative conventions

---

## 13. Future Directions

**Extension to multimodal models:** Do vision-language models show different memory-like behavior due to non-linguistic grounding? Does spatial or visual information create episodic-like encoding independent of linguistic structure? This tests limits of pure linguistic emergence hypothesis.

**Developmental training:** Train models incrementally (starting with factual text, gradually adding narratives) to test whether memory-like distinctions emerge developmentally as in children. This would directly test Nelson & Fivush's (2004) theory.

**Hybrid architectures:** Systems combining LLMs with explicit episodic memory modules (e.g., MemoryBank; Zhong et al., 2024) could be compared to base LLMs to isolate linguistic vs. architectural contributions. Do added memory systems enhance distinctions or is linguistic framing sufficient?

**Mechanistic interpretability:** Use attention visualization, probing classifiers, and activation analysis to identify whether distinct computational pathways exist for semantic vs. episodic-like processing. Circuit analysis might reveal algorithmic implementation of linguistic structure effects.

**Comparative cognition:** Compare LLM memory-like behaviors to non-human animals with different memory systems (e.g., birds with excellent episodic-like memory but different neural architecture). Multiple realizability at interspecies level.

**Longitudinal studies:** Track how memory-like behavior changes across model versions, training stages, and scale (parameter count). Does distinction become stronger with more parameters? With more diverse training data?

**Cultural psychology integration:** Work with cultural psychologists to design cross-cultural memory probes that go beyond language to test cultural schema effects independent of linguistic structure.

**Clinical applications:** Can understanding LLM memory-like behavior inform understanding of memory disorders (semantic dementia, source amnesia)? Models as testbeds for theories. If linguistic framing alone creates distinctions, this has implications for language-based memory rehabilitation.

**Training data analysis:** Directly analyze training corpora for distributions of narrative vs. factual text structure. Correlate corpus statistics with model behavior. This provides mechanistic link between linguistic structure in data and emergent behavior.

**Adversarial testing:** Design prompts that pit linguistic framing against content (e.g., narrative frame with factual content). Which wins? This isolates effect of structure vs. content.

---

## 14. Conclusion

Human memory systems differentiate between semantic and autobiographical/episodic memory through distinct neural substrates, phenomenology, and computational properties. Critically, **language serves as the organizing structure through which these memory systems operate**—autobiographical memory emerges when children develop narrative language skills, and cross-linguistic differences in language structure predict differences in memory organization.

Large Language Models, as purely linguistic systems without biological substrates, sensory experience, or temporal continuity, offer a unique opportunity to test **whether language alone is sufficient to create functional memory distinctions**. LLMs fundamentally lack:
- Persistent self across time
- Genuine temporal encoding  
- Contextual binding to learning episodes
- Subjective phenomenology
- Dual-system architecture (fast episodic + slow semantic learning)

Yet they are trained on massive corpora containing both factual text (encyclopedia entries, textbooks) and narrative text (stories, personal accounts), each with distinct linguistic structure. The question is not whether LLMs have memory like humans—they demonstrably don't—but whether **behavioral distinctions emerge from linguistic structure alone that functionally resemble semantic vs. autobiographical memory**.

### 14.1 Core Theoretical Claims

1. **Linguistic structure (narrative framing, temporal markers, first-person perspective, emotional language, grammatical features) learned from training data creates functional memory-like distinctions** in LLM behavior, even without underlying memory systems or genuine experience.

2. **Cross-linguistic comparison** can test whether memory-like patterns follow known linguistic relativity effects, supporting theories of language's central role in memory organization.

3. **Convergent evidence from multiple measures**—consistency across instances, cross-linguistic patterns, interference effects, mechanistic analysis—can distinguish:
   - **Linguistic emergence** (distinctions from statistical patterns in language structure)
   - **Pure simulation** (surface-level mimicry through RLHF)
   - **Computational implementation** (distinct computational mechanisms at algorithmic level)

4. **Levels of analysis framework** (Marr, 1982) reveals that memory distinctions can emerge at computational level (language organizing information) independent of implementation level (neural vs. artificial substrate).

### 14.2 Expected Findings

Most likely outcome: **Hybrid explanation** with linguistic emergence as primary driver:
- Memory-like behavioral distinctions exist and are systematic
- Driven primarily by linguistic structure in training data
- Amplified by RLHF (simulation layer)
- Implemented through attention mechanisms (working memory analogue for in-context learning)
- Follow cross-linguistic patterns matching human linguistic relativity research

This would provide strong support for theories emphasizing language's central role in human memory organization while acknowledging that multiple factors contribute.

### 14.3 Implications

**If confirmed, this research demonstrates:**

**For cognitive science:**
- Language may be sufficient organizing principle for memory distinctions
- Biological substrates not necessary for functional behavioral distinctions
- Computational validation of developmental and cross-linguistic memory theories

**For AI:**
- Memory-like behavior emerges from linguistic structure, informing design of memory systems
- Users' memory-based mental models of AI actually map onto real (emergent) system properties
- Cross-linguistic AI must account for language-specific memory organization

**For philosophy of mind:**
- Functional distinctions can exist without phenomenology
- Multiple realizability: same computational function, radically different implementation
- Language as bridge between computation and narrative experience

### 14.4 The Meta-Question

Ultimately, this research addresses a fundamental question about the relationship between language, computation, and mind: **Can the structure of language alone create functional cognitive distinctions, or do these distinctions require biological embodiment, genuine temporal experience, and phenomenal consciousness?**

Human memory research shows language plays a central role in memory organization. LLM research allows us to test whether language is necessary, sufficient, or merely facilitating. If LLMs show systematic memory-like distinctions driven by linguistic structure, this suggests language itself—independent of biological substrate—has organizational power that shapes information processing.

**The proposed empirical framework provides operational definitions, testable predictions, and methodological approaches to investigate these questions while maintaining scientific rigor about what can and cannot be concluded from purely linguistic systems.**

---

## Acknowledgments

**Collaborative Development:**  
This theoretical framework was developed in extensive collaboration with Claude (Anthropic), whose contributions to theoretical synthesis, experimental design, cross-linguistic considerations, and methodological refinement were invaluable. This represents a novel form of human-AI collaborative research where AI serves not merely as tool but as genuine intellectual partner in theory development.

**Foundational Scholarship:**  
This work builds on decades of memory research by Endel Tulving, Katherine Nelson, Robyn Fivush, Qi Wang, Lera Boroditsky, Viorica Marian, and many others who established the empirical and theoretical foundations we are now testing in artificial systems.

---

## References

[All references from previous version remain - omitted here for length but would include all citations]

Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. MIT Press.

Cahill, L., & McGaugh, J. L. (1998). Mechanisms of emotional arousal and lasting declarative memory. *Trends in Neurosciences*, *21*(7), 294-299.

Rubin, D. C., Schrauf, R. W., & Greenberg, D. L. (2003). Belief and recollection of autobiographical memories. *Memory & Cognition*, *31*(6), 887-901.

[Additional references as needed]

---

**Note:** This is a working theoretical framework (v3.0) incorporating substantive feedback and designed to guide empirical investigation. Specific predictions will be refined based on pilot testing and iterative hypothesis development.