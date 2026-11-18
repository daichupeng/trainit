# AI Training Coach

A reusable, file-based coaching agent for an individual user's goals: general fitness, strength, muscle gain, body composition, endurance, sport, outdoor performance, or a combination. It interviews a new user, creates four working Markdown files, then maintains them as training continues.

## Install and Start

1. Extract the shareable `ai-training-coach.zip` into a separate writable folder for each user. Alternatively copy only the reusable files listed below. Do not distribute this development folder wholesale: its archives contain private records.
2. Use an AI agent with access to read/write that folder. Have it read `AGENTS.md` as its project instructions. This is an instruction-and-template package, not a hosted service or an independently running application.
3. Start with: **“Start my training coach. Read AGENTS.md and begin the initiation interview if I do not already have a training plan.”**
4. Answer short interview rounds about goals, recent training, current function, health constraints, schedule, equipment, and preferences, including a private hosted website, local website, or no website. Existing records can supply answers. Optional measurements are not required.
5. The agent creates the four root working files, recommends the first concrete session, and configures the chosen website following fitness-site/README.md. Website setup requires available build/hosting tools; incomplete setup is tracked separately and does not block coaching. Thereafter submit completed training normally; it records, analyzes, updates progression, and recommends the next session.

There is deliberately **no root training_plan.md in a fresh install**. Do not copy the plan template into the root manually as a setup marker. An existing usable root plan skips initiation; an empty file, unfilled template, archived plan, or template-directory plan does not. Interrupted interviews resume from saved profile/status. An ended block triggers review, not a new intake interview.

## Reusable Package

| Path | Purpose |
|---|---|
| `AGENTS.md` | Entry gate, generic coaching behavior, recording, assessment, progression, and file-maintenance rules |
| `initiation.md` | Adaptive first-use interview, minimum planning information, resume rules, four-file creation and handoff |
| `templates/profile.md` | Goals/priorities, personal background, conditions, health constraints, preferences and conventions |
| `templates/current_status.md` | Goal-relevant capacity/evidence, uncertainty, recent load, recovery, execution progress and next training |
| `templates/training_log.md` | Completed-session format, set-level/activity-specific evidence, recovery attribution and traceable corrections |
| `templates/training_plan.md` | Block information, training overview, active session prescriptions and concise progress |
| `capability_assessment_methodology.md` | Reusable inference rules; detailed strength/endurance/hiking modules selected only when relevant |
| `fitness-site/README.md` | First-initiation website configuration, implementation/verification, and ongoing synchronization rules |
| `scripts/capability_sensitivity.py` | Optional Brzycki/RIR scenario utility; its existing CLI takes/returns lb, so convert explicitly for metric users; not a capacity score |
| `scripts/package_coach.py` | Build a shareable ZIP from an explicit reusable-file allowlist |

Templates retain the original four files' useful structure and evidence rules. Goal priorities, units, exercise continuity/A-B preferences, and activity interests belong in the user profile. Examples are interview prompts, never new-user defaults. Remove unused fields/examples when creating working files. Initial capacity may be unknown; establish a baseline through ordinary training rather than copying the previous owner's performance.

## Daily Use and Storage

- One writable project per user. Reusable templates are shared schemas; root working files contain only that user's data.
- Give the agent a completed workout or activity and any available feedback. Plans and discussions never become completed sessions.
- The ongoing loop is read → parse → deduplicate/log → assess → update status → implement next prescriptions → synchronize a configured dashboard → recommend the next session.
- Existing continuity/progression, task-specific recovery, evidence/uncertainty, and history-preservation rules remain in force. Session structure and success criteria follow this user's goals.
- Keep private working files and archives out of shared packages. The included `.gitignore` excludes them from future version control by default; it does not protect files already tracked elsewhere.
- `sources/` and any marked read-only references remain untouched. Archived personal records are excluded from ordinary coaching and packaging.
- Website configuration is addressed during initiation. Users choose private hosted, local, or disabled; per-installation settings in fitness-site/config.json are excluded from sharing. Pending website setup resumes without repeating the personal interview, and all four training files continue to update.

## Build a Shareable Copy

From the project folder:

```sh
python3 scripts/package_coach.py --output outputs/ai-training-coach.zip
```

The ZIP includes only the allowlisted instructions, four templates, methodology, optional dashboard instructions and utilities. It excludes root personal working files, archives, source references, generated dashboard data, hidden hosting configuration, and account/site identifiers. Existing output is not replaced unless `--force` is supplied.

## Personal Archive in This Development Copy

The previous owner's four working files, original instructions/README/methodology, and entire populated dashboard were archived under `archives/personal-2026-11-18/`. Original bytes are preserved with a SHA-256 manifest. They are local records, excluded from the distributable. The separate original fitness project and its hosted website were not changed.

To resume that owner's coaching here, explicitly request restoration of that named archive's four working files. A restored usable plan bypasses initiation. Restore dashboard tooling only by explicit request; its deployment identity/authorization still needs to be checked for this installation.
