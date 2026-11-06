# Lab 01 - Discussion Answers

## 1. Why use git mv?

git mv moves a tracked file and stages the change in one
operation. This helps keep file moves organized.

Git can also detect renames made with ordinary file operations
by comparing file contents.

## 2. Is release/lab01 a baseline?

Yes. The release/lab01 branch represents the agreed state
of the project after completing Lab 01.

It serves as a reference for the Lab 01 submission.
Unlike a tag, a branch can move, so it should be protected
from unintended changes.

## 3. Why avoid committing directly to master?

Using separate branches and Pull Requests makes changes
easier to review, test, and trace.

It also keeps master stable, even when working alone.

## 4. What is the difference between global and local Git config?

Global configuration applies to repositories belonging to
the current user. On Windows, it is commonly stored in
C:\Users\DUC\.gitconfig.

Local configuration applies only to the current repository
and is stored in .git/config.

Local settings override global settings for the same key.