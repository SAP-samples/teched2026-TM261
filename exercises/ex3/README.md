# Chapter 4 – Plan with AI

**Prerequisite:** You have completed [Chapter 3](../ex2/README.md); a confirmed *Test Case* scope exists for the BJ5 process.

---

## What You'll Do

The scope you confirmed at the end of Chapter 3 has been handed to the **Preparation Agent**, which is already working in the background. This chapter covers the first of its two phases: planning of the *Test Plan* and its *Test Cases*, up to the point where you review and confirm the plan. While the agent works, you will learn what it is doing and why it matters.

---

## 4.1 – The Preparation Agent: Planning Phase

The Preparation Agent is a two-phase agent with a human review gate between the phases. This chapter follows Phase 1: from your confirmed scope to a proposed *Test Plan*. Phase 2 (*Test Case* generation) is covered in Chapter 5.

> **The challenge:** Similar to scoping, *Test Case* preparation relies on expertise that cannot scale. *Test Case* volumes grow into the hundreds per project; without structured reuse, duplicates accumulate across teams. Under time pressure, process variants get skipped: happy paths are covered, but error paths, authorisation checks, and boundary cases drop out. Acceptance Criteria end up patchily defined; tests pass but do not prove what they claim to verify.
>
> For each *Test Case* a skilled analyst would need to determine the right application, define preconditions, sequence steps at the correct level of detail, assign a role, and link everything back to *Requirements*, across an entire business process.
>
> **The solution:** The Preparation Agent maps execution paths and Acceptance Criteria from the process model into complete *Test Cases*. It optimises for coverage and *Test Case* efficiency; the expert shifts from producing to reviewing, and covers scope more reliably.

<br><img src="images/ex3_01_prep_agent_flow.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>28 – Preparation Agent: pipeline up to HITL Gate 2</em></p>

> **What the Preparation Agent works through:**
> 1. **Validate incoming scope:** checks quality and completeness of the scope from the Scoping Agent; flags issues before test generation begins
> 2. **Map all process variants:** reads the BPMN diagram to identify every execution path: happy path, error flows, boundary conditions, and negative flows
> 3. **Draft test plan:** creates a categorised plan covering all identified process variants; this is what you will review and approve
> 4. **HITL Gate 2 (Approve plan):** no *Test Cases* are written to Cloud ALM without your explicit approval; you review and adjust before the agent continues into Phase 2

⏱️ **While the agent works: try it yourself**

Pick one of the *Scope Items* from Chapter 3 (for example: "Confirm Production Operations") and try to write a *Test Plan* entry: a clear description (1–2 sentences), the role performing it (Production Planner or Warehouse Clerk), the preconditions that must be true, and a rough sequence of Test Steps.

How long does that take for one item? Now multiply by the full scope, and note that this is still not the final, well-formed set of *Test Case* steps. That is what *Test Plan* preparation normally looks like.

---

## 4.2 – Review the Agent's Test Plan

By now the Preparation Agent should have returned with a *Test Plan* proposal. Switch back to your Joule conversation and scroll to find its response.

**When Joule responds successfully**, it presents a structured **Test Plan Summary**. This may come in slight variations, but typical components and structure are:

- **Test Case Overview**: total number of *Test Cases*, split by path type (happy path vs. error case)
- **Role-Based Distribution**: how *Test Cases* are distributed across roles (Production Planner and Warehouse Clerk) and which *User Stories* each role covers
- **Planned Test Cases**: a deeper look at each proposed *Test Case*, with its process path, linked Acceptance Criteria, and assigned role
- **Acceptance Criteria Coverage**: a summary showing how many Acceptance Criteria from each *User Story* are addressed
- **Key Features**: summary of structural properties the agent applied, such as role isolation, balanced path coverage, and no cross-role tests

<br><img src="images/ex3_03_plan_summary.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>29 – Test Plan Summary: overview, role distribution, and planned test cases</em></p>

▶️ **Your task:** Review the plan and consider:
- Does the number of *Test Cases* feel right for the scope you confirmed?
- Are roles properly separated? No *Test Case* should span two roles.
- Are both the happy path (P1) and the error path (P2) represented?
- Do the Acceptance Criteria align with what you saw in the *User Stories*?

> **Compare with your try-it-yourself notes from Step 4.1:** Did the agent structure the plan differently than you expected? Did it catch anything you missed?

**Review (HITL) Gate 2: Approve the Test Plan**

The agent will not start writing *Test Cases* until you confirm the plan.

<br><img src="images/ex3_04_plan_confirm.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>30 – HITL Gate 2: confirm or revise the test plan</em></p>

Click **Select** next to **Confirm plan** to approve and start *Test Case* generation.

The agent confirms that *Test Case* generation has started, acknowledging your approved plan and the *User Stories* it will work on.

<br><img src="images/ex3_05_tc_generation_started.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>31 – Test case generation started</em></p>

Joule provides a rundown of what was created and what happens next:
- A **generation summary**: *Test Plan* name and total *Test Cases*
- **Key features** of this *Test Plan*: role isolation, complete Acceptance Criteria coverage, balanced path scenarios, and EARL alignment
- **Next steps**: you will receive a notification when generation is complete (typically 5–10 minutes), after which you can review and execute the *Test Cases* in the native Cloud ALM Test Management app (the next exercise covers this)

Joule also provides quick-access prompts; common options are **Check generation progress** and **Open test plan in Test Management**, which opens the *Test Plan* in the native Cloud ALM app for review. Follow up if you like, or continue to the next exercise.

<br><img src="images/ex3_06_generation_summary.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>32 – Generation summary and next steps</em></p>

---

## Summary

The Preparation Agent has completed its planning phase and started *Test Case* generation:
- [x] *Test Plan* reviewed and approved (HITL Gate 2)
- [x] *Test Case* generation triggered for several *Test Cases* across *User Stories* 3-157, 3-158, 3-159
- [ ] *Test Cases*: generation in progress; you will be notified when ready (see next exercise)

Continue to [Chapter 5 – Generate Test Cases](../ex4/README.md)
