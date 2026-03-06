"""
OWASP Foundation Standards — Application security testing.

Covers Top 10, ASVS verification levels, and API Security Top 10.
"""

STANDARD_ID = "OWASP"

SECTIONS: dict[str, dict] = {
    "top10:2021": {
        "title": "OWASP Top 10 — 2021",
        "sections": {
            "A01": {
                "title": "A01:2021 — Broken Access Control",
                "content": (
                    "Access control enforces policy such that users cannot act outside their intended "
                    "permissions. Failures typically lead to unauthorized information disclosure, modification, "
                    "or destruction of data. Common weaknesses: violation of least privilege, CORS misconfiguration, "
                    "accessing API with missing access controls for POST, PUT, DELETE, "
                    "elevation of privilege. Testing: verify RBAC enforcement on every endpoint, test IDOR "
                    "(Insecure Direct Object Reference), verify horizontal and vertical privilege escalation."
                ),
                "keywords": ["access control", "authorization", "RBAC", "IDOR", "privilege escalation"],
            },
            "A02": {
                "title": "A02:2021 — Cryptographic Failures",
                "content": (
                    "Formerly 'Sensitive Data Exposure.' Failures related to cryptography that lead to "
                    "exposure of sensitive data. Testing: verify TLS in transit, verify encryption at rest "
                    "for sensitive data, check for weak algorithms (MD5, SHA1, DES), "
                    "verify proper key management, test for information exposure in error messages."
                ),
                "keywords": ["cryptography", "encryption", "TLS", "sensitive data", "key management"],
            },
            "A03": {
                "title": "A03:2021 — Injection",
                "content": (
                    "SQL, NoSQL, OS, LDAP injection occurs when untrusted data is sent to an interpreter "
                    "as part of a command or query. Testing: test all user-supplied input fields for injection, "
                    "verify use of parameterized queries/prepared statements, test for ORM injection, "
                    "verify input validation and sanitization."
                ),
                "keywords": ["injection", "SQL", "NoSQL", "XSS", "input validation", "sanitization"],
            },
            "A05": {
                "title": "A05:2021 — Security Misconfiguration",
                "content": (
                    "Missing appropriate security hardening, improperly configured permissions, "
                    "unnecessary features enabled, default accounts/passwords. Testing: verify security "
                    "headers (CSP, X-Frame-Options, HSTS), check for default credentials, "
                    "verify error handling doesn't expose stack traces, test directory listing."
                ),
                "keywords": ["misconfiguration", "hardening", "headers", "defaults", "error handling"],
            },
            "A07": {
                "title": "A07:2021 — Identification and Authentication Failures",
                "content": (
                    "Confirmation of user identity, authentication, and session management. "
                    "Testing: verify password policies, test for credential stuffing protections, "
                    "verify MFA implementation, test session timeout and invalidation, "
                    "test JWT token expiration and signing, verify account lockout mechanisms."
                ),
                "keywords": ["authentication", "session", "JWT", "password", "MFA", "credential"],
            },
            "A09": {
                "title": "A09:2021 — Security Logging and Monitoring Failures",
                "content": (
                    "Insufficient logging, detection, monitoring, and active response. "
                    "Testing: verify login attempts are logged, verify high-value transactions are logged "
                    "with audit trail, test that logs are protected from tampering, "
                    "verify alerting mechanisms for suspicious activity."
                ),
                "keywords": ["logging", "monitoring", "audit", "alerting", "detection"],
            },
        },
    },
    "asvs:4.0": {
        "title": "OWASP Application Security Verification Standard (ASVS) v4.0",
        "sections": {
            "levels": {
                "title": "ASVS Verification Levels",
                "content": (
                    "Level 1 (Opportunistic): Minimum assurance. Adequate for low-risk applications. "
                    "Testable via automated tools and manual inspection. "
                    "Level 2 (Standard): Recommended for applications containing sensitive data. "
                    "Effective against most risks. Required for healthcare, financial, and PII-handling systems. "
                    "Level 3 (Advanced): Highest level. Required for critical applications (military, health, "
                    "safety, critical infrastructure). Requires thorough design review and code analysis."
                ),
                "keywords": ["ASVS", "verification level", "assurance", "Level 1", "Level 2", "Level 3"],
            },
            "V1": {
                "title": "V1: Architecture, Design, and Threat Modeling",
                "content": (
                    "Verify that a threat model exists for the application. "
                    "Verify that all security controls have a centralized implementation. "
                    "Verify the application uses a single vetted authentication mechanism. "
                    "Verify all components are up to date with proper dependencies."
                ),
                "keywords": ["architecture", "threat model", "design", "security controls"],
            },
            "V2": {
                "title": "V2: Authentication",
                "content": (
                    "Verify that all authentication pathways and identity management APIs "
                    "implement consistent authentication security control strength. "
                    "Verify that anti-automation controls are effective at mitigating credential stuffing. "
                    "Verify that all authentication functions (login, password reset) are resistant to "
                    "timing attacks. Rate-limit authentication attempts."
                ),
                "keywords": ["authentication", "identity", "credential", "rate limiting"],
            },
            "V3": {
                "title": "V3: Session Management",
                "content": (
                    "Verify the application generates a new session token on user authentication. "
                    "Verify session tokens have at least 128 bits of entropy. "
                    "Verify the application only stores session tokens in the browser using secure methods. "
                    "Verify session timeout and absolute timeout mechanisms."
                ),
                "keywords": ["session", "token", "timeout", "cookie", "CSRF"],
            },
            "V5": {
                "title": "V5: Validation, Sanitization, and Encoding",
                "content": (
                    "Verify that the application has defenses against HTTP parameter pollution. "
                    "Verify that all input is validated using positive validation (allowlists). "
                    "Verify structured data is strongly typed and validated against a defined schema. "
                    "Verify all output encoding is relevant for the interpreter and context."
                ),
                "keywords": ["validation", "sanitization", "encoding", "input", "output", "XSS"],
            },
        },
    },
    "api_security:2023": {
        "title": "OWASP API Security Top 10 — 2023",
        "sections": {
            "API1": {
                "title": "API1:2023 — Broken Object Level Authorization",
                "content": (
                    "APIs expose endpoints handling object identifiers. "
                    "Every function accessing a data source using user-supplied input should verify authorization. "
                    "Testing: access other users' resources by manipulating object IDs in the request."
                ),
                "keywords": ["BOLA", "object", "authorization", "API", "IDOR"],
            },
            "API2": {
                "title": "API2:2023 — Broken Authentication",
                "content": (
                    "Authentication mechanisms are often implemented incorrectly, allowing attackers to "
                    "compromise authentication tokens or exploit implementation flaws. "
                    "Testing: test token expiration, verify API key rotation, test for weak JWT secrets."
                ),
                "keywords": ["API", "authentication", "token", "JWT", "API key"],
            },
            "API4": {
                "title": "API4:2023 — Unrestricted Resource Consumption",
                "content": (
                    "APIs that don't limit the size or number of resources requested are susceptible "
                    "to Denial of Service (DoS). Testing: verify rate limiting on all endpoints, "
                    "test pagination limits, test file upload size limits, verify timeout mechanisms."
                ),
                "keywords": ["rate limiting", "DoS", "resource", "pagination", "timeout"],
            },
        },
    },
}
