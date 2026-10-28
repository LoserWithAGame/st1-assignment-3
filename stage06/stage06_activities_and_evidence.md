# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: [Wednesday 4:30pm - 6:30pm Group 1]
- Members, GitHub usernames and cohorts: [MastrRoshiiii -, LoserWithAGame - Liam Smilie- warunabandara11-wq]
- Repository URL: [https://github.com/LoserWithAGame/st1-assignment-3]
- Starting SHA: [79cad13]

## A Requirement to issue activities

### FR-02 Patient Search

- Title: [Implement patient lookup by ID - FR-02]
- Context: [The starter couild register patients, but the patient lookup method was unfinished. I needed to make it find a patient that was already registered.]
- Requirement: [Fr-02 Paitent Search and the stage 6 lookup contract.]
- Acceptance criteria: [
    - Searching for a registered ID returns the same stored patient object.
    - Space around the ID are accepted.
    - ID's are case-sensitive.
    - A valid ID that is not registered raises LookupError.
    - A blank or invalid ID raises ValueError.
    - An unsuccessful search leaves the existing patients unchanged.
]
- Scope: [Complete PatientServices.find_patient in project/smartcare.services.py and add patient lookup tests to project/tests/test_services.py. Preserve existing practitioner behaviour and tests.]
- Definition of Done: [The required behaviour has meaninful tests, the full suite passes, another member reviews the pull request, the human and Copilot reviews are compared, feeback is addressed, and the merged result is tested and recorded.]
- Owner: [Quiet-learner]
- Actual issue link: [https://github.com/LoserWithAGame/st1-assignment-3/issues/5]

### FR-06 Appointment Cancellation with FR-07 retained history


Title: Implement appointment cancellation with retained history — FR-06/FR-07

Context: AppointmentService.cancel_appointment currently raises NotImplementedError.
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

Scope:
In scope:
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
| changes                                        | [weak]       | [Not clearly identifying what was changed.] |
| final version                                  | [weak]       | [It does not describe the behaviour changed and “final” may become inaccurate after later work.] |
| Add patient search by ID                       | [Strong]       | [Clear identification of a FR.] |
| fix stuff                                      | [weak]       | [Neither the defect nor the affected component is identified.] |
| Prevent cancellation of completed appointments | [Strong]       | [Clearly stating which issue was addressed and what chnages were made.] |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: [Patient-field renaming is unrelated to cancellation, restructuring and adding a dependency are not required by the FR.]
- Responsibility and architecture concerns: [Cancellation should be handled by AppointmentService using the exisiting store lookup for the Appointment.cancel domain.
Unrelated Patient changes could affect registration and lookup behaviour The new dependency also introduces unnecessary coupling unless a specific requirement justifies it.]
- Testing and review concerns: [Cancellation tests would not provide sufficient evidence for unrelated patient, structural changes or a new dependency. Reviewers would need to
verify several independent behaviours in one large diff.]
- Changes to remove or separate, with reasons: [The cancellation PR should retain only the cancellation service implementation,
its focused tests and directly related evidence. Patient-field renaming should e removed or placed in a separate requirement-linked issue and PR.
Unrelated restructuring should be handled as a separate refactoring PR under passing before-and-after tests. 
The dependency should be rejected unless a requirement demonstrates that it is necessary; if justified, it should receive its own review and dependency checks. Separating these changes keeps each PR focused, traceable, testable and easier to reverse.]

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [The Copilot review does not identify which requirement or acceptance criteria were checked, which files or lines were inspected or whether the changes respect the domain, store and services responsibilities.
It does not provide any test details, the results. It provides no assertion quality, negative cases.]
- Follow-up review question 1: [Which requirement and acceptance criteria does each changed behaviour satisfy.]
- Follow-up review question 2: [Did you inspect every chnaged file, and did you identify any unrelated or unnecessary chnages?]
- Follow-up review question 3: [Which test assertions prove that cancellation changes the status, returns the same object and retains the appointment in the store?]
- Follow-up review question 4: [Which tests verify unknown or invalid IDs, repeated cancellation, completed appointments and unchanged state after rejection?]
- Follow-up review question 5: [What exact test command, working directory, result and commit SHA support the claim that the tests pass?]
- Additional questions if useful: [Were all supplied tests retained without weakened assertions? Were any new dependencies, real data or unnecessary files introduced? 
Was the implementation checked against the existing domain and service boundaries? Did an independent human reviewer verify the actual diff and test evidence?]

## E Team workflow agreement ##agree on during tutorial

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
| [https://github.com/LoserWithAGame/st1-assignment-3/issues/7]  | [FR-06 Appointment Cancellation and FR-07 Retained History] | [@MastrRoshiiii] | [Cancel a scheduled appointment; return and retain the same object; reject unknown/invalid IDs and illegal transitions; preserve state after failure.] | [Closed - Merged onto Main.] |
| [https://github.com/LoserWithAGame/st1-assignment-3/issues/5]  | [FR-02 Patient Search]  | [@quiet-learner] | [Return the original patient; accept surrounding whitespace; retain case sensitivity; invalid IDs raise ValueError; unknown IDs raise LookupError; failed lookup preserves records] | [Closed - Merged onot Main.] |


## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [https://github.com/LoserWithAGame/st1-assignment-3/pull/6  Implemented patient lookup with service tests]
- Linked issue and requirement: [https://github.com/LoserWithAGame/st1-assignment-3/issues/5 - FR-02 Patient Search]
- Feature branch: [feature/patient-lookup]
- Changed behaviour: [I finished find_patient so it asks the existing store for the patient and returns that same object. Spaces around an ID are accepted, but its case must match. Unknown IDs raise LookupError, while blank or invalid IDs are rejected by the store's existing validation.]
- Meaningful commits: [https://github.com/LoserWithAGame/st1-assignment-3/commit/e68f4ea644f7afb781b7f7815f8db5b0a5011790]
- Test command, directory and observed result: [I ran python -m pytest from project/. All 24 cases passed: 9 patient cases, 7 practitioner cases and 8 starter cases.]
- Another-member reviewer: [MastrRoshiiii]
- Human observations recorded before Copilot: [masterRoshiiii checked the lookup code and tests against the requirements before I asked Copilot. They identified a double space and a missing final newline. Review evidence comment:
"I have reviewed the current changes that include the Patient and Practitioner lookup tests against the FR requirements. The test associated with these changes cover errors such as unknown ID, does not create or modify patient records, with spacing, case sensitivity. Double spacing error on line 2 can be fixed, add the missing final newline, and complete the required Copilot comparison. The reported full-suite result is 24 passed." https://github.com/LoserWithAGame/st1-assignment-3/pull/6#pullrequestreview-5650816620]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [The service uses the existing store instead of creating replacement patients or adding another storage system. The tests check the returned object, accepted whitespace, case sensitivity, errors and unchanged records after failure. I kept the practitioner tests.]
- Key feedback: [Fix the double space, add the final newline and complete the required Copilot comparison.]
- Author response/change and verification: [I fixed the double space missing final newline, completed the Copilot comparison, and brought the latest main into my patient branch. I resolved the shared evidence-file conflict while keeping both patient and cancellation entries. I ran python -m pytest from project/: 32 passed. The tested combined code is recorded in commit 713c17881bca272461c808cf7d3b2408e366078b]
- Reviewer recheck and approval: [masterRoshiiii approved the original changes. A final recheck of the formatting and evidence updates is pending.]
- Merge outcome and SHA: [pending]
- Significant Copilot assistance: [Github Copilot reviewed commit e68f4ea and found no blocking bug. Its suggestions and my decisions are recorded in H and I.]
- Linked issue closure: [pending]
- Each member updated main: [member and confirmation] <- [pending]
- Integrated verification after merge: [command, directory, result and code SHA] <- pending merge


- PR link and title: [PR #8 — Feature/stage06 appointment cancellation](https://github.com/LoserWithAGame/st1-assignment-3/pull/8)]
- Linked issue and requirement: [[Issue #7 — FR-06 Appointment Cancellation and FR-07 Retained History](https://github.com/LoserWithAGame/st1-assignment-3/issues/7)]
- Feature branch: [feature/stage06-appointment-cancellation]
- Changed behaviour: [AppointmentService.cancel_appointment now finds the stored appointment, calls its guarded domain cancel method, returns the same Appointment object and retains it in the shared store. Tests cover successful cancellation, invalid and unknown IDs, repeated cancellation, completed appointments and unchanged state after rejection.]
- Meaningful commits: [  - [Implement appointment cancellation with retained history](https://github.com/LoserWithAGame/st1-assignment-3/commit/f4e4af4aae1703011f970df0fe6fca17fb73fba9) - [Update Stage 6 cancellation evidence](https://github.com/LoserWithAGame/st1-assignment-3/commit/962a8abe06019275fa217c312178d39f9af81640)]
- Test command, directory and observed result: [python -m pytest from project/. [Insert the exact full-suite count you personally observed and the tested code SHA. Do not estimate.]]
- Another-member reviewer: [No another-member review was recorded on GitHub before merge.]
- Human observations recorded before Copilot: [No human-first review observations were recorded on the PR before merge.]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [The implementation was checked against FR-06/FR-07. AppointmentService coordinates lookup, Appointment.cancel enforces the state transition, and SmartCareDataStore retains the object. Tests assert object identity, CANCELLED status, retained history, correct exceptions and unchanged state. The production change is limited to the cancellation service method.]
- Key feedback: [No reviewer feedback was recorded before merge.]
- Author response/change and verification: [No reviewer-requested change was recorded before merge.]
- Reviewer recheck and approval: [Appoved by @LoserWithAGame and approved.]
- Merge outcome and SHA: [Merged into main as commit 86b3ac2ef33424e815e5f0f276d6b40add955eac.]
- Significant Copilot assistance: [Copilot offered little to no assistance. Verified test cases worked and program functioned as it should.]
- Linked issue closure: [https://github.com/LoserWithAGame/st1-assignment-3/pull/8]
- Each member updated main: [All group members have updated main.]
- Integrated verification after merge: [python -m pytest`, run from `project/`, 32 passed in 0.11s, 3e992e1128657d708db10ad36e1cd1654d45936e]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [Liam Smilie, FR-02]
- Prompt/purpose and relevant issue/diff: [
    Act as a GitHub Copilot code-review assistant.

Context: SmartCare uses domain objects, one SmartCareDataStore and service classes. The human reviewer
has already recorded independent observations.

Linked requirement and acceptance criteria: 
Requirement: FR-02 Patient Search, including the published Stage 6 lookup contract.

Acceptance criteria:
    A registered ID returns the actual stored patient object.
    Surrounding whitespace is accepted.
    IDs remain case-sensitive.
    A valid unknown ID raises LookupError.
    Blank or invalid IDs raise ValueError.
    Failed lookup preserves existing patient records.

Task: Summarise the supplied PR diff, then review it against the linked requirement, acceptance criteria and
SmartCare responsibilities. Identify correctness risks, responsibility violations, missing or weak tests,
accidental unrelated changes and maintainability concerns. Suggest review questions.

Constraints: Do not assume unstated requirements. Do not recommend deleting cancelled appointments.
Do not introduce new frameworks or features. Separate each observed concern, question and suggestion.
Cite the relevant diff lines and distinguish observed evidence from inference. Rank findings Critical,
Important or Optional. If evidence is missing, say what must be checked; do not claim tests ran.

PR diff and relevant synthetic project context: 
Context: PatientService.find_patient needs to retrieve a registered patient
through the existing shared data store.
     ]
     - Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]
- Summary of output: []


- Member and task: [Quiet-learner - Copilot review of patient lookup, issue #5 and Pull Request #6]
- Prompt/purpose and relevant issue/diff: [I Used the stage 6 part H review prompt with the patient-search acceptance criteria and the diff from commit e68f4ea. I asked Copilot to check the behaviour, responsibilities, tests and scope.]
- Summary of output: [Copilot found no blocking bug. It raised two optional suggestions: serperate data-store tests and clarification of invalid IDs. It also reported no unrelated funcitonal changes.]
- Human check against actual code, requirements and tests: [I checked that the service calls the existing store, which trims IDs and rejects blank or non-sring values. My service tests use that real store and check the returned object, errors and unchanged records. My full test run reported 24 passed. Copilot did not run the tests.]
- Decision — Accept / Modify / Reject: [Accept the overall correctness and scope observations. Modify the direct-store test suggestion by leaving it as a possible later improvement. Reject the suggestion that the allowed ID types are unresolved.]
- Reason: [The service tests already exercise the real store's lookup and validation. The stage 6 cantract specifies string IDs, so there is no need to broaden or duplicate the existing validation.]
- Verification/evidence: [Pr #6 https://github.com/LoserWithAGame/st1-assignment-3/pull/6 Reviewed code commit: e68f4ea644f7afb781b7f7815f8db5b0a5011790. Command python -m pytest from project/. Observed result: 24 passed. [https://github.com/LoserWithAGame/st1-assignment-3/pull/6#issuecomment-6436689921]]



- Member and task: [Liam Smilie, Practitioner Lookup]
- Prompt/purpose and relevant issue/diff: [
    Act as a GitHub Copilot code-review assistant.

Context: SmartCare uses domain objects, one SmartCareDataStore and service classes. The human reviewer
has already recorded independent observations.

Linked requirement and acceptance criteria: 
Requirements: Return the existing practitioner when a valid ID is entered.
            Remove surrounding spaces from the ID.
            Raise ValueError for blank or invalid IDs.
            Raise LookupError if the practitioner does not exist.
            Keep practitioner IDs case-sensitive.
            Do not modify existing practitioner records.
Acceptance Criteria: An existing practitioner can be found using their ID.
                    The original stored practitioner object is returned.
                    Invalid and unknown IDs produce the correct errors.
                    Existing application functionality remains unchanged.

Task: Summarise the supplied PR diff, then review it against the linked requirement, acceptance criteria and
SmartCare responsibilities. Identify correctness risks, responsibility violations, missing or weak tests,
accidental unrelated changes and maintainability concerns. Suggest review questions.

Constraints: Do not assume unstated requirements. Do not recommend deleting cancelled appointments.
Do not introduce new frameworks or features. Separate each observed concern, question and suggestion.
Cite the relevant diff lines and distinguish observed evidence from inference. Rank findings Critical,
Important or Optional. If evidence is missing, say what must be checked; do not claim tests ran.

PR diff and relevant synthetic project context: 
Context: Implement the PractitionerService.find_practitioner() method so SmartCare can search for a registered practitioner using their unique ID.
     ]
- Summary of output: [The AI concluded that the program was implemented well, however, the test file needs change. The AI highlighted that the system tested for null inputs but not invalid inputs, as the input is a string, there needs to be a test for invalid input strings.]
- Human check against actual code, requirements and tests: [The program for the Practitioner Lookup by ID was implemented well, the code has comments and is easy to read. The program functions as required by the requirements, and the tests reflect this.]
- Decision — Accept / Modify / Reject: [Rejected]
- Reason: [The only suggestion is to add a test for an ID that does not exist, to test invalid IDs, this is already implemented in the program, but specified under the function "test_unknown_practitioner_raises_lookup_error()".]
- Verification/evidence: [https://github.com/copilot/share/c227500c-40e4-80a4-a952-14070025087d]



- Member and task: [Liam Smilie, FR-06 and FR-07]
- Prompt/purpose and relevant issue/diff: [
    Act as a GitHub Copilot code-review assistant.

Context: SmartCare uses domain objects, one SmartCareDataStore and service classes. The human reviewer
has already recorded independent observations.

Linked requirement and acceptance criteria: 
Requirement: FR-06 Appointment Cancellation and FR-07 Retained History. A user must be able to cancel an existing SCHEDULED appointment by its ID. Cancellation must change the appointment status to CANCELLED without deleting or replacing the appointment. Cancelled appointments must remain retrievable from the shared store during the current session.

Acceptance criteria: 
        A valid ID for a SCHEDULED appointment changes its status to CANCELLED.

        The service returns the original stored Appointment object.
        The cancelled appointment remains retrievable from the shared store.
        A valid but unknown appointment ID raises LookupError.
        A blank, whitespace-only or otherwise invalid ID raises ValueError.
        Repeated cancellation raises ValueError.
        Cancelling a COMPLETED appointment raises ValueError.
        A rejected cancellation leaves the appointment status and stored records unchanged.
        No appointment is deleted or replaced.
        All existing and new tests pass.

Task: Summarise the supplied PR diff, then review it against the linked requirement, acceptance criteria and
SmartCare responsibilities. Identify correctness risks, responsibility violations, missing or weak tests,
accidental unrelated changes and maintainability concerns. Suggest review questions.

Constraints: Do not assume unstated requirements. Do not recommend deleting cancelled appointments.
Do not introduce new frameworks or features. Separate each observed concern, question and suggestion.
Cite the relevant diff lines and distinguish observed evidence from inference. Rank findings Critical,
Important or Optional. If evidence is missing, say what must be checked; do not claim tests ran.

PR diff and relevant synthetic project context: 
Context: AppointmentService.cancel_appointment currently raises NotImplementedError. The Appointment domain object already provides guarded cancellation, and the shared SmartCareDataStore retains appointment objects. The missing service workflow must locate the stored appointment, invoke the domain cancellation operation and return the same retained object.
     ]
- Summary of output: [The AI did not find any errors within the program for this section, however the AI in Github was unable to find the Testing file. The AI recommended checking the PyTest for the program before merging, but found no issues aside from that.]
- Human check against actual code, requirements and tests: [To review the code: The program made by Daniel Spence was well structured and simplistic, it met all of the requirements listed. The tests revealed no errors.]
- Decision — Accept / Modify / Reject: [Accepted]
- Reason: [The program is fully functional, passing all the tests and operating properly, and the AI has verified this through the suggestions provided. Also accepting the AI suggestion to test before merging with the finalised project.]
- Verification/evidence: [https://github.com/copilot/share/4a4e410c-00c4-8822-9142-864704a5012f]


## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [MasterRoshiiii checked the lookup code and tests against the requirements. They pointed out a double space and a missing final newline, and reminded me to complete the Copilot comparison.]
- Copilot noticed: [Copilot found no blocking bug. It suggested serperate seperate data-store tests and checking wheather the meaning of an invalid ID was clear.]
- Overlap: [Both considered whether the lookup and tests matched the requirements. Neither reported a blocking patient-lookup defect.]
- What did the human reviewer notice that Copilot did not: [The double space and missing final newline.]
- What did Copilot identify that the human reviewer initially missed: [Copilot raised direct-store test coverage and inalid-ID clarification as optional suggestions. These were not confirmed bugs.]
- Unsupported or incorrect Copilot suggestion: [Copilot quesitoned which ID types were allowed, but the stage 6 instructions already specify string IDs. Existing validation rejects blank and non-string inputs.]
- Human judgement accepted, modified or rejected, and why: [I accepted the overall review after checking the code and test results. I left sperate store tests as a possible later improvment because my service tests already use the real store. I rejected chjanging ID validation because the existing rules already cover it.]
- Which evidence justified merge approval: [MasterRoshiiii approved the original changes, and my full suite reported 24 passed. FInal merge is still pending verification of the formatting corrections and a teammate recheck of the updated branch.]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [quiet-learner]
- Implementation: [I compelted PatientService. find_patient using the existing shared sotre. Code commit: e68f4ea644f7afb781b7f7815f8db5b0a5011790.]
- Testing: [I added 9 patient test cases covering successful lookup, missing Ids, surrounding spaces, case sensitivity, invalid IDs and unchanged records after failure. THe full suite reported 24 passed.]
- Review: [I checked my own diff and considered the teammate and Copilot feedback. I have not recorded ani independent review of another member's pull request here. ]
- Issue refinement: [I created issue #5 with acceptance criteria and compleetion conditions after implementing the change.]
- Design and responsibility discussion: [I worked through why the service asks the store for the patient and returns the original object rather than making a replacement.]
- Debugging or integration: [I corrected assertions that were incorrectly inside pytest.raises and reran the tests successfully. Integration into main is still pending.]
- Documentation or team support: [I recorded the patient issue, Pull request, test results, review feedback and Copilot decisions in this shared record.]

- Member: [@MastrRoshiiii]
- Implementation: [I implemented AppointmentService.cancel_appointment using the existing service lookup and Appointment.cancel domain method. The implementation returns the original stored appointment and retains its history. Evidence: [implementation commit](https://github.com/LoserWithAGame/st1-assignment-3/commit/f4e4af4aae1703011f970df0fe6fca17fb73fba9) and [PR #8](https://github.com/LoserWithAGame/st1-assignment-3/pull/8).]
- Testing: [I created project/tests/test_cancellation.py with successful, unknown-ID, invalid-ID, repeated-cancellation and completed-appointment cases. The parametrised invalid-ID test covered blank text, whitespace, None and an integer. I ran the focused tests and the full suite. The later full-suite run collected 32 tests and reported 32 passed. Evidence: PR #8 and recorded terminal result]
- Review: [Reviewed by @LoserWithAGame, approved and merged into main.]
- Issue refinement: [I created and expanded [Issue #7](https://github.com/LoserWithAGame/st1-assignment-3/issues/7) with FR-06/FR-07 context, requirements, acceptance criteria, scope, Definition of Done and ownership.]
- Design and responsibility discussion: [I kept cancellation responsibilities separated: AppointmentService locates and coordinates the operation, Appointment.cancel enforces the legal status transition, and SmartCareDataStore retains the appointment object.]
- Debugging or integration: [I diagnosed a NameError in test_cancellation.py caused by missing imports, added the required SmartCareDataStore, service, datetime and AppointmentStatus imports, and reran the test successfully. I later ran the accumulated suite and observed 32 passed.]
- Documentation or team support: [I updated the Stage 6 cancellation evidence and completed Sections C, D and F. Evidence includes [PR #11](https://github.com/LoserWithAGame/st1-assignment-3/pull/11) and the Stage 6 evidence commits.]

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

[The main Definition of Done is the set of requirements that indicate a finalised program. This could be based on functionality, design, modularity, testing capability, or any other requirements present.]

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
