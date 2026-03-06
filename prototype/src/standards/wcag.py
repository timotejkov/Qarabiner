"""WCAG 2.2 Level AA — Web Content Accessibility Guidelines.

Comprehensive coverage of WCAG 2.2 Level AA success criteria with practical testing methods
and detailed information about common failure patterns.
"""

STANDARD_ID = "WCAG 2.2"

SECTIONS: dict[str, dict] = {
    "wcag:2.2": {
        "title": "Web Content Accessibility Guidelines (WCAG) 2.2 Level AA",
        "part": "Accessibility Standards",
        "sections": {
            "1_perceivable": {
                "title": "Principle 1: Perceivable",
                "part": "Principle 1",
                "clause": "Information Accessibility",
                "content": (
                    "Information and user interface components must be presentable to users in ways they can perceive. "
                    "This principle addresses the need for accessible perception through multiple sensory channels. "
                    "Visual content must be perceivable to users with color blindness, low vision, or complete blindness. "
                    "Audio content must be accessible to deaf and hard of hearing users through transcripts and captions. "
                    "Time-based media must have alternatives and synchronization. "
                    "Content must be adaptable to different screen sizes and magnification levels. "
                    "All color-based information must have redundant indicators. "
                    "Contrast must be sufficient for visibility. Testing: verify text alternatives for non-text content, captions for multimedia, "
                    "sufficient color contrast (4.5:1 for normal text, 3:1 for large text), content reflow at 320px width without horizontal scrolling. "
                    "Perceivability is foundational to accessibility as content must be perceivable before it can be operable, understandable, or robust."
                ),
                "keywords": [
                    "perceivable", "contrast", "alt text", "captions", "reflow", "adaptable content",
                    "text alternatives", "color blindness", "visual perception", "audio alternatives",
                    "multimedia", "content presentation"
                ],
            },
            "1_1_text_alternatives": {
                "title": "1.1: Text Alternatives",
                "part": "1.1",
                "clause": "Alternative Text for Images",
                "content": (
                    "All non-text content must have text alternatives that serve an equivalent purpose. Text alternatives are essential for users who cannot "
                    "see images, icons, charts, diagrams, maps, and other visual content. Screen readers read alt text to convey the content and purpose of images. "
                    "Success Criteria 1.1.1 (Level A) requires text alternatives for all images of text, buttons, decorative images, image maps, and other images. "
                    "For decorative images that don't convey information, alt text should be empty (alt='') to prevent screen readers from announcing them. "
                    "For informative images, alt text should concisely describe the image content and purpose. "
                    "For complex images like charts or diagrams, alt text should provide a text alternative that conveys the essential information. "
                    "Image text (text appearing in images) must either have alt text containing the same text or have text alternatives elsewhere. "
                    "Testing: verify all images have alt text, verify alt text is descriptive and meaningful, verify decorative images have empty alt text, "
                    "verify complex images have adequate descriptions, test with screen reader to ensure text alternatives are conveyed properly. "
                    "Common failures: missing alt text, meaningless alt text (e.g., 'image' or filename), alt text that doesn't convey image purpose, "
                    "null alt text on informative images."
                ),
                "keywords": [
                    "text alternatives", "alt text", "image alternatives", "screen reader", "image description",
                    "decorative images", "informative images", "complex images", "image of text", "ARIA labels"
                ],
            },
            "1_2_time_based_media": {
                "title": "1.2: Time-Based Media",
                "part": "1.2",
                "clause": "Audio and Video Alternatives",
                "content": (
                    "All time-based media (audio and video content) must have accessible alternatives. Time-based media presents unique accessibility challenges "
                    "as the content unfolds over time and users with hearing impairments cannot access audio, while users with vision impairments cannot access video. "
                    "Success Criteria 1.2.1 (Level A) requires either captions or an audio description for pre-recorded video-only content. "
                    "Success Criteria 1.2.2 (Level A) requires captions for all pre-recorded audio in videos. Captions must include all dialogue, music cues, "
                    "sound effects, and other audio information. Captions should be synchronized with the audio. "
                    "Success Criteria 1.2.3 (Level A) requires either audio descriptions or a transcript for pre-recorded video content. Audio descriptions "
                    "describe visual information for blind and low vision users. An alternative is providing a transcript of both audio and visual content. "
                    "Success Criteria 1.2.4 (Level AA) requires captions for all live video. Success Criteria 1.2.5 (Level AA) requires audio descriptions "
                    "for pre-recorded video. "
                    "Testing: verify captions are present and synchronized with audio, verify captions include all dialogue and essential audio information, "
                    "verify audio descriptions are provided, verify transcripts are complete and accurate, test with video player controls and caption toggle. "
                    "Common failures: missing captions, out-of-sync captions, incomplete captions missing sound effects or speaker identification, "
                    "missing audio descriptions, inaccurate transcripts."
                ),
                "keywords": [
                    "captions", "audio description", "transcript", "pre-recorded video", "live video",
                    "synchronized captions", "audio alternatives", "multimedia alternatives",
                    "video player", "audio track", "sign language"
                ],
            },
            "1_3_adaptable": {
                "title": "1.3: Adaptable",
                "part": "1.3",
                "clause": "Content Adaptability",
                "content": (
                    "Content must be adaptable to different presentations and must not rely on a single sensory channel or presentation. Content must work "
                    "at different screen sizes, zoom levels, and with assistive technologies. This allows content to be accessed by users with different "
                    "disabilities and on different devices. "
                    "Success Criteria 1.3.1 (Level A) requires that information, structure, and relationships are conveyed through markup and not just visual presentation. "
                    "This means proper semantic HTML must be used with headings, lists, landmarks, and other semantic elements. Information conveyed through visual "
                    "position or styling must also be available programmatically. "
                    "Success Criteria 1.3.2 (Level A) requires that the sequence in which content is presented is meaningful and logical. Screen reader users experience "
                    "content in source order, so content must read logically in source order. "
                    "Success Criteria 1.3.3 (Level A) requires that instructions don't rely solely on shape, size, visual location, or orientation. Instructions "
                    "must not say 'click the round button' but should provide additional identification like labels or position references. "
                    "Testing: verify semantic HTML structure, verify content reads logically in source order, verify information is conveyed through markup not just visuals, "
                    "verify zoom works to 200%, verify instructions don't rely on sensory characteristics alone. "
                    "Common failures: layout using HTML tables instead of CSS, visually presented information not conveyed in markup, content not in logical reading order, "
                    "instructions referring only to shape or color."
                ),
                "keywords": [
                    "adaptable", "semantic HTML", "structure", "relationships", "headings", "lists",
                    "reading order", "zoom", "responsive design", "content structure", "landmarks",
                    "logical sequence", "programmatic relationships"
                ],
            },
            "1_4_distinguishable": {
                "title": "1.4: Distinguishable",
                "part": "1.4",
                "clause": "Visual Clarity and Contrast",
                "content": (
                    "Content must be distinguishable and users must be able to see and hear content including distinguishing foreground from background. "
                    "Color contrast, text sizing, and visual distinction are essential for users with color blindness, low vision, and cognitive disabilities. "
                    "Success Criteria 1.4.1 (Level A) requires that color is not the only means of conveying information. Visual information conveyed through color "
                    "must have redundant indicators such as text labels, icons, or patterns. This ensures color blind users can access the information. "
                    "Success Criteria 1.4.3 (Level AA) requires minimum contrast ratios: 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt+ bold), "
                    "and 3:1 for graphics and UI components. Low contrast text is difficult for users with low vision to read. "
                    "Success Criteria 1.4.4 (Level AA) requires that text can be resized up to 200% without loss of functionality. Users with low vision often zoom content. "
                    "Success Criteria 1.4.5 (Level AA) requires that images of text have sufficient contrast and that text is used instead of images of text where possible. "
                    "Success Criteria 1.4.10 (Level AA) requires that content reflows without horizontal scrolling at 320px width and text can be reflowed at 50% zoom. "
                    "Success Criteria 1.4.11 (Level AA) requires 3:1 contrast for non-text elements, graphics, and UI component borders. "
                    "Testing: verify color contrast ratios with color contrast analyzer tools, verify content at 200% zoom, verify at 320px width, "
                    "verify information not conveyed by color alone, test with color blind simulator. "
                    "Common failures: low contrast text, text that can't be resized, horizontal scrolling at 320px, information conveyed only by color, "
                    "images of text without alternatives."
                ),
                "keywords": [
                    "contrast", "color contrast", "distinguishable", "visual distinction", "color blindness",
                    "text size", "zoom", "reflow", "responsive", "color alone", "graphics contrast",
                    "UI contrast", "WCAG AA", "contrast ratio"
                ],
            },
            "2_operable": {
                "title": "Principle 2: Operable",
                "part": "Principle 2",
                "clause": "User Control and Navigation",
                "content": (
                    "User interface components and navigation must be operable through keyboard, mouse, voice, and other input methods. Users must be able to navigate "
                    "through content and interact with controls. This is essential for users who cannot use a mouse, including users with motor impairments, "
                    "blind users using keyboard navigation, and users with voice control. "
                    "Keyboard accessibility is fundamental to operability. All functionality must be available through keyboard. Screen reader users rely on keyboard "
                    "navigation. Users with motor impairments may use alternate keyboards or switch controls. "
                    "Navigation must be logical and predictable. Users must be able to understand how to navigate and find content. Skip links should allow users "
                    "to skip repetitive content. "
                    "There must be no content that flashes more than three times per second to prevent seizures in users with photosensitive epilepsy. "
                    "Users must have sufficient time to interact with content. Auto-playing media can be problematic. "
                    "Testing: verify all functionality is available through keyboard, verify keyboard focus is visible, verify no keyboard traps, "
                    "verify skip navigation links, verify no flashing content, verify sufficient time for interactions. "
                    "Operability enables users with various disabilities to interact with content and is prerequisite for understanding content."
                ),
                "keywords": [
                    "operable", "keyboard accessible", "focus", "navigation", "timing", "seizures",
                    "motor disabilities", "keyboard only", "skip links", "predictable", "navigable"
                ],
            },
            "2_1_keyboard_accessible": {
                "title": "2.1: Keyboard Accessible",
                "part": "2.1",
                "clause": "Keyboard Navigation",
                "content": (
                    "All functionality of content must be operable through a keyboard interface and keyboard only. Keyboard accessibility is essential for users "
                    "with motor disabilities, blind users, and users using assistive technologies like screen readers. "
                    "Success Criteria 2.1.1 (Level A) requires that all functionality is available via keyboard except where the underlying function requires "
                    "input dependent on the path of user movement (like freehand drawing). Every button, link, form field, and interactive component must be "
                    "accessible and operable through keyboard. "
                    "Success Criteria 2.1.2 (Level A) requires no keyboard traps. When users navigate with keyboard, they must be able to move focus away from "
                    "each component using only keyboard. Traps occur when focus cannot be moved away with standard keyboard navigation. "
                    "Success Criteria 2.1.3 (Level AAA) requires that keyboard functionality is available without a specific timing requirement (no time-dependent input). "
                    "Testing: navigate through all content using only keyboard (Tab, Enter, Space, arrow keys), verify all interactive elements are reachable by keyboard, "
                    "verify focus is visible while navigating, verify no keyboard traps, verify keyboard shortcuts don't conflict with browser shortcuts. "
                    "Common failures: mouse-only functionality, no visible focus indicator, keyboard trap in modal dialog, keyboard shortcuts that override browser navigation, "
                    "drag-and-drop requiring mouse."
                ),
                "keywords": [
                    "keyboard accessible", "keyboard navigation", "TAB key", "keyboard shortcuts",
                    "keyboard trap", "focus management", "keyboard only", "motor disabilities",
                    "assistive technology", "keyboard operation"
                ],
            },
            "2_2_enough_time": {
                "title": "2.2: Enough Time",
                "part": "2.2",
                "clause": "Time Limits and Pausing",
                "content": (
                    "Users must have sufficient time to read and use content. Time limits can be problematic for users with cognitive disabilities, low vision, "
                    "motor disabilities, or those using assistive technologies that slow down interaction. "
                    "Success Criteria 2.2.1 (Level A) requires that there is no time limit for interacting with content, or if there is a time limit, "
                    "the user can turn it off, extend it, or adjust it to at least 10 times the default. Time limits for authentication (like session timeouts) "
                    "are exceptions if they are part of a real-time event. "
                    "Success Criteria 2.2.2 (Level A) requires controls to pause, stop, or hide any moving, blinking, or auto-updating content that starts automatically "
                    "and lasts more than 5 seconds. This includes auto-playing video, scrolling text, animated advertisements, and other auto-updating content. "
                    "Success Criteria 2.2.3 (Level AAA) requires no time limits except for real-time events and user-initiated events. "
                    "Success Criteria 2.2.5 (Level AAA) requires re-authentication not to cause loss of data. If the user's session expires during a transaction, "
                    "they should be able to log back in and resume without losing their data. "
                    "Testing: identify any time limits and verify they meet requirements, verify auto-starting media can be paused, verify sufficient time for interactions, "
                    "test with screen reader which may slow down interaction. "
                    "Common failures: session timeout without ability to extend, auto-playing video without pause control, no way to turn off time limits, "
                    "data loss after re-authentication."
                ),
                "keywords": [
                    "time limits", "enough time", "session timeout", "auto-playing media", "pause",
                    "stop", "hide", "auto-updating", "blinking", "animated content", "cognitive disability",
                    "re-authentication", "data preservation"
                ],
            },
            "2_3_seizures_physical_reactions": {
                "title": "2.3: Seizures and Physical Reactions",
                "part": "2.3",
                "clause": "Photosensitive Seizures",
                "content": (
                    "Content must not contain anything that flashes more than three times per second in a way that is likely to cause photosensitive seizures. "
                    "Some users have photosensitive epilepsy where exposure to flashing lights can trigger seizures. This is a critical safety issue. "
                    "Success Criteria 2.3.1 (Level A) requires no content that flashes more than three times per second. This applies to the entire screen or "
                    "any region of the screen. Even if the flashing region is small, three or more flashes in one second can be dangerous. "
                    "The guideline uses a complex mathematical formula to determine flash rate and flashing region size. Generally, avoid any flashing or use "
                    "extremely cautious flashing limited to very small areas. "
                    "Success Criteria 2.3.2 (Level AAA) requires no animation that could cause vestibular disorders (dizziness, disorientation, nausea). "
                    "Testing: review content for any flashing or animated GIFs, check for flashing in all regions including advertisements, test video content "
                    "for flashing, use tools to analyze flash frequency. "
                    "Common failures: animated GIFs that flash, scrolling text that flashes, advertisement animations that flash, video content with flashing lights, "
                    "animation effects that could trigger seizures."
                ),
                "keywords": [
                    "seizures", "photosensitive", "flashing", "three times per second", "epilepsy",
                    "animated GIF", "animation", "vestibular disorder", "dizziness", "animation effects",
                    "video flashing", "critical safety"
                ],
            },
            "2_4_navigable": {
                "title": "2.4: Navigable",
                "part": "2.4",
                "clause": "Page Navigation and Structure",
                "content": (
                    "Users must be able to navigate through content and locate information. Navigation must be consistent, predictable, and easy to find. "
                    "This is essential for users with cognitive disabilities and all users trying to locate specific information. "
                    "Success Criteria 2.4.1 (Level A) requires skip navigation links to allow users to skip repetitive content like navigation menus. "
                    "When navigating through a page with a screen reader, users must listen through the entire navigation menu each time they visit a new page. "
                    "A skip link allows users to jump directly to main content, saving time and frustration. "
                    "Success Criteria 2.4.2 (Level A) requires that each page has a unique, descriptive title. The page title helps users understand the page purpose "
                    "and is often the first thing a screen reader announces. "
                    "Success Criteria 2.4.3 (Level A) requires that focus order is logical and meaningful. When navigating with Tab key, focus should move through "
                    "components in a logical order that follows the visual layout and content meaning. "
                    "Success Criteria 2.4.4 (Level A) requires descriptive link text. Link purpose must be clear from the link text alone. Links with text like "
                    "'click here' or 'read more' don't convey their purpose. Link text should describe where the link goes or what it does. "
                    "Success Criteria 2.4.5 (Level AA) requires multiple ways to find a page, such as search functionality, navigation menu, site map, or list of related pages. "
                    "Success Criteria 2.4.6 (Level AA) requires visible focus indicators. When navigating with keyboard, the currently focused element must be clearly visible. "
                    "Success Criteria 2.4.7 (Level AA) requires visible focus indicator for keyboard. This is especially important for keyboard navigation. "
                    "Testing: verify skip navigation links are present and functional, verify page titles are descriptive, navigate with Tab key and verify focus order, "
                    "verify focus is visible, verify link text describes link purpose, verify multiple ways to find pages. "
                    "Common failures: missing skip links, non-descriptive page title, focus order doesn't match visual order, missing or invisible focus indicator, "
                    "link text is 'click here', no navigation or site map."
                ),
                "keywords": [
                    "navigable", "skip links", "page title", "focus order", "link text", "descriptive links",
                    "focus indicator", "visible focus", "keyboard navigation", "site navigation",
                    "multiple navigation methods", "site map", "navigation consistency"
                ],
            },
            "2_5_input_modalities": {
                "title": "2.5: Input Modalities",
                "part": "2.5",
                "clause": "Alternative Input Methods",
                "content": (
                    "Users must be able to interact with content using multiple input modalities including keyboard, mouse, voice, and touch. This supports users "
                    "with different abilities and allows use of different devices. "
                    "Success Criteria 2.5.1 (Level A) requires that pointer-based gestures (like drag and drop, pinch to zoom) have keyboard equivalents. "
                    "Users with motor disabilities may not be able to perform complex gestures. "
                    "Success Criteria 2.5.2 (Level A) requires that content doesn't require specific touch gestures unless there is a keyboard equivalent. "
                    "Success Criteria 2.5.3 (Level A) requires that for content using motion or orientation sensors, there must be a UI control for the same functionality. "
                    "Success Criteria 2.5.4 (Level A) requires that target size is at least 44 x 44 pixels (CSS pixels). Small targets are difficult to click for users "
                    "with motor disabilities or those using touchscreens. "
                    "Success Criteria 2.5.5 (Level AAA) requires label and name for all components. "
                    "Testing: verify pointer-based interactions have keyboard alternatives, verify no pointer-only functionality, verify touch targets are at least "
                    "44 x 44 pixels, verify components can be identified by name. "
                    "Common failures: drag-and-drop without keyboard alternative, pinch-zoom required without keyboard control, touch gestures without alternatives, "
                    "tiny tap targets, motion-based functionality without keyboard alternative."
                ),
                "keywords": [
                    "input modalities", "pointer gestures", "touch gestures", "gesture alternatives",
                    "keyboard equivalent", "motion sensors", "orientation", "target size", "touch target",
                    "motor disability", "voice input", "alternative input"
                ],
            },
            "3_understandable": {
                "title": "Principle 3: Understandable",
                "part": "Principle 3",
                "clause": "Content Clarity",
                "content": (
                    "Information and user interface operation must be understandable to users. Content must be written clearly, navigation must be predictable, "
                    "and input must be assisted. This is essential for users with cognitive disabilities, learning disabilities, language barriers, and all users. "
                    "Clear language, simple design, and proper formatting help all users understand content. Users with cognitive disabilities benefit most from "
                    "clear, simple content that avoids jargon and complex structures. "
                    "Navigation and site functionality must be consistent and predictable so users can understand how to interact with the site. "
                    "When input is required, the site must help users avoid and correct mistakes. Error messages must be clear and helpful. "
                    "Testing: review text for clarity and readability, verify consistent navigation, verify form labels and instructions are clear, "
                    "verify error messages are helpful, test with users with cognitive disabilities. "
                    "Understanding content is prerequisite for users to complete tasks and achieve their goals online."
                ),
                "keywords": [
                    "understandable", "readable", "predictable", "simple", "clear language",
                    "cognitive disability", "learning disability", "navigation consistency", "form labels",
                    "error messages", "input assistance", "readability"
                ],
            },
            "3_1_readable": {
                "title": "3.1: Readable",
                "part": "3.1",
                "clause": "Language and Readability",
                "content": (
                    "Text must be readable and understandable. This includes declaring the language of the page, simplifying text, and using clear language. "
                    "Success Criteria 3.1.1 (Level A) requires that the primary language of the page is identified using the HTML lang attribute. "
                    "Screen readers use this to pronounce words correctly. If the language is not declared, screen readers may use the wrong language, making "
                    "content unintelligible. "
                    "Success Criteria 3.1.2 (Level AA) requires identifying changes in language within the page. If a page contains text in multiple languages, "
                    "each language change must be marked with the lang attribute so screen readers pronounce it correctly. "
                    "Success Criteria 3.1.3 (Level AAA) requires defining uncommon words, abbreviations, acronyms, and technical terms. Words with special meanings "
                    "in a particular context should be defined using <dfn>, <abbr>, or other mechanisms. "
                    "Success Criteria 3.1.4 (Level AAA) requires that abbreviations are expanded at least once on the page. "
                    "Success Criteria 3.1.5 (Level AAA) requires text be simple enough for users with reading disabilities to understand. This might include using "
                    "simpler vocabulary, shorter sentences, avoiding jargon, and using illustrations to explain complex concepts. "
                    "Testing: verify lang attribute on html element, verify language changes are marked, verify technical terms are defined, verify readability level, "
                    "test with screen reader to verify correct pronunciation. "
                    "Common failures: missing lang attribute, language changes not marked, undefined jargon and technical terms, overly complex language."
                ),
                "keywords": [
                    "readable", "language", "lang attribute", "language changes", "pronunciation",
                    "abbreviations", "acronyms", "uncommon words", "readability", "simple language",
                    "jargon", "reading disability", "dyslexia"
                ],
            },
            "3_2_predictable": {
                "title": "3.2: Predictable",
                "part": "3.2",
                "clause": "Navigation Consistency",
                "content": (
                    "Navigation and functionality must be predictable and consistent. Users should be able to predict how components work based on their appearance "
                    "and previous interactions. Unpredictable behavior disorients users with cognitive disabilities. "
                    "Success Criteria 3.2.1 (Level A) requires that receiving focus on a component does not cause significant change of context. When a form field "
                    "receives focus, it should not automatically submit the form or change page content. "
                    "Success Criteria 3.2.2 (Level A) requires that changing the setting of any component does not automatically cause a change of context unless "
                    "the user has been informed of this behavior. Form submissions should require explicit action. If a select menu automatically submits, "
                    "users should be informed of this. "
                    "Success Criteria 3.2.3 (Level AA) requires consistent navigation and components across related pages. If navigation appears in the same location "
                    "on multiple pages, it should look and function the same way. Consistent labeling of components reduces confusion. "
                    "Success Criteria 3.2.4 (Level AA) requires consistent identification of components. A component with the same function should be identified consistently. "
                    "Testing: verify receiving focus doesn't cause unexpected changes, verify form controls don't auto-submit, verify navigation is consistent across pages, "
                    "verify similar components are labeled and function consistently. "
                    "Common failures: form field receives focus and page changes, select menu auto-submits without warning, navigation inconsistent across pages, "
                    "similar buttons have different labels, unexpected page changes."
                ),
                "keywords": [
                    "predictable", "consistency", "navigation consistency", "consistent components",
                    "context change", "focus change", "auto-submit", "consistent labeling",
                    "form behavior", "expected behavior", "cognitive disability"
                ],
            },
            "3_3_input_assistance": {
                "title": "3.3: Input Assistance",
                "part": "3.3",
                "clause": "Form Assistance and Error Prevention",
                "content": (
                    "Users must be helped to avoid and correct mistakes when providing input. Forms should provide clear labels, instructions, error identification, "
                    "and error suggestions. Input assistance prevents user frustration and helps all users complete forms successfully. "
                    "Success Criteria 3.3.1 (Level A) requires that input errors are identified and described in plain language. When a form validation error occurs, "
                    "users must be told which field has an error and what the problem is. Error messages should be specific (e.g., 'Email address must include @') "
                    "not generic (e.g., 'Error'). "
                    "Success Criteria 3.3.2 (Level A) requires descriptive labels or instructions for user input. Each form field should have a label that describes "
                    "what information is needed. Placeholder text alone is not sufficient. "
                    "Success Criteria 3.3.3 (Level AA) requires error suggestions. When input errors occur, the site should suggest how to correct the error if possible. "
                    "Success Criteria 3.3.4 (Level AA) requires error prevention for submissions that have legal, financial, or data consequences. For important transactions, "
                    "the site should allow users to review, confirm, or correct data before submission. "
                    "Testing: verify form fields have descriptive labels, verify error messages are specific and helpful, verify error suggestions are provided, "
                    "verify important forms require review and confirmation. "
                    "Common failures: form fields without labels, generic error messages, errors on wrong field, no error suggestions, automatic submission of important forms "
                    "without confirmation."
                ),
                "keywords": [
                    "input assistance", "form labels", "error identification", "error messages",
                    "error prevention", "form assistance", "descriptive labels", "error recovery",
                    "form validation", "legal consequences", "financial consequences", "instructions"
                ],
            },
            "4_robust": {
                "title": "Principle 4: Robust",
                "part": "Principle 4",
                "clause": "Assistive Technology Compatibility",
                "content": (
                    "Content must be robust and compatible with current and future assistive technologies. This means using proper HTML markup, ARIA when necessary, "
                    "and semantic elements. Assistive technologies like screen readers, magnifiers, speech recognition, and switch control rely on web standards. "
                    "Content must be marked up properly so assistive technologies can interpret it. This includes using semantic HTML (headings, lists, landmarks), "
                    "proper ARIA roles and properties, and testing with assistive technologies. "
                    "Valid HTML is essential for compatibility with assistive technologies. Parsing errors and invalid markup can cause assistive technology to malfunction. "
                    "Testing: validate HTML, verify semantic markup is used appropriately, verify ARIA is used correctly, test with screen reader, "
                    "test with screen magnifier, test with keyboard only. "
                    "Robust content ensures that accessibility improvements benefit all users, not just those using specific assistive technologies."
                ),
                "keywords": [
                    "robust", "assistive technologies", "screen reader", "ARIA", "semantic HTML",
                    "HTML validity", "markup", "compatibility", "future compatibility", "parsing",
                    "ARIA roles", "landmarks", "programmatic accessibility"
                ],
            },
            "4_1_compatible": {
                "title": "4.1: Compatible",
                "part": "4.1",
                "clause": "Assistive Technology Compatibility",
                "content": (
                    "Content must be compatible with current and future assistive technologies. This means writing valid, semantic HTML and properly implementing ARIA. "
                    "Success Criteria 4.1.1 (Level A) requires valid HTML with no parsing errors. Assistive technologies rely on HTML parsing to understand content structure. "
                    "Errors in HTML can cause assistive technologies to fail or misinterpret content. "
                    "Success Criteria 4.1.2 (Level A) requires that names, roles, and states of all components are exposed to assistive technologies. This means using proper "
                    "semantic HTML (button for buttons, input type='checkbox' for checkboxes, nav for navigation, etc.) or ARIA roles, properties, and states when semantic "
                    "HTML isn't available. "
                    "For custom components, ARIA must be used to identify the component type (role), its name (aria-label or associated label), its state (aria-checked, "
                    "aria-pressed, etc.), and relevant properties. "
                    "Success Criteria 4.1.3 (Level AA) requires that status messages are programmatically determinable. When important information is added to the page "
                    "(like error messages or dynamic content), screen reader users must be notified through ARIA live regions (aria-live). "
                    "Testing: validate HTML with HTML validator, verify semantic HTML is used appropriately, verify ARIA is correct and not conflicting with semantic markup, "
                    "test with screen reader to verify names, roles, states are conveyed, verify status messages are announced. "
                    "Common failures: invalid HTML, custom components without ARIA, semantic HTML with conflicting ARIA, status messages not announced, "
                    "improper ARIA usage."
                ),
                "keywords": [
                    "compatible", "ARIA", "semantic HTML", "HTML validity", "roles", "states",
                    "names", "aria-label", "aria-live", "status messages", "assistive technology",
                    "screen reader", "parsing", "landmarks"
                ],
            },
        },
    },
}
