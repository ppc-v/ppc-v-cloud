# ppc-v-cloud

## Who's asking (soft rule)
This workspace may be used by several people under a shared login.

### Team
| Name | Goes by | Initials |
|---|---|---|
| John Wylie | John | JW |
| Jacob Froats | Jacob | JF |
| Sara Stuka | Sara | SS |
| Stella Crosti | Stella | SC |
| Izzat Arif | Arif | IA |

### How it works
- Start your first message in a session with your name or initials, e.g. "JF: build a negative keyword list for…".
- If someone hasn't identified themselves, Claude asks once at the start of the session. If they'd rather not say, Claude carries on without it.
- Claude adds a `Requested-by: <initials>` line to commit messages and includes the requester in pull request descriptions.
- Claude notes the requester in any Salesforce update summary or Slack message it posts on someone's behalf.
- If someone gives a name not on this list, Claude records it as given and carries on. The list is for convenience, not access control.
