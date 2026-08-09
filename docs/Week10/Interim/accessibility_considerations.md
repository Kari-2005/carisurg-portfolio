# Week 10 Interim — Accessibility Considerations

## Purpose

The Mercer ED triage interface may be used during busy clinical shifts, under variable lighting conditions and by staff with different visual and cognitive needs. Accessibility therefore needs to be considered during the initial design rather than added after testing.

Three initial accessibility concerns were identified for the prototype.

---

## 1. Colour-Vision Deficiency

### Concern

The proposed urgency system uses red, amber, yellow and green. Red and green may be difficult to distinguish for users with red-green colour-vision deficiency. Colour appearance may also vary depending on clinical lighting and monitor quality.

### Design Response

Colour will not be used as the only method of communicating urgency.

Each tier will combine:

- Colour
- Distinct icon
- Written urgency label
- Border treatment
- Action wording

Proposed border treatments are:

- Critical — solid
- High — dashed
- Medium — dotted
- Low — no additional pattern

This allows urgency to remain distinguishable even if colour differences are reduced.

### Residual Limitation

The effectiveness of the colours and patterns may still vary across displays and lighting environments.

The prototype will therefore be reviewed using a deuteranopia simulation before finalisation.

---

## 2. Cognitive Load and Staff Fatigue

### Concern

Emergency department staff may need to interpret information quickly while managing several patients simultaneously. Long messages, inconsistent layouts or excessive information could increase cognitive load, particularly during long or overnight shifts.

### Design Response

The prototype will:

- Keep alert messages to a maximum of 12 words.
- Use short, action-oriented language.
- Maintain a consistent patient-row layout.
- Group related information together.
- Keep detailed clinical information within the view-details panel.
- Present one primary action for each patient row.

These choices are intended to make the interface easier to scan without requiring staff to interpret unnecessary information.

### Residual Limitation

Several simultaneous High or Critical cases may still increase visual and cognitive load. This should be considered during user testing and later iterations.

---

## 3. Alarm Fatigue and Excessive Interruption

### Concern

If every model prediction generates a prominent alert, staff may become desensitised to the system and begin ignoring alerts.

### Design Response

The intensity of the interface response will increase with urgency.

- Critical — strongest visual alert and potential audio cue
- High — prominent visual alert
- Medium — static queue indicator
- Low — static queue indicator

Alert banners will therefore be reserved for Critical and High cases rather than appearing for every patient.

### Residual Limitation

Several Critical or High alerts occurring simultaneously could still create competing signals. Further user testing would be required to determine how multiple urgent cases should be prioritised.

---

## Additional Accessibility Checks

Before finalisation, the prototype should also be reviewed for:

- WCAG AA text contrast
- Readability at desktop and tablet sizes
- Adequate button and touch-target size
- Plain-English terminology
- Visibility of the clinician override mechanism
- Deuteranopia simulation

## Next Step

Accessibility observations from peer testing will be used alongside these initial considerations to identify changes required for the next prototype iteration.
