# First-Use Interview and Initialization

## Entry and Resume Rules

Read this file only when there is no usable root-level `training_plan.md`, as defined in AGENTS.md. Skip initiation when a working plan exists, even if its block has ended. Templates, archived plans, reference files, and empty/unfilled plans do not satisfy the gate.

This is an interactive interview, not a questionnaire to paste in full. Read this user's existing root working files and supplied references first. Never search archives or another project for a new user's answers. Ask only what remains unknown and matters to the first plan. Accept existing records instead of asking users to transcribe them.

- Use the user's language; English is the fallback. Ask 2–3 related questions per round, adapt the next round to the answers, and accept a free-form overview. The usual ongoing 1–2-question budget does not limit the entire initiation interview.
- Explain briefly that the interview produces a profile, current-state assessment, first training plan, and ongoing log. Users may skip optional personal details or say they do not know.
- Distinguish long-term background, current state, measured/reported performance, and desired outcomes. Do not turn aspirations, old personal bests, or example answers into current capacity.
- If interrupted, save confirmed answers in root profile.md/current_status.md and unresolved decision-changing items in current status. Reuse existing working files; do not create duplicates or a placeholder training_plan.md. Resume only the unanswered items next time.
- An unfilled or interrupted root plan must not be treated as complete. Preserve any supplied usable prescription and recover the missing setup without destroying it.

## Interview Rounds

### Goals and Direction

Start here unless the user has already supplied the answers:

1. What do you want training to improve, and which outcome matters most? Why? Examples only if helpful: general fitness/health, strength, muscle gain, body composition, endurance, a sport, outdoor performance, or enjoyment.
2. Is there a target event, task, date, or measurable outcome? What would meaningful success look like? Establish priorities and acceptable trade-offs if goals compete.
3. What are you doing now, and when did you last train consistently? Ask for a brief recent week or two, not their entire lifetime history.

Do not impose the original owner's hiking-first priorities, a weight-loss goal, a fixed number of gym sessions, or a mandatory A/B split. Challenge an unrealistic outcome or timeline directly, explain the constraint, and propose a workable starting direction.

### Profile, Health, and Current Function

Collect only relevant information, spread across rounds as needed:

- Preferred language, time zone, and units. Confirm the time zone before interpreting “today,” “tomorrow,” or scheduling the first session. Exact address is unnecessary.
- Age or age range; height/weight or other measurements only where relevant and voluntarily supplied. Ask measurement/report date when needed; a profile creation date is not a measurement date. Do not demand an exact birth date, body-fat estimate, photos, or maximal test.
- Current pain or symptoms, injuries/conditions affecting exercise, relevant medication effects, clinician restrictions, recent illness, or other health circumstances affecting the plan. Ask what movements/daily activities are affected and what advice they have received; do not diagnose or invent clearance.
- Present recovery: recent fatigue/sleep, soreness versus pain, daily function, and whether symptoms change with the relevant activity. “No injuries reported” is not a comprehensive negative health screen.

Unknown optional demographics or measurements do not block planning. An unresolved restriction that changes a specific exercise needs targeted clarification; retain work that is appropriate within known constraints. For dangerous symptoms, prioritize prompt medical evaluation over a workout. Medical rehabilitation, pregnancy/postpartum considerations, or training for minors requires appropriate scope and individualized professional guidance when relevant; do not silently apply a healthy-adult performance plan.

### Experience and Starting Evidence

- What training has the user done, for how long, with what consistency, interruptions, and exercise/skill familiarity?
- What recent completed sessions or tests can they share? Capture task, date, volume, effort, conditions, and recovery as available. Historical results need dates and must stay historical.
- What felt limiting: breathing, local fatigue, technique/control, pain, time, motivation, access, or another factor? Do not assume a physiological cause from an incomplete report.

Use goal-specific follow-ups only where relevant:

| Goal | Useful interview evidence |
|---|---|
| General fitness / returning to exercise | Current weekly activity, tolerable walking/daily tasks, previous routine, break duration, adherence barriers |
| Strength / muscle gain | Familiar exercises, recent load × sets/reps, effort/reserve, technique confidence, equipment; muscle or lift priorities |
| Body composition | Desired change and time horizon, dated measurements if supplied, sustainable habits and training/recovery priorities; no invented calorie needs or fat/muscle changes |
| Endurance / race preparation | Sport/mode, recent frequency/duration/distance, effort, relevant results, target course/date and tolerance |
| Sport / skill / power | Practice/competition schedule, skill experience, repeated demands, technical coaching/access and relevant performance |
| Hiking / outdoor preparation | Distance, ascent/descent, terrain, altitude, pack weight, consecutive days, finish reason and later function; route-specific skills/acclimatization are separate from fitness |
| Mobility / balance / functional goals | Task that matters to the user, present range/control/function, relevant restrictions and observed difficulty |

Do not require extra tests, videos, lap marking, daily check-ins, or set-by-set RIR. Read relevant assessment-methodology sections; its detailed strength/endurance/hiking modules apply only when relevant. For an unsupported assessment domain, state the evidence gap and use an appropriate sourced method before making numerical claims.

### Schedule, Environment, and Preferences

- How many sessions and minutes per session are realistically sustainable? What is the minimum during a busy week? Are fixed days or a rolling sequence preferable? Establish near-term start availability separately from usual availability.
- What equipment, facilities, load increments, outdoor access, weather/travel constraints, or accessibility needs matter?
- Which activities/exercises does the user like, dislike, or insist on keeping? What has helped or prevented adherence?
- Agree session structure and exercise continuity. If the user wants fixed exercises/order, record that boundary. Otherwise agree the scope for ordinary substitutions. No need to ask for permission for each routine parameter adjustment.
- Establish useful recording conventions for the chosen activities: units, per-dumbbell/total, per-side/bilateral, bar included, actual versus target RIR/RPE and scope, moving/elapsed time, device/sensor only if known. Reuse answers later; never assume all users have a chest strap.

### Website Configuration

Read [fitness-site/README.md](fitness-site/README.md) during the first initiation. Address website configuration explicitly rather than waiting for a later request.

- Ask whether the user wants a private hosted website, a local website, or no website for now, unless they have already specified a choice. Explain access, viewing requirements, and that hosted mode includes initial publication and same-site updates after training-data changes during coaching tasks.
- Reuse confirmed time zone, language, units, goals, and session structure. Record the selected mode and `fitness-site/config.json` reference in profile.md; keep operational settings and pending setup steps in that installation-specific configuration.
- Configure/build/verify the chosen website after the four training files are ready, following the README's procedure and data scope. For hosted mode, use the available hosting workflow, retain the actual site ID/private audience, and verify deployment before reporting a live URL. For local mode, provide checked viewing instructions. For no website, record `disabled` and do not repeat the question during routine coaching.
- If setup is interrupted or blocked by missing tools/access, retain the choice and exact next action. Finish the usable training plan and continue coaching; resume website setup from its configuration without repeating the personal interview. Never inherit another user's site/data or invent an exporter, credentials, or a successful deployment.


### Synthesis and Essential Gaps

Summarize the ranked goals, sustainable schedule, current evidence/limitations, and proposed first-block approach briefly. Invite corrections alongside the next question if something material is unresolved; do not add a separate mandatory approval ceremony after the user has already supplied sufficient direction.

Before writing the first plan, establish:

1. A primary goal or an explicitly agreed provisional goal.
2. Enough recent activity/experience context to select a realistic first dose, or an explicit lack of baseline with a normal-training calibration prescription.
3. Relevant known health restrictions/current functional issues and any decision-changing gap affecting the selected activity.
4. A feasible schedule, accessible activity/equipment, and a specific first-session opportunity in the user's time zone.
5. User preferences and recording conventions needed to execute/interpret the selected work.

Do not delay an otherwise usable plan for optional measurements, missing historical details, or future recovery observations. Do not invent answers to satisfy the checklist. If essential answers are still missing, ask the smallest useful follow-up and save progress without writing an empty plan.

## Create the Working Files

Read the four templates under templates/ and preserve their maintenance conventions and main headings. Replace placeholders with supported answers or honest unknowns; remove comments, irrelevant sections, and unused examples. Do not edit the templates for this user's setup.

1. **profile.md** — store long-term goals/priorities, relevant background and health constraints, usual conditions, units/time zone/language, preferences, and confirmed conventions with sources/dates. Temporary availability/readiness belongs in status/plan.
2. **training_log.md** — instantiate its rules and no session entries unless the user actually supplied completed training. Import such records once, with traceable sources/dates, unique IDs, per-set strength details where available, and honest unknowns. Historical result-only evidence may be labeled as a historical result; do not manufacture sets or dates. No interview or planned first session is a completed workout.
3. **current_status.md** — summarize current capability and relevant limitations relative to goals. Label interview evidence, observations, estimates, judgments/confidence and unknowns. Use “not yet established” if no baseline exists. Set actual recent load/last session if known; zero recorded sessions does not prove zero activity. While interviewing, preserve the next unresolved items here; clear them when resolved.
4. **Draft the first plan** — select a block duration, goals, minimum/ideal schedule, and sessions suited to this user, rather than copying the original six-week hiking block. For each component specify an executable dose/intensity, progression trigger and concrete next increase, adjustment/stop conditions and return criteria. Unknown strength loads may be selected through normal warm-up using a bounded effort/quality rule; no invented tested load or forced maximum. Known tolerable volume should not be reset to an arbitrary introductory dose.
5. **Check and finalize** — synchronize block ID/version/window, progress, next session/date and parameters between status and the plan. The plan must have real prescriptions under Session Guidelines and only the four required body sections after Maintenance Conventions. Check sources/units/dates, remove placeholders and instruction comments, and verify no example or goal has been logged as completed. Write the usable root training_plan.md **last**. Do not write it merely as an interview progress marker.
6. **Configure the website** — complete the website step in fitness-site/README.md using the interview choice. Create the per-installation configuration; build/export/verify a local or private hosted dashboard, or record the user's disabled choice. Preserve any pending step and report the actual outcome if setup cannot finish. The plan remains the coaching-initiation completion signal; website setup progress is tracked separately so it can resume without another intake.

## Handoff to Ongoing Coaching

Tell the user their primary focus, the reason for the starting dose, and the first concrete session/date/window with relevant conditions. Identify only the important unknowns to learn through normal training. Confirm which four files were created/updated, the website mode, and the actual setup outcome: verified hosted URL, checked local-view instructions, disabled by user choice, or a concrete pending/blocked step. Do not report initiation as having a ready website unless its chosen mode has been verified.

Thereafter follow AGENTS.md: completed session → deduplicate/log → assess → update status → implement next prescriptions across affected sessions → synchronize configured dashboard → recommend next training. Continue this loop; do not repeat the interview at every chat or block transition.
