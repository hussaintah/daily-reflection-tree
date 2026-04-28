# Design Rationale: Daily Reflection Tree

## Approach

I designed the reflection tool as a deterministic conversation rather than a chatbot. The goal was to help an employee reflect at the end of the day without relying on runtime AI. Every question has fixed options, every branch has a known destination, and every reflection is pre-written. This keeps the tool predictable, auditable, and safe from AI hallucination.

I structured the tree around the three required axes:

1. Locus: Victim vs Victor
2. Orientation: Contribution vs Entitlement
3. Radius: Self-Centrism vs Altrocentrism

The flow moves from personal agency, to contribution, to wider perspective. This sequence felt natural because a person first reflects on how they responded, then what they gave, and finally who else was affected.

## Why These Questions Were Chosen

For Axis 1, I used questions about control, reaction, and responsibility. These are based on Locus of Control and Growth Mindset. I avoided asking “Were you a victim today?” because that would feel judgmental. Instead, the tree asks about specific reactions such as adapting, waiting, blaming, or fixing what was controllable.

For Axis 2, I focused on whether the employee noticed what they gave or what they expected. This connects to Psychological Entitlement and Organizational Citizenship Behavior. The questions are designed to surface entitlement without shaming the user. For example, feeling under-recognized is not treated as “bad”; it becomes a reflection point.

For Axis 3, I used questions that widen the employee’s perspective from self, to team, to colleague, to customer. This is based on self-transcendence and perspective-taking. The aim is not to make the employee ignore their own stress, but to help them place their experience inside a wider human and organizational context.

## Branching Design

The branching is intentionally simple. I used decision nodes to separate broad response patterns:

- Internal vs external control
- Contribution vs entitlement
- Self-focused vs wider perspective

I avoided complex scoring models because the assignment emphasizes deterministic trees, not AI classification or hidden psychological scoring. The tree uses signals only as simple tallies, such as `axis1:internal` or `axis2:contribution`.

The reflections are not meant to diagnose the employee. They reframe the answer gently. For example, if someone chooses an external-control answer, the reflection does not blame them. It says that the day may have felt outside their control, but asks them to notice one choice they still made.

## Trade-offs

One trade-off was depth versus readability. A much larger tree could explore every answer in more detail, but it might become tiring for an employee at the end of the day. I kept the tree short enough to feel usable while still covering all three axes.

Another trade-off was fixed options versus emotional accuracy. Real human experiences are complex, and fixed options cannot capture everything. However, fixed options are necessary for determinism. I tried to make the options broad enough that most users could find a close match.

A third trade-off was tone. If the reflections are too soft, the user may not think deeply. If they are too direct, the tool may feel moralizing. I chose a tone similar to a wise colleague: honest, calm, and non-judgmental.

## Psychological Sources

The design was informed by:

- Julian Rotter’s Locus of Control theory
- Carol Dweck’s Growth Mindset
- Psychological Entitlement research by Campbell et al.
- Organizational Citizenship Behavior by Dennis Organ
- Maslow’s idea of self-transcendence
- Perspective-taking research associated with Batson

I used these theories as design anchors, not as diagnostic labels. The tree does not claim to measure personality. It simply guides structured reflection.

## Use of AI and Hallucination Guardrails

I used AI as a design assistant to brainstorm questions, critique options, and test possible employee personas. However, the final product does not call an LLM at runtime.

The guardrails are:

- No free-text input
- No AI-generated runtime responses
- Fixed options only
- Deterministic routing
- Pre-written reflection text
- Visible tree structure
- Simple signal tallying instead of hidden scoring

I rejected AI suggestions that sounded like therapy, moral judgment, or motivational quotes. I also removed questions that were too vague or had overlapping options.

## What I Would Improve With More Time

With more time, I would improve the tree in four ways:

1. Add more nuanced branches inside each axis.
2. Test the questions with real employees to see if the options feel natural.
3. Add a lightweight UI to make the experience smoother.
4. Create more personalized summary templates based on different signal combinations.

The current version is intentionally simple, deterministic, and readable as data.
