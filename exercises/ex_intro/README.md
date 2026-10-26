<img src="images/Kapitelbanner_Welcome.png" style="width:100%;margin-bottom:1em;" />

# TM261 – Agent-Led Test Management: Hands-on Lab with Joule in SAP Cloud ALM

**Date:** Wednesday, 28 October 2026 · SAP TechEd 2026, Berlin  
**Presenters:** SAP Cloud ALM Product Ownership:  
Christina Pickhardt · Daniel Lorenz · Niclas Weidner · Tobias Keller

---

## Agenda

| # | Section | Topic |
|---|---|---|
| – | Introduction | Test Management Assistant: context and functional agent overview |
| 1 | Getting Started | Log In & Orient Yourself |
| 2 | Generate *Requirements* | Turn an interview transcript into *Requirements* with AI |
| 3 | Scope with AI | Scoping agent; compare with manual scoping |
| 4 | Plan with AI | Planning agent; HITL Gate 2; review |
| 5 | Generate *Test Cases* | TC generation agent; quality review; parameters |
| 6 | Generate Test Data | Data agent; classify & explore; dependencies |
| 7 | Recap & Outlook | Time saved; roadmap; key takeaways |

---

# Introduction: Test Management Assistant

**Context – SAP Migration & Modernization Assistants**

Before we jump into the hands-on, a quick word on context, because what you're about to use is not an isolated feature.

SAP has developed seven AI-powered assistants for Migration and Modernization scenarios, built to help customers move from SAP ECC to S/4HANA Cloud Private Edition faster and with significantly less manual effort:

<br><img src="images/intro_7_assistants.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>01 – Seven SAP Migration & Modernization Assistants</em></p>

The **Test Management Assistant** is one of these seven, and Test Management is an area where the shift from manual to AI-driven work matters most:

End-to-end test management for SAP migrations and modernizations is still heavily dependent on business and IT personnel. It is a consistent cost driver across transition projects, and complexity grows with every regression cycle: more scenarios, more variants, more manual effort.

The Test Management Assistant targets the upstream side of this: the preparation of manual end-to-end testing. It applies AI to test scoping, test case writing, and test data preparation; these are the stages where expert effort is highest and where days of work can be compressed into minutes of guided review.

Test execution itself is outside the current scope of the assistant. That stage is covered by the partner ecosystem: Tricentis, SAP's strategic partner for test automation, provides execution capabilities that complement the AI-driven preparation in SAP Cloud ALM.

## What is the Test Management Assistant?

The Test Management Assistant is not a single AI feature; it's a pipeline of four specialized agents, each transforming a stage of manual Test Preparation into an AI-driven capability:

<br><img src="images/intro_agent_architecture.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>02 – Test Management Assistant: four-agent pipeline</em></p>

The Scoping, Preparation, and Test Data Management agents (Phase 1\*) have been released and are currently in Early Adopter Care with selected customers. GA is targeted before the end of this year. The Test Execution Quality Management agent is planned for 2027\*\*.

> *\* Partly available; \*\*planned functionality. Subject to change by SAP at any time without notice.*

> **Today's hands-on covers the three agents available today**: Scoping, Preparation, and Data Management. Execution Management is on the roadmap.


Continue to [Chapter 1 – Getting Started](../ex0/README.md)
