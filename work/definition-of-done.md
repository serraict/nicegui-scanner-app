# Definition of Done

This document defines our shared understanding of what it means to complete a backlog item (increment).
1.
- Each increment should result in a **working, runnable application**
- Focus on delivering value, not perfect code
- Iterate and improve based on learnings from each increment

## Completion Criteria

An increment is considered **done** when:

### ✅ Functionality

- [ ] Feature works as described in backlog item
- [ ] All acceptance criteria are met
- [ ] No breaking changes to existing functionality

## Testing Approach

We prioritize **working software over comprehensive testing**:

1. **Manual verification** is our primary testing approach
2. **Integration testing** by running the full app and verifying features work together
3. **Working examples** serve as living documentation and regression tests
4. Automated testing may be added later if the project grows in complexity

### ✅ Documentation

- [ ] **User documentation** - Usage instructions added to readme if needed
- [ ] **Code documentation** - Complex logic has inline comments
- [ ] **Architecture updates** - CLAUDE.md updated if patterns changed

### ✅ Code Quality

- [ ] Code follows existing patterns and conventions
- [ ] Use NiceGUI/Quasar styles and components where possible instead of custom CSS
- [ ] Use Quasar components (q-select, q-btn, etc.) instead of plain HTML elements in Vue templates
- [ ] No obvious performance issues
- [ ] Clean, readable implementation

### ✅ Project Management

- [ ] doing.md updated with completion status
- [ ] Work committed to git with descriptive message
- [ ] Ready for next increment
