# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [Wednesday 4:30pm - 6:30pm Group 1]
Members and UG/PG applicability: [@MastrRoshiiii, @LoserWithAGame, @warunabandara11-wq, @quiet-learner]


## A Release scope and starting SHA

- Release label/version and requirements baseline: SmartCare Stage 12 Common RC1. Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2. The common scope covers registration and lookup, booking and conflict checks, cancellation and retained history, appointment listing, and the console.
- Common starting SHA / branch / applicable members: 'f615f78795d031f8b525a7a388e9c340ac296a61', doc/stage12, @MastrRoshiiii
- PG starting SHA / branch / applicable members or not applicable: [N/A]
- Working-state review and approved integration: Stage 9 console and appointment listing work was merged into main through PR #35. An independent test run on the exact starting commit returned 38 passed in 0.06 seconds using Python 3.14.7 and pytest 8.3.5.
- Protected common candidate and PG differences: The common starting point is pinned to 'f615f78795d031f8b525a7a388e9c340ac296a61'. (No PG members).
- Feature freeze / owner / verifier: Feature Freeze date - 9/11/2026, (Owner TBD), Verifier - @LoserWithAGame


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: I would hold off on releasing. Passing tests show that the tested features work, but another person still needs clear setup instructions. I would finish the README, check the dependency, and document the known limitations. Then I would ask a teammate to set up the project from a fresh copy and run the operation tests before releasing it.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works - FR-07 - common scope | The test cancels appointment A1, then checks that looking it up returns the same appointment with status `CANCELLED`. It passed in the 38-test suite. | 'test_cancellation.py', line 18, at 'f615f78795d031f8b525a7a388e9c340ac296a61' | Team reviewer pending | Yes for the behaviour tested. Release review is pending. | Independent check pending. Reviewer should rerun the cancellation history test on the final release. |
| Architecture responsibilities are appropriate — common scope | `domain.py` decides when an appointment can be cancelled. `data_store.py` keeps the records. `services.py` finds the appointment and asks it to cancel. `queries.py` filters and sorts a new list without changing the original records. `console.py` asks for input and displays the results. | These five files are in `project/smartcare` at `f615f78795d031f8b525a7a388e9c340ac296a61`. | Team reviewer pending | Yes for the separation shown in the code. Independent review is pending. | Team member should follow one cancellation and one appointment listing through the code, then record their name and findings. |
| Rescheduling is safe — PG only | N/A | N/A| N/A | N/A | N/A |
| AI use is responsible — common scope | In Stage 8, Copilot suggested that the practitioner comparison was reversed. I checked the `!=` comparison against both failing behaviours before accepting the suggestion. After the repair, all three focused tests passed. | [Stage 8, Part F](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/stage08/stage08_activities_and_evidence.md#L295), SHA `f615f78` | @MastrRoshiiii checked the Stage 8 diagnosis. Stage 12 reviewer pending. | Yes for this example. Final release recheck pending. | Verifier to review this evidence in Part E and record their decision - approved/declined. |
| System is maintainable — common scope | The Stage 8 refactor uses `AppointmentStatus.SCHEDULED` in the conflict check so the code uses the same status value as the rest of the project. All 37 tests passed before and after the refactor. | [Conflict check](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/data_store.py#L112), SHA `f615f78`. Test evidence is in Stage 8, Part H. | Stage 12 reviewer pending | Partly. The code change is supported by tests, but the project README still lists completed work as TODOs in Part F. | Update the README in Part F, reviewer to follow it from a clean copy and record the result. |
| FR-01–03 register/find and validation — common scope | Tests check that registered patients and practitioners can be found, duplicate registrations leave the original records in place, and invalid or unknown lookup IDs raise the expected errors. These tests passed in the 38-test suite. | [Registration tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_starter.py#L61) and [lookup tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_services.py#L19), SHA `f615f78`. | Stage 12 reviewer pending | Yes for the automated checks listed. Console verification is pending. | In Part D, a team member can demonstrate registering and finding a patient and two practitioners, then show that the console can recover from a failed lookup. Results should be recorded as pass/fail. |
| FR-04–05 booking and conflict rules — common scope | The tests show that a valid booking succeeds, a booking with an unknown patient is rejected, and the same practitioner cannot be booked twice at the same time. A different practitioner can take a booking at that time (AC-04.2). These tests passed in the 38-test suite. | [Booking and conflict tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_starter.py#L101), SHA `f615f78`. | Stage 12 reviewer pending | Yes for the automated checks listed. Console verification is pending. | In Part D, show a valid booking, a rejected double-booking, and a successful same-time booking with a different practitioner. Record the final test run in Part C. |
| FR-06–08 cancellation, history, and lookup — common scope | Tests confirm that looking up a known ID returns the original appointment, cancelling it changes its status to `CANCELLED`, and the same record can still be found afterward. A second cancellation is rejected without removing the record. These tests passed in the 38-test suite. | [Appointment lookup test](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_starter.py#L55) and [cancellation tests](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/tests/test_cancellation.py#L18), SHA `f615f78`. | Stage 12 reviewer pending | Yes for the automated checks listed. Console verification is pending. | In Part D, cancel A1, find it again and show its `CANCELLED` status, then try cancelling it a second time and record what happens. Record the final test run in Part C. |
| FR-09 and QRY-01–04 / FP-01–03 — listing, filtering, ordering, and purity — common scope | A focused check showed that the query returned a new list containing the original appointment objects, sorted by date/time and then ID. Status filtering worked, and the original records stayed unchanged. A known practitioner with no bookings returned an empty list, while an unknown ID raised `LookupError`. | [Query code](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/queries.py#L15) and [listing service](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/services.py#L160), SHA `f615f78`. | Stage 12 reviewer pending | Partly. The checks passed for `D1`, but ` D1 ` returned an empty list. | Record the spaces-in-ID issue in Part H. After fixing it, test both inputs and record the result in Part C. Show listing and filtering through the console in Part D. |
| UI-01 and UI-02 — full console sequence and error recovery — common scope | An independent console check covered registering and finding records, booking, rejecting a double-booking, cancelling and finding the same appointment, listing appointments, and exiting. The menu kept working after invalid choices, dates, statuses, and unknown IDs. | [Console menu](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/console.py#L72), SHA `f615f78`. Ran `python -B main.py --interactive` from `project`. | Stage 12 team reviewer pending | Yes. The main workflow and error recovery worked. | Record the console walkthrough in Part D. Track the listing issue in Part H, then repeat that step after the fix. |
| Session-only scope / FR-10 retired — common scope | I registered sample patient `P1`, exited the console, and opened a fresh session. Looking up `P1` returned `Patient not found`. The console also warned on exit that session data would be lost. | [Console menu](https://github.com/LoserWithAGame/st1-assignment-3/blob/f615f78795d031f8b525a7a388e9c340ac296a61/project/smartcare/console.py#L72), SHA `f615f78`. Ran `python -B main.py --interactive` from `project`. | Stage 12 team reviewer pending | Yes for the session-only behaviour checked. | Record the exit and restart demonstration in Part D. List the loss of records on exit as an accepted scope limit in Part G. |
| PG RES and assurance integration | N/A | N/A | N/A | N/A | N/A |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [response] | [response] | [response] | [response] | [response] |
| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |
| Affected focused checks after correction | [response] | [response] | [response] | [response] | [response] |
| Full integrated recheck | [response] | [response] | [response] | [response] | [response] |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [Identifying Problem and Stakeholders] | [Problem is an incomplete SmartCare appointment booking system, stakeholders are SmartCare, Practitioners, Staff, Patients, Management] | [System is functional] | [Refer to Assignment Sheet and main.py for results] |
| Register and find Patient and two Practitioners | [Two Practitioner ID's and a Patient ID] | [Patient and Practitioners Found or non-existent] | [Without Registering Patients or Practitioner: Not Found. With Registered Patients and Practitioners: Found] | [response] |
| Valid booking | [Appointment ID, Practitioner ID, Patient ID, Time and Date of Appointment] | [Books an appointment using Inputs] | [response] | [response] |
| Same practitioner exact-time conflict rejected | [Appointment ID, Practitioner ID, Patient ID, Time and Date of Appointment. Duplicated with the same Practitioner ID and Time and Date] | [Prevents the booking of an appointment and Raises an Error] | [response] | [response] |
| Different practitioner same time allowed | [Appointment ID, Practitioner ID, Patient ID, Time and Date of Appointment. Duplicated with the same Time and Date] | [Allows the booking of an appointment] | [response] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [Appointment ID, Practitioner ID, Patient ID, Time and Date of Appointment, Appointment Status.] | [Sets appointment Status to Cancelled, and is still stored within the system] | [response] | [response] |
| Invalid/repeated cancellation rejected | [response] | [response] | [response] | [response] |
| Default all-status listing | [response] | [response] | [response] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [Any input] | [Filters Empty and Unknown input types without crashing the program] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [Inputs of Time and Date, Appointment Status] | [Raises an Error at all Invalid inputs, but allows the program to continue.] | [response] | [response] |
| Session-only limitation and normal exit | [The recorded data only exists until the program is ended.] | [When the program ends, all appointments, practitioners, and patients are deleted from the system.] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [FR-05: Prevent Practitioner Conflict] | [When a Duplicate appointment for the same Practitioner and Time and Date is attempted to be booked. When this situation occurs the appointment is not booked, raising a conflict error to the user.] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [The AI suggested adding a padding remover for parsing the Patient, Practitioner, and Appointment ID's] | [This was accepted, as it was an oversight, we used padding removers for the Input verification but forgot to implement them in the parsing.] | [This was changed to the AI's suggestion] | [response] |
| PG reschedule identity/participants/time and no-op | [N/A] | [N/A] | [N/A] | [N/A] |
| PG conflict/invalid status/failure non-mutation | [N/A] | [N/A] | [N/A] | [N/A] |
| PG old slot / current lookup/list ordering / assurance risks | [N/A] | [N/A] | [N/A] | [N/A] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [N/A]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
