# Training Website Setup and Maintenance

This file governs first-use website configuration, synchronization, data scope, and publication. Website configuration is a standard step of [initiation](../initiation.md); it is not postponed until the user independently asks about a dashboard.

## Configuration State

A fresh package has no website implementation, hosting identity, or user configuration. During initiation, create this installation's `fitness-site/config.json` after establishing the user's website preference. Keep this README reusable; do not replace it with personal URLs, account details, or commands tied to another user's machine.

Configuration is installation-specific and must never be included in the shareable coach package. The old populated dashboard is archived and is not a starter or a source of user data, site IDs, or publishing permission.

## First-Use Configuration

### Establish the Website Preference

Read the user's working profile/status/plan/log first. As part of the initiation interview, ask one concise question offering:

- **Private hosted website:** accessible through the supported hosting service, with access restricted to this user. Explain that choosing this mode authorizes initial setup/publication and updates to the same private site after training-data changes during coaching tasks.
- **Local website:** build and verify a dashboard in this project without publication. Explain that the local preview must be running to view it and that it reads an exported snapshot.
- **No website for now:** record the choice and continue file-based coaching. Do not ask again every session.

Reuse an already stated choice instead of asking again. Confirm only missing decisions that affect setup, such as which existing site to use. Do not ask the user to choose frameworks, write commands, supply account secrets in chat, or approve each ordinary authorized synchronization. Hosted setup requires a service that actually supports the requested private access; do not substitute a public URL.

### Record This Installation's Settings

Create `fitness-site/config.json` with actual values and explicit unknowns where needed. Record only non-secret operational settings:

| Setting | Required content |
|---|---|
| `mode` | `private-hosted`, `local`, or `disabled` |
| `status` | `pending`, `ready`, `blocked`, or `disabled`; ready requires verification of the selected mode |
| `timezone`, `language`, `units` | Values confirmed in profile.md; no inherited time zone or lb preference |
| `data_sources` | Selected root training documents from the allowlist below; paths relative to the project |
| `data_scope` | Which sections/fields are displayed or exported, including any intentional exclusions |
| `sync_policy` | Local export after training-data changes; same-site publication only within the user's chosen/authorized hosted scope |
| `host`, `site_id`, `url`, `audience` | Actual provider/identity/result for hosted mode; null when not applicable or not yet assigned |
| `export_command`, `verify_commands`, `preview_command` | Commands that have actually been implemented and checked, expressed as argument arrays; null/empty until available |
| `last_sync`, `pending_action` | Last successful local export/deployment outcome and remaining step if setup is incomplete |

Do not store access tokens, credentials, sensitive profile text, or deployment secrets here. Record the user's website preference and the config path briefly in profile.md. Put temporary setup blockers in this configuration, not in the training log or as training-readiness limitations.

### Build and Configure the Selected Website

After the four working training files are ready:

1. For `disabled`, save the choice and finish; do not build or publish anything.
2. For `local` or `private-hosted`, implement this user's dashboard under `fitness-site/` using the available website-building workflow. The package supplies these instructions, not an already implemented exporter or frontend. Create the required frontend, exporter and verification commands before recording them as available. Never read the personal archive to bootstrap another user's site.
3. Build a responsive read-only view of next training, recent completed activity, current progress/capacity, recovery notes relevant to training, and history. Add other views only when useful to this user's goals. Support their actual session structure and activity types; do not hard-code A/B sessions, hiking, a six-week block, a device, or a time zone.
4. Read the root working Markdown as the source of truth. Use an explicit allowlist and selected fields/sections. Resolve calendar dates in the user's time zone; plans remain planned, completed Sessions are deduplicated by ID, and recovery additions never create sessions. Show snapshot freshness so refresh is not mistaken for reading current local files.
5. Export an initial snapshot only after the four files are consistent. Check displayed prescriptions/dates against plan/status and completed records against the log. Verify relevant layouts and the actual build/export commands. Never call a site ready merely because its source files exist.
6. For `local`, provide the verified preview command/address and report that no publication occurred. Keep exported personal data local.
7. For `private-hosted`, follow the currently available hosting workflow. Create a new owner-private site unless this user has identified an existing one; persist its actual ID immediately and reuse it on later updates/retries. Verify the audience, prepare the checked source/build, deploy, and wait for native deployment success before reporting a live URL. Read the current service instructions at execution time rather than copying stale provider commands or inventing tool availability.
8. Save the actual configuration/result, update the profile's short website preference/config reference, and give the user the working URL or local-view instructions. Set `status` to `ready` only after the chosen outcome is verified. Website activity never creates a completed-training entry.

If the required service/tools/account connection are unavailable, finish the coaching files, set website status to `blocked` or `pending`, record the concrete missing prerequisite/next action, and report it plainly. Do not claim a live site or quietly treat an unfinished hosted setup as complete. A website blocker does not block appropriate training.

## Interrupted Setup and Existing Installations

- Resume from config.json, preserving the selected mode, existing site ID, and successful steps. Resolve uncertain creation/deployment before retrying; do not create duplicate sites.
- A working training plan still skips the initiation interview. If website setup is pending/blocked, continue the recorded setup when prerequisites permit without repeating the personal interview or recreating the training files.
- If this is an older installation with a working plan and no website config, keep coaching normally. Configure its website when requested; do not retroactively force a first-use interview.
- A recorded `disabled` choice is complete configuration. Change it only when the user requests a website later.

## Data Scope and Source of Truth

The maximum source allowlist is the five root files below. Select only the sections/fields required for the chosen views; permission to read a file for coaching does not imply displaying every personal detail on a website.

- `profile.md`
- `current_status.md`
- `training_log.md`
- `training_plan.md`
- `capability_assessment_methodology.md`

Do not export archives, templates, agent/interview instructions, configuration, credentials, unrelated files, or another user's records. Avoid exporting raw demographic/health background that is not needed for the requested training views. Project Markdown remains authoritative; website/deployment output must never overwrite training history or convert a plan into a completed session.

## Synchronization After Setup

1. After changing allowlisted training data, finish and verify all local-file changes, then produce one combined snapshot using the configured exporter.
2. Run the configured verification commands and check source freshness, key prescriptions, completion counts, dates, and units. Export only the configured data scope.
3. In local mode, report the verified local snapshot update and how to view it. In authorized hosted mode, update the same site with its existing identity/audience and await deployment success before reporting synchronization.
4. On failure, preserve local updates, record the pending action, and distinguish “local snapshot updated” from “hosted website not synchronized.” A snapshot timestamp, source upload, or saved version alone does not establish publication.
5. If mode is disabled, report “website disabled by user preference.” If setup has not completed, report the pending/blocked state; do not silently publish or skip a recorded setup request.

Instruction-only edits do not trigger a personal-data export or deployment. This is end-of-task synchronization, not a background watcher. Another execution environment needs the latest working files/configuration before synchronization. A change to audience, site ownership, or data scope requires the corresponding user direction; a former owner's authorization never transfers.
