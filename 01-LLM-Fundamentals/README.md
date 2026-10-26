# LLM Fundamentals

Foundational notes on large language models (LLMs), the concepts behind them, and the mechanisms that enable them to process and generate language.

## Table of Contents

- [Introduction](#introduction)
- [Why LLMs Matter](#why-llms-matter)
- [Core Concepts](#core-concepts)
- [Learning Objective](#learning-objective)

## Introduction

Large Language Models (LLMs) are deep learning models trained on large text datasets to process and generate human language. They can support tasks such as question answering, summarization, translation, coding assistance, and text generation.

Rather than relying only on a collection of predefined answers, an LLM learns statistical patterns and relationships in token sequences during training. During generation, it uses the context available to it to predict a likely next token, repeating this process to produce a sequence of text.

Understanding these fundamentals provides a foundation for studying retrieval systems, orchestration frameworks, and practical AI applications.

## Why LLMs Matter

Traditional software commonly follows explicitly programmed rules and logic:

```text
Input
  ↓
Programmed logic
  ↓
Output
```

LLMs take a different approach: they learn patterns from training data and use those learned patterns to produce context-sensitive outputs. This makes them useful for language-oriented tasks that can be difficult to handle through manually written rules alone.

Common applications include:

- Understanding and responding to natural-language input
- Generating and transforming text
- Summarizing documents
- Answering questions
- Assisting with code
- Extracting structured information from unstructured text
- Supporting decision-making workflows

LLM outputs can be incorrect or misleading, so applications should validate outputs and apply appropriate human review where needed.

## Core Concepts

The following concepts form the scope of this learning phase:

| Concept | Focus |
|---|---|
| Artificial Intelligence (AI) | The broader field of systems performing tasks associated with intelligence |
| Machine Learning vs. Deep Learning | How learning approaches relate to one another |
| Natural Language Processing (NLP) | Techniques for working with human language |
| Large Language Models (LLMs) | Models trained to process and generate language |
| Tokens and Tokenization | How text is divided into model-readable units |
| Embeddings (Introduction) | Numerical representations of text or other data |
| Transformers | A neural-network architecture used by many modern LLMs |
| Attention Mechanism | How models weigh relationships among elements in a sequence |
| Encoder vs. Decoder Architecture | Different transformer design patterns |
| BERT vs. GPT | Examples of models built for different language-modeling approaches |
| Context Window | The amount of input context a model can process at one time |
| Next-Token Prediction | A common mechanism used to generate text token by token |

## Learning Objective

The objective of this section is to build conceptual clarity about how language models represent text, process context, and generate outputs. These foundations will support later study of embeddings, retrieval-augmented generation (RAG), orchestration frameworks, and AI application development.

---

*These notes are part of an ongoing, hands-on LLM learning journey and may be refined as concepts are revisited and tested.*
