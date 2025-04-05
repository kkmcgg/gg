# Extended POBS-QC Format Specification

The **Extended POBS-QC** (Predicate-Object-By-Subject with Qualifiers and Conjunctions) format is a structured schema for representing knowledge as atomic, composable statements. It extends the base POBS format by introducing distinct lettered components to handle complex linguistic and logical structures.

## Element Definitions

Each component is assigned a unique letter identifier:

- **S** – **Subject**: The entity performing or being described.  
- **P** – **Predicate**: The verb or relational descriptor.  
- **O** – **Object**: The entity being acted upon or described.  
- **B** – **By**: The source or agent responsible for the statement.  
- **Q** – **Qualifier**: Conditional/contextual info modifying the truth (e.g., time, place, state).  
- **C** – **Conjunction**: Logical connectors (AND, OR, IF, WHEN, UNLESS, etc.).  
- **M** – **Modifier**: Adjectives or adverbs qualifying S, P, or O.  
- **N** – **Negation**: Explicit negation of predicate or object.  
- **R** – **Relation**: Comparative or hierarchical relationships (e.g., “greater than,” “part of”).  
- **T** – **Temporal Frame**: Specifies when the statement holds true (more precise than Q).  
- **Z** – **Certainty**: Degree of confidence, probability, or fuzziness.  

## Example

**Sentence**: _“The lake was frozen by nature, when it was winter, with high certainty.”_

Structured as:

- **S**: The lake  
- **P**: was  
- **O**: frozen  
- **B**: by nature  
- **Q**: when it was winter  
- **Z**: high certainty  

## Advantages

- **Atomicity**: Each fragment is discrete and traceable.  
- **Composability**: Enables reassembly and integration across sources.  
- **Scalability**: Handles increasingly complex sentences without collapsing.  
- **Interoperability**: Aligns with RDF, triples, graph databases, and natural language parsing pipelines.