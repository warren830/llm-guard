# Langchain

[Langchain](https://github.com/langchain-ai/langchain) stands out as a leading AI framework, renowned for its unique approach to "Constructing applications using LLMs via composability."
But, while LangChain facilitates application construction, it doesn't directly handle LLM security. That's where LLMGuard comes into play. By pairing LLMGuard with LangChain, you're equipped with a comprehensive platform for creating regulated and adherence-driven applications anchored by language models.

## Installation

1. Install dependencies:

```bash
 pip install llm-guard langchain
```

2. Configure API key:

```bash
export OPENAI_API_KEY="<your key>"
```

## LLM Wrapper

!!! info

    This is recommended way to integrate but it has limitation when using in the asynchronous mode.

Applying LLM Guard to your application could be as simple as wrapping your LLM using the `LLMGuard` class by replacing `llm=OpenAI()` with `llm=LLMGuard(base_llm=OpenAI(), input_scanners=[], output_scanners=[])`.

Example can be found in [langchain_llm.py](https://github.com/laiyer-ai/llm-guard/blob/main/examples/langchain_llm.py).

## LLM Chain

In [langchain_chain.py](https://github.com/laiyer-ai/llm-guard/blob/main/examples/langchain_chain.py), you can find
custom `LLMGuard` chain, which can be used instead of common `LLMChain`.