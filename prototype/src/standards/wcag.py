"""WCAG 2.2 Level AA — Web Content Accessibility Guidelines."""

STANDARD_ID = "WCAG 2.2"

SECTIONS: dict[str, dict] = {
    "wcag:2.2": {
        "title": "Web Content Accessibility Guidelines (WCAG) 2.2 Level AA",
        "sections": {
            "1_perceivable": {
                "title": "Principle 1: Perceivable",
                "content": (
                    "Information and UI components must be presentable to users in ways they can perceive. "
                    "Testing: verify text alternatives for non-text content, captions for multimedia, "
                    "sufficient color contrast (4.5:1 for normal text, 3:1 for large text), "
                    "content reflow at 320px width without horizontal scrolling."
                ),
                "keywords": ["perceivable", "contrast", "alt text", "captions", "reflow"],
            },
            "2_operable": {
                "title": "Principle 2: Operable",
                "content": (
                    "UI components and navigation must be operable. "
                    "Testing: all functionality available via keyboard, no keyboard traps, "
                    "skip navigation links, focus indicators visible, "
                    "no content that flashes more than 3 times per second."
                ),
                "keywords": ["operable", "keyboard", "focus", "navigation", "timing"],
            },
            "3_understandable": {
                "title": "Principle 3: Understandable",
                "content": (
                    "Information and UI operation must be understandable. "
                    "Testing: page language declared, consistent navigation, "
                    "input assistance (labels, error identification, error suggestion)."
                ),
                "keywords": ["understandable", "language", "labels", "errors", "consistent"],
            },
            "4_robust": {
                "title": "Principle 4: Robust",
                "content": (
                    "Content must be robust enough for interpretation by assistive technologies. "
                    "Testing: valid HTML, ARIA roles correctly used, status messages programmatically determinable."
                ),
                "keywords": ["robust", "ARIA", "assistive", "HTML", "semantic"],
            },
        },
    },
}
