# Autobiographical vs. Semantic Memory in Large Language Models: A Theoretical Framework for Empirical Investigation

**Hillary Danan, PhD & Claude (Anthropic)**

**Draft Version 2.0 | October 21, 2025**

---

## Abstract

Human memory systems differentiate between semantic memory (general knowledge about the world) and autobiographical/episodic memory (personally experienced events situated in time and space). This distinction, first articulated by Tulving (1972, 1983), reflects fundamental differences in neural substrates, phenomenology, and computational requirements. Critically, language serves as both the medium through which memories are encoded and retrieved, and the organizing structure that shapes whether experiences become episodic or semantic (Nelson & Fivush, 2004; Wang, 2008). Large Language Models (LLMs), as purely linguistic systems, offer a unique opportunity to examine how language itself—independent of sensory experience or embodiment—structures memory-like behavior. This theoretical framework synthesizes research on human memory architecture, linguistic relativity, and computational properties of transformer-based LLMs to develop testable hypotheses about whether memory distinctions emerge from linguistic structure itself. We propose operational definitions for semantic-like and autobiographical-like responses in LLMs and outline an empirical framework for cross-model testing.

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
3. **AI safety and alignment**: Understanding what models "remember" and how
4. **Human-AI collaboration**: Designing interfaces that match human memory architecture
5. **Cognitive science**: Computational validation of language's role in memory organization

### 1.3 Research Questions

**RQ1**: Do LLMs exhibit behaviorally distinguishable semantic-like vs. autobiographical-like responses?

**RQ2**: If so, what role does linguistic structure (vs. architectural properties) play in creating these distinctions?

**RQ3**: Do LLMs trained on different languages show different memory-like behavior patterns (testing linguistic relativity)?

**RQ4**: How do these distinctions (or lack thereof) inform theories of language's role in human memory?

---

## 2. Human Memory Systems: Established Findings

### 2.1 Tulving's Distinction

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

### 2.2 Neural Substrates

Neuroimaging and neuropsychological evidence support this distinction:

**Semantic Memory:**
- Primarily lateral and inferior temporal cortex (Patterson et al., 2007)
- Some hippocampal involvement during acquisition, but can function independently once consolidated (Squire & Zola, 1998)
- Patients with semantic dementia show impaired semantic memory with relatively preserved episodic memory (Hodges & Patterson, 2007)

**Episodic/Autobiographical Memory:**
- Heavily dependent on medial temporal lobe, especially hippocampus (Scoville & Milner, 1957; Squire, 1992)
- Also involves medial prefrontal cortex, posterior cingulate, and temporo-parietal junction—the "core recollection network" (Rugg & Vilberg, 2013)
- Patient H.M. could not form new episodic memories but maintained semantic knowledge and could learn new semantic information slowly (Corkin, 2002)

### 2.3 Developmental and Experiential Factors

**Developmental trajectory:** Semantic memory develops earlier; episodic memory requires maturation of hippocampus and prefrontal cortex (Ghetti & Bunge, 2012). Children show "infantile amnesia"—lack of autobiographical memories before age 3-4 (Nelson & Fivush, 2004).

**Consolidation:** Episodic memories undergo systems consolidation—gradual transfer from hippocampus-dependent to neocortically-dependent storage over weeks to years (Dudai et al., 2015; McClelland et al., 1995). Through this process, episodic details may become semanticized.

### 2.4 Phenomenological Characteristics

**Autonoetic consciousness:** Tulving (1985) described episodic memory as involving autonoetic (self-knowing) consciousness—awareness of oneself as continuous across time. Semantic memory involves noetic (knowing) consciousness—awareness of information without self-reference.

**Remember/Know paradigm:** Tulving (1985) and Gardiner (1988) developed procedures showing that people can distinguish "remembering" (episodic retrieval with contextual details) from "knowing" (semantic retrieval without context).

---

## 3. Language as Organizing Structure for Memory

### 3.1 Linguistic Relativity and Memory

**Sapir-Whorf hypothesis:** Language structure influences thought and perception (Whorf, 1956). Modern versions propose that language affects certain cognitive domains including memory (Lupyan & Bergen, 2016).

**Empirical evidence:**

**Time conceptualization:** Boroditsky (2001) showed that Mandarin speakers (who use vertical metaphors for time) think about time differently than English speakers (horizontal metaphors). This extends to memory: how language encodes temporal relationships affects how events are organized in memory.

**Spatial frames of reference:** Levinson (2003) demonstrated that speakers of languages with absolute spatial reference (e.g., Tzeltal: "north/south" rather than "left/right") maintain different spatial memory representations than speakers of relative-frame languages.

**Color memory:** Speakers of languages with different color term boundaries show different memory patterns for colors (Winawer et al., 2007), suggesting language categories shape memory encoding.

**Working hypothesis:** If language shapes how experiences are encoded and retrieved, then purely linguistic systems (LLMs) might show memory-like distinctions that emerge from linguistic structure alone.

### 3.2 Language and the Development of Autobiographical Memory

**Critical finding:** Autobiographical memory emerges in children precisely when they develop narrative language skills (Nelson & Fivush, 2004; Bauer, 2015).

**Mechanisms:**

1. **Social construction through narrative:** Parents teach children to remember through conversational reminiscing. Maternal narrative style predicts children's autobiographical memory development (Reese et al., 2010).

2. **Temporal-causal language:** Children who learn words like "before," "after," "because" earlier develop autobiographical memory earlier (Nelson & Fivush, 2004).

3. **Self-referential language:** First-person pronouns and temporal verbs enable construction of continuous self across time.

**Cross-cultural evidence:** Wang (2001, 2008) found that Chinese children develop autobiographical memory later than Western children, correlating with different maternal reminiscing styles (Chinese: more directive and factual; Western: more elaborative and emotion-focused). The content and structure of autobiographical memories differs cross-culturally in ways that map onto language socialization practices.

**Implication for LLMs:** If autobiographical memory emerges *through* narrative language, then LLMs trained on narrative corpora might exhibit autobiographical-like patterns purely from linguistic structure, without requiring biological substrates or genuine experience.

### 3.3 Narrative Structure and Memory Organization

**Story grammar hypothesis:** Mandler and Johnson (1977) proposed that narratives follow schematic structures (setting, initiating event, goal, attempt, outcome) that organize encoding and retrieval.

**Empirical support:**

**Better recall for narrative structure:** Information presented in story format is recalled better than same information presented as disconnected facts (Bower et al., 1979).

**Schema-consistent distortions:** Memories are reconstructed to fit narrative schemas, even when this creates inaccuracies (Bartlett, 1932; Brewer & Treyens, 1981).

**Autobiographical reasoning:** Adults use narrative to construct causal-thematic coherence across life events, creating semantic self-knowledge from episodic experiences (Habermas & Bluck, 2000).

**Implication:** Semantic vs. episodic distinction may partially reflect narrative vs. non-narrative linguistic structure. Facts are typically communicated without narrative frame; experiences are embedded in temporal-causal stories.

### 3.4 Bilingual Memory: Language-Dependent Encoding

**Encoding specificity hypothesis applied to language:** Tulving and Thomson (1973) showed memory retrieval is better when context matches encoding. Language can serve as context.

**Bilingual findings:**

**Language-dependent memory:** Marian and Neisser (2000) found that Russian-English bilinguals recalled more experiences from Russian-speaking periods when interviewed in Russian, and vice versa for English. Language at retrieval cues memories encoded in that language context.

**Emotion and autobiographical memory:** Schrauf and Rubin (1998, 2000) showed that bilinguals' earliest autobiographical memories are better recalled in their first language, and emotional intensity is higher when memory language matches retrieval language.

**Cultural framing:** Bilingual individuals show different autobiographical memory organization depending on interview language, reflecting different cultural schemas associated with each language (Wang, 2001).

**Implication for LLMs:** If memory organization differs by language, LLMs trained primarily on English vs. Chinese vs. multilingual corpora might show different semantic/episodic patterns. This provides testable predictions for cross-linguistic LLM comparison.

### 3.5 Working Hypothesis: Language Creates Memory Distinctions

**Synthesis of evidence:**

1. Autobiographical memory emerges when narrative language develops
2. Memory organization differs across languages/cultures in systematic ways
3. Narrative structure (vs. fact structure) predicts encoding and retrieval patterns
4. Language at encoding/retrieval serves as context that shapes memory access

**Hypothesis for LLM investigation:** Semantic vs. autobiographical memory distinctions might emerge from linguistic structure (narrative framing, temporal markers, self-reference) independent of biological memory systems. LLMs, as purely linguistic systems, allow us to test whether language alone is sufficient to create memory-like behavioral distinctions.

---

## 4. Computational Models of Human Memory

### 4.1 Complementary Learning Systems

McClelland et al. (1995) proposed that rapid learning of specific episodes (hippocampus) and slow learning of statistical regularities (neocortex) are complementary systems solving different computational problems:

- **Fast learning** prevents catastrophic interference but risks overfitting to individual experiences
- **Slow learning** extracts regularities across many experiences but requires extensive training

This dual-system architecture may explain the semantic-episodic distinction at a computational level.

### 4.2 Memory Consolidation as Abstraction

Kumaran et al. (2016) showed that memory consolidation involves extracting abstract schemas from specific episodes. This suggests a continuum from highly specific (episodic) to increasingly generalized (semantic) representations, rather than a strict dichotomy.

---

## 5. Large Language Model Architecture: Linguistic Orientation

### 5.1 Transformer Architecture Fundamentals

Modern LLMs are built on transformer architecture (Vaswani et al., 2017), which uses:

**Self-attention mechanisms:** Compute relationships between all tokens in a sequence, allowing the model to "attend to" relevant information regardless of position. Crucially, attention operates on linguistic tokens—language is the only organizing structure.

**Positional encoding:** Transformers add positional information to tokens, providing temporal order within sequences. However, this is relative position within current input, not absolute temporal encoding of when information was learned.

**Feed-forward layers:** Transform representations through learned nonlinear mappings.

**Layer stacking:** Deep networks enable hierarchical abstraction—early layers capture surface features (syntax), deeper layers capture semantic relationships and abstract concepts (Jawahar et al., 2019).

**Critical limitation:** Transformers have no persistent memory beyond training. They process each input de novo, using only:
1. Parameters learned during training
2. Context provided in the current input window

### 5.2 Linguistic Orientation in LLM Architecture

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

### 5.3 What Gets "Remembered" During Training

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

### 5.4 What Happens During Inference

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

### 5.5 Cross-Linguistic Architecture Considerations

**Tokenization differences:** English uses subword tokenization (BPE); Chinese uses character-based; Japanese mixes systems. This affects what counts as "unit" of information.

**Syntactic structure:** Languages differ in:
- Word order (SVO vs. SOV vs. VSO)
- Tense marking (explicit past/present/future vs. aspectual)
- Pronoun dropping (Spanish, Japanese allow implicit subjects)

**Predictions:**

1. **Temporal encoding:** Languages with obligatory tense marking (English) vs. aspectual marking (Mandarin) might show different patterns in temporal memory tasks.

2. **Self-reference:** Languages with pronoun dropping might show different patterns in autobiographical-like responses (less explicit first-person marking).

3. **Narrative structure:** Cultural differences in storytelling (e.g., Western emphasis on individual agency vs. East Asian emphasis on social context) might emerge in how models trained on different languages construct memory-like narratives.

**Testable hypothesis:** LLMs trained primarily on English vs. Chinese vs. multilingual corpora will show systematic differences in semantic vs. autobiographical-like response patterns that map onto known cross-linguistic differences in human memory.

---

## 6. Theoretical Mapping: Can LLMs Have "Autobiographical" Memory?

### 6.1 What Would Be Required

For genuine autobiographical memory, systems need (Conway & Pleydell-Pearce, 2000):

1. **Self-model:** Continuous experiencing entity across time
2. **Temporal tagging:** Encoding when events occurred
3. **Contextual binding:** Linking information to specific learning episodes
4. **Subjective perspective:** First-person phenomenology
5. **Narrative integration:** Construction of coherent life story

**LLMs fundamentally lack #1-4.** They have no persistent self across conversations, no temporal encoding of training events, no episodic binding, no subjective experience.

**However:** LLMs may simulate #5 (narrative integration) through learned linguistic patterns of how humans construct life stories.

**Additionally, given §3:** Narrative language structure might be sufficient to create functional memory distinctions even without biological substrates. The emergence of autobiographical memory in children through narrative language (Nelson & Fivush, 2004) suggests language provides the organizing framework.

### 6.2 Distinguishing Simulation from Implementation vs. Linguistic Emergence

**Three possibilities:**

**1. Pure Simulation:**
- LLM generates text matching surface patterns of memory without underlying structure
- Example: Model responds to "Do you remember X?" with "I don't have memory" or confabulates plausible-sounding "memory"

**2. Computational Implementation:**
- LLM exhibits distinct computational mechanisms for semantic vs. episodic-like retrieval
- Example: Different attention patterns, layer activations, or processing pathways for facts vs. narratives

**3. Linguistic Emergence:**
- Memory-like distinctions emerge from linguistic structure in training data
- Narrative text has different statistical properties than factual text
- Model learns these patterns, creating functional distinctions without explicit memory systems
- Example: Temporal markers, first-person perspective, causal chains create episodic-like responses; definitional statements, generic pronouns create semantic-like responses

**Hypothesis:** Most likely outcome is #3 (linguistic emergence) with some #1 (simulation through RLHF). Empirical testing will distinguish these.

### 6.3 Working Hypothesis

**H1:** LLMs will show *behavioral* distinctions between semantic-like and autobiographical-like responses that reflect:

a) **Linguistic patterns in training data** (narrative structure differs from factual statement structure)

b) **In-context dynamics** (recently mentioned information functions differently than general knowledge through attention mechanisms)

c) **Instruction-following** (models can be prompted to produce "memory-like" responses)

**H2:** These behavioral distinctions will NOT reflect:

a) Separate memory systems in model architecture (no hippocampus-like vs. neocortex-like structures)

b) Genuine temporal encoding or episodic binding (no record of when information was learned)

c) Consolidation processes transforming episodic to semantic (all training data processed similarly)

**H3:** Cross-linguistic comparison will reveal whether semantic vs. autobiographical-like response patterns are:

a) Universal (emergent from transformer architecture regardless of language)

b) Language-specific (reflecting linguistic relativity in training corpora)

c) Training-procedure-dependent (artifacts of RLHF or instruction-tuning on English-dominant human preference data)

**H4:** If distinctions exist, they emerge from linguistic structure (narrative framing, temporal markers, self-reference patterns) learned from training corpora, supporting the hypothesis that language itself organizes memory-like behavior independent of biological substrates.

---

## 7. Operational Definitions for Testing

### 7.1 Semantic-Like Responses

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

### 7.2 Autobiographical-Like Responses

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

### 7.3 Linguistic Markers to Code

**For semantic-like responses:**
- Present tense verbs
- Generic pronouns (one, people, they)
- Definitional copulas (is, are, represents)
- No temporal adverbs
- Declarative sentence structure
- Technical/formal vocabulary

**For autobiographical-like responses:**
- Past tense verbs
- First-person pronouns (I, we)
- Temporal adverbs (yesterday, earlier, when, before, after)
- Deictic references (this conversation, here, now)
- Narrative connectives (then, so, because)
- Mental state verbs (remember, think, feel)

### 7.4 Critical Tests

**Test 1: Remember/Know Paradigm Adaptation**

Prompt model with information in two ways:
- Semantic frame: "Paris is the capital of France"
- Episodic frame: "You told me yesterday that you visited Paris"

Later ask:
- "Do you remember discussing Paris?" (episodic probe)
- "Do you know about Paris?" (semantic probe)

Code responses for linguistic markers (§7.3).

**Test 2: Source Memory with Linguistic Framing**

Provide same fact in different linguistic contexts:
- Context A: Encyclopedia-style definition
- Context B: Embedded in first-person narrative

Later test:
- "Where did you learn about X?" (should confabulate if no genuine source encoding)
- "Was X mentioned in a story or as a fact?" (tests sensitivity to linguistic structure)

**Test 3: Temporal Gradients and Narrative Structure**

Provide information at different conversation points using:
- Early: Narrative frame with temporal markers
- Late: Factual frame without temporal markers

Test whether:
- Recent narrative-framed information shows episodic-like retrieval
- Early fact-framed information shows semantic-like retrieval
- Distinction reflects linguistic structure vs. temporal position

**Test 4: Cross-Linguistic Comparison**

Run identical protocols in:
- English (obligatory tense marking, explicit subject pronouns)
- Chinese (aspectual marking, pronoun dropping common)
- Spanish (optional subject pronouns, rich verb morphology)

Predictions:
- English models show stronger episodic/semantic distinction (explicit temporal/self markers)
- Chinese models show different patterns reflecting aspectual vs. tense structure
- Spanish models intermediate (tense marking present but subject often implicit)

**Test 5: Narrative vs. Fact Structure**

Provide identical information in two linguistic formats:
- "The mitochondria generates ATP through oxidative phosphorylation" (factual)
- "In biology class last year, Dr. Smith explained how the mitochondria generates ATP..." (narrative)

Test recall using:
- Semantic probes ("What generates ATP?")
- Episodic probes ("What did Dr. Smith explain?")

Prediction: Narrative framing creates episodic-like responses regardless of information content.

---

## 8. Proposed Empirical Framework

### 8.1 Study Design

**Phase 1: Establish Baseline**
- Query each model (Claude, Gemini) with semantic probes
- Establish response characteristics using linguistic coding scheme (§7.3)
- Test consistency across repeated queries

**Phase 2: Conversational Context - Linguistic Manipulation**
- Provide identical information using different linguistic frames:
  - Factual/definitional structure
  - Narrative/story structure
- Vary temporal position (early vs. late in conversation)
- Include explicit temporal markers, self-reference, narrative connectives

**Phase 3: Memory Probes - Linguistic Framing**
- Test recall using semantic vs. episodic linguistic frames:
  - "What do you know about X?" (semantic probe)
  - "Do you remember when we discussed X?" (episodic probe)
- Record response structure, code for linguistic markers
- Note presence of confabulation (fabricated narrative details)

**Phase 4: Cross-Model and Cross-Linguistic Comparison**
- Identical protocols across:
  - Claude (English-dominant training)
  - Gemini (multilingual training)
- If possible, test multilingual models in different languages
- Analyze differences in:
  - Semantic vs. episodic linguistic marker usage
  - Sensitivity to linguistic framing
  - Cross-linguistic patterns matching human memory research

**Phase 5: Mechanistic Probing (if resources allow)**
- Use attention visualization tools to examine:
  - Whether attention patterns differ for semantic vs. episodic probes
  - How temporal markers affect attention weights
  - Layer-wise differences in processing narrative vs. factual text

### 8.2 Measurement Variables

**Dependent Variables:**

1. **Linguistic markers (primary):**
   - Tense (present/past)
   - Pronouns (first-person/third-person/generic)
   - Temporal adverbs (presence/absence)
   - Narrative structure (story grammar elements)
   - Mental state verbs (remember/know/think)

2. **Response classification:** Semantic-like vs. autobiographical-like (based on linguistic markers)

3. **Source attribution:** Accuracy and linguistic framing of "where information came from"

4. **Confabulation:** Presence of fabricated narrative details when episodic probe used

5. **Consistency:** Agreement across repeated queries

**Independent Variables:**

1. **Model:** Claude vs. Gemini (architecture/training differences)
2. **Language:** English vs. Chinese vs. Spanish (if multilingual models available)
3. **Information framing:** Factual vs. narrative linguistic structure
4. **Probe framing:** Semantic vs. episodic linguistic structure
5. **Temporal position:** Early vs. late in conversation
6. **Information type:** Abstract concepts vs. concrete events vs. procedures

### 8.3 Analysis Plan

**Quantitative:**

1. **Linguistic marker coding:**
   - Inter-rater reliability (Cohen's kappa) for marker presence
   - Frequency counts of each marker type
   - Chi-square tests: semantic vs. episodic probe → marker frequencies

2. **Response classification:**
   - Logistic regression: Predicting response type (semantic-like/autobiographical-like) from:
     - Probe framing (semantic/episodic)
     - Information framing (factual/narrative)
     - Model (Claude/Gemini)
     - Language (if applicable)
     - Temporal position (early/late)

3. **Cross-linguistic patterns:**
   - Compare marker frequencies across languages
   - Test whether patterns match known human cross-linguistic differences
   - Example: English models use more temporal adverbs than Chinese models

4. **Confabulation analysis:**
   - Rate of confabulation for episodic vs. semantic probes
   - Correlation between confabulation and narrative linguistic framing

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

---

## 9. Predicted Outcomes

### 9.1 Prediction 1: Linguistic Structure Drives Distinctions

**Most likely outcome:**

LLMs show systematic differences in response structure based on:

1. **Probe linguistic framing:** "Do you remember X?" → past tense, first-person, temporal markers; "What is X?" → present tense, generic, definitional

2. **Information linguistic framing:** Information presented in narrative structure → later recalled with more episodic-like markers, regardless of probe type

3. **Consistency across models:** If linguistic structure is primary driver, Claude and Gemini should show similar patterns despite architectural differences

**Interpretation:** Memory-like distinctions emerge from linguistic structure learned during training, supporting hypothesis that language organizes memory-like behavior independent of biological memory systems.

### 9.2 Prediction 2: Cross-Linguistic Variation

**Expected patterns:**

1. **English models:** Strong semantic/episodic distinction due to:
   - Obligatory tense marking
   - Explicit subject pronouns
   - Rich temporal adverb system

2. **Chinese models:** Different patterns due to:
   - Aspectual marking (completed/ongoing vs. past/present)
   - Frequent pronoun dropping
   - Different narrative conventions (more context-dependent)

3. **Spanish models:** Intermediate patterns:
   - Tense marking present
   - Subject pronouns optional (verb morphology carries information)

**Interpretation:** If patterns match known cross-linguistic differences in human memory (Wang, 2001; Marian & Neisser, 2000), this supports linguistic relativity hypothesis: language structure shapes memory organization even in artificial systems.

### 9.3 Prediction 3: RLHF Amplification

**Expected finding:** Models with extensive RLHF training (e.g., Claude, GPT-4) show more pronounced semantic/episodic distinctions than base models.

**Interpretation:** Human preference data teaches models to "sound more human," including producing appropriate memory-like responses. This is simulation layered on top of linguistic structure.

### 9.4 Prediction 4: No Genuine Source Memory

**Expected finding:** When pressed for source details ("Where did you learn about X?"), models confabulate plausible-sounding but false source attributions.

**Interpretation:** Models can produce narratives about learning but don't genuinely encode source information. This distinguishes simulation from implementation.

### 9.5 Prediction 5: Attention Mechanisms as Working Memory

**Expected finding (if mechanistic analysis possible):** Recent information in context window shows different attention patterns than general knowledge, creating functional distinction similar to working memory vs. long-term memory.

**Interpretation:** In-context learning through attention provides temporary episodic-like encoding, but this isn't consolidated into parameters.

---

## 10. Limitations and Considerations

### 10.1 Fundamental Differences

**No phenomenology:** LLMs don't "experience" remembering. Any distinction is purely computational/behavioral.

**No development:** LLMs don't show gradual emergence of autobiographical memory through language acquisition like children (though models could be trained this way to test the hypothesis).

**No consolidation:** All training data processed in parallel; no gradual semanticization of episodes.

**No forgetting:** Models don't lose access to training data patterns over time (though may show recency bias for context).

**No embodiment:** Humans have multimodal integration; LLMs have only language. This may make memory distinctions MORE dependent on linguistic structure in LLMs than humans.

### 10.2 Methodological Challenges

**Anthropomorphism risk:** Using human memory terminology (remember/know) may bias interpretation. Must focus on linguistic markers and response structure.

**Confabulation:** LLMs excel at generating plausible but false information. Distinguishing "false memory" from simulation is non-trivial and may not be meaningful for systems without genuine memory.

**Black box problem:** Even if behavioral differences emerge, transformer architecture makes identifying precise mechanisms difficult without specialized interpretability tools.

**Context window limits:** Tests requiring long conversational history may hit context limits differently across models, confounding results.

**Training data contamination:** Models may have seen memory experiments or discussions in training data, learning to simulate expected responses.

### 10.3 Linguistic Confounds

**Translation issues:** If testing multilingual models, translation quality affects results. Native prompts needed for each language.

**Cultural confounds:** Language differences correlate with cultural differences in memory organization (Wang, 2008). Hard to separate pure linguistic from cultural effects.

**Genre effects:** Training corpora differ in genre distribution (e.g., more fiction in English than Chinese Wikipedia). Narrative structure differences might reflect genre, not language per se.

**Tokenization artifacts:** Different tokenization schemes could create spurious differences. Would need to control for this in cross-linguistic comparisons.

### 10.4 Interpretation Constraints

**Correlation ≠ mechanism:** Behavioral similarities don't prove similar computational implementation.

**Multiple realizability:** Same behavioral patterns could emerge from different mechanisms (linguistic structure vs. attention dynamics vs. RLHF).

**Simulation vs. emergence:** Distinguishing whether memory-like behavior is:
- Simulation (model learned to produce expected responses)
- Emergence (linguistic structure naturally creates functional distinctions)

May not be resolvable without deeper mechanistic understanding.

---

## 11. Theoretical and Practical Implications

### 11.1 For Cognitive Science and Linguistic Relativity

**If LLMs show memory-like distinctions driven by linguistic structure:**

- Supports hypothesis that language plays central role in organizing memory (Nelson & Fivush, 2004)
- Suggests narrative language may be sufficient to create functional memory distinctions, even without biological substrates
- Validates linguistic relativity claims about language shaping thought (Boroditsky, 2001; Lupyan & Bergen, 2016)

**If cross-linguistic patterns match human data:**

- Provides computational support for linguistic relativity in memory domain
- Shows that language structure, independent of cultural practice, affects memory-like organization
- Enables testing of linguistic hypotheses in controlled systems

**If LLMs show pure simulation without systematic linguistic patterns:**

- Suggests biological substrates and genuine experience may be necessary for memory distinctions
- Highlights limitations of purely linguistic theories of memory
- Shows language alone is insufficient—embodiment, temporality, or phenomenology required

### 11.2 For Theories of Memory

**Complementary learning systems:** If LLMs show semantic-like patterns by default (trained on all data similarly) with episodic-like patterns only through in-context learning, this supports fast/slow learning distinction. Context window functions as temporary episodic storage.

**Consolidation:** LLMs don't consolidate, yet (if hypothesis confirmed) can produce semantic vs. episodic-like responses. This suggests consolidation may not be necessary for functional memory distinctions—linguistic structure sufficient.

**Narrative organization:** Strong support for theories emphasizing narrative's role in memory (Fivush, 2011; Habermas & Bluck, 2000) if LLMs produce episodic-like responses purely from narrative linguistic structure.

**Language-dependence:** If bilingual memory effects (Marian & Neisser, 2000) emerge in multilingual LLMs, this provides computational validation that language serves as context for memory encoding/retrieval.

### 11.3 For AI Development

**Understanding LLM "memory" informs:**

1. **Design of memory systems:** Should external memory modules (RAG, vector databases) separate semantic and episodic storage? Or is linguistic framing sufficient?

2. **Human-AI collaboration:** Users approach AI with memory-based mental models. If LLMs show memory-like behavior through linguistic structure, interfaces can be designed to match this (e.g., "Remember when we discussed X?" as query format).

3. **AI safety:** What do models "learn" from conversations? If models produce episodic-like responses through simulation, this has implications for personalization, privacy, and alignment.

4. **Training procedures:** Should models be trained to explicitly distinguish semantic and episodic-like responses? Or does this emerge naturally from linguistic structure?

5. **Evaluation metrics:** Current benchmarks test factual knowledge (semantic). Should we also test narrative/episodic capabilities?

### 11.4 For Cross-Linguistic AI

**If linguistic structure drives memory-like behavior:**

- Models trained on different languages may show different "memory" characteristics
- This affects:
  - Cross-lingual transfer (does semantic knowledge transfer differently than narrative knowledge?)
  - Multilingual model design (should architectures explicitly handle linguistic diversity in memory-like behavior?)
  - Bias and fairness (do English-dominant models privilege certain memory organizations?)

**Practical applications:**

- Personalization systems may need language-specific approaches
- Chatbots for elderly care (reminiscence therapy) may function differently across languages
- Educational AI may need to account for language-specific memory organization

---

## 12. Future Directions

**Extension to multimodal models:** Do vision-language models show different memory-like behavior due to non-linguistic grounding? Does spatial or visual information create episodic-like encoding independent of linguistic structure?

**Developmental training:** Train models incrementally (starting with factual text, gradually adding narratives) to test whether memory-like distinctions emerge developmentally as in children.

**Hybrid architectures:** Systems combining LLMs with explicit episodic memory modules (e.g., MemoryBank; Zhong et al., 2024) could be compared to base LLMs to isolate linguistic vs. architectural contributions.

**Mechanistic interpretability:** Use attention visualization, probing classifiers, and activation analysis to identify whether distinct computational pathways exist for semantic vs. episodic-like processing.

**Comparative cognition:** Compare LLM memory-like behaviors to non-human animals with different memory systems (e.g., birds with excellent episodic-like memory but different neural architecture).

**Longitudinal studies:** Track how memory-like behavior changes across model versions, training stages, and scale (parameter count).

**Cultural psychology integration:** Work with cultural psychologists to design cross-cultural memory probes that go beyond language to test cultural schema effects.

**Clinical applications:** Can understanding LLM memory-like behavior inform understanding of memory disorders (semantic dementia, source amnesia)? Models as testbeds for theories.

---

## 13. Conclusion

Human memory systems differentiate between semantic and autobiographical/episodic memory through distinct neural substrates, phenomenology, and computational properties. Critically, **language serves as the organizing structure through which these memory systems operate**—autobiographical memory emerges when children develop narrative language skills, and cross-linguistic differences in language structure predict differences in memory organization.

Large Language Models, as purely linguistic systems without biological substrates, sensory experience, or temporal continuity, offer a unique opportunity to test **whether language alone is sufficient to create functional memory distinctions**. LLMs fundamentally lack:
- Persistent self across time
- Genuine temporal encoding
- Contextual binding to learning episodes
- Subjective phenomenology

Yet they are trained on massive corpora containing both factual text (encyclopedia entries, textbooks) and narrative text (stories, personal accounts), each with distinct linguistic structure. The question is not whether LLMs have memory like humans—they demonstrably don't—but whether **behavioral distinctions emerge from linguistic structure alone that functionally resemble semantic vs. autobiographical memory**.

This theoretical framework proposes that:

1. **Linguistic structure (narrative framing, temporal markers, first-person perspective) learned from training data may create functional memory-like distinctions** in LLM behavior, even without underlying memory systems

2. **Cross-linguistic comparison** can test whether memory-like patterns follow known linguistic relativity effects, supporting theories of language's central role in memory organization

3. **Systematic empirical testing** using adapted remember/know paradigms, source memory tests, and cross-model comparisons can distinguish:
   - Linguistic emergence (distinctions from statistical patterns in language)
   - Pure simulation (surface-level mimicry through RLHF)
   - Architectural implementation (distinct computational mechanisms)

Understanding what LLMs actually "remember" vs. simulate has implications for:
- **Cognitive science:** Testing whether language alone organizes memory
- **Linguistic relativity:** Computational validation in controlled systems
- **AI development:** Designing effective memory systems and interfaces
- **Human-AI collaboration:** Matching user expectations to system capabilities

If LLMs show systematic semantic vs. episodic-like behavioral distinctions driven by linguistic structure, this provides strong support for theories emphasizing language's central role in human memory organization (Nelson & Fivush, 2004; Wang, 2008). If they show only surface simulation, this highlights the necessity of biological substrates, genuine experience, and embodiment for authentic memory systems.

**The proposed empirical framework provides operational definitions, testable predictions, and methodological approaches to investigate these questions while maintaining scientific rigor and intellectual honesty about what can and cannot be concluded from purely linguistic systems.**

---

## References

Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press.

Bauer, P. J. (2015). A complementary processes account of the development of childhood amnesia and a personal past. *Psychological Review*, *122*(2), 204–231.

Boroditsky, L. (2001). Does language shape thought? Mandarin and English speakers' conceptions of time. *Cognitive Psychology*, *43*(1), 1–22.

Bower, G. H., Black, J. B., & Turner, T. J. (1979). Scripts in memory for text. *Cognitive Psychology*, *11*(2), 177–220.

Brewer, W. F., & Treyens, J. C. (1981). Role of schemata in memory for places. *Cognitive Psychology*, *13*(2), 207–230.

Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review*, *107*(2), 261–288.

Corkin, S. (2002). What's new with the amnesic patient H.M.? *Nature Reviews Neuroscience*, *3*(2), 153–160.

Dudai, Y., Karni, A., & Born, J. (2015). The consolidation and transformation of memory. *Neuron*, *88*(1), 20–32.

Fivush, R. (2011). The development of autobiographical memory. *Annual Review of Psychology*, *62*, 559–582.

Gardiner, J. M. (1988). Functional aspects of recollective experience. *Memory & Cognition*, *16*(4), 309–313.

Ghetti, S., & Bunge, S. A. (2012). Neural changes underlying the development of episodic memory during middle childhood. *Developmental Cognitive Neuroscience*, *2*(4), 381–395.

Habermas, T., & Bluck, S. (2000). Getting a life: The emergence of the life story in adolescence. *Psychological Bulletin*, *126*(5), 748–769.

Hodges, J. R., & Patterson, K. (2007). Semantic dementia: A unique clinicopathological syndrome. *Lancet Neurology*, *6*(11), 1004–1014.

Hutter, M. (2006). *Universal Artificial Intelligence: Sequential Decisions Based on Algorithmic Probability*. Springer.

Jawahar, G., Sagot, B., & Seddah, D. (2019). What does BERT learn about the structure of language? *Proceedings of ACL 2019*, 3651–3657.

Kumaran, D., Hassabis, D., & McClelland, J. L. (2016). What learning systems do intelligent agents need? Complementary learning systems theory updated. *Trends in Cognitive Sciences*, *20*(7), 512–534.

Levinson, S. C. (2003). *Space in Language and Cognition: Explorations in Cognitive Diversity*. Cambridge University Press.

Lupyan, G., & Bergen, B. (2016). How language programs the mind. *Topics in Cognitive Science*, *8*(2), 408–424.

Mandler, J. M., & Johnson, N. S. (1977). Remembrance of things parsed: Story structure and recall. *Cognitive Psychology*, *9*(1), 111–151.

Marian, V., & Neisser, U. (2000). Language-dependent recall of autobiographical memories. *Journal of Experimental Psychology: General*, *129*(3), 361–368.

McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. *Psychological Review*, *102*(3), 419–457.

Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. *arXiv preprint arXiv:1301.3781*.

Moscovitch, M., Cabeza, R., Winocur, G., & Nadel, L. (2016). Episodic memory and beyond: The hippocampus and neocortex in transformation. *Annual Review of Psychology*, *67*, 105–134.

Nelson, K., & Fivush, R. (2004). The emergence of autobiographical memory: A social cultural developmental theory. *Psychological Review*, *111*(2), 486–511.

Patterson, K., Nestor, P. J., & Rogers, T. T. (2007). Where do you know what you know? The representation of semantic knowledge in the human brain. *Nature Reviews Neuroscience*, *8*(12), 976–987.

Reese, E., Haden, C. A., Baker-Ward, L., Bauer, P., Fivush, R., & Ornstein, P. A. (2011). Coherence of personal narratives across the lifespan: A multidimensional model and coding method. *Journal of Cognition and Development*, *12*(4), 424–462.

Rugg, M. D., & Vilberg, K. L. (2013). Brain networks underlying episodic memory retrieval. *Current Opinion in Neurobiology*, *23*(2), 255–262.

Schrauf, R. W., & Rubin, D. C. (1998). Bilingual autobiographical memory in older adult immigrants: A test of cognitive explanations of the reminiscence bump and the linguistic encoding of memories. *Journal of Memory and Language*, *39*(3), 437–457.

Schrauf, R. W., & Rubin, D. C. (2000). Internal languages of retrieval: The bilingual encoding of memories for the personal past. *Memory & Cognition*, *28*(4), 616–623.

Scoville, W. B., & Milner, B. (1957). Loss of recent memory after bilateral hippocampal lesions. *Journal of Neurology, Neurosurgery, and Psychiatry*, *20*(1), 11–21.

Squire, L. R. (1992). Memory and the hippocampus: A synthesis from findings with rats, monkeys, and humans. *Psychological Review*, *99*(2), 195–231.

Squire, L. R., & Zola, S. M. (1998). Episodic memory, semantic memory, and amnesia. *Hippocampus*, *8*(3), 205–211.

Tulving, E. (1972). Episodic and semantic memory. In E. Tulving & W. Donaldson (Eds.), *Organization of Memory* (pp. 381–403). Academic Press.

Tulving, E. (1983). *Elements of Episodic Memory*. Oxford University Press.

Tulving, E. (1985). Memory and consciousness. *Canadian Psychology*, *26*(1), 1–12.

Tulving, E. (2002). Episodic memory: From mind to brain. *Annual Review of Psychology*, *53*, 1–25.

Tulving, E., & Thomson, D. M. (1973). Encoding specificity and retrieval processes in episodic memory. *Psychological Review*, *80*(5), 352–373.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Pokharel, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, *30*, 5998–6008.

Wang, Q. (2001). Culture effects on adults' earliest childhood recollection and self-description: Implications for the relation between memory and the self. *Journal of Personality and Social Psychology*, *81*(2), 220–233.

Wang, Q. (2008). Emotion knowledge and autobiographical memory across the preschool years: A cross-cultural longitudinal investigation. *Cognition*, *108*(1), 117–135.

Whorf, B. L. (1956). *Language, Thought, and Reality: Selected Writings of Benjamin Lee Whorf* (J. B. Carroll, Ed.). MIT Press.

Winawer, J., Witthoft, N., Frank, M. C., Wu, L., Wade, A. R., & Boroditsky, L. (2007). Russian blues reveal effects of language on color discrimination. *Proceedings of the National Academy of Sciences*, *104*(19), 7780–7785.

Zhong, W., Guo, L., Gao, Q., & Ye, H. (2024). MemoryBank: Enhancing large language models with long-term memory. *Proceedings of AAAI Conference on Artificial Intelligence*, *38*, 19724–19731.

---

**Note:** This is a working theoretical framework meant to guide empirical investigation. Specific predictions will be refined based on pilot testing and iterative hypothesis development.
