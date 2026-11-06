# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [Wednesday 4:30pm - 6:30pm Group 1]
Members and UG/PG cohorts: [MastrRoshiiii -, LoserWithAGame - Liam Smilie- warunabandara11-wq]
Record owner / contribution links for each member: [complete]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: 
1. Symptom: This describes the problem someone notices, but it does not explain why it happens. The appointment might still be stored but hidden from searches.
2. Hypothesis: This suggests a possible cause, but we need to inspect the code to check it. The instructions say the current project has no public delete operation, so we should not assume the appointment was deleted.
3. Evidence: The failing test shows that store.find_appointment('A1') returns None after cancellation. The earlier checks show that cancellation returned the original appointment and its status became CANCELLED.
4. Opinion: This is a broad judgement without specific evidence explaining why.
5. Evidence: A traceback identifies where an error was reported. Line 42 is only an example in the question. In our cancellation test, the traceback points to services.py line 142, which raises ‘Appointment not found’. This identifies where the error appeared, but does not establish its cause.

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason:
- Cancelled-history

- Expected Behaviour: Under FR-07 a cancelled appointment must remain stored and available to search. Looking up an appointment, example: (A1) after cancellation should return the original appointment with its status set to CANCELLED.

- Observed behaviour: Cancellation returns the original appointment and chnages its status to CANCELLED. But when attempting to look up (A1) through the data_store.py returns None.
- Minimal Production: 
1. Register a patient and a practitioner.
2. Book appointment A1.
3. Cancel appointment A1.
4. Look up A1 using store.find_appointment('A1').
5. Observe that the lookup returns None instead of the cancelled appointment.

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:
- The test expecting cancelled appointments to be deleted should be corrected. FR-07 requires cancelled history to remain stored. The test should check that the original appointment can still be found and has the status CANCELLED.
- The test expecting different practitioners to conflict simply because their appointments share the same time should also be corrected. Under AC-04.2, different practitioners can have appointments at the same time. The conflict rule should prevent the same practitioner from being booked twice at that time.
- A failing test does not automatically mean the application is wrong. The test’s expectation must agree with the requirement.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason:
- The method contains several code smells, for example:
1. It handles too many responsibilities in one place, making it harder to understand and test.
2. Repeated status strings increase the chance of spelling mistakes.
3. Directly changing stored collections bypasses the SmartCareDataStore methods.
4. Printing mixes screen output with appointment processing.
5. Four levels of nested conditions make the decision process difficult to follow.


Small improvements would include using the existing AppointmentStatus enum, extracting repeated checks into clearly named helper methods, using the existing data-store methods, and keeping printing in the console layer. Simple checks that reject invalid requests early could also reduce nesting.

- Classification of the proposed changes:
1. Rename “appt” to “appointment”: Refactoring. It improves readability without changing what the code does.
2. Extract a repeated conflict helper: Refactoring. It removes duplication while keeping the same booking rules.
3. Add rescheduling: Feature. It introduces a new capability.
4. Restore retained cancellation lookup: Repair. It corrects behaviour that breaks the requirement to retain cancelled history.
5. Replace a magic status string with the existing enum: Refactoring, provided the replacement preserves the existing behaviour.


### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason:
- Test: test_cancel_appointment_returns_retained_cancelled_object()

- Exception: AssertionError: The test expected to return the stored appointment, but returns None.

- Exepcted Value: The original appointment (A1), with its status set to CANCELLED.

- Observed Value: store.find_appointment (A1) returend None.

- Test Location: test_cancellation.py, line 41, in test_cancel_appointment_returns_retained_cancelled_object.

- Application Call Path: The test books A1 through AppointmentService, cancels it through AppointmentService, and then calls SmartCareDataStore.find_appointment('A1'). The final lookup does not return the appointment, so the assertion fails.


Supoorting Requirement:

FR-07 requires cancelled appointment history to remain stored and available to find.

Three possible causes ranked:
1. The lookup excludes cancelled appointments.
- This best fits the evidence because cancellation returns the correct object and changes its status successfully, but the later lookup fails.
- Check: Inspect find_appointment for a condition that ignores cancelled appointments. Check whether A1 remains in the stored collection.
2. Cancellation removes the appointment from storage.
- This could explain the missing result, although we have not seen evidence of removal and the project has no public delete operation.
- Check: Follow the cancellation code and compare the stored appointments before and after cancellation.
3. The appointment is stored under a different ID.
- This could cause a lookup for A1 to fail, but the screenshot gives no evidence that its ID changed.
- Check: Compare the appointment’s ID and its storage key before and after cancellation.



Why the traceback is not enough:
- The traceback identifies the failed assertion and the unexpected result. Several could potentially be different problems that could produce that result, so I must inspect the code and stored data before confirming the cause.

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: Chnaging the code immediately might be fixing a symptom rather then a cause. Its also possible for the test itself to be wrong. Check the expected behaviour against the requirement, and gather evidence to test possible explanations. This would help with making small fixes without accidently breaking working behaviour.


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [complete]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [complete] | [complete] | [complete] |
| F8-01 after repair | [complete] | [complete] | [complete] |
| F8-02 before repair | [complete] | [complete] | [complete] |
| F8-02 after repair | [complete] | [complete] | [complete] |
| Full suite after both repairs, before refactor | [complete] | [complete] | [complete] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
