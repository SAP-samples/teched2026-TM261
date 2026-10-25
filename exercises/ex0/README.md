← Back to [Introduction](../ex_intro/README.md)

# Chapter 1 – Getting Started

---

## Your Story Today

You are a **Test Business Process Expert** at a company rolling out SAP S/4HANA. As part of that rollout, your team activated SAP S/4HANA *Scope Item* BJ5: Make-to-Stock Production – Discrete Manufacturing, and adapted it to fit your specific operational needs; creating a custom process variant called **BJ5_simple**. Your task today: **prepare test coverage for this process, with a focus on validating the role assignments and workflow changes** that came with the customisation. You're starting from scratch.

In this hands-on you'll work with AI agents in SAP Cloud ALM Test Management to speed up every stage, from *Requirements* to test data, dramatically reducing the manual effort that would normally take days.

---

## 1.1 – Log In to SAP Cloud ALM

It's the start of your work day, and preparing test coverage for the newly customised process is on your agenda. SAP Cloud ALM Test Management is where this work happens: the platform where you plan, execute, and track test projects end to end, with every test artifact traceable back to *Requirements*, providing documented assurance of what has been validated and why.

Open your browser and navigate to the Cloud ALM tenant.

> **Your credentials:**
>
> | Field | Value |
> |---|---|
> | **Tenant** | [SAP Cloud ALM (TM261)](https://tm261-000-l2fw0ndj.eu10-004.alm.cloud.sap/launchpad) |
> | **User** | `tm261-###@education.cloud.sap` |
> | **Password** | `Acce$$teched26` |
>
> Replace **###** with your workstation number, zero-padded to three digits: desk 3 → `003`, desk 18 → `018`, desk 42 → `042`. Your number is on the tent card on your desk.
>
> Whenever you see `###` in a field value, filename, or prompt in this guide, that's your cue to substitute your own number. Screenshots in this guide use `099` as the example; wherever you see `099`, read it as your own number.

**1.** Enter your username and password, then click **Log On**.

<br><img src="images/ex0_01_login.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>03 – Login to SAP Cloud ALM</em></p>

---

## 1.2 – Open Joule

After logging in you land on the SAP Cloud ALM home page. We'll explore more of the platform in a moment, but first: let's call your most valuable tool for today: **Joule**.

Joule is a chat-style AI interface built into SAP Cloud ALM. You'll use it throughout this session to interact with AI agents, ask questions, and drive the Test Preparation workflow; all in natural language.

**1.** Look for the **diamond icon** in the upper-right area of the screen and click it to open Joule.

<br><img src="images/ex0_02_home.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>04 – SAP Cloud ALM home page</em></p>

**2.** Joule opens as a panel that slides over the application screen; it's always available, regardless of where you are in SAP Cloud ALM.

The panel header gives you three controls:
- **Expand icon**: open Joule in full-screen mode
- **Close (×)**: close the panel
- **Sidebar icon**: manage multiple concurrent conversations (you can run several Joule chats in parallel, one per topic or agent)

> **Good to know:** Joule is stateful. Close the panel, navigate elsewhere, reopen it; your conversation is still there where you left it.
> The sidebar shows your conversation list: up to **10 conversations can be active** at the same time, with older ones moved to **Expired**.

<br><img src="images/ex0_03_joule_panel.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>05 – Joule panel open</em></p>

**3.** Wake up Joule with a simple message in the input box at the bottom; just type naturally, for example: **"Joule on :)"** or any greeting.

Joule will start processing; this can take a moment, feel free to read ahead while waiting. When it responds, you'll see an introduction of its capabilities covering areas like **Test Data Management**, **Test Scoping**, **Test Planning**, and **ALM Project Setup**. These are exactly the capabilities you'll use today.

<br><img src="images/ex0_04_joule_hello.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>06 – Joule greeting and capabilities</em></p>

> ⚠ **Before you continue: a word on stability.** The agentic capabilities you're about to use involve complex multi-step orchestration across multiple AI skills and agent calls. This session runs on a shared productive tenant, designed for normal corporate use, not for dozens of simultaneous participants. Expect some variability in response times.
>
> If Joule appears frozen, read ahead and give it a moment. If it seems to have timed out or lost context entirely, send a gentle follow-up ("still there?" or "hi") to wake it up, or re-send the original prompt. This is a known behaviour in the agentic framework; don't be surprised if it happens.

---

## 1.3 – Jump Ahead: What Happens Without Preparation? *(Optional)*

> **Optional step**: try this if you want to see what happens when you skip straight to *Test Case* generation without proper setup.

In the initial view you'll notice the process has a BPMN flow diagram, but nothing else linked to it. Let's see what Joule does when asked to work with that incomplete input.

In the Joule message window, prompt it to generate *Test Cases* directly; specifying the process and project:

> *"I need to test process "Beta_Straight Make-to-Stock Production – Discrete Manufacturing (BJ5_simple)" in project "###_TestProject""*
>
> Replace **###** with your workstation number.

> **Tip:** Click the **expand icon** (⤢) in the Joule panel header to open Joule in full-screen mode; much easier to read the agent outputs, especially the longer ones coming later in this session.

Joule navigates to the process in your project and analyses its content, but it hits a problem:

> **⚠️ Blocker: No Requirement or User Story Assigned**
>
> Joule found the process and confirmed the BPMN diagram is available, but it immediately flags a blocker: **no Requirement or User Story is linked to the process**. The agents require at least a *Requirements* description before *Test Cases* can be generated; the more background they have, the better the output quality.
>
> **Garbage in, garbage out** is true for AI agents too. The quality of the output depends directly on the quality of the input. Before Joule can do useful work, we need to enrich the process with *Requirements* and *User Stories*. That's exactly what we'll do next.

---

# Chapter 2 – Feed the Agents

Before the AI agents can do useful work, the process needs to be populated with the documentation they'll work from. A BPMN diagram is already there, as you'll see; but a *Requirements* document and linked *User Stories* add the business context and process intent that language models are best at processing.

In this chapter you'll navigate to your project, assign pre-prepared *User Stories*, and generate a *Requirements* document from an expert interview transcript.

---

## 2.1 – Navigate to Your Project

Time to find your process. Give Joule a break first; close the panel (click **×** in the panel header), then navigate to the project.

**1.** Back on the Cloud ALM home screen, click the **Implementation** tab in the top navigation bar. This is the launchpad for all Test Management related apps and more: *Requirements*, process authoring, Test Preparation, *Test Plans*, Test Execution, *Defects*.

<br><img src="images/ex0_06_implementation.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>07 – Implementation tab</em></p>

**2.** In the **Preparation and Setup** section, click the **Projects and Setup** tile to reach the overview of all projects in Cloud ALM.

<br><img src="images/ex0_07_projects_setup.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>08 – Projects and Setup tile</em></p>

**3.** In the **Manage Projects** list, locate your project: **`###_TestProject`** (replace ### with your workstation number, e.g. `033`). Click it to open the project details.

**4.** In the project detail view, click the **Scopes** tab. This section can hold multiple scopes; here you'll find exactly one: **`###_CustomScope`**, the container for all the BJ5_simple process content you'll work with today. Click on it.

<br><img src="images/ex0_08_project_list.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>09 – Project list and scope</em></p>

**5.** The view switches to **Open Solution Processes**, with filters pre-set to your project and scope. In a real-life implementation this list could contain dozens of processes; today you have exactly one: **`Beta_Straight Make-to-Stock Production – Discrete Manufacturing (BJ5_simple)`**. Click on it to open its details.

<br><img src="images/ex0_09_process_list.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>10 – BJ5 process in the custom scope</em></p>

**6.** The process detail view opens. A process record in Cloud ALM can hold a lot of information; for now, not much has been added here.

**7.** Click the **Solution Process Flow** tab (next to Solution Value Flow). Here you'll find something promising: a BPMN process diagram showing the BJ5 flow across two swimlanes; Production Planner and Warehouse Clerk. This diagram was imported from a process modelling tool such as **SAP Signavio** and is stored natively in Cloud ALM (a direct live integration with Signavio is planned as a future capability).

> **But here's the catch:** the diagram alone is not sufficient for the AI agents to generate high-quality test output. It provides the process skeleton, but without *Requirements* and *User Stories* the agents can't derive meaningful test coverage from structure alone.

<br><img src="images/ex0_11_process_flow.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>11 – BJ5 process flow diagram</em></p>

**8.** Return to the **Solution Value Flow** tab. On the right-hand panel, click **+8** to expand the full list of content types that can be linked to this process. All counters are at zero: no *Requirements*, no *User Stories*, no *Test Cases*.

<br><img src="images/ex0_10_process_detail.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>12 – Process detail: all content at zero</em></p>

> **This is the root cause** of Joule's rejection in Step 1.3. Without *Requirements* or *User Stories*, the agents have no process intent to work from; and by design, they won't make things up. Before we can generate anything meaningful, we need to populate this process, and that's exactly what the next steps will do.

---

## 2.2 – Assign User Stories

*User Stories* for the BJ5_simple process have already been defined and created in the system; they just haven't been linked to this process yet. Let's do that now.

**1.** Make sure you are on the **Solution Value Flow** tab. On the right-hand panel, click the **+8** dropdown and select **User Stories** to bring that section into view.

<br><img src="images/ex0_12_user_stories_nav.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>13 – Opening User Stories section</em></p>

**2.** The **User Stories** section appears in the right panel, currently empty ("No *User Story* assigned"). Click the **Assign** button to open the selection dialog.

<br><img src="images/ex0_13_user_stories_assign.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>14 – Assign User Stories dialog</em></p>

**3.** The **Assign User Stories** dialog opens, pre-populated with *User Stories* prepared for this process. Find the 7 entries prefixed **BJ5_US-**, select all of them, then click **Assign**.

<br><img src="images/ex0_14_user_stories_select.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>15 – Selecting all 7 BJ5 user stories</em></p>

**4.** Back in the process, open one of the *User Stories* to inspect it. Each story follows the same structure: **story points**, a **user story** narrative ("As a [role], I want to... so that..."), and granular **acceptance criteria**: exactly the kind of structured input the AI agents need.

<br><img src="images/ex0_15_user_story_detail.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>16 – User story: narrative and acceptance criteria</em></p>

When done, click the **back arrow** (←) at the top left to return to the process view.

**5.** Back in the process, open the **+8** dropdown again; **User Stories** now shows **(7)**. The assignment worked.

But look at **Requirements (0)**: still empty, and arguably the most important input for the agents. A well-formed *Requirements* document gives the agents the building blocks of the process: business rules, role responsibilities, preconditions, expected outcomes, and the constraints that separate a happy path from an error scenario. This is the context that lets them generate meaningful, traceable test coverage rather than generic steps.

Here's the good news: you were recently in a structured interview with a BJ5 process expert, walking through the process step by step. Your colleague promised to post the transcript in SAP Cloud ALM. Time to retrieve it and turn it into a *Requirements* document.

<br><img src="images/ex0_16_requirements_needed.png" style="border:1px solid #ddd;border-radius:4px;" />
<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>17 – Requirements count still zero</em></p>

---

## Summary

Chapters 1 and 2 (so far):
- [x] Logged in and opened Joule
- [x] BJ5_simple process located in `###_TestProject / ###_CustomScope`
- [x] 7 *User Stories* assigned to the process
- [ ] *Requirements* document: still missing; covered in step 2.3

Continue to [Chapter 2 – Feed the Agents (continued)](../ex1/README.md)
