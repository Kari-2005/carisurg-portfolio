# Mercer AI-Assisted Triage Review System

## Overview

This folder contains the final Week 9 mock-up designs for a proposed human-centred triage review system for Mercer General Hospital. The concept expands the original nurse-facing triage dashboard into a connected three-screen system: two screens for clinical staff and one patient-facing portal.

The current Logistic Regression model remains an experimental baseline and is not ready for clinical deployment. The mock-ups therefore present the model as a decision-support tool rather than an autonomous triage system. AI recommendations are intended to prompt review, highlight uncertainty and support prioritisation, while the nurse remains responsible for every final clinical decision.

## Vision for the System

The proposed system is designed to improve communication and situational awareness across the Emergency Department waiting process. It combines:

1. a nurse-facing patient priority list;
2. a detailed nurse patient-review screen; and
3. a patient-facing waiting portal.

The patient portal could be opened by scanning a secure QR code printed on the patient's triage slip. Patients who do not have a compatible phone, require accessibility support, or prefer not to use their own device could instead be given a small hospital-issued device containing the same interface.

Information submitted through the patient portal, including reports of new or worsening symptoms, would appear on the nurse dashboard for clinical review. The system would not automatically change a patient's final ESI level or clinical priority. It would flag the update and allow the nurse to decide whether reassessment or escalation is needed.

---

## Mock-up 1: Nurse Patient Priority Dashboard

The priority dashboard gives the triage team an overview of patients currently waiting in the Emergency Department.

### Main functions

- Displays the nurse-assigned ESI level alongside the AI-suggested ESI level.
- Shows the model's confidence for each recommendation.
- Separates clinical priority from waiting time.
- Highlights new or worsening symptoms submitted through the patient portal.
- Displays the time since initial triage and the most recent reassessment.
- Allows the nurse to filter patients by high, medium or low review priority.
- Provides quick access to urgent alerts and detailed patient records.
- Includes an audit log and manual override access.

### Purpose

This screen helps nurses identify which patients may need additional attention without treating the AI output as a final answer. Waiting time, low model confidence, incomplete information and symptom updates may all prompt review, but clinical judgement remains primary.

---

## Mock-up 2: Nurse Patient Review Screen

The patient review screen opens when a nurse selects an individual patient from the priority list.

### Main functions

- Displays patient identifiers, arrival time and triage history.
- Shows the original nurse-assigned ESI level.
- Shows the AI-suggested ESI level and confidence score.
- Displays the current clinical review priority.
- Presents the patient's complaint, pain score, vital signs, relevant history and medications.
- Shows the clinical factors that most influenced the AI recommendation.
- Displays patient-submitted messages and symptom updates.
- Provides options to accept the suggestion, override the ESI level, reassess the patient, update observations or add a note.
- Records override history and the timeline of assessments and updates.

### Purpose

This screen brings the information needed for reassessment into one place. It supports transparency by showing why the model reached its recommendation and allows the nurse to compare the AI output with the full clinical context before taking action.

---

## Mock-up 3: Patient Waiting Portal

The patient-facing portal provides updates and a simple way to report changes while waiting.

### Access options

- Secure QR code provided after triage.
- Small hospital-issued digital device for patients without a suitable phone or who need assistance.

### Main functions

- Shows a broad clinical status rather than an exact queue position.
- Provides an estimated waiting-time range.
- Displays check-in information and the current stage of the patient's visit.
- Explains what happens next in simple language.
- Allows the patient to report new or worsening symptoms.
- Includes quick symptom options such as worsening pain, breathing difficulty, dizziness, nausea, vomiting or bleeding.
- Sends submitted updates to the nurse dashboard.
- Displays safety instructions for symptoms that require immediate in-person help.
- Provides language, help and privacy information.

### Purpose

The portal keeps patients informed during the waiting period and creates an additional communication route for reporting deterioration. It does not replace direct contact with clinical staff. Patients are clearly advised to approach a staff member immediately for severe or rapidly worsening symptoms.

---

## Proposed Workflow

1. A patient arrives and receives an initial assessment from a triage nurse.
2. The nurse records the presenting complaint, vital signs and other relevant information.
3. The AI model produces an advisory ESI suggestion, confidence score and contributing factors.
4. The nurse confirms or overrides the recommendation and remains responsible for the final triage decision.
5. The patient receives a QR code or hospital-issued device to access the waiting portal.
6. The patient can view their status and report new or worsening symptoms while waiting.
7. New reports appear as alerts on the nurse priority dashboard.
8. The nurse reviews the alert and decides whether reassessment, reprioritisation or escalation is required.
9. Actions, overrides and reassessments are recorded for audit and quality improvement.

---

## Human-Centred Design Principles

The mock-ups were designed around the following principles:

- The nurse remains the final decision-maker.
- AI recommendations are advisory and must be reviewable.
- Model confidence and contributing factors should be visible.
- Colour should not be the only way priority is communicated.
- Waiting time should trigger review rather than automatically change clinical priority.
- Patient updates should be acknowledged by clinical staff.
- Manual workflows must remain available if the AI, network or portal becomes unavailable.
- The interface should remain understandable during busy shifts and periods of fatigue.
- Patient information should be limited to the minimum necessary and protected through secure access controls.

---

## Current Limitations

The mock-ups describe a future implementation vision rather than a clinically validated product.

The current model has important performance limitations, particularly for rare and highly urgent ESI categories. Before clinical use, the system would require:

- improved model performance;
- validation using representative local data;
- clinician usability testing;
- prospective safety evaluation;
- secure EHR and device integration;
- accessibility and language testing;
- clear downtime and manual-fallback procedures; and
- formal clinical governance approval.

For these reasons, the proposed implementation is framed as a triage review and communication system, not an autonomous triage tool.

---

## Future Integration

Future development could include:

- integration with the Mercer Electronic Health Record;
- automatic import of vital signs from approved devices;
- configurable reassessment reminders;
- multilingual patient support;
- accessibility settings for text size, contrast and audio assistance;
- secure analytics for reviewing override and alert trends; and
- a later Observation Unit kiosk or robotic vitals station after appropriate HRI testing.

## Files in This Folder

This folder is intended to contain:

- the nurse patient priority dashboard mock-up;
- the annotated nurse priority dashboard;
- the nurse patient review mock-up;
- the annotated nurse patient review screen;
- the patient waiting portal mock-up;
- the annotated patient waiting portal; and
- this README explaining the overall design vision.
