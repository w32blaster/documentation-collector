title=Smart Commits
date=2015-07-14
type=post
tags=java,guice,git
status=published
author=John Doe
jira=http://jira.server.com/issue/PROJECT-ONE-11
docker=project-one
~~~~~~

      NB! the content is copied from the [Revizor](https://github.com/w32blaster/revizor/wiki/Smart-commits) wiki for demonstration purposes.

# Revizor Smart Commits

Revizor supports quite common technology, like "Smart Commits", also used in other tools dealing with CVS.

Smart commit - is a short commands, added to a commit message. When Revizor detects these commands, it automatically perfors some actions (like create new review).

## Commands

The main command is create new review. It looks like:

```
+review email1 email2 #key1 #key2
```


where

| Argument  | Description  |
|---|---|
| `+revizor`  | mandatory tocken. Asks Revizor to create a new review  |
| `email1 email2`  |  (optional) list of emails separated by blank spaces or comma. Assignees in Revizor. New review will be assigned to the given users and they will receive an email notifications. If these emails are not existing in Revizor database, then the they will be ignored. |
| `#key1 #key2`  |  (optional) if some issue trackers are set for Revizor, then current review will be associated with the given issue(s). Please check [Issue Tracker support](https://github.com/w32blaster/revizor/wiki/Issue-tracker-support) page for details. |

### Create a review (example)

When Revizor detects this command, it creates new review with current revision:

```
+review reviewer1@email.com reviewer2@email.com #ISSUE-KEY-01 #ISSUE-KEY-02
```

The author will be the CVS committer, header and message will be extracted from the commit message. Each user in Revizor can have any number of aliaces: alternative emails that could be associated with this user.

For example, a developer with email _max@company.com_ can commit the changeset to the Git/Mercurial and leave this message (regarding [common rules for commit messages](http://git-scm.com/book/ch5-2.html#Commit-Guidelines)):

````
"Fix the broken layout

Within this commit I repaired the broken layout on the
user settings page. 
+review john@company.com, alice@company.com #KEY-1"
````

When Revizor pulls this commit, it automatically will create an review with these details:

| Field | Value |
|---|---|
| **header** | "Fix the broken layout"  |
| **description** | "Within this commit I repaired the broken layout on the user settings page."  |
| **author**  |  _max@company.com_ (**if this user does not exist in the Revizor system or no one user has this alias, then the upcoming review will be ignored!**) |
| **reviewers** |  _john@company.com_ and _alice@company.com_. If these users do not exist in the Revizor, then a review will be created without reviewers |
| **issue ticket** | let's assume, there is at least one issue tracker in Revizor, having the pattern `KEY-\d+`. Then the current review will be associated with the issue having ID *KEY-1*. |

### Associate a review with an issue
Please, check the page [Issue Tracker support](https://github.com/w32blaster/revizor/wiki/Issue-tracker-support) for details.

