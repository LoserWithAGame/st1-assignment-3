# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | Register a new patient using a unique ID (`P1`) and name (`Alex Example`). | Attempt to register another patient using the same ID (`P1`). | The first registration returns the stored patient object. A duplicate ID raises `ValueError`, and the original record remains unchanged. |
| FR-05 Prevent practitioner conflict | [Appointment is rejected when Practitioner ('D2') and Time (2026, 10, 1, 9) is the same as an existing appointment.] | [Appointment is booked when Practitioner ('D2') and Time (2026, 10, 1, 9) are the same as an existing appointment.] | [Key Assertion: "with pytest.raises(ValueError): appointment_service.book_appointment('A2', 'P1', 'D1', when)", which returns a ValueError if there is a duplicate appointment.] |
| FR-06 Cancel appointment | [Cancel an exisiting SCHEDULED appointment using its ID] | [Attempt to cancel a COMPLETED or already CANCELLED appointment.] | [The successful call returns the original object with `status is AppointmentStatus.CANCELLED`, the invalid transition raises `ValueError` and leaves the status unchanged.] |
| FR-07 Retain cancelled history | [Cancel an appointment and retrieve it again from the shared store using the same ID] | [Attempt to repeat a cancellation of the same appointment with the same ID] | [`store.find_appointment('A1') is appointment`, and the retained object remains `CANCELLED` even after the rejected repeated cancellation.] |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Weak/unclear]  Why: [Always passes, even when the code is wrong.]

`assert appointment is not None`
Judgement: [Weak/unclear]  Why: [Checks that an appointment exists, but not whether its details are correct.]

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour]  Why: [Checks that the appointment is marked as cancelled. It does not check whther it is still retained.]

`assert len(results) > 0`
Judgement: [Weak/unclear]  Why: [Checks whether there is at least one result, but does not check is the results are correct.]

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour]  Why: [Checks that finding (A1) returns the same appointment object. It does not check its status.]

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract:

|Scenario|Input or starting state|Expected result|Supporting contract|
|---|---|---|---|
|Blank Identifiers|search using patient_id: "" (empty string)|Raise ValueError, with message saying this field cannot be empty.|The patient lookup requires IDs to be non-blank strings.|
|Whitespace-only names|Attempting to register a new user with name as: "   " <- empty space OR "\n\n" <- new line|ValueError is raised and no new patient is stored.|patient name is a requirement so it must contain non whitespace text.|
|Same-time practitioner bookings|IF  A1 <- appointment is SCHEDULED for pracitioner D1 at 10:00 AM. Try booking A2 for D1 at the same time and date.|ValueError is raised, A2 is not stored and A1 remains unchainged and still booked.|Fr-05 rejects a bookinjg if that doctor already has a SCHEDULED appointment at the same time.|
|Cancelled appointments|Cancel SCHEDULED appointment A1, then attempt to find it|reutrn that same appointment but with cancelled status instead of booked. Hisotry needs to remain|FR-07 retain cancelled history|
|Invalid status transitions|attempting to cancel a finished appointment.|Should give a ValueError and leave the appointment unchanged.|Only SCHEDULED appointments can be cancelled.|

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | [By checking an object is not None only proves that something was returned. it could still therefore be the wrong patient] | [Register a patient, look up their ID and verify that the results is the same exact registered patient that was registered.] |
| 2 | [An object being not None does not prove the cancellation worked or history was retained.] | [Cancel a SCHEDULED appointment, then check its status is CANCELLED and that the lookup returns the same previusly stored appointment.] |
| 3 | [Assert True checks nothing abuot the program's result, so incorrect bnehaviour could still pass if not checking other paremiters.] | [Attempt a booking that connflicts with a current appointment for the same practitioner at the same date and time. Check that a ValueError is raised and no new appointments were stored as a result.] |
| 4 | [SMS notifications are not part of requirment scope of the program features. So its checking invented behaviour.] | [Reject the sms test. Change to an alternative test that validates the booking appointment status was changed to SCHEDULED and the actual registered patient and pratitioner objects exist.] |
| 5 | [This also tests a feature called SMS notification that is assumed to exist. Passing this test does not establish that the rules are working correctly.] | [Reject the SMS test. An alternative test could be checking that repeated cancellations raises ValueError and leaves the cancelled appointment unchanged and retrievable as requested.] |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[Code Coverage is not a measure of a functional program, as the code coverage test model outlines specific lines of code, functions, or classes to test. Testing each individually means that collaboratively each could be unfunctional. The program needs to be tested in this method as well as a whole to see the best results.]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| [FR-07 Retain cancelled history] | [Cancelling an appointment must not delete or replace it.] | [TEST-FR07-01] | [Service-level unit test] | [test_cancellation.py::test_cancel_appointment_returns_retained_cancelled_object/tests/test_cancellation.py] | [The cancelled appointment remains retrievable from the store as the same object.] | [Passed] | [Student Authored] |
| [FR-07 Retain cancelled history] | [A rejected repeated cancellation must not remove or replace the cancelled appointment.] | [TEST-FR07-02] | [Retained history service-level unit test] | [test_cancellation.py::test_repeated_cancellation_is_rejected_and_retains_history/tests/test_cancellation.py] | [After the rejected second cancellation, the same CANCELLED object remains retrievable and remains the only stored appointment.] | [Passed] | [Student Authored] |
| [FR-06 Cancel appointment] | [A known SCHEDULED appointment can be cancelled using its ID.] | [TEST-FR06-01] | [Service-level unit test] | [test_cancellation.py::test_cancel_appointment_returns_retained_cancelled_object/tests/test_cancellation.py] | [The service returns the original appointment and changes its status to CANCELLED.] | [Passed] | [Student Authored] |
| [FR-06 Cancel appointment] | [A valid but unknown appointment ID must be rejected without changing existing appointments.] | [TEST-FR06-02] | [Negative service-level unit test] | [test_cancellation.py::test_unknown_appointment_raises_lookup_error_and_preserves_state/tests/test_cancellation.py] | [The service raises LookupError, the existing appointment remains SCHEDULED and the stored list remains unchanged.] | [Passed] | [Student Authored] |
| [FR-06 Cancel appointment] | [Blank, whitespace-only and non-text appointment IDs must be rejected without changing state.] | [TEST-FR06-03] | [Boundary and negative parametrised test] | [test_cancellation.py::test_invalid_appointment_id_raises_value_error/test/test_cancellation.py] | [Empty text, whitespace, None and 123 each raise ValueError. The existing appointment remains SCHEDULED and stored.] | [Passed — four parametrised cases] | [Student Authored] |
| [FR-06 Cancel appointment] | [Only a SCHEDULED appointment may be cancelled; a second cancellation must be rejected.] | [TEST-FR06-04] | [Invalid-transition service-level unit test] | [test_cancellation.py::test_repeated_cancellation_is_rejected_and_retains_history/tests/test_cancellation.py] | [The first cancellation succeeds, the second raises ValueError and the appointment remains CANCELLED.] | [Passed] | [Student Authored] |
| [FR-06 Cancel appointment] | [A COMPLETED appointment cannot be cancelled, and a failed attempt must leave it unchanged.] | [TEST-FR06-05] | [Invalid-transition service-level unit test] | [test_cancellation.py::test_completed_appointment_cannot_be_cancelled/tests/test_cancellation.py] | [The service raises ValueError. The appointment remains COMPLETED, retrievable and stored as the same object.] | [Passed] | [Student Authored] |
| [FR-06 Cancel appointment] | [A SCHEDULED appointment can be cancelled, and a repeated cancellation is rejected.] | [TEST-FR06-S01] | [Domain unit test] | [test_starter.py::test_domain_cancellation_and_guard/tests/test_starter.py] | [The first cancellation changes the status to CANCELLED. A second cancellation raises ValueError, and the status remains CANCELLED.] | [Passed] | [Supplied] |
| [FR-05 Prevent practitioner conflict] | [Appointments with duplicate times and Practitioners are not booked.] | [TEST-FR05-01] | [Service Level Unit Test] | [test_services.py::test_practitioner_conflict_prevents_appointments/tests/test_services.py] | [The service raises a ValueError if there is a duplicate appointment] | [Passed] | [Mixed] |
| [FR-05 Prevent practitioner conflict] | [Appointments with the different Practitioner and same Times are Booked.] | [TEST-FR05-02] | [Service Level Unit Test] | [test_services.py::test_different_practitioner_books_appointment/tests/test_services.py] | [The service is asserted if there is a no conflict.] | [Passed] | [Student Authored] |
| [FR-05 Prevent practitioner conflict] | [Appointments with the same Practitioner and Different Times are Booked.] | [TEST-FR05-03] | [Service Level Unit Test] | [test_services.py::test_different_time_books_appointment/tests/test_services.py] | [The service is asserted if there is a no conflict.] | [Passed] | [Student Authored] |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| [TEST-FR07-01] | [FR-07 Retain cancelled history] | [Positive] | [Cancelling an appointment must not delete or replace it.] | [The cancelled appointment remains retrievable from the store as the same object.] | [The cancelled appointment remains retrievable from the store as the same object.] | [Not Applicable] |
| [TEST-FR07-02] | [FR-07 Retain cancelled history] | [A rejected repeated cancellation must not remove or replace the cancelled appointment.] | [Positive] | [After the rejected second cancellation, the same CANCELLED object remains retrievable and remains the only stored appointment.] | [After the rejected second cancellation, the same CANCELLED object remains retrievable and remains the only stored appointment.] | [Not Applicable] |
| [TEST-FR06-01] | [FR-06 Cancel appointment] | [A known SCHEDULED appointment can be cancelled using its ID.] | [Positive] | [The service returns the original appointment and changes its status to CANCELLED.] | [The service returns the original appointment and changes its status to CANCELLED.] | [Not Applicable] |
| [TEST-FR06-02] | [FR-06 Cancel appointment] | [A valid but unknown appointment ID must be rejected without changing existing appointments.] | [Positive] | [The service raises LookupError, the existing appointment remains SCHEDULED and the stored list remains unchanged.] | [The service raises LookupError, the existing appointment remains SCHEDULED and the stored list remains unchanged.] | [Not Applicable] |
| [TEST-FR06-03] | [FR-06 Cancel appointment] | [Blank, whitespace-only and non-text appointment IDs must be rejected without changing state.] | [Boundary] | [Empty text, whitespace, None and 123 each raise ValueError. The existing appointment remains SCHEDULED and stored.] | [Empty text, whitespace, None and 123 each raise ValueError. The existing appointment remains SCHEDULED and stored.] | [Not Applicable] |
| [TEST-FR06-04] | [FR-06 Cancel appointment] | [Only a SCHEDULED appointment may be cancelled; a second cancellation must be rejected.] | [Positive] | [The first cancellation succeeds, the second raises ValueError and the appointment remains CANCELLED.] | [The first cancellation succeeds, the second raises ValueError and the appointment remains CANCELLED.] | [Not Applicable] |
| [TEST-FR06-05] | [FR-06 Cancel appointment] | [A COMPLETED appointment cannot be cancelled, and a failed attempt must leave it unchanged.] | [Positive] | [The service raises ValueError. The appointment remains COMPLETED, retrievable and stored as the same object.] | [The service raises ValueError. The appointment remains COMPLETED, retrievable and stored as the same object.] | [Not Applicable] |
| [TEST-FR06-S01] | [FR-06 Cancel appointment] | [A SCHEDULED appointment can be cancelled, and a repeated cancellation is rejected.] | [Positive] | [The first cancellation changes the status to CANCELLED. A second cancellation raises ValueError, and the status remains CANCELLED.] | [The first cancellation changes the status to CANCELLED. A second cancellation raises ValueError, and the status remains CANCELLED.] | [Not Applicable] |
| [TEST-FR05-01] | [FR-05 Prevent practitioner conflict] | [Appointments with duplicate times and Practitioners are not booked.] | [Positive] | [The service raises a ValueError if there is a duplicate appointment.] | [The service raises a ValueError if there is a duplicate appointment.] | [Not Applicable] |
| [TEST-FR05-02] | [FR-05 Prevent practitioner conflict] | [Appointments with different Practitioner and same Times are Booked.] | [Positive] | [The service is asserted if there is a no conflict.] | [The service is asserted if there is a no conflict.] | [Not Applicable] |
| [TEST-FR05-03] | [FR-05 Prevent practitioner conflict] | [Appointments with the same Practitioner and Different Times are Booked.] | [Positive] | [The service is asserted if there is a no conflict.] | [The service is asserted if there is a no conflict.] | [Not Applicable] |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [TEST-FR05-01] | [('A1', 'P1', 'D1', when)] | [Practitioner Conflict Prevents Appointments] | ["with pytest.raises(ValueError): appointment_service.book_appointment('A2', 'P1', 'D1', when)"] | [This asserts that when the Practitioner has a conflicting appointment it will raise a ValueError.] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [TEST-FR05-03] | [Test that appointments with a different time but same practitioner cause no conflicts] | [test_services.py::test_different_time_books_appointment()] | [Passed] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [TEST-FR05-02] | [Tests that appointments with different practitioner but same time causes no conflict.] | [Appointments with different Practitioner and same Times are Booked.] | [test_services.py::test_different_practitioner_books_appointment()] | [Passed] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [The first registration returns the stored patient object. A duplicate ID raises `ValueError`, and the original record remains unchanged.] | [(`P1`)] | [Attempt to register another patient using the same ID (`P1`).] | [FR-01] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [FR-05]
Acceptance criterion: ["Appointment is rejected when Practitioner ('D2') and Time (2026, 10, 1, 9) is the same as an existing appointment"]
Behaviour to test: [Prevent practitioner conflict]
Human-first test idea/categories: [Appointments with duplicate times and Practitioners are not booked. Appointments with different Practitioner and same Times are Booked. Appointments with the same Practitioner and Different Times are Booked.]
Prompt and purpose: [https://github.com/copilot/share/0247419e-40e0-80a4-a142-960f006f613f]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [Valid: no existing appointment.]
- What it claims to verify: [A booking at the criterion’s practitioner and time can be made when no conflicting appointment exists.]
- Requirement trace: [Book A1 for P1, practitioner D2, at WHEN.]
- Assertion quality: [Booking returns an appointment with ID A1, and store.find_appointment("A1") returns that appointment.]
- Human critique: [This verifies that an appointment can be booked in the first place, which is extremely important to testing conflicting practitioners.]
- Decision: [Modify]
- Reason: [This is already verified in other tests, as the tests would not function without it.]
- Final test reference if accepted/modified: [test_services.py::test_practitioner_conflict_prevents_appointments/tests/test_services.py]
- Actual verification result: [none: testing software broken.]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [Invalid: exact conflict]
- What it claims to verify: [A booking is rejected when practitioner D2 and time (2026, 10, 1, 9) match an existing appointment.]
- Requirement trace: [First book A1 for D2 at WHEN; then attempt A2 for D2 at WHEN.]
- Assertion quality: [The second call raises ValueError; A1 remains findable and A2 is absent from the store.]
- Human critique: [Good assertion, tests that duplicate appointments are not booked.]
- Decision: [Accept]
- Reason: [Testing that the conflicting appointments does not book is the main requirement.]
- Final test reference if accepted/modified: [test_services.py::test_practitioner_conflict_prevents_appointments/tests/test_services.py]
- Actual verification result: [none: testing software broken.]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [Boundary: same time, different practitioner]
- What it claims to verify: [The repository’s Stage 12 demo criterion says the same time with a different practitioner is allowed; this distinguishes a practitioner conflict from a time-only conflict.]
- Requirement trace: [Book A1 for D1 at WHEN, then book A2 for D2 at WHEN.]
- Assertion quality: [Both bookings succeed and are findable.]
- Human critique: [Good assertion, testing whether the appointment can be booked with a different practitioner at the same time]
- Decision: [Accept]
- Reason: [Great test to ensure functionality.]
- Final test reference if accepted/modified: [test_services.py::test_different_practitioner_books_appointment()]
- Actual verification result: [none: testing software broken.]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [Boundary: same practitioner, different time]
- What it claims to verify: [The stated conflict is for the same practitioner and same time; a different time should not be treated as that exact conflict.]
- Requirement trace: [Book A1 for D2 at WHEN, then book A2 for D2 at datetime(2026, 10, 1, 10).]
- Assertion quality: [Both bookings succeed and are findable.]
- Human critique: [Good assertion, testing different times with the same practitioner is extremely important.]
- Decision: [Accept]
- Reason: [Great test to ensure functionality.]
- Final test reference if accepted/modified: [test_services.py::test_different_time_books_appointment()]
- Actual verification result: [none: testing software broken.]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [Valid: no existing appointment.]
Why was it weak? [This test verifies a test that is ingrained in every other test for this Functional Requirement.]
How did you strengthen it? [I got rid of it entirely]
Accepted / modified / rejected test decisions and evidence: [Modified, as I embedded this element in every other test for this Functional Requirement.]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [code used to test: python -m pytest -v] | [project/] | [2fba9705ec1baabf68b34fd0b74a200cd5bdca8b] | [32 passed] | [0 Failed] | [No failure observed] | [Current baseline: All collected cancellation, patient/practitioner lookup and starter test cases passed.] | [baseline run using puthon 3.14.7 and pytest 8.3.5. All 32 collected cases passed. REPLACE THIS PART -> PENDING comment of 32 passed tests to the comment section when uploading. then link that comment here <- pending] |

Individual test runs and changed-order independence evidence

|test|Command used|Results|link pending|
|---|---|---|---|
|Individual patient lookup|python -m pytest tests/test_services.py::test_find_patient_returns_registered_patient -v|1 Passed, 0 failed|https://github.com/LoserWithAGame/st1-assignment-3/pull/15#issue-6094613216|
|Individual cancellation|python -m pytest tests/test_cancellation.py::test_cancel_appointment_returns_retained_cancelled_object -v|1 passed, 0 failed|https://github.com/LoserWithAGame/st1-assignment-3/pull/15#issue-6094613216|
|Patient lookup followed by cancellation|python -m pytest tests/test_services.py::test_find_patient_returns_registered_patient tests/test_cancellation.py::test_cancel_appointment_returns_retained_cancelled_object -v|2 passed, 0 failed|https://github.com/LoserWithAGame/st1-assignment-3/pull/15#issue-6094613216|
|CAncellation followed by patient lookup|python -m pytest tests/test_cancellation.py::test_cancel_appointment_returns_retained_cancelled_object tests/test_services.py::test_find_patient_returns_registered_patient -v|2 passed, 0 failed|https://github.com/LoserWithAGame/st1-assignment-3/pull/15#issue-6094613216|


Optional tutor-led demonstration notes: [optional; leave blank if not used] # not used as of 29/10/2026
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [Register Patient]
Coverage if used: [Under other tests the Patient is proven to be registered, although there is no test for it specifically]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [This is one of the main requirments for the Stage07 Tests.]
Optional fixtures/parametrisation used and why, if any: [not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| Complete Activities 3 and 4, regression evidence in J, and formative answers in N | doc/stage07-testing-evidence | PR #15 https://github.com/LoserWithAGame/st1-assignment-3/pull/15  | @LoserWithAGame was requested as review; no submitted review was completed. | No written review feedback, The auther added individual and changed-order test evidence and linkted it in part J | @LoserWithAGame merged into main 0c3c68e |
| Add stage 7 evidence, inluding entries in Activities A and section B | docs/stage07-evidence | PR #16 https://github.com/LoserWithAGame/st1-assignment-3/pull/16  | No submitted review recorded | The auther asked teammates to conform the additions to A and B. No review response was recorded | @loserWithAGame merged into main as 8cfa26a. |
| Complete the FR-01 patient registration test design in Activity 1 | stage07/fr01-test-design | PR #21  https://github.com/LoserWithAGame/st1-assignment-3/pull/21  | No submitted review record | The auther added positive and negative resistration scenarios and expected assertions | @LoserWithAGame merged into main as 867e4d2. |
| Updated syntheic practioner details in two tests and add a final blank line to the evidence record | stage07/activites-respone | PR #22 https://github.com/LoserWithAGame/st1-assignment-3/pull/22  | @quiet-learner approval was recorded after merge | No written feedback provided | @LoserWithAGame merged into main as 57e1255. @quiet-learner subsequently approved. |
| Update stage 7 sections B-I and K, edit service tests and add VS code settings | Stage07/activities-response | PR #26 https://github.com/LoserWithAGame/st1-assignment-3/pull/26  | @quiet-learner | Approved with "looks great! feedback is approved. Merging now".  | @quiet-learner approved before merging into main as 5e07414. |
| Update contribution evidence and completion record in Sections M and O | stage07/activites-response | PR #27 https://github.com/LoserWithAGame/st1-assignment-3/pull/27  | @quiet-learner | Approved with "good work!". | @quiet-learner approved before @LoserWithAGame merged into main as 9de01bb. |


## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
[Is the program behaving according to its stated requirements? for example, does it reject a conflicting booking when someone attempts to book an appoitment with the same practitioner at the same date/time.]

2. What question does validation answer?
[does the program meet the intented use of the users needs. for exampple can the staff that book appointments do those tasks effectively.]

3. What is a unit test?
[A unit test is a small specific tesst to varify behaviour. for example, it should check that when registering a patient that the name field is not empty.]

4. What is a pytest fixture?
[A fixture provides reusable setup for tests. IT can create fresh store and objects for each test, thus helping prevent tests from affecting one another.]

5. What is parametrisation in pytest?
[Parametrisation runs the same test function multiple times using different set of data inputs. By providing a list of arguments you can test many variables.]

6. What is regression testing?
[regression testing means rerunning tests that prevously done after adding changes to check that the behaviour still works as intended and nothing broke.]

7. What does code coverage tell us, and what does it not prove?
[Code coverage shows witch parts of the code executed during testing. IT can help dientify untested areas. It does not prove that expected results are correct.]

8. What makes an assertion weak?
[An assertion is weak when an incrorect results could still pass. When testing passes but fails to prove that the system is corking correctly or not.]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[Copilot can be used to suggest test cases and assertions. We must check that they match the correct checks that provide meaninful results. Github copilot can be used to brainstorm and apply critical thinking to the project.]

10. What is the Stage 7 engineering rule?
[A passing test should contain meaninful assertions linked to the current requirements. Passing alone does not prove the test was good.]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]

