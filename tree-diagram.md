# Reflection Tree Diagram

```mermaid
flowchart TD
    START[START: Evening greeting] --> A1_OPEN[A1_OPEN: Describe your day]

    A1_OPEN --> A1_D1{Productive/Mixed or Tough/Frustrating?}

    A1_D1 -->|Productive or Mixed| A1_Q_HIGH[Axis 1: What helped things go well?]
    A1_D1 -->|Tough or Frustrating| A1_Q_LOW[Axis 1: What was your instinct?]

    A1_Q_HIGH --> A1_D2_HIGH{Preparation/Adaptability or Team/Luck?}
    A1_Q_LOW --> A1_D2_LOW{Control or External reaction?}

    A1_D2_HIGH -->|Preparation or Adaptability| A1_R_INT[Reflection: Internal agency]
    A1_D2_HIGH -->|Team support or Luck| A1_R_MIX[Reflection: Mixed agency]
    A1_D2_LOW -->|Fix what I can control| A1_R_INT
    A1_D2_LOW -->|Wait/Blame/Stuck| A1_R_EXT[Reflection: External locus]

    A1_R_INT --> BRIDGE_1_2[Bridge: Control to contribution]
    A1_R_MIX --> BRIDGE_1_2
    A1_R_EXT --> BRIDGE_1_2

    BRIDGE_1_2 --> A2_OPEN[A2_OPEN: What stood out in interactions?]

    A2_OPEN --> A2_D1{Contribution or entitlement?}

    A2_D1 -->|Helped / Extra work| A2_Q_CONTRIB[Axis 2: Why did you go beyond role?]
    A2_D1 -->|Under-recognized / Others did not perform| A2_Q_ENTITLE[Axis 2: What bothered you?]

    A2_Q_CONTRIB --> A2_D2{Intentional giving or situational giving?}
    A2_Q_ENTITLE --> A2_D3{Recognition issue or support issue?}

    A2_D2 -->|Wanted to help / Felt right| A2_R_HIGH[Reflection: Contribution]
    A2_D2 -->|Team needed it / Habit| A2_R_MED[Reflection: Moderate contribution]
    A2_D3 -->|Lack of credit / Unfair expectations| A2_R_ENT[Reflection: Entitlement]
    A2_D3 -->|Others not working / No support| A2_R_EXT[Reflection: External frustration]

    A2_R_HIGH --> BRIDGE_2_3[Bridge: Contribution to perspective]
    A2_R_MED --> BRIDGE_2_3
    A2_R_ENT --> BRIDGE_2_3
    A2_R_EXT --> BRIDGE_2_3

    BRIDGE_2_3 --> A3_OPEN[A3_OPEN: Who comes to mind?]

    A3_OPEN --> A3_D1{Radius of concern}

    A3_D1 -->|Just me| A3_SELF[Axis 3: Main concern]
    A3_D1 -->|My team| A3_TEAM[Axis 3: Team impact]
    A3_D1 -->|A colleague| A3_COL[Axis 3: Colleague perspective]
    A3_D1 -->|Customer| A3_CUST[Axis 3: Customer impact]

    A3_SELF --> A3_R_SELF[Reflection: Self-focused]
    A3_TEAM --> A3_R_TEAM[Reflection: Team lens]
    A3_COL --> A3_R_COL[Reflection: Empathy]
    A3_CUST --> A3_R_CUST[Reflection: Wider impact]

    A3_R_SELF --> SUMMARY[Summary]
    A3_R_TEAM --> SUMMARY
    A3_R_COL --> SUMMARY
    A3_R_CUST --> SUMMARY

    SUMMARY --> END[END]
