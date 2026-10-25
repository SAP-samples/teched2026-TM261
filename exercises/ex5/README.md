# Chapter 6 – Generate Test Data

Good test data may be one of the most underestimated parts of Test Preparation. A single wrong value (an invalid material, the wrong plant, a date outside the planning horizon) is enough to make a test fail for the wrong reasons, wasting time and masking real *Defects*. It is also a recurring burden: even for established *Test Cases*, data values get consumed during Test Execution (orders confirmed, stock moved, documents created) and must be refreshed before the next run. Yet gathering valid, consistent test data for a business process like BJ5 traditionally demands expert knowledge of both the process and the system configuration.

**Prerequisite:** You have completed [Chapter 5](../ex4/README.md); *Test Cases* have been generated for the BJ5 process and are visible in Test Preparation.

---

## What You'll Do

In this chapter you'll work with the **Test Data Management Agent**. In its current Phase 1 form, the agent reads a *Test Case* and extracts every parameter placeholder: the fields where a tester will need to provide a specific value to execute the step. It classifies them by data category; for parameters that are constant across the project (such as company code, plant, and client), it applies the known project-level values automatically so the tester does not need to look them up.

The current Phase 1 capability is the foundation for a progressively richer roadmap. Future phases will connect the agent to a live S/4HANA system: first to suggest values that actually exist in the test environment, then to propose new master data records where the right values do not yet exist, modelled on patterns from a productive system. The final step will extend to writing data directly into target systems; not only master data but also transient data: the prerequisite document chains (inquiry, offer, order, delivery) needed for *Test Cases* that begin mid-flow in a business process.

For now, Phase 1 turns unstructured Test Step text into a structured, actionable parameter checklist.

---

## 6.1 – Understanding the Agent

The diagram below shows the full pipeline of the Test Data Management Agent in Phase 1:

<br><img src="images/ex5_01_tdm_agent_flow.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>37 – Test Data Management Agent: Phase 1 pipeline</em></p>

> **What the Test Data Management Agent works through:**
> 1. **Fetch the **Test Case**:** reads the *Test Case* and all its activity steps from SAP Cloud ALM; if the *Test Case* is not found or has no activities, the agent stops and asks you to verify the input
> 2. **Extract parameters:** reads every Test Step and identifies each place where a specific value is needed; each parameter is named, typed, and described
> 3. **Classify:** groups each parameter into one of four categories: Organisational data, Master data, Configuration data, or Transactional data
> 4. **Apply project context:** fills in known fixed values from the project configuration (company code, plant, client), reducing manual lookup for values shared across all *Test Cases*
> 5. **Output:** a structured parameter table per category, with descriptions, example values where available, and dependency reasoning

> **Phase 1 scope note:** The agent identifies and classifies parameters; it does not yet look up or suggest actual system values. The tester uses the output as a structured checklist.

---

## 6.2 – Identify the Parameters in Your Test Case

⏱️ **While the agent works: try it yourself**

Open one of your generated *Test Cases* in Test Preparation, go to the **Content** tab, and read through the Test Steps. For each step, note every parameter: every place where the tester will need to enter a specific value.

Look for patterns like these:

- **Material**: `<replacement material number>`; must exist in the system
- **Plant**: `<plant>`; the plant where the production operation takes place
- **Order Type**: PP01; a configuration value, already fixed here
- **Total Qty**: `<required quantity>`; must be valid for the material and order, and the quantity must be available in a storage location so the picking steps can be executed
- **Basic Finish Date**: `<planned finish date>`; must fall within the planning horizon

For a make-to-stock production and warehousing process like BJ5, you'll typically also encounter:

- **Sales Area**: a combination of Sales Org, Distribution Channel, and Division, tied to a specific company code; all fixed from the project configuration
- **Work center**: must exist in the plant and be assigned to the correct cost center
- **Storage location**: must be valid for the plant and movement type
- **Production order number**: a transactional reference that only exists after the order is created
- **Confirmed quantity**: depends on the output of a prior step

Note the distinction: some values are fixed (company code, plant), some are looked up once before the test (material, work center), and some are only generated at runtime (production order number). This is exactly the classification the agent applies.

<br><img src="images/ex5_02_tc_parameters.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>38 – *Test Case* parameters: placeholder values in the instruction text</em></p>

---

## 6.3 – Trigger the Data Agent

Unlike the Preparation Agent covered in previous chapters, the Test Data Management Agent does not start automatically after *Test Case* generation. This is intentional: test data is a separate output, used alongside Test Steps rather than embedded in them. A *Test Case* describes *what* to do; test data provides *with what* to do it. These two artefacts have different lifecycles in SAP Cloud ALM; data will typically be resolved when the *Test Case* is in an advanced status or already assigned to a tester. The decision of when to enrich a *Test Case* with data is often made by the person preparing for execution: initially a key user, and later the tester directly.

There is also a practical reason to start fresh: generated *Test Cases* need to be processed and indexed by Cloud ALM before the agent can read them; starting a new Joule conversation ensures a clean context.

If you noted down the *Test Case* ID in Chapter 5, you are ready to proceed. If not, **retrieve the test case ID** first:
- Switch to the **General Information** tab of the *Test Case* you reviewed in Step 6.2.
- Scroll to the **Object** section at the bottom. Note down the **ID** shown there; it follows the format `8-1-123`.

**Triggering the agent**

**1.** Open a **new Joule conversation** (click the new conversation icon or close and reopen the Joule panel).

**2.** Send this prompt, replacing `###` with your workstation number and inserting the *Test Case* ID noted above:

> *"Please suggest test data for test case [your test case ID] in project "###_TestProject""*

<br><img src="images/ex5_03_tdm_trigger.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>39 – New Joule conversation: triggering the Test Data Management Agent</em></p>

The agent starts working: it fetches the *Test Case*, reads all activity steps, extracts and classifies every parameter, and applies the project context.

---

## 6.4 – Review the Agent's Output

When the agent returns, it presents a structured table of all data parameters identified in the *Test Case*, grouped into four categories.

**Organisational data**
The fixed organisational frame: sales organisation, distribution channel, division, and dependent org units such as plant and storage location. These values are typically re-usable across *Test Cases* in a project, and the agent applies them automatically from the project context wherever possible.

**Master data**
Objects that must exist in the system before the test can run: materials valid for the sales area and plant, business partners in the correct role (for example: sold-to party, ship-to, payer), and any dependencies between them. A sold-to party determines which ship-to and payer are valid; a material type determines which item category is auto-assigned.

**Configuration data**
System settings that affect process behaviour: pricing procedures, document types, workflow configurations, authorisation roles. These rarely change between test runs but must be verified to exist and be correctly set up before testing.

**Transactional data**
Values that are either chosen by the tester at runtime or generated on the fly during execution: quantities, dates, and document numbers (order numbers, delivery numbers, production order IDs) that only exist after a preceding step has been completed.

**Why dependencies matter**

The agent does not just list parameters; it explains which values drive which others. This is more valuable than it first appears. Consider a quantity of "10" entered in a production order step: taken in isolation it looks arbitrary. Trace it forward through the process and that same quantity must arrive at a picking step where the storage location needs to hold sufficient stock. If it does not, the test will fail for the wrong reasons: not a *Defect*, but a data setup problem. Understanding these dependencies upfront is the prerequisite for future agent phases to run automated checks and resolve such blocking conditions before a test is even started.

<br><img src="images/ex5_04_tdm_output.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>40 – Test Data Management Agent output: parameters grouped by category with example values and reasoning</em></p>

▶️ **Your task:** Compare the agent's parameter table against your manual notes from Step 6.2:

| Quality check | What to look for |
|---|---|
| **Completeness** | Are all parameter placeholders from the Test Steps in the table? Are there steps where a value is clearly needed but not captured? |
| **Classification** | Are categories assigned correctly? Company code = Org Data; material = Master Data; production order number = Transactional Data |
| **Project context** | Are fixed values like plant and company code already populated from the project record? |
| **Reasoning** | Does the agent trace each parameter back to the Test Step it came from and explain why it is needed? |
| **Dependencies** | Does the output indicate which parameters drive or constrain others? Use the follow-up prompt below if not. |

> **Compare with your manual notes from Step 6.2:** Did the agent capture everything you identified? Did it find parameters you missed?

At the end of its response, the agent offers suggestions for next steps; one of the most useful is an analysis of the dependencies between the parameter groups. Try sending one of the offered follow-up prompts, or write your own:

> *"Outline the dependencies between the parameters you identified."*

The agent should map which values must be consistent with which others; useful both for manual data lookup and as a foundation for future automated data preparation.

---

## Summary

The Test Data Management Agent turned unstructured Test Step text into a structured parameter checklist; classifying every placeholder by data category and applying fixed project values automatically.

- [x] *Test Case* parameters extracted and classified by the agent
- [x] Parameter dependencies and categories understood
- [ ] Actual system values: to be looked up by the tester using the agent's output as a checklist

You have now completed the full AI-assisted Test Preparation cycle:
- [x] *Requirements* generated from interview transcript (Chapter 2)
- [x] Test scope proposed by Scoping Agent (Chapter 3)
- [x] *Test Plan* structured by Preparation Agent: Phase 1 (Chapter 4)
- [x] *Test Cases* written by Preparation Agent: Phase 2 (Chapter 5)
- [x] *Test Case* parameters identified and classified (Chapter 6)

**Time saved**

To put the session in perspective: the table below shows rough estimates of the manual effort each stage would typically take a skilled practitioner. The AI agents deliver the first draft in minutes; human review adds time, but the net result is already a substantial reduction, and it will grow as the agents become more capable.

| Stage | Manual effort (estimate) | AI-assisted |
|---|---|---|
| *Requirements* from transcript | 2–4 hours (BA) | ~2 minutes + review |
| *Test Case* scoping | 4–8 hours (architect) | ~3 minutes + review |
| *Test Plan* creation | 2–4 hours (test analyst) | ~3 minutes + review |
| *Test Case* writing | 1–2 days (test analyst) | ~5 minutes + review |
| Test data parameters | 2–4 hours (analyst) | ~2 minutes + review |
| **Total** | **3–5 days** | **< 30 minutes** |

Continue to [Chapter 7 – Recap & Outlook](../ex6/README.md)
