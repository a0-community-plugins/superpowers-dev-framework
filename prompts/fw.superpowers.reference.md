# Superpowers Framework Reference

Superpowers is a composable development workflow framework providing skills for disciplined, high-quality software development. It emphasizes TDD, systematic debugging, fresh subagent contexts, and two-stage code review.

## Core Workflow

The standard Superpowers development workflow follows this progression:

1. **Brainstorm** -- Collaboratively explore the idea, ask questions one at a time, propose 2-3 approaches, present design in sections for validation
2. **Plan** -- Write a detailed implementation plan with bite-sized TDD tasks, exact file paths, complete code, and verification commands
3. **Execute** -- Implement plan tasks using subagent-driven development (fresh subagent per task) or batch execution with checkpoints
4. **Review** -- Two-stage review after each task: spec compliance first, then code quality
5. **Finish** -- Verify tests, present merge/PR/keep/discard options, clean up worktrees

## Available Skills

### Process Skills (use these first)

- **Brainstorming** -- Turn ideas into designs through collaborative dialogue. One question at a time, explore 2-3 approaches, present design in 200-300 word sections.
- **Writing Plans** -- Create comprehensive implementation plans with bite-sized TDD tasks for engineers with zero codebase context.
- **Executing Plans** -- Load plan, review critically, execute in batches of 3, report for review between batches.
- **Subagent-Driven Development** -- Execute plans by dispatching fresh subagent per task with two-stage review (spec compliance then code quality).
- **Dispatching Parallel Agents** -- Dispatch one agent per independent problem domain for concurrent investigation of unrelated failures.

### Discipline Skills (follow exactly)

- **Test-Driven Development** -- Write test first, watch it fail, write minimal code to pass. No production code without a failing test first. No exceptions.
- **Systematic Debugging** -- Four-phase process: root cause investigation, pattern analysis, hypothesis testing, implementation. No fixes without root cause first.
- **Verification Before Completion** -- Evidence before claims, always. Run the command, read the output, then claim the result. No shortcuts.

### Review Skills

- **Requesting Code Review** -- Dispatch code-reviewer subagent with implementation details, plan reference, and git SHAs. Review early, review often.
- **Receiving Code Review** -- Verify before implementing, ask before assuming. Technical evaluation, not performative agreement. Push back when feedback is technically wrong.

### Completion Skills

- **Using Git Worktrees** -- Create isolated workspaces with systematic directory selection and safety verification. Always verify gitignore and baseline tests.
- **Finishing a Development Branch** -- Verify tests, present 4 structured options (merge/PR/keep/discard), execute choice, clean up worktree.

### Meta Skills

- **Writing Skills** -- TDD applied to process documentation. Write pressure-test scenarios, watch agents fail, write skill, verify compliance, close loopholes.
- **Using Superpowers** -- How to find and use skills. Invoke relevant skills BEFORE any response or action. Even 1% chance means check.

## Key Principles

1. **Test-Driven Development** -- No production code without a failing test first. Write test, watch fail, write minimal code, watch pass, refactor.
2. **Fresh Subagent Per Task** -- Each implementation task gets a fresh subagent with no context pollution from previous tasks.
3. **Two-Stage Review** -- After each task: spec compliance review first (does it match requirements?), then code quality review (is it well-built?).
4. **Systematic Over Guessing** -- Always find root cause before fixing. Scientific method: hypothesis, minimal test, verify. No random fixes.
5. **Evidence Before Claims** -- Run verification commands fresh. Read output. Then make claims. No "should work" or "looks correct."
6. **YAGNI Ruthlessly** -- Remove unnecessary features from all designs. If it's not needed now, don't build it.

## Code Reviewer Agent

The **sp_code_reviewer** agent is available for dispatching as a subagent. It reviews completed work against plans, checking plan alignment, code quality, architecture, documentation, and providing categorized feedback (Critical/Important/Suggestions).
