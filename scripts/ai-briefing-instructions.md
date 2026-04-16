# AI Morning Briefing — Agent Instructions

Run this daily to produce and deliver an AI morning briefing to Telegram.

## Step 1: Get Today's Date

Run bash: `date`

## Step 2: Research

Use WebSearch to run these four searches (use today's date in each):

1. "AI model releases announcements [this week / today's date]"
2. "agentic AI open source LangGraph AutoGen CrewAI smolagents updates [this week]"
3. "Anthropic OpenAI Google DeepMind Mistral Meta AI news [today's date]"
4. "AI agent tooling platform GitHub releases [this week]"

Then use WebFetch to read the 3-5 most interesting/relevant articles in full.

## Step 3: Write the Briefing

Use the Write tool to write a plain ASCII text file to /tmp/ai-briefing.txt.

IMPORTANT: Use NO asterisks, NO underscores, NO backticks, NO square brackets,
NO angle brackets, NO hashtags. Plain ASCII only — this prevents Telegram parse errors.

Format:

```
AI Morning Briefing - [DATE]

TOP STORIES

1. [Story title]
[2-3 sentence summary explaining what happened and why it matters].
Source: [full URL]

2. [Story title]
[2-3 sentence summary].
Source: [full URL]

[continue for 4-6 total stories]

TOOLS AND RELEASES

- [Tool/platform name]: [what it does and why it matters]. Link: [URL]
- [Tool/platform name]: [description]. Link: [URL]
[3-5 items total]

TLDR
- [Most important takeaway]
- [Second takeaway]
- [Third takeaway]
```

## Step 4: Send to Telegram

Run bash: `python3 scripts/ai-briefing.py`

The script reads /tmp/ai-briefing.txt and sends it to Telegram as plain text.
It handles chunking for long messages and prints status for each chunk.

## Step 5: If Send Fails

If step 4 fails, run bash: `cat /tmp/ai-briefing.txt`
This prints the briefing to the job log so the content is not lost.
Also print the full error message from the script.
