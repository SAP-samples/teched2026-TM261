# Getting Started – Log In & Orient Yourself

**Session:** TM261 – Agent-Led Test Management: Hands-on Lab with Joule in SAP Cloud ALM  
**Date:** Thursday, 29 October 2026 · SAP TechEd 2026, Berlin  
**Presenters:** Christina Pickhardt · Niclas Weidner · Tobias Keller  
**Scenario:** Sales Order Processing with Customer Down Payment (BKJ)

---

## Your Story Today

You are a **Test Business Process Expert** at a company that just activated SAP S/4HANA Scope Item BKJ: Sales Order Processing with Customer Down Payment. Your task: **prepare test coverage for the new process** from scratch.

In this hands-on you'll work with AI agents in SAP Cloud ALM Test Management to speed up every stage, from requirements to test data, dramatically reducing the manual effort that would normally take days.

---

## Step 1 – Log In to SAP Cloud ALM

You are a business and process expert at a large multinational corporation. It's the start of your work day, and you have an important task on your agenda: preparing test coverage for a newly activated SAP process.

Open your browser. The SAP Cloud ALM login page is already loaded.

> **Your credentials:**
>
> | Field | Value |
> |---|---|
> | User | `tm261-XXX@education.cloud.sap` |
> | Password | `Acce$$teched26` |
>
> Replace **XXX** with your **workstation number** (shown on your desk). This number is yours for the entire session; it identifies your personal data and work in the shared system.

1. Confirm the tenant name on the left reads **SAP Cloud ALM (TM261_000)**: this is the shared demo system for this session.

2. Enter your username and password, then click **Log On**.

<br><img src="images/ex0_01_login.png" />

---

## Step 2 – Open Joule

After logging in you land on the SAP Cloud ALM home page. Time to call your most valuable tool: **Joule**.

Joule is a chat-style AI interface built into SAP Cloud ALM. You'll use it throughout this session to interact with AI agents, ask questions, and drive the test preparation workflow; all in natural language.

1. Look for the **diamond icon** (◇) in the upper-right area of the screen and click it to open Joule.

<br><img src="images/ex0_02_home.png" />

2. Joule opens as a panel that slides over the application screen; it's always available, regardless of where you are in SAP Cloud ALM.

   The panel header gives you three controls:
   - **Sidebar icon**: manage multiple concurrent conversations (you can run several Joule chats in parallel, e.g. one per topic or agent)
   - **Expand icon**: open Joule in full-screen mode
   - **Close (×)**: close the panel

   > **Good to know:** Joule is stateful. Close the panel, navigate elsewhere, reopen it; your conversation is still there exactly as you left it.

<br><img src="images/ex0_03_joule_panel.png" />

3. Wake up Joule with a simple message in the input box at the bottom; just type naturally, for example: **"Joule on :)"** or any greeting.

   Joule responds with an introduction of its capabilities. Scroll through its response; you'll see areas like **Test Data Management**, **Test Scoping**, **Test Planning**, and **ALM Project Setup**. These are exactly the capabilities you'll use today.

<br><img src="images/ex0_04_joule_hello.png" />

---

## Step 3 – Jump In Early *(Optional)*

> **Optional step**: try this if you want to see what happens when you skip straight to test case generation without proper setup.

Let's see what Joule does when asked to work with incomplete input.

1. In Joule, prompt it to generate test cases directly; specifying the process and project:

   > *"I want to test and need test cases for: Process "Custom Sales Order Processing with Customer Down Payment (BKJ)", Project "XXX_TestProject""*
   >
   > Replace **XXX** with your workstation number.

   Joule navigates to the process in your project and analyses its content, but it hits a problem.

   > **Tip:** Click the **expand icon** (⤢) in the Joule panel header to open Joule in full-screen mode: much easier to read Joule's responses, especially for longer agent outputs. The left sidebar shows your conversation list: up to **10 concurrent conversations** can be active at the same time, with older ones moved to **Expired**.

<br><img src="images/ex0_05_joule_jump_in.png" />

> **⚠️ Cannot Proceed with Test Case Generation**
>
> Joule found the process but immediately flags that the information in it is insufficient for a meaningful scoping and test case run; the process diagram exists but has no content (no flows, no steps, no acceptance criteria to work from).
>
> This is intentional. **Garbage in, garbage out**: even for AI agents. The quality of the output depends directly on the quality of the input. Before Joule can do useful work, we need to enrich the process with proper documentation.
>
> That's exactly what we'll do in the next steps.

---

## Step 4 – Navigate to Your Project

Time to find our process. Close the Joule panel first (click **×** in the panel header), then navigate to the project.

1. Back on the home screen, click the **Implementation** tab in the top navigation bar. This is the launchpad for all test management related apps, and much more: requirements, process authoring, test preparation, test plans, test execution, defects.

<br><img src="images/ex0_06_implementation.png" />

2. Under **Preparation and Setup**, click the **Projects and Setup** tile.

<br><img src="images/ex0_07_projects_setup.png" />

3. In the **Manage Projects** list, locate your project: **`XXX_TestProject`** (replace XXX with your workstation number). Click it to open the project details.

4. In the project detail view, click the **Scopes** tab. You'll see one scope: **`XXX_CustomScope`**: this is the container for all the process content you'll work with today. Click on it.

<br><img src="images/ex0_08_project_list.png" />

5. The view switches to **Open Solution Processes**, with the filter pre-set to your project and scope. You should see exactly one process: **`Custom Sales Order Processing with Customer Down Payment (BKJ)`**: your process for today. Click on it to open its details.

<br><img src="images/ex0_09_process_list.png" />

6. The process detail view opens. On the right-hand panel, next to the **General Information** and **Description** tabs, click **+8** to expand the full list of content types that can be linked to this process:

   | Content Type | Count |
   |---|---|
   | Process Hierarchy Nodes | 0 |
   | Configurations | 0 |
   | Interfaces | 0 |
   | Documents | 0 |
   | Test Cases | 0 |
   | Requirements | 0 |
   | User Stories | 0 |
   | Tasks | 0 |

   Everything is at zero. The process diagram on the left is also empty; no flows, no steps. This is your starting point.

   > **This is the root cause** of Joule's rejection in Step 3. With no requirements, no user stories, and no process content, there is nothing for the AI agents to work from. Before we can generate anything meaningful, we need to populate this process, and that's exactly what the next exercises will do.

<br><img src="images/ex0_10_process_detail.png" />

7. Now click the **Solution Process Flow** tab (next to Solution Value Flow). Here you'll find something more promising: a BPMN process diagram showing the full BKJ flow across four swimlanes; Internal Sales Representative, Billing Clerk, Accounts Receivable Accountant, and Shipping Specialist.

   This diagram was imported from **SAP Signavio** into SAP Cloud ALM. It is natively stored here; a direct live integration with Signavio is planned as a future capability.

   > **But here's the catch:** the diagram alone is not sufficient for the AI agents to generate high-quality scope, test plan, and test cases. It provides the process skeleton, but without requirements, user stories, and linked documentation, the agents can't derive meaningful test coverage from it.
   >
   > Feel free to explore the diagram. You can even make small changes, but don't alter it too dramatically, or the AI agents may flag inconsistencies between the diagram and the other content you'll add next.

<br><img src="images/ex0_11_process_flow.png" />

> **In short:** A process structure exists and the diagram provides the skeleton. However, the process still lacks enriched content the AI agents need to do useful work. That's exactly what the next steps will fix.

---

## Step 4C – Assign Pre-Prepared User Stories

To give the AI agents enough to work with, we need to link supporting content to the process. Let's start with the user stories.

1. Make sure you are on the **Solution Value Flow** tab. On the right-hand panel, click **+8** to open the dropdown and select **User Stories**: this brings the User Stories section into view.

<br><img src="images/ex0_12_user_stories_nav.png" />

2. The **User Stories** section is now visible in the right panel: currently empty ("No user story assigned"). Click the **Assign** button to open the selection dialog. It comes pre-populated with user stories prepared for the BKJ process.

<br><img src="images/ex0_13_user_stories_assign.png" />

3. The **Assign User Stories** dialog opens, pre-populated with all 9 BKJ user stories prepared for this exercise:

   | # | Story |
   |---|---|
   | 1 | Create Sales Order with Milestone Billing Plan |
   | 2 | Release Billing Block for Down Payment |
   | 3 | Create Down Payment Request (FAZ) |
   | 4 | Post and Clear Incoming Down Payment |
   | 5 | Enforce Delivery Block Until Payment Is Cleared |
   | 6 | Create Delivery and Execute Picking |
   | 7 | Post Goods Issue |
   | 8 | Release Final Invoice Block and Create Final Invoice (F2) |
   | 9 | End-to-End Document Flow Traceability |

   Click the **select all** checkbox in the header row (all 9 stories should now show as selected), then click **Assign**.

<br><img src="images/ex0_14_user_stories_select.png" />

4. After returning to the process, feel free to open one of the user stories to inspect it. Each story is fully defined with **story points**, the **user story** narrative ("As an [role], I want to... so that..."), and granular **acceptance criteria**: exactly the kind of structured input the AI agents need.

<details>
    <summary>📷 Example: User Story 1: Create Sales Order with Milestone Billing Plan</summary>
    <br><img src="images/ex0_15_user_story_detail.png" />
</details>

   When done, click the **back arrow** (←) at the top left of the screen to return to the process view.

5. Back in the process, open the **+8** dropdown again; **User Stories** now shows **(9)**. The assignment worked.

   But look at **Requirements (0)**. That entry is still empty, and it's arguably the most important input for the AI agents. A well-formed requirements document gives the agents the business rules, constraints, and acceptance detail they need to generate meaningful test coverage.

   Here's the good news: you were recently in a structured interview with a UX colleague, walking through the BKJ process step by step in detail. Your colleague promised to post the transcript in SAP Cloud ALM for further use. Time to retrieve it and turn it into a requirements document.

<br><img src="images/ex0_16_requirements_needed.png" />

---

## Summary

You've logged in, met Joule, and oriented yourself in the project:
- ✅ Joule opened and introduced its capabilities
- ✅ Process located: BKJ in `XXX_TestProject / XXX_CustomScope`
- ✅ 9 user stories assigned to the process
- ❌ Requirements document: still missing; that's where we go next

Continue to [Exercise 1 – Generate Requirements with AI](../ex1/README.md)
