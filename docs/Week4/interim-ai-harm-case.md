# Week 4 AI-Harm Case Study

## Case: External Validation Failure of the Epic Sepsis Model

### Case Selected

For my documented AI-harm case, I selected the Epic Sepsis Model, which was a sepsis prediction tool used in hospital electronic health record systems. Sepsis is a serious and life-threatening condition where the body has a dangerous response to infection, so early detection is very important. I chose this case because it is closely related to my project on AI-supported emergency triage. Both involve using patient data to help identify high-risk patients earlier, and both could affect patient safety if the model performs worse than expected in a real hospital setting.

### Root-Cause Analysis

The Epic Sepsis Model was designed to warn hospital staff when a patient might be at risk of developing sepsis. This sounds useful because sepsis can worsen quickly, and earlier treatment can improve patient outcomes. However, the concern in this case was that the model was already being used widely before enough independent testing showed that it worked safely across different hospital settings.

Wong et al. tested the model at Michigan Medicine using data from 27,697 adult patients and 38,455 hospitalisations. The results showed that the model did not perform as well as expected. Its AUC score was 0.63. In simple terms, this means the model was not very strong at separating patients who would develop sepsis from those who would not. More importantly, the model missed 67% of patients who developed sepsis, while still creating alerts for 18% of hospitalisations. This means the case can be considered a documented near-miss or patient-safety risk rather than a confirmed fatal harm case. It did not prove that patients died because of the model, but it showed that multiple high-risk patients could have been placed in danger if clinicians relied too heavily on the alert system.

The immediate problem was that the model did not perform well when tested in a real hospital environment outside of its original development setting. The deeper root cause was that the system had not been strongly validated across different hospitals before being used widely. Since the model was proprietary, meaning owned by a company, hospitals may not have been able to fully examine how it worked, what data it was trained on, or whether it was suitable for their own patients.

The system failed to anticipate that a model can perform differently when moved into a new clinical setting. It also failed to fully consider the effect of too many alerts on hospital staff. In a busy ward or emergency department, frequent alerts can become overwhelming. If staff receive too many warnings, they may start ignoring them, even when some are important.

I would classify this case as both a technical and workflow-related failure. It was technical because the model missed many sepsis cases during external testing. It was also workflow-related because too many alerts could affect how clinicians respond during routine care.

This case is relevant to Mercer General Hospital because an AI triage tool should not be trusted only because it performs well in early testing. Before any real deployment, the model should be tested locally, checked for missed high-risk cases, and reviewed with clinicians to see whether its alerts are actually useful. A safeguard that could have caught this earlier would be mandatory local validation before use, including checks for sensitivity, false alerts, subgroup performance, and staff feedback.

### Reference

Wong A, Otles E, Donnelly JP, Krumm A, McCullough J, DeTroyer-Cooley O, et al. External validation of a widely implemented proprietary sepsis prediction model in hospitalized patients. *JAMA Internal Medicine*. 2021;181(8):1065–1070. doi:10.1001/jamainternmed.2021.2626.

