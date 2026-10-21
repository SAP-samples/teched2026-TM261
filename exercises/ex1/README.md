<!-- Chapter 2 – Build Your Input, continued from exercises/ex0/README.md -->

## 2.3 – Generate Requirements from an Interview Transcript

**Prerequisite:** You have completed [Chapter 2 – steps 2.1 and 2.2](../ex0/README.md); the BJ5 process is set up with user stories.

---

## What You'll Do

In this step you'll use the SAP Cloud ALM Requirements app to generate a requirements document from an interview transcript. This is your first AI-assisted step; instead of drafting requirements manually, the AI reads an expert interview and structures it for you.

> **Why this matters:** Good requirements are the foundation for good test cases. Without them, the scoping and planning agents in later chapters won't have enough context to produce high-quality output. You'll see this contrast directly.

---

A requirements interview with a BJ5 process expert was recorded and transcribed for you. The transcript captures all the key business rules, process steps, and constraints discussed in the expert session.

### 2.3.1 – Open the Requirements App

Navigate to the **Requirements** app. There are two ways:

- **Search bar** (top center): type `require` and select **Requirements** from the results
- **Left toolbar**: click the quick-link icon that looks like a document being written on with a pen

<br><img src="images/ex1_01_requirements_nav.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>01 – Requirements app</em></p>

### 2.3.2 – Create a Requirement via Generate

1. The Requirements app opens with the filter pre-set to your project and scope; confirm both show your **workstation number** (`###_TestProject` / `###_CustomScope`). The list is empty: no requirements exist yet.

2. Click **Create**, then hover over **Requirement**: a sub-menu appears with two options:
   - **Manual**: write the requirement yourself
   - **Generate** ✨; let AI generate it from a source document

   Click **Generate**.

<br><img src="images/ex1_02_requirements_create.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>02 – Create → Generate menu</em></p>

### 2.3.3 – Configure the Generation Dialog

The **Generate Requirement with AI** dialog opens. Fill in the fields:

| Field | Value |
|---|---|
| **Title** | `###_BJ5_Requirement` (replace ### with your workstation number) |
| **Requirement Template** | (Not Assigned) |
| **Scope** | `###_CustomScope` |
| **Solution Process** | Beta_Straight Make-to-Stock Production – Discrete Manufacturing (BJ5_simple) |
| **Documents** | ← click the selection icon to open the document picker |

Click the **selection icon** next to the **Documents** field to choose the source document; the interview transcript your colleague posted.

<br><img src="images/ex1_03_generate_dialog.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>03 – Generate Requirement with AI dialog</em></p>

### 2.3.4 – Select the Interview Transcript

The **Assign Documents** dialog opens, showing the documents available in your project. You should see the interview transcript your colleague posted:

**`###_Interview Transcript_Make-to-Stock Production – Discrete Manufacturing (BJ5_simple)`**

Select it and click **Assign**.

<br><img src="images/ex1_04_transcript_select.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>04 – Selecting the interview transcript</em></p>

### 2.3.5 – Generate

Back in the **Generate Requirement with AI** dialog, the transcript now appears in the **Documents** field. Everything is set. Click **Generate**.

SAP Cloud ALM's built-in AI agent reads the full 30-minute conversation transcript and converts it into a structured requirements document; automatically. You'll be able to review the result in the next screen.

<br><img src="images/ex1_05_generate_action.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>05 – Triggering AI generation</em></p>

### 2.3.6 – Review and Save the Generated Requirement

The AI has created the new requirement. The detail view opens automatically.

A few things worth noting here:

- **Scroll up** to read the generated description; this is the structured requirements content extracted from your interview transcript.
- **Scroll down** to the **Solution Processes** section: the BJ5 process has been **automatically detected and linked**: no manual assignment needed. The AI recognised the context from the document.
- The info banner at the top reminds you that the description is editable while the status is *In Refinement*. Feel free to make adjustments if needed.
- At the bottom you can optionally fill in approver, priority, and other fields; skip this for now.

When satisfied, click **Save and Close**.

<br><img src="images/ex1_06_requirement_created.png" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>06 – Generated requirement: detail view</em></p>

---

## Summary

Chapter 2 complete. The process now has everything the AI agents need:
- [x] BPMN process diagram (from Signavio)
- [x] 7 user stories (assigned in Step 2.2)
- [x] Requirements document (generated in Step 2.3)

A 20-minute expert interview was converted into a structured requirements document, automatically linked to the BJ5 process. Time to head back to Joule and try what failed in Step 1.3; this time with proper input in place.

Continue to [Chapter 3 – Scoping Agent](../ex2/README.md)
