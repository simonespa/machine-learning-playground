# LLM Shortcomings

It all started with conversation answering questions covering a wide range of human knowledge

Then it evolved in:
- Summarisation and revision of text documents
- Generate text from a text instruction (prompt)
- Learn new tasks from a small number of training samples using the so-called "in-context learning"

## Problems

They produce:
- incorrect and often contraddicting content
- hallucination
- biased and offensive answers

Knowledge cannot be updated, it's hardwired in the network weights

Training, re-training and inference is expensive

It doesn't support the "ask" and "tell" operation like in the knowledge bases where "ask" generates answers, "tell" is used to add facts to the knowledge base which will then be used to update the internal knowledge and give subsequent answers on top of. LLMs only support "ask".

Lack of attribution to determine which sources are responsible for the answer in which percentage

Lack of logic inference. If we give a description to the model and then we ask question about that description, the model will fail to answer information that can be inferred by the description. For example, lack of spatial knowledge reconstruction when described through text.

## What's the cause

LLMs are not knowledge bases. They are statistical models of a knowledge base. They synthetise the answer based on the data they have been trained, but are incapable of reasoning.

## Reduce Hallucination

Retrieval-Augmented LM: they query fresh information from sources and feed it together with the prompt to the LLM in order to give a more accurate response. It reduces the hallucination and the answers can be attributed. The drawbacks are that the retrieved knowledge can conflict with the internal one and are vulnerable to information poisoning.

## Improve consistency

Ask logically-related questions multiple times and apply MaxSAT solver to find the most coherent belief. Self-refinement is to ask the model to critique itw own output to return a better refined version of it.

## Reduce dangerous output

By using reinforcment learning from human feedback

## Multimodal Models

The idea is to combine language knowledge with non-language one (visual, etc.)


## Aleatoric vs Epistemic uncertainty

From: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-quantifying-uncertainty/aleatoric-uncertainty.html and https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-quantifying-uncertainty/epistemic-uncertainty.html

Epistemic uncertainty refers to the uncertainty of the model, and is often due to a lack of training data. Examples of epistemic uncertainty include underrepresented minority groups in a facial recognition dataset or the presence of rare words in a language modeling context.

Epistemology is the study of knowledge.

Aleatoric uncertainty refers to the data's inherent randomness that cannot be explained away (aleator refers to someone who rolls the dice in Latin). Examples of data with aleatoric uncertainty include noisy telemetry data and low-resolution images or social media text.
