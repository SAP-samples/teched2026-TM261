# Exercise 4 – Generate Test Cases with AI

**Prerequisite:** You have completed [Exercise 3](../ex3/README.md); a confirmed test plan exists for the BKJ process.

---

## What You'll Do

In this exercise you'll unleash the **Test Case Generation Agent**: an AI agent that takes the test plan and writes detailed, executable test cases. While it works, you'll draft one test case yourself, then compare results. After that you'll dive into one of the most overlooked aspects of test case quality: **test data and parameters**.

---

## Step 15 – Unleash the TC Generation Agent

### 15.1 – Confirm the Plan and Prompt for Generation

1. Make sure your test plan from Exercise 3 is in its final state.

2. Open Joule and enter: **"The plan looks good. Please generate the test cases."** or **"Confirm plan, start test creation."**

<!-- 📷 TODO: screenshot ex4_01_generate_prompt.png: Joule prompt to start TC generation agent, acknowledgement -->
<br><img src="images/ex4_01_generate_prompt.png" />

3. The generation agent starts. This is the most comprehensive agent; it writes detailed steps, expected results, and parameter placeholders for every test case in the plan.

<!-- 📷 TODO: screenshot ex4_02_generation_running.png: TC generation agent running indicator -->
<br><img src="images/ex4_02_generation_running.png" />

> ⏱️ **While the agent works: try it yourself:**
>
> Pick one test case from your plan (e.g. "Post Incoming Payment and Clear Down Payment") and try to write it manually:
>
> 1. Break it into functional units: what app? what action?
> 2. Assign the correct role: AR Accountant
> 3. Write the test steps at the right level of detail (not too high, not too granular)
> 4. For each step, write the expected result
>
> **In particular:** note down any input parameters (company code, posting date, customer account, amount, house bank). Draw arrows to show dependencies; which parameter values are determined by earlier steps?
>
> Keep your notes for Step 18.

---

## Step 16 – Manual Test Case Work

While the agent runs, try a more structured breakdown:

For your chosen test case, fill in this template:

| Element | Your Draft |
|---|---|
| **Test Case Name** | |
| **Role** | AR Accountant |
| **Precondition** | |
| **App** | Post Incoming Payments (F1345) |
| **Step 1** | Open the app, select company code |
| **Step 1: Expected Result** | |
| **Step 2** | Enter posting date and journal entry type DZ |
| **Step 2: Expected Result** | |
| **Step 3** | Filter for Special G/L transactions, find FAZ open item |
| **Step 3: Expected Result** | |
| **Step 4** | Select FAZ item, choose Clear, Post |
| **Step 4: Expected Result** | |
| **Parameters needed** | Company code, posting date, G/L account, house bank, customer, amount |

---

## Step 17 – Review the Generated Test Case

The agent has finished. Let's see what it produced.

### 17.1 – Open the First Test Case

1. Go to the **Notification Area** and open the TC generation agent's completion notification.

<!-- 📷 TODO: screenshot ex4_03_tc_notification.png: Notification of TC generation agent completion -->
<br><img src="images/ex4_03_tc_notification.png" />

2. Navigate to the first generated test case and open it in detail.

<!-- 📷 TODO: screenshot ex4_04_tc_overview.png: Generated test case list overview -->
<br><img src="images/ex4_04_tc_overview.png" />

<!-- 📷 TODO: screenshot ex4_05_tc_detail.png: Single test case detail: steps, expected results, parameters, traceability -->
<br><img src="images/ex4_05_tc_detail.png" />

### 17.2 – Quality Check

Review the generated test case against these criteria:

| Quality Criterion | Check |
|---|---|
| Correct role assigned | ☐ |
| Clear, actionable steps (not too vague, not too granular) | ☐ |
| Expected result for every step | ☐ |
| Input parameters identified | ☐ |
| Traceable to a user story or requirement | ☐ |
| Logical grouping of steps | ☐ |

> **Compare with your manual draft:** Did the agent's version match what you wrote? What did it do better? What would you change?

---

## Step 18 – Understand Test Data Parameters

This is where test preparation often gets underestimated. Let's go deeper.

### 18.1 – Identify the Parameters

Open the test case you've been looking at (the payment posting case, or any other complex one) and focus on the **input parameters**: the specific values that must be entered to execute each step.

1. For each step in the test case, note down all parameter fields (not the values yet, just the parameter names).

<!-- 📷 TODO: screenshot ex4_06_parameters.png: Test case with parameter fields highlighted / annotated -->
<br><img src="images/ex4_06_parameters.png" />

2. Now think about **dependencies** between parameters. For the BKJ process:

   - The **Sales Organization** (e.g. 1010) determines which **Distribution Channel** and **Division** are available
   - The **Sold-to Party** (customer) determines the **Ship-to Party** and **Payer**
   - The **Plant** (e.g. 1010) determines which **Storage Location** is available
   - The **Material** type determines which **Item Category** is auto-assigned (CBAO, CTAD, or CTAX)

   Draw or describe these dependency relationships; which parameter determines which others?

<!-- 📷 TODO: screenshot ex4_07_dependencies.png: Whiteboard or annotation showing parameter dependency relationships -->
<br><img src="images/ex4_07_dependencies.png" />

> **This dependency map is what the Data Agent will use in Exercise 5**: it's not just about picking values, it's about picking consistent combinations.

### 18.2 – Note the Test Case ID

1. Note down the **test case ID** of the case you've been reviewing. You'll use it to prompt the data agent in Exercise 5.

<!-- 📷 TODO: screenshot ex4_08_tc_id.png: Test case ID highlighted in the test case header -->
<br><img src="images/ex4_08_tc_id.png" />

---

## Summary

The TC generation agent wrote detailed, executable test cases for the full BKJ scope; complete with steps, expected results, and parameter placeholders.

You now understand:
- What a high-quality AI-generated test case looks like
- How to evaluate it for correctness, completeness, and traceability
- That **test data and parameters** are a critical dimension that needs its own attention

Continue to [Exercise 5 – Generate Test Data with AI](../ex5/README.md)
