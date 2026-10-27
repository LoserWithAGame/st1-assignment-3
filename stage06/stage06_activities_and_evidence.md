# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: [Wednesday 4:30pm - 6:30pm Group 1]
- Members, GitHub usernames and cohorts: [MastrRoshiiii -, LoserWithAGame - Liam Smilie]
- Repository URL: [https://github.com/LoserWithAGame/st1-assignment-3]
- Starting SHA: [79cad13]

## A Requirement to issue activities

### FR-02 Patient Search

- Title: [response]
- Context: [response]
- Requirement: [response]
- Acceptance criteria: [response]
- Scope: [response]
- Definition of Done: [response]
- Owner: [response]
- Actual issue link: [response]

### FR-06 Appointment Cancellation with FR-07 retained history

Title: Implement appointment cancellation with retained history — FR-06/FR-07

Context:AppointmentService.cancel_appointment currently raises NotImplementedError.
The Appointment domain object already provides guarded cancellation, and the
shared SmartCareDataStore retains appointment objects. The missing service
workflow must locate the stored appointment, invoke the domain cancellation
operation and return the same retained object.

Requirement: FR-06 Appointment Cancellation and FR-07 Retained History.
A user must be able to cancel an existing SCHEDULED appointment by its ID.
Cancellation must change the appointment status to CANCELLED without deleting
or replacing the appointment. Cancelled appointments must remain retrievable
from the shared store during the current session.

Acceptance criteria: A valid ID for a SCHEDULED appointment changes its status to CANCELLED.
- The service returns the original stored Appointment object.
- The cancelled appointment remains retrievable from the shared store.
- A valid but unknown appointment ID raises LookupError.
- A blank, whitespace-only or otherwise invalid ID raises ValueError.
- Repeated cancellation raises ValueError.
- Cancelling a COMPLETED appointment raises ValueError.
- A rejected cancellation leaves the appointment status and stored records unchanged.
- No appointment is deleted or replaced.
- All existing and new tests pass.

Scope: In scope:
- AppointmentService.cancel_appointment in project/smartcare/services.py.
- Focused cancellation service tests in project/tests/test_cancellation.py.
- Necessary Stage 6 issue, PR, review and verification evidence.

Out of scope:
- Deleting appointments.
- Rescheduling appointments.
- Persistence or database changes.
- Console/menu changes.
- Notifications.
- New dependencies.
- Unrelated refactoring.

Definition of Done: AppointmentService.cancel_appointment uses the existing appointment lookup and Appointment.cancel domain operation.
- Positive, negative and boundary tests verify all acceptance criteria.
- Existing tests are retained without weakened assertions.
- The complete pytest suite passes from project/.
- The test command, environment, result and tested commit SHA are recorded.
- Another group member reviews the actual diff.
- Human observations are recorded before the required Copilot comparison.
- Significant AI assistance and human decisions are disclosed honestly.
- Review feedback is resolved and rechecked before approval.
- The feature branch is merged into main.
- The integrated main branch is pulled and retested.
- Stage 6 evidence is updated with the actual issue, PR, review and merge links.

Owner: Daniel Spence (@MastrRoshiiii)

Actual issue link: https://github.com/LoserWithAGame/st1-assignment-3/issues/7

## B Commit quality

| Original example                               | Strong or Weak | Reason     |
| ---------------------------------------------- | -------------- | ---------- |
| changes                                        | [select]       | [response] |
| final version                                  | [select]       | [response] |
| Add patient search by ID                       | [select]       | [response] |
| fix stuff                                      | [select]       | [response] |
| Prevent cancellation of completed appointments | [select]       | [response] |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: [response]
- Responsibility and architecture concerns: [response]
- Testing and review concerns: [response]
- Changes to remove or separate, with reasons: [response]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [response]
- Follow-up review question 1: [response]
- Follow-up review question 2: [response]
- Follow-up review question 3: [response]
- Follow-up review question 4: [response]
- Follow-up review question 5: [response]
- Additional questions if useful: [response]

## E Team workflow agreement

| Practice                            | Team agreement |
| ----------------------------------- | -------------- |
| Branch naming                       | [response]     |
| Commit message convention           | [response]     |
| PR size                             | [response]     |
| Another-member review requirement   | [response]     |
| Merge rule                          | [response]     |
| Significant Copilot disclosure rule | [response]     |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner      | Acceptance criteria or precise link | Status     |
| ---------- | ----------- | ---------- | ----------------------------------- | ---------- |
| [issue 1]  | [response]  | [response] | [response]                          | [response] |
| [issue 2]  | [response]  | [response] | [response]                          | [response] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

[The process of making a Commit is to add a change, this could be in the same task or in multiple different sections of the assignment. This is why having a high commit count is not evidence of strong contribution, as a single person could make multiple commits for the same section of the project, and thus not contribute to the rest of the project.]

## L Stage 6 formative questions

1. What is version control?

[Version Control includes many functions, including making a history for any changes that are made, being able to change the file to a specific iteration of the project, and review changes before fully adding them to the project. This is especially good in the case that an unknown error appears, as the project can be reset to before the error to recreate the intended solution.]

2. Why is a feature branch useful?

[A feature branch is useful because it allows the development and testing of a single aspect of program. This implements modularity into projects, and allows proper testing of a single feature individually, rather than collectively.]

3. What makes a commit a good engineering commit?

[response]

4. What is a pull request?

[A pull request is an attempt to merge an individual branch with the centralised Github Repository. The person makes a pull request with the changes made to their local files, then the moderator of the Repository can determine whether or not to follow through with the request.]

5. What is the purpose of code review?

[The purpose of Code Review is to verify that a program is working properly before merging it with the overall project. The process allows the entire group to add any input and feedback for the program in question.]

6. What does a Git diff show?

[Git Diff is an aspect of version control, as it shows the changes and differences between two commits. This is used to compare and contrast each commit to properly review the program.]

7. What is a Definition of Done?

[response]

8. What is the appropriate role of GitHub Copilot in pull-request review?

[The appropriate role of Github CoPilot should be to review the programs presented and offer suggestions for change. The changes suggested would not be an immediate implementation, rather a thought of if it needs changing. As CoPilot is unreliable in certain areas, it's word should never be taken at face value, and a person should be reviewing the suggested changes to identify the best course of action.]

9. Why should individual contribution not be judged only by commit count?

[Commit count is a terrible way to determine individual contribution in a Git Group project, as one person could have multiple commits to update regarding a single issue rather than multiple contributions to the project.]

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.