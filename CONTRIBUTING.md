# Contributing to the group project

## Choose your assignment

Tell the group which notebook you claim. Add your name and reviewer in that notebook. Work in your own notebook, outputs/member_XX and figures/member_XX. Use the exact handover columns and filenames from artifact_contracts.json.

## If you have been invited as a collaborator

Accept your personal GitHub invitation, then clone the repository. Work on a role branch rather than editing main directly. Example for Member 02:

```bash
git switch main
git pull --ff-only
git switch -c member-02/title-topics
```

Complete your work, run your notebook in order, save outputs and explanations, and stage only your own files:

```bash
git add team_notebooks/02_title_topic_modeling.ipynb outputs/member_02 figures/member_02
git commit -m "Complete title topic modeling and handover"
git push -u origin member-02/title-topics
```

On GitHub, open a pull request into main. Describe your methods, input checksum, files/row counts, checks, findings and remaining limitations. Ask your reviewer to read it before the coordinator merges it. Use your own assignment number and branch name.

## If you have not been invited

The repository is public. You can fork it into your GitHub account, clone your fork, make a role branch, and open a pull request from your fork to this repository's main branch. Public visibility does not grant direct push permission. Send the coordinator your GitHub username if you want a collaborator invitation.

## See teammates' changes

Fetch and pull have different jobs. Fetch updates the origin/... branch references; pull updates your current branch from its tracked branch. A teammate's branch does not become part of main until its pull request is reviewed and merged.

To see all pushed branches, open a terminal in this repository and run:

```bash
git fetch origin --prune
git branch -a
```

Save and commit your own edits before switching branches. To inspect Member 5's branch for the first time:

```bash
git switch --track origin/member-05/time-anomalies
```

If that local branch already exists, use git switch member-05/time-anomalies instead. For another member, substitute their actual pushed branch name. Branches under remotes/origin/ are fetched GitHub branches, even if they do not yet have a local branch.

After the coordinator merges a pull request, get the accepted changes with:

```bash
git switch main
git pull --ff-only
```

Keep main tracking origin/main. Fast-forward-only pulls stop when local commits diverge; resolve the difference deliberately rather than force-resetting your work. VS Code's branch selector can show local branches and remote origin/... branches. Enable Git: Autofetch and Git: Fetch On Pull in this folder's settings if you want its remote references to refresh in the background. Fetching does not merge or apply changes to your open notebook.

For each new contribution: accept your collaborator invitation, commit and push your role branch, open a pull request targeting main, mark it Ready for review when it can be accepted, and tell the WhatsApp group. Draft pull requests cannot be merged. An early name/role claim can be merged while the notebook's analysis status remains In progress. After a merge, later commits on the same branch need another pull request.

Only the coordinator integrates accepted results into the main workstation. Discuss changes that affect shared inputs, schemas, project structure or other members in the WhatsApp group before making them. A commit saved only on your computer will not appear on GitHub or anyone else's computer.

## Shared-data rules

- Keep raw data, source_manifest and reports_base unchanged.
- Use permanent report_id values and the same approved preparation version.
- Member 1's prepared handover is needed before final modeling; Member 6's approved labels are needed for final district/time/elderly tables.
- Do not edit another member's notebook or the main workstation without agreeing it with the group.
- If shared schemas or preparation/labels change, discuss the version change and rebuild dependent results.
- Use relative paths; keep credentials, .env files, virtual environments, caches and private scratch files out of commits.
- Keep identifying detail and long raw report/vector dumps out of notebook output. Check the actual staged files before pushing to this public repository.
- GitHub's normal file limit is 100 MiB. Do not commit ZIP packs, large model caches or oversized generated exports; coordinate a suitable artifact handover if needed.

## Before opening a pull request

- [ ] My notebook runs top-to-bottom and its interpretations match saved outputs.
- [ ] My required files are complete and my handover.md explains them.
- [ ] Report IDs, schemas, statuses, counts and input/category versions pass the agreed checks.
- [ ] Charts are readable and include labels, periods, units and denominators.
- [ ] Genuine empty results and unassigned/unknown cases are explained.
- [ ] A peer reviewer is named and unresolved issues are stated.
- [ ] I staged only the intended notebook and role files.

## Main-workstation integration

The coordinator merges reviewed role outputs, imports accepted tables/figures into the main notebook, checks the common report/category versions, and writes question-by-question results with the contributing owners. Everyone signs off the final report. Invite the instructor at the submission stage according to the course instructions.
