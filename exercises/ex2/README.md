# Chapter 3 – Scoping Agent

**Prerequisite:** You have completed [Chapter 2](../ex1/README.md); the BJ5 process has linked requirements and user stories.

---

## What You'll Do

In this chapter you'll unleash the **Scoping Agent**: an AI agent that reads all your linked process documentation and proposes a structured set of test cases. While the agent works, you'll experience what manual scoping looks like, so you can appreciate the comparison.

---

## 3.1 – Trigger the Scoping Agent

Time to try again; with proper input now in place.

### 3.1.1 – Prompt Joule (same as Step 1.3)

1. Open a new conversation in Joule and send the **same prompt** as in Step 1.3:

   > *"I need to test process "Beta_Straight Make-to-Stock Production – Discrete Manufacturing (BJ5_simple)" in project "###_TestProject""*
   >
   > Replace **###** with your workstation number.

2. The scoping agent starts working in the background. You'll see a notification or progress indicator.

<br><img src="images/ex2_02_agent_running.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>02 – Scoping agent running</em></p>

---

## 3.2 – What's Happening? (Narration)

<br><img src="images/ex2_03_scoping_agent_flow.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>03 – Scoping agent methodology</em></p>

> The scoping agent applies a structured methodology:
> 1. It resolves the process name, requirements, and user stories to exact identifiers in SAP Cloud ALM
> 2. It validates that the required input exists; if not, it blocks and returns clear instructions on what to fix
> 3. It classifies each input: process scope variants or detailed reference steps
> 4. It enriches the scope with SAP standard test baselines and extracts acceptance criteria from your linked content
> 5. It scores each scope item for completeness, ranks items by priority, and flags coverage gaps
> 6. It presents the result for your review and sign-off; no downstream work starts without your approval (HITL Gate 1)
>
> This is the same analysis a skilled test architect would do, but compressed from hours into minutes.

---

## 3.3 – Manual Scoping Exercise

While you wait for the agent, try a structured manual scoping exercise.

For the BJ5 process, work through these dimensions on a piece of paper or sticky note:

| Dimension | Your Answer |
|---|---|
| What **acceptance criteria** can you identify from the user stories and requirements? | |
| How many distinct **apps/UIs** are involved? | |
| How many **roles** participate? | |
| What are the main **process paths** (happy path + variants)? | |
| Which steps have **blocking conditions** worth testing? | |
| What **error scenarios** should be covered? | |

> Hint: The BJ5 process involves 2 roles (Production Planner and Warehouse Clerk) and spans the full make-to-stock cycle from production order creation to finished goods receipt. There is 1 critical quality gate where output is assessed before goods receipt, and a separate failure path for scrap and replenishment.

Keep your notes; you'll compare them to the agent's output next.

---

## 3.4 – Review the Scoping Agent's Work

### 3.4.1 – Open the Agent's Output

When the agent is ready, it replies directly in the Joule chat window with a **Test Scope Summary**. The response is detailed; switch Joule to **full-screen mode** first using the **expand icon** (⤢) in the top-right of the Joule panel for a much easier reading experience.

The response gives you:

- **Process context**: the solution process, flow diagram, and applicable countries it resolved
- A **summary of identified process flow paths**, reflecting any splits or variants in the process structure
- An overview of the **items it ingested**: your requirement and the 7 user stories
- Related **standard process procedures** retrieved from the SAP Enterprise Architecture Reference Library (EARL)
- A conclusive list of **acceptance criteria** derived from all of the above

<br><img src="images/ex2_04_scope_result.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>04 – Test Scope Summary in Joule</em></p>

> **HITL Gate 1: Test Scope Summary.** This is the first checkpoint in the agentic workflow. The agent stops, presents its detailed structured analysis, and waits for your review and sign-off. Nothing proceeds until you confirm.

---

### 3.4.2 – Evaluate and Compare

Take a few minutes to work through the proposed scope. For each item, check:
- **Name and description**: does it clearly describe what's being tested?
- **Linked acceptance criteria**: is it traceable back to a user story or requirement?
- **Role separation**: are Production Planner tasks and Warehouse Clerk tasks kept in separate test cases?
- **Coverage**: does the overall set cover the happy path (P1), the quality gate failure path (P2), and the scrap/replenishment scenario?

> **Compare with your manual notes from Step 3.3:** Did the agent catch everything you identified? Did it find things you missed? This is the key learning moment of this chapter.

---

## 3.5 – Refine the Scope in Joule

The first scoping suggestion is your starting point. Joule lets you refine it through conversation.

> **Note for participants sharing a system:** The agents run on shared infrastructure. To avoid overloading the system with concurrent calls, keep your refinement focused. We recommend limiting the scope to **user stories 5, 6, and 7** (the quality gate, goods receipt, and failure path).

**Option 1: Use the built-in Revise Scope shortcut**

Click the **Select** button in the Joule output panel, then choose **Revise Scope** from the dropdown. Joule converts your selection into a refinement prompt and sends it to the agent automatically.

<!-- 📷 TODO: screenshot ex2_06_revise_button.png: Select button → dropdown → Revise Scope / "No, let me revise" option -->
<br><img src="images/ex2_06_revise_button.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>06 – Built-in Revise Scope option</em></p>

**Option 2: Write your own prompt**

You can also type your refinement directly in the Joule chat window. Use this starting point:

> *"Focus on user stories [insert three user story IDs from your scope, format 3-456, for example the last three focusing on the decision point / path split]. In particular take care of roles and create test cases which do NOT cross multiple roles."*

<br><img src="images/ex2_05_refine_scope.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>05 – Refinement prompt: focusing on three user stories</em></p>

Or try one of these:
- **Narrow the scope:** "Remove user stories 1–4 from the scope for now; focus only on the quality gate, goods receipt, and scrap path."
- **Split a test case by role:** "Split the goods issue test case into two; one for the Production Planner and one for the Warehouse Clerk."

---

## Summary

When you're satisfied with the scope, signal your approval in Joule. This is **HITL Gate 1**: the preparation agent will not begin building the test plan until you confirm.

The scoping agent analyzed all your linked process artifacts and proposed a structured test case scope; with traceability to requirements and user stories; in the time it took you to sketch a rough outline manually.

You now have a **confirmed test case scope** ready for test planning.

Continue to [Chapter 4 – Preparation Agent: Test Plan](../ex3/README.md)
