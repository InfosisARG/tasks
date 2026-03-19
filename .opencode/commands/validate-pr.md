---
description: Validate an MR for errors/vulnerabilities (asks for MR; lists assigned MRs)
agent: OpenRepoManager
---

1. Load skill: validate-pr
2. If `$1` is provided (MR IID or URL), validate that MR; otherwise list MRs assigned to `@me` and ask which MR to validate.
