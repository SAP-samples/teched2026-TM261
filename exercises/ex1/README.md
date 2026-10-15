# Exercise 1 – Generate Requirements with AI

**Prerequisite:** You have completed [Getting Started](../ex0/README.md); the BKJ process is set up with user stories and solution documentation.

---

## What You'll Do

In this exercise you'll use the SAP Cloud ALM **Requirements** app to generate a requirements document from an interview transcript. This is your first AI-assisted step; instead of drafting requirements manually, the AI reads an expert interview and structures it for you.

> **Why this matters:** Good requirements are the foundation for good test cases. Without them, the scoping and planning agents in later exercises won't have enough context to produce high-quality output. You'll see this contrast directly.

---

## Step 5 – Generate Requirements from an Interview Transcript

A requirements interview with a BKJ process expert was recorded and transcribed for you. The transcript captures all the key business rules, process steps, and constraints discussed in the expert session.

### 5.1 – Open the Requirements App

Navigate to the **Requirements** app. There are two ways:

- **Search bar** (top center): type `require` and select **Requirements** from the results
- **Left toolbar**: click the quick-link icon that looks like a document being written on with a pen

<br><img src="images/ex1_01_requirements_nav.png" />

### 5.2 – Create a Requirement via Generate

1. The Requirements app opens with the filter pre-set to your project and scope; confirm both show your **workstation number** (`XXX_TestProject` / `XXX_CustomScope`). The list is empty: no requirements exist yet.

2. Click **Create**, then hover over **Requirement**: a sub-menu appears with two options:
   - **Manual**: write the requirement yourself
   - **Generate** ✨; let AI generate it from a source document

   Click **Generate**.

<br><img src="images/ex1_02_requirements_create.png" />

### 5.3 – Configure the Generation Dialog

The **Generate Requirement with AI** dialog opens. Fill in the fields:

| Field | Value |
|---|---|
| **Title** | `XXX_BKJ_Requirement` (replace XXX with your workstation number) |
| **Requirement Template** | (Not Assigned) |
| **Scope** | `XXX_CustomScope` |
| **Solution Process** | Custom Sales Order Processing with Customer Down Payment (BKJ) |
| **Documents** | ← click the selection icon to open the document picker |

Click the **selection icon** (📋) next to the **Documents** field to choose the source document; the interview transcript your colleague posted.

<br><img src="images/ex1_03_generate_dialog.png" />

### 5.4 – Select the Interview Transcript

The **Assign Documents** dialog opens, showing the documents available in your project. You should see the interview transcript your colleague posted:

**`XXX_Interview Transcript_Sales Order Processing with Customer Down Payment (BKJ)`**

Select it and click **Assign**.

<br><img src="images/ex1_04_transcript_select.png" />

### 5.5 – Generate

Back in the **Generate Requirement with AI** dialog, the transcript now appears in the **Documents** field. Everything is set. Click **Generate**.

SAP Cloud ALM's built-in AI agent reads the full 30-minute conversation transcript and converts it into a structured requirements document; automatically. You'll be able to review the result in the next screen.

<br><img src="images/ex1_05_generate_action.png" />

### 5.6 – Review and Save the Generated Requirement

The AI has created the new requirement. The detail view opens automatically.

A few things worth noting here:

- **Scroll up** to read the generated description; this is the structured requirements content extracted from your interview transcript.
- **Scroll down** to the **Solution Processes** section: the BKJ process has been **automatically detected and linked**: no manual assignment needed. The AI recognised the context from the document.
- The info banner at the top reminds you that the description is editable while the status is *In Refinement*. Feel free to make adjustments if needed.
- At the bottom you can optionally fill in approver, priority, and other fields; skip this for now.

When satisfied, click **Save and Close**.

<br><img src="images/ex1_06_requirement_created.png" />

---

## Summary

Step 5 complete; AI-supported requirements generation done. A 30-minute expert interview was converted into a structured requirements document, automatically linked to the BKJ process.

The process now has everything the AI agents need:
- ✅ BPMN process diagram (from Signavio)
- ✅ 9 user stories (assigned in Getting Started)
- ✅ Requirements document (generated in this exercise)

Time to head back to the process and try what failed in Step 3; this time with proper input in place.

Continue to [Exercise 2 – Scope Your Tests with AI](../ex2/README.md)
