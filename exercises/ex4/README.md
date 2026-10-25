# Chapter 5 – Generate Test Cases

**Prerequisite:** You have completed [Chapter 4](../ex3/README.md); a confirmed *Test Plan* exists for the BJ5 process, and *Test Case* generation has been triggered and is running in the background.

---

## What You'll Do

In this chapter you'll follow the **Test Case Generation Agent** as it takes the approved *Test Case* skeletons and generates detailed, executable Test Steps. While it works, you can try drafting one *Test Case* manually, then compare your result with what Joule produces.

---

## 5.1 – Phase 2: Test Case Generation

The Preparation Agent is now in its second phase. Having cleared review (HITL) Gate 2 with your approved *Test Plan*, it is working through the following steps:

<br><img src="images/ex4_01_tc_agent_phase2.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>33 – Preparation Agent Phase 2: test case generation pipeline</em></p>

- **Write test cases**: For each planned *Test Case*, the agent creates a complete entry in SAP Cloud ALM via ContentAssist, including Test Steps, expected results, preconditions, and role assignments. Progress is streamed live as *Test Cases* are written.
- **Establish traceability**: Each *Test Case* is linked to the corresponding *Requirement* and *Solution Process*, establishing full traceability.
- **Enrich content**: Where available, the agent enriches the content with SAP standard test procedures from the Enterprise Architecture Reference Library (EARL).
- **Output**: Complete, traceable *Test Cases* written to Cloud ALM Test Management, ready for review and execution.

---

## 5.2 – Manual Test Case Work

⏱️ **While the agent works: try it yourself**

Pick one of the *Test Case* skeletons from Chapter 4's approved plan and try to write it manually before seeing what Joule produces. For the *Test Case* "Post Goods Receipt – Finished Goods" (US-06), fill in this template:

| Element | Your Draft |
|---|---|
| **Test Case Name** | |
| **Role** | Warehouse Clerk |
| **User Story** | BJ5_US-06: Post Goods Receipt – Finished Goods |
| **Precondition** | Production order confirmed; quality assessment passed (Quality OK = Yes, P1 path) |
| **App** | Goods Movements / Post Goods Receipt |
| **Step 1** | Open the Goods Receipt app and select the confirmed production order |
| **Step 1: Expected Result** | |
| **Step 2** | Verify the quantity matches the confirmed production output |
| **Step 2: Expected Result** | |
| **Step 3** | Select movement type and post the goods receipt |
| **Step 3: Expected Result** | |
| **Step 4** | Verify the stock update in the storage location |
| **Step 4: Expected Result** | |
| **Parameters needed** | Production order number, plant, storage location, finished goods material, quantity |

Keep your notes; you'll compare them with what Joule produced in Section 5.3.

---

## 5.3 – Review the Generated Test Cases

By now the *Test Cases* should be ready. Time to see what Joule produced.

**Finding the notifications**

While you were working on your manual *Test Case*, Joule was completing *Test Case* generation in the background. SAP Cloud ALM sends an in-app notification for each *Test Case* created. You will see a red bubble badge on the **notifications bell** in the top-right corner of the screen.

<br><img src="images/ex4_02_notifications_button.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>34 – Notification badge: test cases created</em></p>

Close the Joule panel first, then click the **notifications bell**. An overlay opens showing one entry per *Test Case*, with the *Test Case* name and an indication of when it was created.

<br><img src="images/ex4_03_notifications_overlay.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>35 – Notification overlay: one entry per generated test case</em></p>

**Opening and browsing a test case**

Click on any notification to open the *Test Case* in the SAP Cloud ALM Test Preparation interface. We suggest starting with the first (oldest) *Test Case* in the batch, which is usually the most encompassing end-to-end happy path flow. Click it and the *Test Case* opens in the native Cloud ALM *Test Case* app. Take a few minutes to browse, focusing on:

- **Header area**: indication of a Manual *Test Case*, linking to related artefacts, status "in preparation"
- **General information**: you can find the *Test Case* ID here; note it down, you will need it in a later step
- The **Content** tab: a **Purpose** section describing the business objective, the **Acceptance Criteria** linked from the *User Story*, and the full set of **test steps** with instructions and expected results
- The **General Information** tab: traceability links to the *Solution Process* and *Requirement*, and the source indicator: "Manual *Test Case* – created with AI assistance"
- The **Relations** tab: connection to the *Scope Item* and *Test Plan* entry
- The **References** tab: any EARL standard content applied

<br><img src="images/ex4_04_tc_detail.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>36 – Test case detail: Content tab with purpose, acceptance criteria, and test steps</em></p>

**Quality check**

▶️ **Your task:** Review the *Test Case* against these criteria:

| Quality Criterion | Check |
|---|---|
| Traceable to a *User Story* or *Requirement* | ☐ |
| Correct role assigned | ☐ |
| Logical grouping of steps | ☐ |
| Clear, actionable steps (not too vague, not too granular) | ☐ |
| Expected result for every step | ☐ |
| Input parameters identified | ☐ |

> **Compare with your manual draft from Step 5.2:** Did Joule's version match what you wrote? What did it do better? What would you change?

**What you have learned**

Joule produced several complete, structured *Test Cases*, each with a clear business purpose, traceability to Acceptance Criteria, and a full set of executable Test Steps with expected results; all in the time it took you to draft one manually.

Look closely at the Test Steps: they contain **parameter placeholders** for values the tester will need to enter. Fields like business partner, plant number, production order number, or material number have been identified but not yet filled with actual system values. In some cases, example values from linked artefacts or SAP standard content may appear as a starting point; these are not yet ready for Test Execution. Resolving these parameters is the job of the next agent in the pipeline: the **Test Data Management Agent**, covered in Chapter 6.

---

## Summary

The Preparation Agent's Phase 2 wrote detailed, executable *Test Cases* for the full BJ5 scope; complete with steps, expected results, and parameter placeholders.

- [x] *Test Cases* generated and reviewed
- [x] Quality criteria checked: role assignment, step clarity, traceability, expected results
- [ ] Test data values: parameter placeholders identified; to be verified and resolved in Chapter 6

Continue to [Chapter 6 – Generate Test Data](../ex5/README.md)
