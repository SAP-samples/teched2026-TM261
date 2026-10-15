# Exercise 3 – Plan Your Tests with AI

**Prerequisite:** You have completed [Exercise 2](../ex2/README.md); a confirmed test case scope exists for the BKJ process.

---

## What You'll Do

In this exercise you'll unleash the **Planning Agent**: an AI agent that takes your test case scope and builds a structured **test plan**: organized test case entries with descriptions, assigned roles, preconditions, and logical groupings. While it works, you'll compare it with the effort of doing this manually.

---

## Step 11 – Unleash the Planning Agent

### 11.1 – Confirm the Scope and Prompt for Planning

1. Make sure you're satisfied with the test case scope from Exercise 2. If you made refinements via Joule, confirm the scope is in its final state.

2. Open Joule and enter: **"The scope looks good. Please create a test plan."** or **"Confirm scope, go into planning."**

<!-- 📷 TODO: screenshot ex3_01_plan_prompt.png: Joule prompt to start planning agent, confirmation response -->
<br><img src="images/ex3_01_plan_prompt.png" />

3. The planning agent queues and starts. You'll see a running indicator.

<!-- 📷 TODO: screenshot ex3_02_planning_agent_running.png: Planning agent running in notification area or inline indicator -->
<br><img src="images/ex3_02_planning_agent_running.png" />

> ⏱️ **While the agent works: try it yourself:**
>
> Take one of the test cases from the scope and try to manually write a test plan entry:
>
> 1. Pick a test case (e.g. "Create Sales Order with Billing Plan")
> 2. Try to write: a clear description, the role performing it, the preconditions (what must be true before this step), and a rough sequence of test steps
> 3. How long does that take for one test case? Now multiply by the full scope...
>
> This is what test plan preparation normally looks like.

---

## Step 12 – What's Happening? (Narration)

> **The challenge:** Scope decisions rely on expertise that cannot scale; coverage becomes patchy and acceptance criteria unreliable. For each test case a test analyst would normally have to determine which app to use, define preconditions, sequence the steps at the right level of detail, assign the correct role, and link everything back to requirements. Multiply that by a full BKJ scope.
>
> **The solution:** The **Preparation Agent** maps execution paths from the process model into complete test cases. The expert shifts from producing to reviewing, and covers scope more reliably.
>
> Here is what the agent is doing right now, step by step:
>
> | Stage | What happens |
> |---|---|
> | **Validate incoming scope** | Checks quality and completeness of the scope context from the Scoping Agent. Flags issues before test generation begins. |
> | **Map all process variants** | Reads the BPMN diagram to identify every execution path: happy path, error flows, boundary conditions, auth checks, negative flows. |
> | **Draft test plan** | Creates a categorised plan covering all identified process variants; this is what you'll review and approve in Step 13. |
> | **HITL Gate 2: Approve plan** | ⛔ **No test cases are written to Cloud ALM without your explicit approval.** You review the plan and adjust before the agent continues. |
> | **Write test cases** | Creates test cases in Cloud ALM via ContentAssist. Progress is streamed live so you can watch it work. |
> | **Link cases and apply EARL** | Links each test case to its Requirement and Solution Process. Applies SAP standard content (EARL) where available. |
> | **Output** | Complete, traceable test cases written to Cloud ALM Test Management; ready for execution planning. |
>
> The gate in the middle (HITL Gate 2) is deliberate: the agent cannot proceed past the plan without human sign-off. You are always in control.

---

## Step 13 – Review the Agent's Test Plan

### 13.1 – Open the Completed Plan

1. Go to the **Notification Area** and open the planning agent's completion notification.

2. Review the generated test plan; you should see test cases organized with descriptions, roles, and preliminary step structure.

<!-- 📷 TODO: screenshot ex3_03_plan_notification.png: Notification of planning agent completion -->
<br><img src="images/ex3_03_plan_notification.png" />

<!-- 📷 TODO: screenshot ex3_04_plan_overview.png: Test plan overview showing all test cases with roles and structure -->
<br><img src="images/ex3_04_plan_overview.png" />

### 13.2 – Inspect a Test Case

1. Open a test case in detail; look at the groupings, preconditions, and step-level descriptions.

<!-- 📷 TODO: screenshot ex3_05_plan_detail.png: Single test case detail in test plan: role, preconditions, step groups -->
<br><img src="images/ex3_05_plan_detail.png" />

> **Traceability check:** Does the test case show its link back to the scope item and the user story? Good test plans maintain this chain; it's essential for coverage reporting and audit.

### 13.3 – Check Role Transitions

One of the most common planning mistakes is mixing multiple roles within a single test case. Look at the BKJ process; it involves 4 roles with 5 handover points.

> **Look for:** Are there test cases in the plan that should be split by role? For example, is the delivery step (Shipping Specialist) properly separated from the billing step (Billing Clerk)?

<!-- 📷 TODO: screenshot ex3_06_role_split.png: Test case showing a clean role boundary, or a case that needs splitting -->
<br><img src="images/ex3_06_role_split.png" />

---

## Step 14 – (Optional) Refine the Test Plan in Joule

Use Joule to make targeted adjustments to the plan without restarting from scratch.

**Try one of these:**

- **Split by role:** "Split test case 'Create and Release Billing Documents' into two; one for the Internal Sales Rep (billing block release) and one for the Billing Clerk (billing document creation)."
- **Add a precondition:** "Add a precondition to the delivery test case: down payment must be cleared before delivery creation can proceed."
- **Drop a step:** "Remove the stock setup step from the main test case; it's covered by a prerequisite setup script."

<!-- 📷 TODO: screenshot ex3_07_refine_plan.png: Joule conversation showing a plan refinement, updated test plan entry -->
<br><img src="images/ex3_07_refine_plan.png" />

---

## Summary

The planning agent structured your test case scope into a workable test plan; with roles, preconditions, and step groupings; in minutes.

You now have a **confirmed test plan** ready for test case generation.

Continue to [Exercise 4 – Generate Test Cases with AI](../ex4/README.md)
