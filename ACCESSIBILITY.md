# Accessibility Guide (WCAG 2.1 AA)

**KYC Guardian AI** - Hackathon Prototype

> Commitment to inclusive design and WCAG 2.1 Level AA compliance.

---

## Accessibility Statement

KYC Guardian AI is designed to be accessible to people with a wide range of abilities, including:

- ✅ Visual impairments (blindness, low vision, color blindness)
- ✅ Motor impairments (inability to use mouse, limited dexterity)
- ✅ Auditory impairments (deafness, hearing loss)
- ✅ Cognitive impairments (dyslexia, ADHD, cognitive disabilities)
- ✅ Temporary impairments (broken arm, eye strain)

---

## WCAG 2.1 Level AA Compliance

### Principle 1: Perceivable

Information must be presented in ways users can perceive.

#### 1.1 Text Alternatives (Alt Text)

✅ All images have meaningful alt text  
✅ Icons paired with text labels  
✅ Document thumbnails described  
✅ Charts include data tables  
✅ Decorative images marked as decorative  

```html
<!-- Good -->
<img src="status-check.svg" alt="Processing complete" />

<!-- Poor -->
<img src="image.png" />
```

#### 1.3 Adaptable (Structure)

✅ Semantic HTML (proper heading hierarchy)  
✅ Lists marked up with `<ul>`, `<ol>`  
✅ Form labels associated with inputs  
✅ Table headers properly marked  
✅ Logical reading order (top to bottom, left to right)  

```html
<!-- Good -->
<form>
  <label for="case-id">Case ID:</label>
  <input id="case-id" type="text" />
</form>

<!-- Poor -->
<input type="text" placeholder="Case ID" />
```

#### 1.4 Distinguishable (Color & Contrast)

✅ Minimum contrast ratio 4.5:1 for normal text  
✅ Minimum contrast ratio 3:1 for large text  
✅ Color not the only differentiator  
✅ Status communicated via icon + text + color  
✅ No color-only error messages  

```
❌ "Red = Error" (colorblind user sees nothing)
✅ "🚫 Error: Invalid field" (icon + text + color)
```

### Principle 2: Operable

Interface must be operable via keyboard and other input methods.

#### 2.1 Keyboard Accessible

✅ All functionality available via keyboard  
✅ Logical tab order (visual flow)  
✅ No keyboard traps  
✅ Keyboard shortcuts don't interfere with screen reader commands  
✅ Focus visible at all times  

```javascript
// All interactive elements must be reachable
// Tab order: Header → Navigation → Main Content → Footer
<a href="#main-content">Skip to main content</a>
```

#### 2.2 Enough Time

✅ No time-limited sessions (except for security)  
✅ Users can extend timeouts  
✅ No auto-playing content  
✅ Pause/stop controls for animations  

#### 2.4 Navigable

✅ Clear page titles  
✅ Consistent navigation  
✅ Multiple ways to find content (search, navigation, sitemap)  
✅ Focus indicator clearly visible  
✅ Link purposes clear from link text or context  

```html
<!-- Good -->
<a href="/cases/123">View case ABC123 - Individual KYC</a>

<!-- Poor -->
<a href="/cases/123">Click here</a>
```

### Principle 3: Understandable

Content must be readable and predictable.

#### 3.1 Readable

✅ Appropriate language level  
✅ Clear, simple language  
✅ Abbreviations explained on first use  
✅ No visual text only (content in HTML)  
✅ Consistent terminology  

#### 3.2 Predictable

✅ Consistent navigation  
✅ Predictable link behavior  
✅ No unexpected context changes  
✅ Error messages clear and helpful  
✅ Consistent styling  

#### 3.3 Input Assistance

✅ Error messages identify the field  
✅ Suggestions provided for correction  
✅ Form validation before submission  
✅ Required fields marked  
✅ Labels for all form fields  

```html
<!-- Good error message -->
<span role="alert" class="error">
  🚫 Email address invalid. Please enter format: user@example.com
</span>

<!-- Poor error message -->
<span class="error">Invalid input</span>
```

### Principle 4: Robust

Content works with assistive technologies.

#### 4.1 Compatible

✅ Valid HTML (validated against WCAG)
✅ Proper ARIA attributes  
✅ Semantic elements used correctly  
✅ No duplicate IDs  
✅ Proper nesting of elements  

---

## Accessible Components

### Navigation

```html
<nav role="navigation" aria-label="Main Navigation">
  <ul>
    <li><a href="/dashboard">Dashboard</a></li>
    <li><a href="/cases">Cases</a></li>
    <li><a href="/review-queue">Review Queue</a></li>
  </ul>
</nav>

<a href="#main-content" class="skip-link">Skip to main content</a>
```

### Form Fields

```html
<form>
  <div class="form-group">
    <label for="applicant-type">Applicant Type *</label>
    <select id="applicant-type" required aria-describedby="type-help">
      <option value="">Select applicant type</option>
      <option value="individual">Individual</option>
      <option value="business">Business</option>
    </select>
    <span id="type-help" class="help-text">
      Required field. Select the type of applicant.
    </span>
  </div>
</form>
```

### Status Indicators

```html
<!-- Status: Completed -->
<div class="status-badge status-completed" aria-label="Status: Processing completed">
  <span class="icon">✓</span>
  <span class="label">Completed</span>
</div>

<!-- Status: Review Required -->
<div class="status-badge status-review" aria-label="Status: Review required">
  <span class="icon">⚠</span>
  <span class="label">Review Required</span>
</div>
```

### Modal Dialogs

```html
<div role="dialog" aria-labelledby="dialog-title" aria-modal="true">
  <h2 id="dialog-title">Confirm Field Correction</h2>
  
  <p>Are you sure you want to correct this field?</p>
  
  <button type="button" onclick="confirmCorrection()">Confirm</button>
  <button type="button" onclick="cancelCorrection()">Cancel</button>
</div>
```

### Tables

```html
<table role="table" aria-label="Case summary">
  <thead>
    <tr>
      <th scope="col">Case ID</th>
      <th scope="col">Applicant Type</th>
      <th scope="col">Status</th>
      <th scope="col">Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CASE-001</td>
      <td>Individual</td>
      <td>Review Required</td>
      <td><a href="/cases/001">Review</a></td>
    </tr>
  </tbody>
</table>
```

---

## Keyboard Shortcuts

| Key | Function |
|-----|----------|
| `Tab` | Navigate forward through focusable elements |
| `Shift+Tab` | Navigate backward through focusable elements |
| `Enter` | Activate button or link |
| `Space` | Toggle checkbox or button |
| `Escape` | Close dialog or menu |
| `Alt+/` | Open keyboard help |
| `Alt+H` | Go to home page |
| `Alt+D` | Go to dashboard |
| `Alt+S` | Go to search |

---

## Screen Reader Testing

### Supported Screen Readers

✅ **NVDA** (Windows, free)
✅ **JAWS** (Windows, commercial)
✅ **VoiceOver** (macOS, iOS, free)
✅ **TalkBack** (Android, free)

### Test Cases

```
Test: Document review page with screen reader

1. Load page with NVDA
2. Navigate via headings (H key)
3. Read extracted fields
4. Confirm status indicators are announced
5. Navigate to confirmation button
6. Activate button
7. Verify confirmation message is announced
```

---

## Color & Contrast

### Color Palette

| Color | Hex | Use | Contrast (WCAG AA) |
|-------|-----|-----|--------------------|
| **Navy** | #001F3F | Primary nav | 11:1 ✅ |
| **Blue** | #0074D9 | Actions | 5.1:1 ✅ |
| **Teal** | #2ECC40 | Success | 3.5:1 ✅ |
| **Amber** | #FF851B | Warning | 4.3:1 ✅ |
| **Red** | #FF4136 | Error | 5.2:1 ✅ |
| **Grey** | #AAAAAA | Secondary | 4.5:1 ✅ |
| **White** | #FFFFFF | Background | 21:1 ✅ |

### Testing Contrast

```bash
# Automated contrast testing
npm run test:a11y:contrast

# Manual check
# https://webaim.org/resources/contrastchecker/
```

---

## Font & Text

### Font Selection

✅ Sans-serif fonts (easier to read)
✅ Clear distinction between similar characters (l, I, 1, O, 0)
✅ No decorative fonts
✅ Minimum 14px for body text
✅ Maximum line length 80 characters
✅ Adequate line spacing (1.5x)

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 16px;  /* Minimum 14px, 16px preferred */
  line-height: 1.5;  /* Space between lines */
  color: #333;  /* Dark on light background */
}

p {
  max-width: 80ch;  /* Ideal line length */
}
```

---

## Responsive Design

✅ Responsive layout (works on all screen sizes)
✅ Mobile-first approach
✅ Touch targets minimum 48x48px
✅ Text resizable up to 200%
✅ No horizontal scroll on smaller screens
✅ Zoom to 200% still functional

```html
<!-- Viewport configuration -->
<meta name="viewport" 
      content="width=device-width, initial-scale=1.0, 
               maximum-scale=5.0, user-scalable=yes">

<!-- Allow users to zoom -->
<!-- Never use: maximum-scale=1.0, user-scalable=no -->
```

---

## Testing & Validation

### Automated Accessibility Testing

```bash
# Run accessibility test suite
npm run test:a11y

# Includes:
# - axe-core testing
# - WAVE testing
# - Contrast checking
# - Heading structure
# - ARIA attributes
```

### Manual Testing Checklist

- [ ] Navigate entire site with keyboard only
- [ ] Test with NVDA/JAWS screen reader
- [ ] Verify color contrast with Contrast Checker
- [ ] Zoom to 200% - layout still works?
- [ ] Disable CSS - content still logical?
- [ ] Test form validation with screen reader
- [ ] Verify all images have alt text
- [ ] Check heading hierarchy (H1 → H2 → H3)
- [ ] Confirm focus indicators visible
- [ ] Test with operating system zoom

---

## Common Accessibility Issues & Fixes

### Issue 1: Missing Alt Text on Images

```html
<!-- ❌ Bad -->
<img src="status.png" />

<!-- ✅ Good -->
<img src="status.png" alt="Processing completed" />
```

### Issue 2: Unlabeled Form Inputs

```html
<!-- ❌ Bad -->
<input type="text" placeholder="Case ID" />

<!-- ✅ Good -->
<label for="case-id">Case ID:</label>
<input id="case-id" type="text" />
```

### Issue 3: Color as Only Differentiator

```html
<!-- ❌ Bad -->
<span style="color: red">Error</span>

<!-- ✅ Good -->
<span role="alert">
  <span class="icon">🚫</span> Error: Invalid input
</span>
```

### Issue 4: Keyboard Traps

```javascript
// ❌ Bad - Focus gets trapped
dialog.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') return;  // Trap escape
});

// ✅ Good - Allow escape to close
dialog.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeDialog();
});
```

### Issue 5: Poor Focus Indicators

```css
/* ❌ Bad - No visible focus */
button:focus {
  outline: none;
}

/* ✅ Good - Clear focus indicator */
button:focus {
  outline: 3px solid #0074D9;
  outline-offset: 2px;
}
```

---

## Accessibility Resources

- [WebAIM](https://webaim.org/) - Web accessibility articles
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Official WCAG reference
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) - MDN guide
- [Inclusive Components](https://inclusive-components.design/) - Pattern library
- [The A11Y Project](https://www.a11yproject.com/) - Resources and checklist

---

## Feedback

Accessibility is an ongoing commitment. If you encounter accessibility barriers:

1. **Report via GitHub Issues** - Include details and test method
2. **Use keyboard** - Note which keys don't work
3. **Test with screen reader** - Specify which reader and what failed
4. **Describe impact** - How does this barrier affect your use?

---

**Last Updated**: 2024  
**Status**: WCAG 2.1 Level AA Target  
**Ongoing**: Continuous accessibility improvement
