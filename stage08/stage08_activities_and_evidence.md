# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [Wednesday 4:30pm - 6:30pm Group 1]
Members and UG/PG cohorts: [MastrRoshiiii -, LoserWithAGame - Liam Smilie- warunabandara11-wq]
Record owner / contribution links for each member: @MastrRoshiiii — Stage 8 write-up for Parts B–F (https://github.com/LoserWithAGame/st1-assignment-3/commit/7c56089ca9eacfb3db15f857724fe9e967bf6a59) and review of PR #29 (https://github.com/LoserWithAGame/st1-assignment-3/pull/29#pullrequestreview-5817144792).
@warunabandara11-wq — PR #29, which contains the repairs, regression tests, refactor, and test evidence. (https://github.com/LoserWithAGame/st1-assignment-3/pull/29)

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


Classification responses (1–5, each with reason): See A.1 for all five classifications and their reasons.
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: See A.2 for the expected behaviour, observed behaviour, and steps to reproduce the cancelled-history fault. See Part E, F8-01, for my initial hypothesis and planned checks.
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: See A.5 for the AssertionError in test_cancellation.py, line 41. The test expected the original appointment, but the lookup returned None. A.5 also records the call path, the FR-07 requirement, and the three possible causes with a check for each.

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: - 770ca814cf20519f2717c07e2760aec5b383efef. The requirements baseline was SmartCare A3 Requirements Baseline 2026, revision 2.
- Baseline test command / working directory / observed result / evidence: - The Stage 7 record shows python -m pytest -v, run from the project folder, with 32 passed, 0 failed at the earlier commit 2fba9705ec1baabf68b34fd0b74a200cd5bdca8b.
- Clean preparation SHA if a record-only commit followed Stage 7: Github shows that the fault commit directly followed 829e6e8. There was no seperate.
- Branch and preparer / how teammates obtained this branch: Gupta Pranav authored the preparation commit on debug/stage08. Teammates including myself obtained this branch during our tutorial by pulling the branch from Github.
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): The preparation commit only chnaged data_store.py. 
- Prepared faulty-state commit SHA: d666a560fbc6de3f56636aaf5b0a35f13ffb70ba
- Preparation or recovery issues and resolution, if any: No preparation or recovery issues were reported by @LoserWithAGame.
- Initial prepared full-suite command / result / key failures: I ran python -m pytest -v from the project folder on debug/stage08. It showed 5 failed, and 29 passed. Two of the failures invollved cancelled appointment history and three involved practitioner booking conflicts.  

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: Cancelling appointment A1 returned the original appointment and changed its status to CANCELLED. Looking it up afterward returned None.
- Expected behaviour and requirement: FR-07 requires cancelled appointment history to be retained. Looking up A1 after cancellation should return the same appointment with status CANCELLED.
- Minimal synthetic reproduction steps: Register a sample patient and practitioner, book appointment A1, cancel it, then call store.find_appointment('A1').
- Meaningful failing test path/name and exact relevant failure: test_cancel_appointment_returns_retained_cancelled_object failed at [test_cancellation.py, line 41 (line 41) project/tests/test_cancellation.py:41)]. The check assert store.find_appointment('A1') is appointment raised an AssertionError because the lookup returned None.
- Human hypothesis and intended checks: see E, F8-01. (I plan to compare list_appointments() with find_appointment('A1') after cancellation. If A1 still appears in the list but the lookup returns None, I would inspect the lookup code to see why it skips that record. If A1 is also missing from the list, I would check whether cancellation removes it.)
- Supported root cause and inspected code/runtime evidence: find_appointment() skipped records with status CANCELLED. The original test showed that cancellation returned the same appointment with its status set to CANCELLED, but the lookup returned None. A second cancellation therefore raised LookupError before it could reach the check that raises ValueError.
- Smallest justified fix / diff / why other behaviour is preserved: I reviewed Waruna’s repair. He removed and appointment.status.value != "cancelled" from find_appointment(). This lets the lookup return the original appointment by ID even after it has been cancelled. Invalid IDs still raise ValueError, unknown IDs still return None from the data store, and the existing cancellation check still rejects a second cancellation with ValueError.
- Repair SHA / focused verification result: 2fdc483097fd8902b4dc1c4f74042cc5327e11be. Waruna’s focused verification recorded 2 passed. The first test confirmed that the original cancelled appointment could still be found. The second confirmed that cancelling it again raised ValueError and preserved its history.

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: The system allowed a second appointment for the same practitioner at the same time. It also incorrectly reported a conflict for a different practitioner at that time.
- Expected behaviour and requirement: FR-05 requires the system to prevent double booking a practitioner. A second booking for the same practitioner at the same time should raise ValueError.
- Minimal synthetic reproduction steps: Book appointment A1 for practitioner D1 at 9:00 am. Try to book a second appointment for D1 at the same time. It should be rejected. Then check the same time for practitioner D2, who has no booking. The system should report no conflict.
- Meaningful failing test path/name and exact relevant failure: In [project/tests/test_services.py (line 155)], test_practitioner_conflict_prevents_appointments books A1 with practitioner D1 on line 154, then attempts to book A2 with the same practitioner at the same time on lines 155–156. The second booking should raise ValueError, but it went through, so pytest reported Failed: DID NOT RAISE <class 'ValueError'>. In the same file, test_different_practitioner_books_appointment checks on line 166 that D2 has no conflict when D1 is booked at that time. The check returned True instead of False, so pytest reported AssertionError: assert True is False. In [project/tests/test_starter.py (line 127)], test_conflict_rule_and_different_practitioner also expects ValueError on lines 127–128 when a second appointment is booked with D1 at the same time. Pytest reported Failed: DID NOT RAISE <class 'ValueError'> at line 127, and the test stopped before reaching the check that a booking with D2 succeeds.
- Human hypothesis and intended checks: see E, F8-02. (I plan to book D1 at 9 am, then run the conflict check directly for D1 and D2 at 9am. If the direct check gives the wrong results, Ill inspect the check itself. If it gives the right results, Ill check which ID the booking service passes in.)
- Supported root cause and inspected code/runtime evidence: In has_practitioner_conflict(), the code used != to compare practitioner IDs. That made it look for a booking with a different practitioner. This explains why the test allowed D1 to be booked twice at the same time but incorrectly reported a conflict for D2.
- Smallest justified fix / diff / why other behaviour is preserved: Waruna changed appointment.practitioner.practitioner_id != practitioner_id to appointment.practitioner.practitioner_id == practitioner_id. The check now matches the same practitioner. The checks for the appointment time, SCHEDULED status, and optional excluded appointment ID stayed the same.
- Repair SHA / focused verification result: 2fdc483097fd8902b4dc1c4f74042cc5327e11be. Waruna’s focused verification recorded 3 passed. The tests confirmed that a second booking for the same practitioner at the same time is rejected and that a different practitioner can still take a booking at that time.

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
Actual prompt / output reference and member: (@MastrRoshiiii) Help me investigate F8-01, the cancelled appointment history fault, using the prepared faulty commit d666a56.

To reproduce it, register a sample patient and practitioner, book appointment A1, cancel it, then call store.find_appointment('A1').

Expected behaviour under FR-07: the cancelled appointment should remain stored and the lookup should return the original appointment with its status set to CANCELLED. Under FR-06, a second cancellation should be rejected with ValueError.

Observed behaviour: the first cancellation returns the original appointment and sets its status to CANCELLED, but the lookup returns None. A second cancellation raises LookupError("Appointment not found") instead of ValueError.

Failing tests in project/tests/test_cancellation.py:
- test_cancel_appointment_returns_retained_cancelled_object, line 41: AssertionError because store.find_appointment('A1') returned None instead of the original appointment.
- test_repeated_cancellation_is_rejected_and_retains_history, line 98: expected ValueError, but got LookupError("Appointment not found").

My initial hypothesis and planned check from Part E:
I believe the lookup might be skipping cancelled appointments. I plan to compare list_appointments() with find_appointment('A1') after cancellation. If A1 still appears in the list but the lookup returns None, I’ll inspect why the lookup skips it. If A1 is missing from the list too, I’ll check whether cancellation removes it.

Relevant code from data_store.py:

```python
def find_appointment(self, appointment_id: str) -> Appointment | None:
    if not isinstance(appointment_id, str) or not appointment_id.strip():
        raise ValueError("Appointment ID cannot be blank")
    for appointment in self.list_appointments():
        if (appointment.appointment_id == appointment_id.strip()
                and appointment.status.value != "cancelled"):
            return appointment
    return None

def list_appointments(self) -> list[Appointment]:
    return list(self._appointments.values())
```

Relevant code from services.py, with docstrings omitted:

```python
def find_appointment(self, appointment_id: str) -> Appointment:
    appointment = self.data_store.find_appointment(appointment_id)
    if appointment is None:
        raise LookupError('Appointment not found')
    return appointment

def cancel_appointment(self, appointment_id: str) -> Appointment:
    appointment = self.find_appointment(appointment_id)
    appointment.cancel()
    return appointment
```

Give me three possible causes, ranked from most to least likely. For each one, explain what evidence supports or weakens it and give me one specific check that would distinguish it from the other causes. Clearly separate what the supplied code and test results show from what still needs checking. Suggest checks for me to run. Do not run commands, edit or rewrite code, change tests, or invent requirements.

1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot ranked the lookup skipping cancelled appointments first. The suggested check was to compare `list_appointments()` with `find_appointment('A1')` after cancellation. The original test showed that cancellation returned the same appointment with status `CANCELLED`, but the lookup returned `None`. The lookup code had a condition that skipped cancelled appointments. After that condition was removed, both focused tests passed. I marked this suggestion **correct** and **accepted** it because it explains both failures.
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: Copilot ranked deletion or replacement of the appointment second. The suggested check was to see whether the original A1 object still appeared in `list_appointments()` after cancellation. The first cancellation returned the original object, and the service code showed no step that removed or replaced it. The two focused tests passed after changing only the lookup for this fault. I marked this suggestion **wrong as the cause** and **rejected** it because fixing the lookup was enough to restore the expected behaviour.
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason:  Copilot ranked the order of the cancellation steps third. The suggested check was to compare calling `appointment.cancel()` directly with cancelling through the service a second time. The traceback showed that the service raised `LookupError` during lookup, before it reached `appointment.cancel()`. After the lookup was fixed, the repeated cancellation test passed with the expected `ValueError`. I marked this suggestion **partly correct** and **modified** it. The order explains where the wrong error came from, but the fix belongs in the lookup.

### F8-02 Copilot review
Actual prompt / output reference and member: (@MastrRoshiiii) Help me investigate F8-02, the practitioner booking conflict, on the debug/stage08 branch.

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

The Stage 8 defects were reproduced and repaired in a separate local copy of the project. Testing was performed from the `project/` directory using Python 3.13.5 and pytest 9.0.2. The results below are local verification evidence; the GitHub changes still require team review and integration testing.

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artifact reference |
|---|---|---|---|
| F8-01 before repair | Prepared Stage 8 commit `7c56089`. Appointment lookup incorrectly excluded cancelled records. | `cd project && python -m pytest -q tests/test_cancellation.py` | Two relevant tests failed. See [F8-01 before](verification/01_F8-01_before.txt). |
| F8-01 after repair | Removed the cancelled-status restriction from `find_appointment()`, retaining ID validation. Repair commit SHA to be confirmed. | `cd project && python -m pytest -q tests/test_cancellation.py` | Two previously failing tests passed in the focused local verification. See [F8-01 after](verification/03_F8-01_after.txt). |
| F8-02 before repair | Prepared Stage 8 commit `7c56089`. Practitioner conflict logic incorrectly used `!=` instead of `==`. | Focused practitioner-conflict tests from `project/` | Three tests failed. See [F8-02 before](verification/02_F8-02_before.txt). |
| F8-02 after repair | Changed the practitioner ID comparison to `==`, keeping the existing time and status checks. Repair commit SHA to be confirmed. | Focused practitioner-conflict tests from `project/` | All three previously failing tests passed in local verification. See [F8-02 after](verification/04_F8-02_after.txt). |
| Full suite after both repairs, before refactor | Both functional repairs applied. Original tests were preserved, with three additional regression tests added separately. | `cd project && python -m pytest -q` | All 34 original tests passed. With three additional regression tests, 37 passed. See [original suite](verification/05_repaired_full_suite_before_refactor.txt) and [extended suite](verification/06_extended_full_suite_before_refactor.txt). |

**How the assertions detect defects:** The F8-01 tests verify that cancelled appointments remain retrievable and that repeated cancellation raises the expected error. The F8-02 tests verify that the same practitioner cannot be booked twice at the same time, while different practitioners can be booked simultaneously.

**Unrelated failures investigated:** The original prepared suite produced 5 failures and 29 passes. All five failures related to F8-01 and F8-02. No additional failures were reported in that local run. See [initial test results](verification/00_prepared_full_suite.txt).

**Verification limitation:** These results were produced locally. The repaired GitHub branch must be tested again and its final commit SHA recorded before integration is considered complete.


## H. Refactoring decision and before/after verification

**Smell and exact location:** In `project/smartcare/data_store.py`, the `has_practitioner_conflict()` function used the string comparison `appointment.status.value == "scheduled"`. This duplicates the value already defined by `AppointmentStatus.SCHEDULED`.

**Small structural change and justification:** Replaced the string comparison with `appointment.status is AppointmentStatus.SCHEDULED`. This improves readability and uses the existing enum without changing the booking requirements.

**External behaviour to preserve:** A practitioner cannot have two scheduled appointments at the same time. Different practitioners can be booked at the same time. Cancelled appointments must not cause booking conflicts.

**Before-refactor verification:** After repairing both Stage 8 defects and adding three regression tests, the local full test suite returned 37 passed. Evidence: [Before-refactor test results](verification/06_extended_full_suite_before_refactor.txt).

**Actual refactoring:** Changed the status comparison in `has_practitioner_conflict()` to use the existing enum. The change was made separately from the original bug repairs on branch `fix/stage08-waruna-repairs`. The GitHub refactoring commit SHA should be recorded after confirming the commit.

**After-refactor verification:** Local testing returned 14 passed for the focused tests and 37 passed for the full suite. The application demonstration also completed successfully.

Evidence:
- [Focused test results](verification/07_after_refactor_focused.txt)
- [Full test results](verification/08_after_refactor_full_suite.txt)
- [Application demonstration](verification/09_main_demo.txt)

**Decision and conclusion:** Accepted in local verification because the refactoring preserved the expected application behaviour and all tests passed. Final acceptance requires teammate review and another test run on the integrated GitHub version.


## I. Git, human review and integration

**Issues and owners:** F8-01 concerns retaining cancelled appointment history (FR-07), while F8-02 concerns preventing practitioner booking conflicts (FR-05). @MastrRoshiiii documented the diagnoses in Sections C–F. @warunabandara11-wq contributed the proposed repairs, regression tests and verification evidence. F8-01, F8-02 and the status check refactor were handled in PR #29. Separate Stage 8 issue links are were not used in stage 8. @MastrRoshiiii documented the diagnoses and reviewed the PR. @warunabandara11-wq implemented both repairs and the refactor, added regression tests, and recorded verification evidence. Formal ownership of parts A-F, @MastrRoshiiii, parts G-L, @warunabandara11-wq

**Branches and checkpoints:** The prepared Stage 8 branch is `debug/stage08`, with preparation evidence recorded in Section B and the documented Stage 8 commit `7c56089`. The repairs, regression tests and refactoring were added on `fix/stage08-waruna-repairs`.
- Prepared faulty commit — d666a560fbc6de3f56636aaf5b0a35f13ffb70ba
- Snapshot used for before-repair tests — 7c56089ca9eacfb3db15f857724fe9e967bf6a59
- Both repairs — 2fdc483097fd8902b4dc1c4f74042cc5327e11be
- Additional regression tests — f9f04e90a229a6b6ddd1e7d53fd86f44c8085452
- Status-check refactor — b8c165c3ac6ddc1c5aa57883339223f8d5909531
- PR #29 merge into debug/stage08 — 5e5637ea3e59f8bfe081b703da865121e7c2bca1

**Pull request and reviewer:** PR #29 — Stage 8: Debugging Repairs, Regression Tests and Evidence was opened by @warunabandara11-wq and reviewed by @MastrRoshiiii.

**Human review feedback and Copilot comparison:** I approved Waruna’s changes in PR #29 so they could go through final editing and review before merging to main. My GitHub review recorded the approval. The technical comparison is recorded in Part F. Copilot suggested that the lookup was skipping cancelled appointments and that the practitioner comparison was reversed. Waruna’s changes addressed both causes, and the focused tests passed after the repairs. https://github.com/LoserWithAGame/st1-assignment-3/pull/29#pullrequestreview-5817144792

**Review approval and merge evidence:** - @MastrRoshiiii approved PR #29 before merging it into debug/stage08 at commit 5e5637ea3e59f8bfe081b703da865121e7c2bca1.
**Integrated code and team retesting:** Pending. Local verification produced 37 passing tests after the repairs and refactoring, with results recorded in `stage08/verification/`. After integration, the team must pull the updated code, run `python -m pytest -q` from `project/`, and record the final commit SHA and actual test results.

**Evidence-only commits:** The verified debug/stage08 commit was 5e5637e, which passed all 37 tests. Commit 8450428 added the verification logs. Commits a07dfd5, b4b8a01 and c9a9619 updated the Stage 8 evidence document only. The final verified main SHA and any evidence-only commit made after that test run will be recorded at submission.

**Member contributions:**
- @MastrRoshiiii: Stage 8 preparation, initial failure analysis, defect diagnosis, human hypotheses and Copilot review documentation in Sections A–F.
- @warunabandara11-wq: Stage 8 functional corrections, additional regression tests, local verification evidence, refactoring and documentation in Sections G–H and the remaining assigned sections.

Other members' contributions and final review activities will be recorded using verified GitHub evidence.

**Current status:** PR #29 was reviewed, approved, and merged into debug/stage08. @MastrRoshiiii ran python -m pytest -q from the project folder at commit 5e5637ea3e59f8bfe081b703da865121e7c2bca1. The result was 37 passed in 0.06 seconds using Python 3.14.7 and pytest 8.3.5. The final merge into main and retest there are pending.


## J. Required reflections


1. **Which Copilot diagnosis appeared convincing but lacked evidence?** The suggestion that the booking problem was caused by incorrect time or status checks initially appeared plausible. However, the tests showed those conditions were already satisfied. The actual problem was the practitioner ID comparison, which used `!=` instead of `==`.

2. **What evidence changed your group's view?** The initial test results showed five failures. Inspecting the code and running focused tests identified two problems: cancelled appointments were excluded from lookup, and practitioner conflicts were checked against different practitioners instead of the same practitioner. These findings provided stronger evidence than the initial suggestions.

3. **How did regression tests protect the refactoring?** Regression tests checked that cancelled appointments remained retrievable, conflicting bookings were rejected, and different practitioners could still be booked at the same time. After replacing the string-based status comparison with the enum, all 14 focused tests and 37 full-suite tests passed in local verification. This provided evidence that the refactoring preserved the expected behaviour.



## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: First reproduce the failure, examine the error message and traceback, review the requirements, and identify the possible cause before changing the code.

2. Where should expected behaviour come from during debugging?

Response: Expected behaviour should come from the approved requirements, acceptance criteria and system specifications, rather than assumptions about how the code should work.

3. What is a debugging hypothesis?

Response: A debugging hypothesis is a testable explanation of why a problem occurs. Engineers investigate it using code inspection and testing.

4. What is a regression test and why is it retained?

Response: A regression test checks that previously working functionality still behaves correctly after changes. It is retained to prevent the same bug from returning.

5. What is meant by root cause?

Response: The root cause is the underlying problem in the code or system that produces the failure. Fixing it addresses the actual problem rather than just its symptoms.

6. What is refactoring?

Response: Refactoring means improving the internal structure or readability of code without changing its intended external behaviour.

7. What is a swallowed exception?

Response: A swallowed exception occurs when an error is caught but ignored or not handled properly. This can hide failures and make debugging difficult.

8. What is a code smell?

Response: A code smell is a sign of potentially poor code structure, such as duplicated logic or unnecessary complexity. It may indicate that the code needs improvement.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: Copilot suggestions should be treated as possible explanations, not confirmed facts. Engineers should verify them against the requirements, actual code and test results before accepting them.

10. What is the Stage 8 engineering rule?

Response: Investigate failures using evidence before changing code, make minimal justified repairs, verify them using regression tests, refactor only after achieving a passing baseline, and obtain human review before integration.



## L. Completion and handover

- [x] Existing project, earlier tests and stage records preserved. The Stage 8 changes were made on a separate branch without modifying earlier stage files.
- [x] Passing Stage 7 SHA and safe preparation details recorded completely. The Stage 7 baseline is documented in Section B.
- [x] Both defects reproduced with meaningful failing tests. The original prepared suite recorded 5 failures and 29 passes.
- [x] Both human hypotheses recorded before Copilot and actual suggestions evaluated with evidence. Sections E and F contain the available analysis.
- [x] Supported causes and minimal repairs explained. Focused and full local regression results are recorded in Section G.
- [x] One genuine refactor verified locally with passing before-and-after tests. The full suite returned 37 passed following the refactoring.
- [x] Human pull request review, feedback resolution and integrated retest recorded.
- [x] Tutorial activities, three reflections and ten formative responses completed in Sections A, J and K.
- [x] Local recovery metadata and the teaching preparation utility excluded from the proposed changes.
- [ ] Same project and full suite ready for Stage 9 following Stage 8 integration, final verification and recording.

**Verified integrated code SHA / result:** Pending. Local testing after the repairs and refactoring returned 37 passed using Python 3.13.5 and pytest 9.0.2. These results do not replace final integrated verification. (Still required, pending merge to main)

**Submitted SHA and evidence-only difference:** Pending final pull request review, merge and submission. The verification logs and documentation were prepared separately from the functional code repairs. (Still required, pending merge to main)

**Unresolved issues / owner / next action:**

- @MastrRoshiiii: Confirm the remaining preparation and Copilot evidence in Sections B–F. (COMPLETE)
- @warunabandara11-wq: Submit the Stage 8 repairs, regression tests, refactoring and supporting evidence through a pull request. (COMPLETE)
- Team reviewer: Review the code changes, tests and evidence, and provide feedback before approval. (COMPLETE - @MastrRoshiiii)
- Group integrator: Merge the approved changes, rerun the full test suite and record the final integrated commit SHA. (@MastrRoshiiii merged PR #29 into debug/stage08 at 5e5637ea3e59f8bfe081b703da865121e7c2bca1 and ran python -m pytest -q from project. The result was 37 passed in 0.06 seconds).

**Handover note:** Stage 8 identified two defects involving cancelled appointment history and practitioner booking conflicts. Both defects were corrected and locally verified. Three additional regression tests were added, and a small status-check refactoring preserved the required behaviour. The full local test suite passed 37 tests. The project must receive human review, integration testing and final evidence confirmation before Stage 8 is considered fully complete or handed over to Stage 9.

