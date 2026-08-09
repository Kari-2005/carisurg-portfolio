# Week 10 Interim — Initial GUI Prototype

## Mercer ED Triage Support Interface

The initial prototype explores how the four proposed urgency tiers could be communicated within the Mercer Emergency Department triage workflow.

The design includes:

- Patient queue
- Urgency indicator for each patient
- Critical/High alert banner
- View-details interaction
- Clinician override mechanism

![Week 10 GUI Prototype](docs/Week10/Interim/GUIPrototype.png)

## Design Rationale

All four urgency tiers are displayed within the same patient queue so that the escalation hierarchy can be evaluated in context.

Urgency is not communicated using colour alone. Each tier combines a colour, icon, written label, border treatment and action wording.

Critical and High cases receive greater visual prominence, while Medium and Low cases remain visible within the queue without generating the same level of interruption.

The layout is kept predictable across patient rows to reduce unnecessary cognitive load. Each patient row presents one primary action associated with the urgency tier.

## View-Details Interaction

Selecting a patient opens a view-details panel containing:

- Patient identifier
- Presenting complaint
- Model-assigned urgency tier
- Top three contributing model features
- Primary clinical action
- Override control

The override mechanism remains clearly visible because the model is intended to support rather than replace clinical judgement.

## Prototype Status

This is an initial low-fidelity prototype for the Week 10 interim submission. The design may be modified following accessibility review and peer user testing.
