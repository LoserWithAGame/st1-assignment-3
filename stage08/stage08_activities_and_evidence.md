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

- Stage 7 code SHA and requirement baseline: - 770ca814cf20519f2717c07e2760aec5b383efef. The requirements baseline was SmartCare A3 Requirements Baseline 2026, revision 2.
- Baseline test command / working directory / observed result / evidence: - The Stage 7 record shows python -m pytest -v, run from the project folder, with 32 passed, 0 failed at the earlier commit 2fba9705ec1baabf68b34fd0b74a200cd5bdca8b.
- Clean preparation SHA if a record-only commit followed Stage 7: Github shows that the fault commit directly followed 829e6e8. There was no seperate.
- Branch and preparer / how teammates obtained this branch: Gupta Pranav authored the preparation commit on debug/stage08. Teammates including myself obtained this branch during our tutorial by pulling the branch from Github.
- Downloaded tool version, source SHA256 and --check outcome: 
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): The preparation commit only chnaged data_store.py. 
- Prepared faulty-state commit SHA: d666a560fbc6de3f56636aaf5b0a35f13ffb70ba
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: I ran python -m pytest -v from the project folder on debug/stage08. It showed 5 failed, and 29 passed. Two of the failures invollved cancelled appointment history and three involved practitioner booking conflicts.  

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: Cancelling appointment A1 returned the original appointment and changed its status to CANCELLED. Looking it up afterward returned None.
- Expected behaviour and requirement: FR-07 requires cancelled appointment history to be retained. Looking up A1 after cancellation should return the same appointment with status CANCELLED.
- Minimal synthetic reproduction steps: Register a sample patient and practitioner, book appointment A1, cancel it, then call store.find_appointment('A1').
- Meaningful failing test path/name and exact relevant failure: test_cancel_appointment_returns_retained_cancelled_object failed at [test_cancellation.py, line 41 (line 41) project/tests/test_cancellation.py:41)]. The check assert store.find_appointment('A1') is appointment raised an AssertionError because the lookup returned None.
- Human hypothesis and intended checks: see E, F8-01. (I plan to compare list_appointments() with find_appointment('A1') after cancellation. If A1 still appears in the list but the lookup returns None, I would inspect the lookup code to see why it skips that record. If A1 is also missing from the list, I would check whether cancellation removes it.)
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: The system allowed a second appointment for the same practitioner at the same time. It also incorrectly reported a conflict for a different practitioner at that time.
- Expected behaviour and requirement: FR-05 requires the system to prevent double booking a practitioner. A second booking for the same practitioner at the same time should raise ValueError.
- Minimal synthetic reproduction steps: Book appointment A1 for practitioner D1 at 9:00 am. Try to book a second appointment for D1 at the same time. It should be rejected. Then check the same time for practitioner D2, who has no booking. The system should report no conflict.
- Meaningful failing test path/name and exact relevant failure: In [project/tests/test_services.py (line 155)], test_practitioner_conflict_prevents_appointments books A1 with practitioner D1 on line 154, then attempts to book A2 with the same practitioner at the same time on lines 155–156. The second booking should raise ValueError, but it went through, so pytest reported Failed: DID NOT RAISE <class 'ValueError'>. In the same file, test_different_practitioner_books_appointment checks on line 166 that D2 has no conflict when D1 is booked at that time. The check returned True instead of False, so pytest reported AssertionError: assert True is False. In [project/tests/test_starter.py (line 127)], test_conflict_rule_and_different_practitioner also expects ValueError on lines 127–128 when a second appointment is booked with D1 at the same time. Pytest reported Failed: DID NOT RAISE <class 'ValueError'> at line 127, and the test stopped before reaching the check that a booking with D2 succeeds.
- Human hypothesis and intended checks: see E, F8-02. (I plan to book D1 at 9 am, then run the conflict check directly for D1 and D2 at 9am. If the direct check gives the wrong results, Ill inspect the check itself. If it gives the right results, Ill check which ID the booking service passes in.)
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: I believe that the lookup might be skipping cancelled appointments. The cancellation returned the original appointment with its status set to CANCELLED, but looking up A1 immediately afterward returned None.
Evidence intended to inspect / competing explanation / discriminating check: I plan to compare list_appointments() with find_appointment('A1') after cancellation. If A1 still appears in the list but the lookup returns None, I would inspect the lookup code to see why it skips that record. If A1 is also missing from the list, I would check whether cancellation removes it.
Member and saved sequence/time or commit showing this preceded consultation: @MastrRoshiiii saved on 7/11/2026 at 10:11pm before consulting Copilot. 

### F8-02 human entry
Likely cause and why plausible: I believe the conflict check was comparing practitioner IDs incorrectly. It allowed a second booking for D1 at the same time but reported a conflict for D2, who had no booking at that time.
Evidence intended to inspect / competing explanation / discriminating check: I plan to book D1 at 9 am, then run the conflict check directly for D1 and D2 at 9am. If the direct check gives the wrong results, Ill inspect the check itself. If it gives the right results, Ill check which ID the booking service passes in.
Member and saved sequence/time or commit showing this preceded consultation: @MastrRoshiiii saved on 7/11/2026 at 10:37pm.

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member:
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: 
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: Help me investigate F8-02, the practitioner booking conflict, on the debug/stage08 branch.

To reproduce it, book appointment A1 for practitioner D1 at 9 am. Then try to book A2 for D1 at the same time. Also check whether D2, who has no booking at that time, is reported as having a conflict.

Expected behaviour under FR-05 and AC-04.2: the second booking for D1 should raise ValueError, and the conflict check for D2 should return False.

Actual behaviour: the second booking for D1 went through, and the conflict check for D2 returned True.

Failing tests in project/tests/test_services.py:
- test_practitioner_conflict_prevents_appointments, lines 155–156: Failed: DID NOT RAISE <class 'ValueError'>
- test_different_practitioner_books_appointment, line 166: AssertionError: assert True is False

My initial hypothesis and planned check from Part E: F8-02
```
My initial hypothesis and planned check from Part E:
I believe the conflict check is comparing practitioner IDs incorrectly. It allowed a second booking for D1 at the same time but reported a conflict for D2, who had no booking at that time.

I plan to book D1 at 9 am, then run the conflict check directly for D1 and D2 at 9 am. If the direct check gives the wrong results, I’ll inspect the check itself. If it gives the right results, I’ll check which ID the booking service passes in.
```


Relevant code:
```
```python
def has_practitioner_conflict(
    self,
    practitioner_id: str,
    date_time: datetime,
    exclude_appointment_id: str | None = None,
) -> bool:
    for appointment in self.list_appointments():
        if (appointment.appointment_id != exclude_appointment_id
                and appointment.practitioner.practitioner_id != practitioner_id
                and appointment.date_time == date_time
                and appointment.status.value == "scheduled"):
            return True
    return False
```

Relevant code from book_appointment in project/smartcare/services.py, lines 124–132:

```python
if self.data_store.has_practitioner_conflict(
    practitioner.practitioner_id,
    date_time,
):
    raise ValueError(
        'Practitioner already has a SCHEDULED appointment at this time',
    )
self.data_store.add_appointment(appointment)
return appointment
```

```
Give me three possible causes, ranked from most to least likely. For each one, explain what evidence supports it and give me one specific check that would help tell it apart from the other causes. Clearly separate what the code or tests show from what you are guessing. Use the stated requirements. Do not edit or rewrite the code, change the tests, or invent requirements.
```
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot ranked the reversed practitioner comparison first. The check was to read the practitioner comparison and compare it with the failing tests. The code uses `!=`, which means it matches a different practitioner. This explains why D1's second booking went through and why D2 was incorrectly flagged as busy. I marked this suggestion **correct** and **accepted** it because it explains both failures.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot ranked an incorrect time or status check second. The suggested check was to compare A1's stored time and status with the values used by the conflict check. Copilot reported that A1 was scheduled at the requested time. The D2 test returned `True`, which also shows that the time and status checks passed in that case. I marked this suggestion **wrong as the cause of these failures** and **rejected** it because the wrong result occurred even when those checks passed.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot ranked the booking service passing the wrong practitioner ID third. The check was to see which ID the service passes and compare that with a test that calls the data store directly. The service passes the resolved practitioner's ID, and the direct test passed `D2` to the data store and still got the wrong result. I marked this suggestion **wrong as the cause of these failures** and **rejected** it because the fault also occurs without going through the booking service.
Final human conclusion and comparison with initial hypothesis: I initially believed the conflict check was comparing practitioner IDs incorrectly. The code showed that it was checking for a different practitioner when it should check for the same one. This confirmed my initial suspicion and explained why D1 could be booked twice at the same time while D2 was incorrectly flagged as busy.

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
