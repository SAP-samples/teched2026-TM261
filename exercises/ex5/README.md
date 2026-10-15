# Exercise 5 – Generate Test Data with AI

**Prerequisite:** You have completed [Exercise 4](../ex4/README.md); generated test cases exist and you have noted a test case ID.

---

## What You'll Do

In this exercise you'll unleash the **Data Agent**: an AI agent that analyzes your test cases and proposes meaningful test data: parameter values with the right combinations, boundary cases, and reasoning for each choice. This is the final AI-assisted stage of test preparation.

---

## Step 19 – Unleash the Data Agent

### 19.1 – Prompt Joule with Your Test Case

1. Open Joule.

2. Enter a prompt that references the test case ID you noted in Exercise 4. Something like: **"Please suggest test data for test case [your-TC-ID]."**

<!-- 📷 TODO: screenshot ex5_01_data_prompt.png: Joule prompt referencing a specific test case ID, acknowledgement response -->
<br><img src="images/ex5_01_data_prompt.png" />

3. The data agent queues and starts analyzing the test case; reading its steps, identifying parameters, and cross-referencing the master data requirements from the solution design.

<!-- 📷 TODO: screenshot ex5_02_data_agent_running.png: Data agent running indicator -->
<br><img src="images/ex5_02_data_agent_running.png" />

> ⏱️ **While the agent works:**
>
> Think about what makes good test data:
> - Values that are **valid but exercise boundaries** (e.g. a down payment that is exactly 50% of the order value)
> - Values that are **invalid** but in realistic ways (e.g. insufficient stock, wrong billing type)
> - Values that **respect dependencies** (sales org determines customer pool, plant determines storage)
>
> What would you suggest as test data for the payment posting test case?

---

## Step 20 – What's Happening? (Narration)

> **The challenge:** Finding valid test data demands expert knowledge that doesn't scale; wrong data corrupts test results and steals time from actual testing.
>
> **The solution:** The **Test Data Management Agent** identifies every required data parameter from test case instructions; the tester looks up the known targets; no expert required. *(This is Phase 1 of a longer roadmap.)*
>
> Here is what the agent is working through right now:
>
> | Stage | What happens |
> |---|---|
> | **Fetch test case** | Reads the test case and all its activity steps from Cloud ALM via MCP (TL102). ⚠️ If the test case is not found, has no activities, or the text is empty; the agent stops and asks you to verify the input. |
> | **Extract parameters** | Identifies every required SAP business object and field value from the instruction text; every line of "Enter Sales Organization…" becomes a structured parameter. |
> | **Classify parameters** | Labels each parameter by category: **Org Data · Master Data · Config Data · Transactional Data**. |
> | **Apply project context** | Obtains fixed values (company code, plant, client) from the Cloud ALM project record; so you don't have to look those up yourself. |
> | **Output** | A read-only parameter table per category. Structured guidance for the tester who locates the actual system values manually. |
>
> **Phase 1 scope note:** The agent identifies and classifies parameters; it does not yet automatically look up system values. That's the tester's final step: use the table as a checklist to find values in the target system.

---

## Step 21 – Review the Test Data Agent Output

### 21.1 – Open the Suggested Data

1. Go to the **Notification Area** and open the data agent's completion.

<!-- 📷 TODO: screenshot ex5_03_data_notification.png: Data agent completion notification -->
<br><img src="images/ex5_03_data_notification.png" />

2. Review the suggested test data; you should see a structured set of parameter values with explanations.

<!-- 📷 TODO: screenshot ex5_04_data_result.png: Test data suggestion: parameter table with values and reasoning -->
<br><img src="images/ex5_04_data_result.png" />

### 21.2 – Evaluate the Data Quality

For each parameter group, check:

| Aspect | What to look for |
|---|---|
| **Completeness** | Are all required parameters covered? Any missing? |
| **Consistency** | Are the values consistent with each other (e.g. correct sales org + customer combination)? |
| **Coverage** | Does the set include both valid (happy path) and invalid (negative test) values? |
| **Reasoning** | Does the agent explain *why* specific values were chosen? |
| **Boundary cases** | Are there values that test edge conditions (max amount, exact threshold)? |

<!-- 📷 TODO: screenshot ex5_05_data_evaluation.png: Detailed data suggestion showing reasoning for a specific parameter -->
<br><img src="images/ex5_05_data_evaluation.png" />

---

## Step 22 – Go Deeper into Data Understanding

### 22.1 – Explore Dependencies

1. In Joule, ask: **"What are the dependencies between these parameters?"** or **"Which parameters drive the values of other parameters?"**

   The agent should outline the dependency chain; for example, that the Sales Organization determines which customers and materials are valid.

<!-- 📷 TODO: screenshot ex5_06_dependencies.png: Joule response outlining parameter dependencies -->
<br><img src="images/ex5_06_dependencies.png" />

> **Key insight:** The dependency map the agent produces here is exactly what you started sketching in Exercise 4, Step 18. Notice how parameters like Sales Organization (1010), Plant (1010), and Material type cascade into choices for all other fields.

### 22.2 – Reference Data in Context

For the BKJ process, the core master data values are:

| Parameter | Value (Demo System) | Determines |
|---|---|---|
| Sales Organization | 1010 | Dist. Channel, Division, Customer pool |
| Distribution Channel | 10 (Direct Sales) | Available customers |
| Division | 00 | – |
| Sold-to Party | 10100004 | Ship-to, Payer |
| Plant | 1010 | Storage location, available materials |
| Storage Location | 101A | – |
| Material | TG11 / TG12 | Item Category (CBAO) |
| Item Category | CBAO | Billing plan type |
| Shipping Point | 1010 | Delivery creation |
| House Bank | DEBK1 / DEAC1 | Payment posting |

> **Additional scenario:** The agent's real value shows when you have **unexpected combinations**: e.g. what happens if a non-stock material (NS0002) is used instead of a trading good? The item category changes to CTAX, which uses a different billing plan configuration. These scenarios are hard to spot manually but the agent flags them as meaningful test variants.

<!-- 📷 TODO: screenshot ex5_07_variants.png: Test data variants showing different material type combinations or other meaningful edge cases -->
<br><img src="images/ex5_07_variants.png" />

---

## Step 23 – Recap: Value Created

Let's step back and look at what you've accomplished in this hands-on.

### Time comparison

| Stage | Manual Effort (estimate) | AI-Assisted |
|---|---|---|
| Requirements from transcript | 2–4 hours (BA writing) | ~2 minutes (generation) + review |
| Test case scoping | 4–8 hours (architect) | ~3 minutes (agent) + review |
| Test plan creation | 2–4 hours (test analyst) | ~3 minutes (agent) + review |
| Test case writing | 1–2 days (test analyst) | ~5 minutes (agent) + review |
| Test data suggestion | 4–8 hours (analyst + BA) | ~2 minutes (agent) + review |
| **Total** | **3–5 days** | **< 30 minutes** |

<!-- 📷 TODO: screenshot ex5_08_recap.png: Optional: summary view, completed test cases in system, or any "done" state overview -->
<br><img src="images/ex5_08_recap.png" />

> **The shift:** You didn't just save time; you changed the nature of the work. Instead of *creating* artifacts from scratch, you spent your time *reviewing and validating* AI-generated artifacts. That's the role of the future test expert: quality judgment, not manual production.

---

## Summary

The data agent provided meaningful, dependency-aware test data suggestions with reasoning; turning a multi-hour analysis task into a review exercise.

You've now completed the full AI-assisted test preparation cycle:
1. ✅ Requirements generated from interview transcript
2. ✅ Test case scope proposed by scoping agent
3. ✅ Test plan structured by planning agent
4. ✅ Test cases written by TC generation agent
5. ✅ Test data suggested by data agent

Continue to [Exercise 6 – Recap & What's Next](../ex6/README.md)
