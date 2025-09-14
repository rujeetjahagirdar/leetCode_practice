# LangChain PR #32660 - Required Changes Summary

## Issue
The maintainer (@mdrxy) has requested the addition of a required section called "## Use within an agent" in the Notion integration documentation.

## Required Changes

### 1. Fix Installation Command
In the "Setup" section, change:
```markdown
%pip install --quiet -U langchain-community
```
To:
```markdown
%pip install --quiet -U langchain-notion
```

### 2. Fix Credentials Comment
In the "Credentials" section, change:
```markdown
This integration requires you to set NOTION_API_KEY as an environment variable to authenticate with the Discord API.
```
To:
```markdown
This integration requires you to set NOTION_API_KEY as an environment variable to authenticate with the Notion API.
```

### 3. Fix Environment Variable Setup
Uncomment and fix the environment variable setup:
```python
if not os.environ.get("NOTION_API_KEY"):
    os.environ["NOTION_API_KEY"] = getpass.getpass("NOTION API key:\n")
```

### 4. Fix Code Examples
Remove the error-throwing code and make examples functional:
- Remove the ModuleNotFoundError traceback
- Fix the tool invocation examples to use correct parameter names (`query` instead of `tool_input`)

### 5. Rename "Chaining" Section to "Use within an agent"
The main structural change requested:
- Change the section header from "## Chaining" to "## Use within an agent"
- Keep all the existing content that shows how to use the toolkit with an agent

### 6. Improve Documentation Clarity
- Add better explanations for each step
- Make the agent usage example more comprehensive
- Ensure all code examples are functional and don't show errors

## Key Changes Made

1. **Section Rename**: "Chaining" → "Use within an agent"
2. **Package Fix**: "langchain-community" → "langchain-notion" 
3. **API Fix**: "Discord API" → "Notion API"
4. **Parameter Fix**: "tool_input" → "query" (for search tool)
5. **Code Cleanup**: Remove error outputs and make examples functional
6. **Environment Setup**: Make the API key setup functional

These changes align the documentation with the standard LangChain integration documentation format and address the maintainer's specific request for the "Use within an agent" section.