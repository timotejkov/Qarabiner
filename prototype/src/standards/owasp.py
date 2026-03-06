"""
OWASP Foundation Standards — Application security testing and verification.

Covers Top 10 (2021), ASVS verification levels, API Security Top 10, and secure development practices.
Includes detailed testing approaches, attack vectors, and mitigation strategies.
"""

STANDARD_ID = "OWASP"

SECTIONS: dict[str, dict] = {
    "top10:2021": {
        "title": "OWASP Top 10 — 2021 Critical Risk Categories",
        "part": "Vulnerability Categories",
        "sections": {
            "A01": {
                "title": "A01:2021 — Broken Access Control",
                "part": "A01",
                "clause": "Authorization and Permission Enforcement",
                "content": (
                    "Access control enforces policy such that users cannot act outside their intended permissions. "
                    "This is the most prevalent category of vulnerabilities, found in the vast majority of applications. "
                    "Failures typically lead to unauthorized information disclosure, modification, or destruction of data. "
                    "Common weaknesses include violation of the principle of least privilege, insecure CORS configuration, "
                    "accessing APIs with missing access controls for state-changing operations (POST, PUT, DELETE), "
                    "elevation of privilege from regular user to administrative rights, and insecure direct object reference (IDOR). "
                    "Testing requires verification of RBAC enforcement on every endpoint, testing for IDOR vulnerabilities, "
                    "verifying horizontal and vertical privilege escalation prevention, testing API endpoint authorization, "
                    "and confirming that sensitive operations require appropriate permission checks. "
                    "Mitigation strategies include implementing a centralized authorization service, using role-based or "
                    "attribute-based access control, denying access by default, logging and monitoring failed authorization attempts, "
                    "and conducting regular access control reviews."
                ),
                "keywords": [
                    "access control", "authorization", "RBAC", "IDOR", "privilege escalation",
                    "permissions", "authentication", "least privilege", "CORS", "insecure direct object reference"
                ],
            },
            "A02": {
                "title": "A02:2021 — Cryptographic Failures",
                "part": "A02",
                "clause": "Sensitive Data Protection",
                "content": (
                    "Formerly classified as 'Sensitive Data Exposure,' this category encompasses all failures related to "
                    "cryptography and secure data handling that lead to exposure of sensitive information. "
                    "The focus shifted from exposure to cryptographic failures, recognizing that the root cause is often "
                    "poor cryptographic implementations or missing encryption entirely. "
                    "Common vulnerabilities include storing sensitive data in plaintext, using weak or deprecated cryptographic algorithms "
                    "(MD5, SHA1, DES, RC4), improper key management practices, missing encryption during data transmission, "
                    "hardcoded secrets in source code, and improper use of encryption libraries. "
                    "Testing must verify TLS/SSL deployment for all sensitive data in transit, verify encryption at rest for "
                    "confidential data, identify weak algorithms by reviewing code and configuration, test key management practices "
                    "including key rotation and storage, verify that error messages don't expose sensitive information, and test "
                    "for information leakage through debug logs or comments. "
                    "Mitigation includes classifying data by sensitivity, applying encryption to sensitive data at rest and in transit, "
                    "using only strong, well-vetted encryption algorithms, properly managing encryption keys with secure storage and rotation, "
                    "using industry-standard libraries rather than custom cryptography, and conducting regular security audits of "
                    "cryptographic implementations."
                ),
                "keywords": [
                    "cryptography", "encryption", "TLS", "SSL", "sensitive data", "key management",
                    "data protection", "symmetric encryption", "asymmetric encryption", "hashing",
                    "plaintext", "weak algorithms", "key rotation", "PII", "HIPAA", "PCI-DSS"
                ],
            },
            "A03": {
                "title": "A03:2021 — Injection",
                "part": "A03",
                "clause": "Input Validation and Context-Aware Output Encoding",
                "content": (
                    "Injection occurs when untrusted data is sent to an interpreter as part of a command or query, "
                    "where the attacker's input is processed as code rather than data. "
                    "This category includes SQL injection, NoSQL injection, OS command injection, LDAP injection, "
                    "template injection, and other interpreter injection attacks. "
                    "When user-supplied input is concatenated directly into queries or commands without proper escaping or parameterization, "
                    "attackers can modify the logic of the statement or execute unintended operations. "
                    "Testing must be comprehensive across all user input fields, including form fields, URL parameters, HTTP headers, "
                    "file uploads, and API request bodies. Verify that parameterized queries or prepared statements are used throughout "
                    "the application, test for NoSQL injection through query manipulation, verify ORM frameworks are not vulnerable to injection, "
                    "test for template injection in template engines, and verify input validation and sanitization are in place. "
                    "Mitigation strategies include using parameterized queries and prepared statements for all database operations, "
                    "implementing input validation using positive allowlists, encoding output appropriately for the context, "
                    "using ORM frameworks securely, using stored procedures (when combined with parameterized queries), "
                    "escaping special characters appropriately for the target interpreter, and conducting code reviews focused on "
                    "injection points. Regular security testing and source code analysis should identify injection vulnerabilities."
                ),
                "keywords": [
                    "injection", "SQL injection", "NoSQL injection", "OS command injection", "LDAP injection",
                    "template injection", "XPATH injection", "input validation", "output encoding", "sanitization",
                    "parameterized queries", "prepared statements", "escaping", "allowlist", "ORM", "stored procedures"
                ],
            },
            "A04": {
                "title": "A04:2021 — Insecure Design",
                "part": "A04",
                "clause": "Secure Design Principles and Threat Modeling",
                "content": (
                    "Insecure design represents a new category focusing on risks related to missing or ineffective control design. "
                    "This goes beyond the implementation of controls to address the fundamental design and architecture of security "
                    "into applications from the outset. Insecure design differs from other categories as it encompasses missing security "
                    "controls that should have been incorporated during the design phase. "
                    "Common weaknesses include missing or weak threat models, no formal security requirements during the design phase, "
                    "lack of secure design patterns and reference architectures, missing security in business logic, and absence of "
                    "authentication and authorization design decisions. "
                    "Testing requires reviewing the design documentation and threat models, verifying that security requirements were "
                    "defined during design, checking that secure design patterns are followed, testing business logic for security flaws, "
                    "and verifying that security considerations are documented. "
                    "Mitigation includes establishing and using secure design patterns and libraries, creating threat models at the beginning "
                    "of development, defining clear security requirements before implementation, conducting design reviews with security expertise, "
                    "using threat modeling as a standard part of the development process, implementing separation of concerns and defense in depth, "
                    "and documenting security assumptions and design decisions."
                ),
                "keywords": [
                    "secure design", "threat modeling", "security requirements", "design review",
                    "business logic", "design patterns", "reference architecture", "defense in depth",
                    "separation of concerns", "security by design", "STRIDE", "PASTA"
                ],
            },
            "A05": {
                "title": "A05:2021 — Security Misconfiguration",
                "part": "A05",
                "clause": "Configuration Management and Hardening",
                "content": (
                    "Security misconfiguration occurs when missing or incomplete security hardening is deployed, or when default accounts "
                    "and passwords are left unchanged. This is one of the most common issues in web applications. "
                    "Misconfiguration can occur at any level of the application stack, from the operating system to the framework to the application itself. "
                    "Common vulnerabilities include unnecessary features being enabled, default credentials remaining unchanged in production, "
                    "improper configuration of security headers, unnecessary HTTP methods enabled (TRACE, PUT, DELETE), directory listing enabled, "
                    "detailed error messages exposing sensitive information, incomplete security patches, and insecure default settings. "
                    "Testing requires verifying all security headers are properly configured (Content-Security-Policy, X-Frame-Options, HSTS, "
                    "X-Content-Type-Options, etc.), checking for default credentials on all systems, verifying error handling doesn't expose "
                    "stack traces or sensitive data, testing for directory listing vulnerabilities, verifying unnecessary HTTP methods are disabled, "
                    "reviewing server configuration files, and checking that security updates are current. "
                    "Mitigation strategies include automating deployment with security configuration, removing unnecessary features and modules, "
                    "changing all default credentials immediately, implementing a repeatable and well-documented hardening process, segregating "
                    "systems by function with proper access controls, automating configuration verification, regularly reviewing and updating "
                    "configurations, maintaining an inventory of all software components, and applying security patches promptly."
                ),
                "keywords": [
                    "misconfiguration", "hardening", "security headers", "default credentials", "configuration management",
                    "CSP", "X-Frame-Options", "HSTS", "error handling", "defaults", "directory listing",
                    "unnecessary features", "HTTP methods", "stack traces", "security updates"
                ],
            },
            "A06": {
                "title": "A06:2021 — Vulnerable and Outdated Components",
                "part": "A06",
                "clause": "Dependency Management and Component Security",
                "content": (
                    "This category addresses the risks of using software components with known vulnerabilities, including libraries, "
                    "frameworks, and other modules that are outdated or no longer maintained. "
                    "Organizations often don't know what components they're using, where they are, or how to keep them updated. "
                    "Most components run with the same privileges as the application, so a flaw in any component can lead to serious impact. "
                    "Common vulnerabilities include using outdated or unsupported versions of dependencies, failing to monitor for new vulnerabilities, "
                    "not scanning dependencies regularly, not establishing a component update policy, including unused dependencies, and using "
                    "vulnerable components from insecure supply chains. "
                    "Testing must identify all components and their versions in use, scan for known vulnerabilities in each component, "
                    "verify that a software composition analysis (SCA) tool is in place and regularly used, check the age and maintenance status "
                    "of dependencies, verify that transitive dependencies are also managed, and test update procedures. "
                    "Mitigation includes maintaining an inventory of all components and their versions, removing unnecessary dependencies, "
                    "regularly scanning for and applying security updates, establishing a component update policy and process, monitoring security "
                    "advisories for components, using trusted sources for components, subscribing to security advisories from component vendors, "
                    "using automated dependency management tools, and implementing a supply chain security program."
                ),
                "keywords": [
                    "vulnerable components", "outdated libraries", "dependency management", "software composition analysis",
                    "SCA tools", "security patches", "component inventory", "transitive dependencies", "supply chain",
                    "known vulnerabilities", "CVE", "SBOM", "component updates", "maintenance status"
                ],
            },
            "A07": {
                "title": "A07:2021 — Identification and Authentication Failures",
                "part": "A07",
                "clause": "User Identity Verification and Session Management",
                "content": (
                    "Authentication failures, formerly named 'Broken Authentication,' still represent a critical risk where attackers "
                    "compromise user accounts or sessions. This category covers failures in confirmation of user identity, authentication, "
                    "and session management. "
                    "Common vulnerabilities include weak password policies allowing easy to guess passwords, missing multi-factor authentication, "
                    "credential stuffing attacks not being prevented, weak session management allowing session fixation or hijacking, "
                    "missing logout functionality, JWT tokens with weak signatures or no expiration, session tokens stored insecurely, "
                    "missing or ineffective password recovery mechanisms, and failure to protect against brute force attacks. "
                    "Testing must verify that password policies enforce strong passwords, test for credential stuffing protections through "
                    "rate limiting, verify MFA is implemented and enforced for sensitive operations, test session timeout and invalidation, "
                    "test JWT token expiration and signature validation, verify account lockout mechanisms after failed attempts, test password "
                    "reset tokens have short expiration, verify secure password reset processes, and check that authentication mechanisms use "
                    "secure channels. "
                    "Mitigation includes implementing strong password requirements and hashing algorithms, implementing multi-factor authentication, "
                    "implementing rate limiting on authentication endpoints, enforcing secure session management with proper timeout, using "
                    "secure session storage mechanisms, implementing proper logout functionality, using strong, industry-standard authentication "
                    "libraries, protecting sensitive authentication tokens, implementing account lockout after repeated failures, and regularly "
                    "testing authentication mechanisms."
                ),
                "keywords": [
                    "authentication", "session management", "JWT", "password", "MFA", "credential", "session token",
                    "credential stuffing", "brute force", "account lockout", "multi-factor authentication",
                    "session fixation", "session hijacking", "password reset", "TOTP", "HMAC"
                ],
            },
            "A08": {
                "title": "A08:2021 — Software and Data Integrity Failures",
                "part": "A08",
                "clause": "Update and Dependency Integrity",
                "content": (
                    "This category addresses failures related to code and infrastructure that do not protect against integrity violations. "
                    "Software integrity failures occur when applications rely on insecure update mechanisms, unsigned updates, or updates over "
                    "unencrypted connections. Data integrity failures occur when sensitive data can be modified without proper verification. "
                    "Insecure CI/CD pipelines expose the system to malicious code injection, inadequately secured artifacts, lack of access control, "
                    "and lack of audit logging. "
                    "Common vulnerabilities include insecure direct object references allowing data manipulation, deserialization of untrusted data, "
                    "insufficient controls over continuous integration/continuous deployment (CI/CD) pipelines, unsigned or unencrypted updates, "
                    "missing integrity checks on critical updates, and insecure serialization mechanisms. "
                    "Testing must verify that deserialization mechanisms are secure and don't accept untrusted input, verify that CI/CD pipelines "
                    "include security controls and validation, check that updates are signed and verified, verify integrity controls on critical data, "
                    "test that plugins and dependencies are from trusted sources, and verify audit logging of pipeline activities. "
                    "Mitigation includes securing the CI/CD pipeline with proper access controls and monitoring, using signed and verified updates, "
                    "implementing integrity verification for critical data and updates, avoiding insecure deserialization patterns, using secure "
                    "dependency management, implementing supply chain security measures, using configuration management to lock down systems, "
                    "and maintaining audit logs of all pipeline activities."
                ),
                "keywords": [
                    "data integrity", "software integrity", "CI/CD security", "deserialization", "serialization",
                    "signed updates", "SBOM", "supply chain", "artifact repository", "unsigned code",
                    "integrity verification", "checksum", "digital signature", "code signing"
                ],
            },
            "A09": {
                "title": "A09:2021 — Security Logging and Monitoring Failures",
                "part": "A09",
                "clause": "Audit Trails and Incident Detection",
                "content": (
                    "Security logging and monitoring failures occur when insufficient logging, detection, monitoring, and active response "
                    "allow attackers to attack and maintain control of systems without being detected. "
                    "Auditable events like login and transaction processing are often not logged or are logged insufficiently, and security "
                    "events are not monitored for suspicious activity. Many incidents have been detected months later. "
                    "Common vulnerabilities include missing or insufficient logging of security events, logs not being protected from tampering "
                    "or deletion, logs not being reviewed for suspicious activity, missing alerting on security events, failed login attempts not "
                    "being logged, sensitive operations not being logged, and logs being easily accessible to low-privileged users. "
                    "Testing must verify that login attempts and authentication failures are logged, verify that high-value transactions and "
                    "administrative actions are logged with full audit trail, test that logs are protected from tampering with appropriate access "
                    "controls, verify that log retention policies are in place, verify alerting mechanisms exist for suspicious activity, test that "
                    "logs contain sufficient information for investigation, and verify that logs are monitored and reviewed. "
                    "Mitigation includes logging all authentication attempts, sensitive data access, and state-changing operations, protecting logs "
                    "from tampering through centralized log storage and cryptographic protection, implementing alerting for suspicious activities, "
                    "establishing a log retention and archival policy, conducting regular log reviews and analysis, using log aggregation and SIEM "
                    "tools, implementing incident response procedures, and maintaining audit trails for compliance."
                ),
                "keywords": [
                    "logging", "monitoring", "audit", "alerting", "detection", "SIEM", "log aggregation",
                    "incident response", "audit trail", "failed login", "transaction logging",
                    "log protection", "tampering", "centralized logging", "forensics"
                ],
            },
            "A10": {
                "title": "A10:2021 — Server-Side Request Forgery (SSRF)",
                "part": "A10",
                "clause": "Outbound Request Validation",
                "content": (
                    "Server-Side Request Forgery (SSRF) occurs when a web application fetches a remote resource without properly validating the "
                    "user-supplied URL. SSRF allows attackers to cause the server to make unintended requests to internal resources or external systems. "
                    "Even if the server's network access is restricted, SSRF can still be dangerous if sensitive internal services are exposed. "
                    "Common vulnerabilities include applications fetching remote resources based on user input without validation, lack of URL scheme "
                    "validation, missing network segmentation controls, weak or absent allowlisting of allowed destinations, and failure to disable "
                    "unused URL schemes. "
                    "Attack vectors include accessing internal services like admin consoles, accessing cloud metadata endpoints, scanning internal "
                    "networks, accessing services on non-standard ports, port scanning the local network, accessing file:// schemes to read local files, "
                    "and sending requests to external systems on behalf of the attacker. "
                    "Testing must verify that user-supplied URLs are validated before being used, test that only expected URL schemes are allowed, "
                    "verify that access to internal IP ranges and localhost is blocked, test that administrative endpoints are not accessible via SSRF, "
                    "test for cloud metadata endpoint access, and verify network segmentation controls. "
                    "Mitigation includes implementing strict validation and allowlisting of allowed URLs and destinations, disabling unused URL schemes, "
                    "implementing network-level controls to restrict outbound access, using allow lists rather than blocklists, segmenting networks, "
                    "using security groups to restrict access, avoiding exposing sensitive services on the same network, and regularly testing for "
                    "SSRF vulnerabilities."
                ),
                "keywords": [
                    "SSRF", "server-side request forgery", "URL validation", "outbound requests", "URL scheme",
                    "internal services", "metadata endpoints", "localhost", "127.0.0.1", "private IP ranges",
                    "port scanning", "file:// scheme", "allowlisting", "network segmentation"
                ],
            },
        },
    },
    "asvs:4.0": {
        "title": "OWASP Application Security Verification Standard (ASVS) v4.0",
        "part": "Verification Framework",
        "sections": {
            "overview": {
                "title": "ASVS Overview and Purpose",
                "part": "Framework",
                "clause": "Standard Introduction",
                "content": (
                    "The Application Security Verification Standard (ASVS) is a framework of security requirements and testing procedures "
                    "that can be used as a basis for securing web applications and services. ASVS provides developers, architects, and security "
                    "professionals with a comprehensive checklist of security controls that should be implemented and tested. "
                    "ASVS is risk-driven and prescriptive, allowing organizations to define their target verification level based on the risk "
                    "profile of the application and the sensitivity of the data it processes. "
                    "The standard covers all aspects of application security, from architecture and design through implementation, deployment, "
                    "and operations. It addresses authentication, session management, access control, input validation, cryptography, error handling, "
                    "data protection, communications security, API security, and business logic. "
                    "ASVS can be used as a procurement specification, as a basis for security testing, as a secure development baseline, or as a "
                    "compliance standard for organizational security programs."
                ),
                "keywords": [
                    "ASVS", "verification standard", "security requirements", "testing procedures", "security controls",
                    "compliance", "risk-driven", "application security framework", "comprehensive checklist"
                ],
            },
            "levels": {
                "title": "ASVS Verification Levels",
                "part": "Framework",
                "clause": "Assurance Levels",
                "content": (
                    "The ASVS defines three verification levels, each representing an increasing level of assurance and rigor. "
                    "Level 1 (Opportunistic) represents the minimum assurance level and is adequate for applications with low or negligible risk, "
                    "such as proof-of-concept applications or non-critical systems. Level 1 testing can be performed primarily through automated tools "
                    "and manual inspection by developers without specialized security expertise. Requirements are appropriate for startups and small "
                    "development teams working on non-critical applications. "
                    "Level 2 (Standard) is the recommended verification level for most applications, especially those containing sensitive data or used "
                    "by a significant number of users. Level 2 represents effective assurance against most attacks and is appropriate for healthcare, "
                    "financial, PII-handling systems, and critical business applications. Level 2 verification requires more thorough testing and "
                    "security expertise, combining automated tools with manual security testing. "
                    "Level 3 (Advanced) represents the highest level of assurance and is required for applications handling highly sensitive data, "
                    "critical infrastructure applications, applications with significant security or safety implications, or systems requiring maximum "
                    "protection. Level 3 requires thorough design review, comprehensive code analysis, and advanced testing techniques. Level 3 verification "
                    "should be performed by highly skilled security professionals and may require formal security certification. "
                    "Organizations should select their target verification level based on the risk profile of the application, sensitivity of data "
                    "processed, potential impact of a breach, regulatory requirements, and organizational risk tolerance."
                ),
                "keywords": [
                    "ASVS", "verification level", "assurance", "Level 1", "Level 2", "Level 3",
                    "opportunistic", "standard", "advanced", "risk assessment", "compliance level"
                ],
            },
            "V1": {
                "title": "V1: Architecture, Design, and Threat Modeling",
                "part": "Requirements",
                "clause": "Security Architecture",
                "content": (
                    "V1 addresses the architectural and design aspects of security and ensures that a formal threat modeling process is in place. "
                    "Applications must have an explicit security architecture that is documented and understood by all development team members. "
                    "Verify that a threat model has been created for the application and covers all trust boundaries, external dependencies, and "
                    "potential attack vectors. The threat model should identify high-level threats and mitigations that inform the application's design. "
                    "Verify that all security controls have a centralized implementation that can be used throughout the application rather than "
                    "reimplementing controls in each component. A single, vetted authentication mechanism should be used application-wide rather than "
                    "multiple implementations. "
                    "The application should demonstrate proper separation of concerns with security controls layered throughout the architecture. "
                    "Verify that all dependencies, frameworks, and components are appropriately scoped and that the application uses secure, up-to-date "
                    "versions. The architecture must enforce least privilege principles and implement defense in depth. "
                    "Security must be considered from the earliest design phases and maintained throughout the development lifecycle. Code reviews should "
                    "verify that the implemented architecture matches the documented threat model."
                ),
                "keywords": [
                    "architecture", "threat model", "design", "security controls", "trust boundaries",
                    "attack vectors", "defense in depth", "least privilege", "secure design",
                    "centralized controls", "separation of concerns", "documentation"
                ],
            },
            "V2": {
                "title": "V2: Authentication",
                "part": "Requirements",
                "clause": "Identity Verification",
                "content": (
                    "V2 covers authentication mechanisms and ensures that users are properly verified before granting access to the application. "
                    "Verify that all authentication pathways and identity management APIs implement consistent authentication security control strength. "
                    "This includes login mechanisms, password resets, multi-factor authentication, and API authentication. "
                    "Verify that anti-automation controls are effective at mitigating credential stuffing and brute force attacks. This includes rate "
                    "limiting, account lockout, CAPTCHA, and requiring multi-factor authentication after a threshold of failures. "
                    "Verify that all authentication functions are resistant to timing attacks by using constant-time comparisons and ensuring response "
                    "times are similar for successful and failed authentication attempts. "
                    "Password storage must use strong, salted hashing algorithms such as PBKDF2, scrypt, bcrypt, or Argon2, never plaintext or weak "
                    "algorithms. Password policies should enforce minimum length, complexity requirements, and regular updates. "
                    "Multi-factor authentication should be implemented and enforced for administrative accounts and sensitive operations. "
                    "Default credentials must be changed immediately, and password recovery mechanisms must be secure with time-limited tokens. "
                    "Session management must integrate properly with authentication, creating new session tokens upon successful authentication."
                ),
                "keywords": [
                    "authentication", "identity", "credential", "rate limiting", "brute force",
                    "multi-factor authentication", "MFA", "password hashing", "timing attacks",
                    "account lockout", "credential stuffing", "password policy", "TOTP", "HMAC"
                ],
            },
            "V3": {
                "title": "V3: Session Management",
                "part": "Requirements",
                "clause": "Session Handling and State Management",
                "content": (
                    "V3 requirements address session management and ensure that sessions are properly created, managed, and terminated. "
                    "Verify the application generates a new session token on user authentication and invalidates previous session tokens to prevent "
                    "session fixation attacks. Session tokens must be cryptographically random and unique. "
                    "Verify session tokens have sufficient entropy, at least 128 bits, and are generated using a cryptographically secure random number generator. "
                    "This prevents session prediction attacks. Token format should not reveal information about the session or user. "
                    "Verify the application only stores session tokens in secure browser mechanisms such as HttpOnly, Secure cookies, or secure storage, "
                    "and never in unencrypted local storage or query parameters. Session tokens should not be transmitted over unencrypted connections. "
                    "Verify session timeout mechanisms are implemented, both inactivity timeout and absolute timeout, with reasonable values appropriate "
                    "for the application's risk profile. Sessions must be properly invalidated upon logout. "
                    "Session tokens must be properly signed or encrypted to prevent tampering and must include integrity checks. "
                    "Cross-Site Request Forgery (CSRF) protections must be implemented for state-changing operations using tokens or same-site cookies. "
                    "Verify that session management integrates properly with authentication and that new sessions are properly established after login."
                ),
                "keywords": [
                    "session", "token", "timeout", "cookie", "CSRF", "session fixation", "session token entropy",
                    "HttpOnly", "Secure flag", "SameSite", "session invalidation", "logout", "session hijacking"
                ],
            },
            "V4": {
                "title": "V4: Access Control",
                "part": "Requirements",
                "clause": "Authorization and Permissions",
                "content": (
                    "V4 addresses access control and authorization to ensure that users can only access resources and perform actions they are "
                    "authorized to perform. Access control must be consistently enforced on all requests and sensitive operations. "
                    "Verify that access controls are enforced using a well-documented and testable model such as role-based access control (RBAC) "
                    "or attribute-based access control (ABAC). The access control model should be simple to understand, implement, and verify. "
                    "Access control decisions must deny by default and grant only what is explicitly permitted. Verify that all API endpoints enforce "
                    "access controls for all operations, including GET, POST, PUT, DELETE, and PATCH. "
                    "Prevent insecure direct object reference (IDOR) vulnerabilities by verifying authorization before allowing access to any object "
                    "referenced by user input. Object references should not be sequential or predictable. "
                    "Verify that privileged operations and sensitive data access require strong authentication and authorization checks. "
                    "Administrative interfaces must be protected with additional access controls and should be restricted to authorized personnel only. "
                    "Verify that horizontal privilege escalation (accessing resources of other users at the same privilege level) is prevented and "
                    "vertical privilege escalation (escalating to higher privilege levels) is prevented. "
                    "Access control logic must be centralized and reused across the application rather than duplicated in multiple places."
                ),
                "keywords": [
                    "access control", "authorization", "RBAC", "ABAC", "permissions", "privilege",
                    "IDOR", "insecure direct object reference", "privilege escalation", "deny by default",
                    "administrative access", "resource authorization", "object reference"
                ],
            },
            "V5": {
                "title": "V5: Validation, Sanitization, and Encoding",
                "part": "Requirements",
                "clause": "Input Handling and Output Control",
                "content": (
                    "V5 addresses input validation and output encoding to prevent injection and encoding-based attacks. "
                    "Verify that the application has defenses against HTTP parameter pollution and request smuggling attacks that exploit differences "
                    "in how different components parse HTTP requests. "
                    "Verify that all input is validated using positive validation with allowlists of acceptable values, lengths, and formats rather than "
                    "trying to identify malicious input with blocklists. Input validation must occur on the server side as client-side validation alone "
                    "cannot be trusted. "
                    "Verify that structured data is strongly typed and validated against a defined schema. This applies to JSON, XML, CSV, and other "
                    "structured formats. Schema validation should reject unexpected fields and data types. "
                    "Verify that all output is properly encoded relevant for the interpreter and context. HTML encoding should be used for HTML content, "
                    "URL encoding for URLs, JavaScript encoding for JavaScript contexts, SQL escaping for SQL, and other appropriate encoding for other contexts. "
                    "Verify that file uploads are properly validated for file type, size, and content. Store uploaded files in a location not accessible "
                    "to web server execution. Verify that file names cannot be used to access arbitrary files on the server. "
                    "Verify that the application is protected against XXE (XML External Entity) attacks by disabling external entity parsing. "
                    "Verify that data serialization is implemented securely and dangerous deserialization is avoided."
                ),
                "keywords": [
                    "validation", "sanitization", "encoding", "input", "output", "XSS", "injection",
                    "allowlist", "blocklist", "HTTP parameter pollution", "schema validation",
                    "HTML encoding", "URL encoding", "XXE", "XML external entity"
                ],
            },
            "V6": {
                "title": "V6: Cryptography",
                "part": "Requirements",
                "clause": "Encryption and Hashing",
                "content": (
                    "V6 addresses cryptographic controls and ensures that sensitive data is protected using appropriate encryption and hashing algorithms. "
                    "Verify that cryptographic controls are implemented using strong, modern algorithms and that deprecated or weak algorithms "
                    "(DES, RC4, MD5, SHA1) are not used for security purposes. "
                    "Verify that sensitive data is encrypted at rest using strong encryption algorithms such as AES-256 in CBC or GCM mode. "
                    "Keys must be properly managed, including secure generation, storage, rotation, and destruction. "
                    "Verify that all sensitive data in transit is encrypted using TLS 1.2 or higher. All connections should use HTTPS and avoid downgrade attacks. "
                    "Certificate validation must be properly implemented and certificate pinning should be considered for critical applications. "
                    "Verify that password hashing uses approved algorithms such as Argon2, scrypt, bcrypt, or PBKDF2 with appropriate iterations. "
                    "Passwords should never be stored in plaintext or using reversible encryption. "
                    "Random number generation must use cryptographically secure methods for all security purposes. Weak randomness (Math.random, time-based seeds) "
                    "is not acceptable for security purposes. "
                    "Verify that cryptographic operations are implemented using well-tested, industry-standard libraries rather than custom implementations. "
                    "Key management must include secure generation, storage in protected locations, regular rotation, and secure disposal."
                ),
                "keywords": [
                    "cryptography", "encryption", "hashing", "AES", "TLS", "key management",
                    "password hashing", "Argon2", "bcrypt", "symmetric encryption", "asymmetric encryption",
                    "random number generation", "certificate", "HMAC", "digital signature"
                ],
            },
            "V7": {
                "title": "V7: Error Handling and Logging",
                "part": "Requirements",
                "clause": "Exception Handling and Audit Trails",
                "content": (
                    "V7 addresses error handling and logging to ensure that errors are handled securely and that security-relevant events are properly logged. "
                    "Verify that error handling does not expose sensitive information such as stack traces, database error messages, file paths, or system configuration. "
                    "Custom error messages should be displayed to users while detailed errors are logged for debugging. "
                    "Verify that exceptions are caught and handled appropriately without propagating sensitive information. Generic error messages should be "
                    "returned to users while internal logging captures detailed diagnostic information. "
                    "Verify that all security events are logged, including failed authentication attempts, authorization failures, data access violations, "
                    "and state-changing operations. Logs must contain sufficient information to investigate security incidents. "
                    "Verify that logs are protected from tampering by restricting access, implementing write-once storage, or using cryptographic integrity "
                    "controls. Log retention must follow policy and regulatory requirements. "
                    "Verify that logs are monitored and analyzed for suspicious activity. Alerting should be configured for critical security events. "
                    "Sensitive data must not be logged, including passwords, credit card numbers, API keys, and other sensitive information. "
                    "Verify that audit trails capture who performed what action when and from where, providing complete accountability."
                ),
                "keywords": [
                    "error handling", "logging", "audit trail", "exception handling", "stack traces",
                    "error messages", "sensitive information", "log protection", "log monitoring",
                    "alerting", "incident investigation", "compliance logging"
                ],
            },
            "V8": {
                "title": "V8: Data Protection",
                "part": "Requirements",
                "clause": "Data Security and Privacy",
                "content": (
                    "V8 addresses data protection and ensures that sensitive data is properly protected throughout its lifecycle. "
                    "Verify that sensitive data is classified and that appropriate protections are applied based on classification level. "
                    "Data protection policies should define what is considered sensitive and what protections are required. "
                    "Verify that personally identifiable information (PII) and other sensitive data is encrypted at rest and in transit. "
                    "Encryption keys must be managed securely with appropriate rotation and access controls. "
                    "Verify that sensitive data is not exposed in logs, error messages, memory, or caches. Temporary files containing sensitive data "
                    "must be securely deleted after use. "
                    "Verify that data retention policies are documented and implemented, ensuring sensitive data is not retained longer than necessary. "
                    "When data is deleted, it must be securely disposed of, not just marked as deleted. "
                    "Verify that backup and recovery procedures protect sensitive data with the same controls as production systems. "
                    "Verify that data exposure is minimized through techniques such as data masking, tokenization, pseudonymization, and anonymization. "
                    "Verify that access to sensitive data is properly logged and monitored. "
                    "Verify that privacy controls are implemented in accordance with applicable privacy laws (GDPR, CCPA, HIPAA, etc.)."
                ),
                "keywords": [
                    "data protection", "sensitive data", "encryption", "PII", "privacy",
                    "data classification", "data retention", "secure deletion", "backup", "recovery",
                    "data masking", "tokenization", "anonymization", "GDPR", "CCPA", "HIPAA"
                ],
            },
            "V9": {
                "title": "V9: Communications Security",
                "part": "Requirements",
                "clause": "Network Security and Encryption",
                "content": (
                    "V9 addresses communications security and ensures that data transmitted over the network is protected from eavesdropping and tampering. "
                    "Verify that all sensitive communications are encrypted using TLS 1.2 or higher. All HTTP connections should be redirected to HTTPS. "
                    "HTTP Strict Transport Security (HSTS) headers should be implemented to prevent downgrade attacks. "
                    "Verify that TLS is properly configured with strong cipher suites, appropriate key sizes, and forward secrecy support. "
                    "Weak ciphers and protocol versions (SSLv3, TLSv1.0, TLSv1.1) must be disabled. "
                    "Verify that certificate validation is properly implemented and that self-signed certificates or expired certificates are rejected. "
                    "Certificate pinning should be considered for critical applications to prevent MITM attacks. "
                    "Verify that mixed content (secure and insecure resources on the same page) is not served. "
                    "Verify that APIs use secure communication protocols and that API keys and tokens are transmitted securely. "
                    "Verify that message integrity is protected through the use of HMAC or message signatures where appropriate. "
                    "Verify that endpoint validation prevents connection to untrusted or unexpected endpoints."
                ),
                "keywords": [
                    "TLS", "HTTPS", "encryption", "certificate", "HSTS", "cipher suite",
                    "forward secrecy", "certificate validation", "certificate pinning", "MITM",
                    "mixed content", "secure channels", "message integrity", "HMAC"
                ],
            },
            "V10": {
                "title": "V10: Malicious Code",
                "part": "Requirements",
                "clause": "Code Security and Dependencies",
                "content": (
                    "V10 addresses malicious code and ensures that the application and its dependencies are free from malicious code and known vulnerabilities. "
                    "Verify that the application does not contain malicious code or logic bombs, and that code reviews are performed to ensure code quality. "
                    "Verify that all dependencies, libraries, and frameworks are from trusted sources and that the supply chain is secure. "
                    "Verify that a software composition analysis (SCA) tool is in place and is regularly used to identify vulnerable components. "
                    "Verify that all dependencies are kept up to date and that a process exists to apply security patches promptly. "
                    "Verify that dependencies with known vulnerabilities are not used in production systems. "
                    "Verify that the application does not load or execute code from untrusted sources, including eval() statements and dynamic code loading. "
                    "Verify that plugins and extensions come from trusted sources and are properly validated before being used. "
                    "Verify that the application is not susceptible to code injection attacks through file inclusion, template injection, or other vectors. "
                    "Regular security testing and source code analysis should be performed to identify malicious code or vulnerabilities."
                ),
                "keywords": [
                    "malicious code", "dependencies", "vulnerable components", "SCA", "software composition analysis",
                    "supply chain security", "code injection", "eval()", "plugins", "code quality",
                    "security testing", "source code analysis"
                ],
            },
            "V11": {
                "title": "V11: Business Logic",
                "part": "Requirements",
                "clause": "Application-Specific Security",
                "content": (
                    "V11 addresses business logic and ensures that the application's business logic is secure and resistant to bypass attacks. "
                    "Verify that the application enforces all business logic constraints and doesn't allow users to bypass important processes. "
                    "Verify that the application doesn't allow users to manipulate business logic, including circumventing workflow, "
                    "changing amounts, or modifying critical data without authorization. "
                    "Verify that the application detects and handles duplicate transactions and prevents replay attacks. "
                    "Verify that the application implements proper limits on business operations, such as transaction limits, rate limiting, or quantity limits. "
                    "Verify that the application doesn't allow users to perform transactions in unexpected sequences or out of order. "
                    "Verify that the application properly validates all business logic inputs and doesn't allow invalid state transitions. "
                    "Verify that the application implements proper separation of duties, requiring multiple approvals for sensitive operations. "
                    "Verify that time-based or time-sensitive operations are properly protected against manipulation. "
                    "Verify that the application's business logic integrates properly with access controls to prevent unauthorized actions."
                ),
                "keywords": [
                    "business logic", "workflow", "bypass", "transaction", "replay attack",
                    "duplicate transaction", "rate limiting", "separation of duties", "state transition",
                    "approval", "workflow enforcement", "logic validation"
                ],
            },
            "V12": {
                "title": "V12: File Upload",
                "part": "Requirements",
                "clause": "File Handling Security",
                "content": (
                    "V12 addresses file upload functionality and ensures that uploaded files are properly validated and cannot be used to compromise the system. "
                    "Verify that file uploads are restricted to expected file types and that file type validation is performed server-side "
                    "based on content analysis, not just file extension. "
                    "Verify that file upload size limits are enforced to prevent denial of service attacks. "
                    "Verify that uploaded files are stored in a location that is not directly accessible by the web server. Uploaded files should be "
                    "stored outside the web root or in a protected directory with restricted access. "
                    "Verify that file names cannot be used to access arbitrary files on the server. Uploaded files should be stored with random names "
                    "or names that don't reveal sensitive information. "
                    "Verify that uploaded files are scanned for malware and viruses before being made accessible. "
                    "Verify that the application doesn't execute or interpret uploaded files as code. "
                    "Verify that file permissions are set appropriately to prevent unauthorized access. "
                    "Verify that archive files (ZIP, TAR, RAR) are properly validated to prevent ZIP slip attacks. "
                    "Verify that image metadata is stripped from uploaded images to prevent information disclosure."
                ),
                "keywords": [
                    "file upload", "file validation", "file type", "file size", "file execution",
                    "malware scanning", "ZIP slip", "path traversal", "file permissions", "metadata"
                ],
            },
            "V13": {
                "title": "V13: API and Web Service Security",
                "part": "Requirements",
                "clause": "API Protection",
                "content": (
                    "V13 addresses API security and ensures that web services and APIs are protected with the same controls as traditional web applications. "
                    "Verify that all API endpoints implement proper authentication and authorization checks. "
                    "API authentication may use OAuth 2.0, JWT tokens, API keys, or other authentication mechanisms, but must be strong and secure. "
                    "Verify that API requests are validated for content type, message format, and schema compliance. "
                    "Verify that API responses don't expose sensitive information and that error messages are generic. "
                    "Verify that the API implements rate limiting and protects against abuse and denial of service attacks. "
                    "Verify that the API properly handles versioning and deprecates old versions securely. "
                    "Verify that CORS (Cross-Origin Resource Sharing) is properly configured to prevent unauthorized cross-origin access. "
                    "Verify that the API doesn't expose unnecessary endpoints or operations and that unused endpoints are removed. "
                    "Verify that API documentation doesn't expose sensitive information and that API keys are not embedded in documentation. "
                    "Verify that the API logs all requests and responses appropriately for monitoring and incident investigation."
                ),
                "keywords": [
                    "API security", "web service", "API authentication", "OAuth 2.0", "JWT", "API key",
                    "CORS", "rate limiting", "API versioning", "schema validation", "API documentation"
                ],
            },
        },
    },
    "api_security:2023": {
        "title": "OWASP API Security Top 10 — 2023 Edition",
        "part": "API Vulnerabilities",
        "sections": {
            "intro": {
                "title": "API Security Overview",
                "part": "Introduction",
                "clause": "API Risk Landscape",
                "content": (
                    "APIs have become the backbone of modern applications, connecting services, enabling integrations, and powering mobile and web applications. "
                    "However, APIs present unique security challenges that differ from traditional web applications. APIs are often designed to be programmatically "
                    "accessed, making them targets for automated attacks and making manual security testing more difficult. "
                    "The OWASP API Security Top 10 identifies the ten most critical and prevalent API security risks. These risks are specific to APIs and represent "
                    "the most common and impactful vulnerabilities found in API implementations. Organizations should use this list to prioritize their API security "
                    "efforts and ensure that APIs are properly secured. API security testing should be a regular part of development and should include both "
                    "automated scanning and manual testing. API security should be considered from the early design phases through deployment and ongoing operations."
                ),
                "keywords": [
                    "API security", "API vulnerabilities", "API risks", "API testing", "API design",
                    "REST API", "GraphQL", "SOAP", "microservices", "API gateway"
                ],
            },
            "API1": {
                "title": "API1:2023 — Broken Object Level Authorization",
                "part": "API1",
                "clause": "Object-Level Authorization",
                "content": (
                    "APIs expose endpoints that handle object identifiers, allowing clients to retrieve or manipulate specific resources by ID. "
                    "Broken Object Level Authorization (BOLA), also known as Insecure Direct Object Reference (IDOR), occurs when every function accessing "
                    "a data source using user-supplied input should verify authorization but fails to do so. "
                    "Attackers can manipulate object IDs in API requests to access or modify other users' resources, sensitive data, or critical resources. "
                    "Object IDs might be sequential numeric IDs, UUIDs, or other identifiers, but regardless of the format, each access must be validated. "
                    "Common vulnerabilities include APIs that accept user IDs as parameters without validating that the current user is authorized to access "
                    "that user's data, APIs that don't validate ownership of resources before allowing modification, and APIs that expose predictable object IDs. "
                    "Testing must attempt to access other users' resources by manipulating object IDs in the request, test API endpoints with various object ID "
                    "formats to identify patterns, attempt to access resources belonging to other users, and verify that authorization checks are performed "
                    "regardless of the HTTP method used. "
                    "Mitigation includes implementing proper authorization checks before allowing access to any object, using unpredictable object identifiers, "
                    "implementing role-based access control (RBAC) or attribute-based access control (ABAC), centralizing authorization logic, and logging all "
                    "access attempts for monitoring."
                ),
                "keywords": [
                    "BOLA", "IDOR", "object", "authorization", "API", "object ID", "user ID",
                    "insecure direct object reference", "resource access", "permission check"
                ],
            },
            "API2": {
                "title": "API2:2023 — Broken Authentication",
                "part": "API2",
                "clause": "API Authentication Mechanisms",
                "content": (
                    "Broken authentication in APIs occurs when authentication mechanisms are incorrectly implemented, allowing attackers to compromise "
                    "authentication tokens, API keys, or exploit implementation flaws. Authentication is critical for APIs as it's the first line of defense. "
                    "Common vulnerabilities include weak API key design and management, missing or improper token expiration, weak JWT secrets or algorithms, "
                    "missing multi-factor authentication for sensitive operations, credentials exposed in logs or error messages, and improper credential handling. "
                    "APIs might use API keys, OAuth 2.0 tokens, JWT tokens, basic authentication, or other mechanisms, but each must be properly implemented. "
                    "Testing must verify that API tokens have appropriate expiration times and are invalidated when needed, test that weak JWT secrets are detected, "
                    "verify API key rotation mechanisms, test for credential stuffing and brute force protections, test that tokens are properly validated "
                    "before allowing access, and verify that multi-factor authentication is enforced where appropriate. "
                    "Mitigation includes using strong, random API keys with adequate length, implementing proper token expiration and refresh mechanisms, "
                    "storing API keys securely and never embedding them in source code, using strong JWT secrets and algorithms, implementing rate limiting "
                    "on authentication endpoints, enforcing multi-factor authentication for administrative access, rotating credentials regularly, and "
                    "monitoring for suspicious authentication patterns."
                ),
                "keywords": [
                    "API authentication", "token", "JWT", "API key", "OAuth 2.0", "credential",
                    "token expiration", "weak secret", "credential stuffing", "brute force",
                    "multi-factor authentication", "MFA", "token refresh"
                ],
            },
            "API3": {
                "title": "API3:2023 — Excessive Data Exposure",
                "part": "API3",
                "clause": "API Response Security",
                "content": (
                    "Excessive data exposure occurs when APIs return more data than the client needs or is authorized to see. Many developers implement APIs "
                    "that return all available fields in the data model, assuming the client application will filter what to display to the user. "
                    "This approach exposes sensitive data such as internal IDs, system information, personally identifiable information, or other sensitive data "
                    "that the client application doesn't need and users shouldn't see. "
                    "Common vulnerabilities include APIs that return all database fields including system IDs and internal data, APIs that expose user data "
                    "that clients don't display, APIs that return raw error messages with sensitive information, and APIs that lack field-level access controls. "
                    "Attackers can intercept API responses (through network capture, browser developer tools, or other means) to access sensitive data. "
                    "Testing must inspect API responses to identify data that shouldn't be exposed, test whether sensitive fields can be removed from responses, "
                    "verify that user-accessible data is properly filtered, and check error responses for sensitive information. "
                    "Mitigation includes implementing field-level access controls and only returning data the user is authorized to see, returning only the "
                    "minimum necessary fields for each API endpoint, implementing separate APIs for different data sensitivity levels, documenting what data "
                    "is returned by each endpoint, and regularly auditing API responses for sensitive data exposure."
                ),
                "keywords": [
                    "excessive data exposure", "data leakage", "API response", "sensitive data",
                    "field-level access control", "internal IDs", "system information", "PII",
                    "information disclosure", "data minimization"
                ],
            },
            "API4": {
                "title": "API4:2023 — Unrestricted Resource Consumption",
                "part": "API4",
                "clause": "Rate Limiting and Resource Controls",
                "content": (
                    "APIs that don't limit the size or number of resources requested are susceptible to denial of service (DoS) attacks where attackers "
                    "overwhelm the service by requesting excessive resources. Unrestricted resource consumption includes unbounded pagination, unlimited file uploads, "
                    "excessive request rates, and unbounded data retrieval. "
                    "Common vulnerabilities include pagination without limits allowing retrieval of massive datasets, file upload without size limits, "
                    "request rates not limited by user or IP address, timeout values set too high or not enforced, and memory-intensive operations that can be "
                    "triggered repeatedly. APIs should implement appropriate limits on all resources to prevent abuse. "
                    "Testing must verify rate limiting is in place on all endpoints, test what happens when requesting with extremely high pagination limits, "
                    "test file upload size limits, verify timeout mechanisms are enforced, test what happens when requesting complex queries that consume resources, "
                    "and verify that limits are applied per-user and per-IP address. "
                    "Mitigation includes implementing rate limiting on all endpoints, limiting pagination size to reasonable values, implementing maximum file "
                    "upload sizes, setting appropriate timeout values on all operations, implementing query complexity limits (especially for GraphQL), "
                    "limiting the number of records returned per request, monitoring resource consumption and alerting on anomalies, implementing caching to "
                    "reduce computational load, and using API gateway tools to enforce global rate limits."
                ),
                "keywords": [
                    "rate limiting", "DoS", "denial of service", "resource consumption", "pagination",
                    "timeout", "file upload", "request rate", "API gateway", "circuit breaker",
                    "query complexity", "complexity analysis"
                ],
            },
            "API5": {
                "title": "API5:2023 — Broken Function Level Authorization",
                "part": "API5",
                "clause": "Endpoint-Level Authorization",
                "content": (
                    "Broken Function Level Authorization occurs when APIs don't properly enforce authorization at the endpoint or operation level, allowing "
                    "regular users to access administrative functions or operations they shouldn't be able to perform. "
                    "This vulnerability goes beyond object-level authorization to address whether a user should have access to a particular endpoint or operation. "
                    "Common vulnerabilities include administrative endpoints not being properly protected from regular users, endpoints not validating whether "
                    "the user has the appropriate role to call them, different HTTP methods (GET, POST, PUT, DELETE) on the same endpoint having different "
                    "authorization levels without proper enforcement, and APIs that rely on client-side enforcement of function availability. "
                    "Testing must attempt to call administrative endpoints as a regular user, test whether all HTTP methods on sensitive endpoints are protected, "
                    "verify that function availability is controlled server-side not client-side, attempt to call operations the current user shouldn't have access to, "
                    "and verify that authorization is consistently enforced. "
                    "Mitigation includes implementing function-level access control on all endpoints, verifying user roles and permissions server-side for all operations, "
                    "implementing consistent authorization logic across similar endpoints, removing or securing admin endpoints in production, logging access attempts "
                    "to sensitive operations, and regularly testing authorization enforcement."
                ),
                "keywords": [
                    "function level authorization", "endpoint authorization", "admin endpoints", "role-based access",
                    "permission check", "HTTP method", "server-side enforcement", "client-side enforcement",
                    "operation authorization", "feature flags"
                ],
            },
            "API6": {
                "title": "API6:2023 — Unrestricted Access to Sensitive Business Operations",
                "part": "API6",
                "clause": "Business Operation Protection",
                "content": (
                    "APIs that expose sensitive business operations without appropriate access controls allow attackers to perform critical actions. "
                    "These operations might be intended for specific users or roles only, but without proper authorization, any authenticated user could perform them. "
                    "Sensitive business operations include financial transactions, account modifications, user creation/deletion, payment processing, order placement, "
                    "data export, and other critical operations. "
                    "Common vulnerabilities include business operations without authorization checks, multi-step processes that can be skipped, operations that "
                    "should require approval but don't, and operations that aren't properly validated for authorization. "
                    "Testing must identify all sensitive business operations in the API, attempt to perform each operation as an unauthorized user, test whether "
                    "multi-step operations enforce the sequence, verify that sensitive operations require appropriate confirmation or approval, and test whether "
                    "operation limits are enforced. "
                    "Mitigation includes implementing robust authorization checks for all business operations, requiring multi-factor authentication or additional "
                    "confirmation for highly sensitive operations, implementing separation of duties where multiple approvals are required, logging all business "
                    "operations for audit trails, implementing rate limiting on sensitive operations, and regularly testing that sensitive operations are properly protected."
                ),
                "keywords": [
                    "business operations", "sensitive operations", "financial transactions", "operation authorization",
                    "approval workflow", "separation of duties", "operation logging", "audit trail",
                    "operation limits", "sensitive actions"
                ],
            },
            "API7": {
                "title": "API7:2023 — Server-Side Request Forgery (SSRF)",
                "part": "API7",
                "clause": "Outbound Request Validation",
                "content": (
                    "Server-Side Request Forgery (SSRF) in APIs occurs when an API endpoint accepts user-supplied URLs and fetches the resource without "
                    "properly validating the URL. This allows attackers to cause the API server to make requests to internal services, local services, "
                    "or external services on the attacker's behalf. "
                    "Common vulnerabilities include APIs that fetch remote resources based on user input without validation, APIs that don't restrict "
                    "which URL schemes are allowed (file://, ftp://, etc.), APIs without network segmentation controls preventing access to internal services, "
                    "and APIs without allowlisting of allowed destination hosts. "
                    "Attack vectors include accessing internal admin consoles or control panels, accessing cloud metadata endpoints (AWS EC2 metadata service), "
                    "scanning internal networks from the API server, accessing services on non-standard ports, port scanning the local network, reading local files "
                    "using file:// scheme, and sending requests to external systems on behalf of the attacker. "
                    "Testing must identify API endpoints that fetch remote resources, attempt to fetch internal IP addresses and localhost, test for access to "
                    "metadata endpoints, test different URL schemes, and verify that internal network access is restricted. "
                    "Mitigation includes implementing strict URL validation with allowlisting of acceptable hosts, disabling unused URL schemes, implementing "
                    "network-level controls to restrict outbound access, segmenting networks to isolate sensitive services, using security groups to restrict access, "
                    "and avoiding exposing sensitive services on the same network as the API."
                ),
                "keywords": [
                    "SSRF", "server-side request forgery", "URL validation", "outbound requests", "URL scheme",
                    "internal services", "metadata endpoints", "localhost", "127.0.0.1", "private IP",
                    "port scanning", "file:// scheme", "allowlisting", "network segmentation"
                ],
            },
            "API8": {
                "title": "API8:2023 — Lack of Protection from Automated Threats",
                "part": "API8",
                "clause": "Automated Attack Prevention",
                "content": (
                    "APIs are commonly targeted by automated attacks including bot attacks, scraping, credential stuffing, account enumeration, and other "
                    "automated exploits. Many APIs lack protection against these automated threats. Unlike web applications where human interaction is expected, "
                    "APIs are designed to be programmatically accessed, making it difficult to distinguish legitimate use from automated attacks. "
                    "Common vulnerabilities include lack of rate limiting allowing repeated requests, no account lockout or throttling after failed attempts, "
                    "no CAPTCHA or other bot detection mechanisms, no ability to detect and block automated tools, and no monitoring of automated attack patterns. "
                    "Attack vectors include credential stuffing attacking login endpoints, account enumeration discovering valid usernames/emails, scraping of data, "
                    "resource exhaustion through automated requests, and information disclosure through systematic testing. "
                    "Testing must verify rate limiting per user and IP address, test account lockout mechanisms, test for bot detection capabilities, monitor "
                    "for detection of automated tools and scrapers, and verify alerting on automated attack patterns. "
                    "Mitigation includes implementing rate limiting on all endpoints, implementing account lockout after repeated failed authentication attempts, "
                    "implementing CAPTCHA or other bot detection for sensitive operations, monitoring for patterns of automated attacks, blocking IP addresses "
                    "or accounts exhibiting suspicious patterns, implementing API gateway tools with DDoS protection, and using behavioral analytics to detect "
                    "automated access patterns."
                ),
                "keywords": [
                    "automated threats", "bot attacks", "scraping", "credential stuffing", "rate limiting",
                    "account lockout", "CAPTCHA", "bot detection", "DDoS protection", "account enumeration",
                    "brute force", "attack patterns", "behavioral analytics"
                ],
            },
            "API9": {
                "title": "API9:2023 — Improper Inventory Management",
                "part": "API9",
                "clause": "API Discovery and Documentation",
                "content": (
                    "Improper inventory management occurs when organizations don't maintain a complete and accurate inventory of their APIs, leading to "
                    "unmonitored, unpatched, or forgotten APIs that become security vulnerabilities. Many organizations have shadow APIs or undocumented endpoints "
                    "that are difficult to secure. "
                    "Common vulnerabilities include lack of API inventory, unmonitored or unpatched APIs, APIs left in production after development, development "
                    "and testing APIs accessible in production, old API versions still accessible in production, APIs without documentation, and APIs with unclear "
                    "ownership or responsibility. "
                    "Without proper inventory management, organizations may miss security patches, fail to apply security controls consistently, and leave "
                    "vulnerable APIs in production. "
                    "Testing must identify all APIs in production, document API versions, identify deprecated APIs, test for API discovery techniques (parameter fuzzing, "
                    "analyzing JavaScript), and verify that old API versions are properly deprecated. "
                    "Mitigation includes maintaining a comprehensive API inventory including all versions and endpoints, documenting all APIs with clear ownership "
                    "and responsibility, removing or deprecating old API versions, implementing API gateway tools to monitor and manage all APIs, using API discovery "
                    "tools to identify undocumented APIs, implementing consistent security controls across all APIs, monitoring all APIs for suspicious activity, "
                    "and regularly auditing the API inventory."
                ),
                "keywords": [
                    "API inventory", "API discovery", "shadow API", "undocumented API", "API versioning",
                    "API deprecation", "API gateway", "API documentation", "API management",
                    "API monitoring", "forgotten API", "API ownership"
                ],
            },
            "API10": {
                "title": "API10:2023 — Unsafe Consumption of APIs",
                "part": "API10",
                "clause": "Third-Party API Security",
                "content": (
                    "Unsafe consumption of third-party APIs occurs when an application integrates with external APIs without properly validating responses, "
                    "verifying TLS certificates, or implementing security controls. Just because an API is consumed from a third party doesn't mean it's secure. "
                    "Common vulnerabilities include trusting API responses without validation, not validating TLS certificates when making API calls, not implementing "
                    "timeouts on API requests, not handling API errors securely, not rate limiting requests to external APIs, and exposing API keys or credentials. "
                    "Testing must verify that API responses are validated before use, verify TLS certificate validation, test timeout mechanisms on external API calls, "
                    "verify that API errors are handled securely, test rate limiting on external API consumption, and verify that credentials are properly protected. "
                    "Mitigation includes validating all API responses including data type and format, verifying TLS certificates when making API calls, implementing "
                    "timeouts on all external API requests, handling API errors securely without exposing sensitive information, implementing rate limiting to prevent "
                    "external API abuse, protecting API credentials in secure storage never embedding in code, monitoring API consumption for anomalies, implementing "
                    "fallback mechanisms when external APIs are unavailable, and regularly testing third-party API integrations."
                ),
                "keywords": [
                    "third-party API", "unsafe consumption", "API integration", "response validation",
                    "TLS certificate validation", "timeout", "error handling", "rate limiting",
                    "API credentials", "fallback mechanism", "dependency"
                ],
            },
        },
    },
    "secure_development": {
        "title": "Secure Development Practices and Secure SDLC",
        "part": "Development Practices",
        "sections": {
            "threat_modeling": {
                "title": "Threat Modeling",
                "part": "Development",
                "clause": "Security Design Phase",
                "content": (
                    "Threat modeling is a structured process for identifying, understanding, and prioritizing security threats to an application or system. "
                    "Threat modeling should be performed early in the development process, starting during the design phase, and should be updated as the "
                    "application architecture changes. The goal is to identify potential security threats and vulnerabilities so that appropriate mitigations "
                    "can be designed and implemented. "
                    "Common threat modeling methodologies include STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation "
                    "of Privilege), PASTA (Process for Attack Simulation and Threat Analysis), and data flow diagrams. "
                    "The threat modeling process typically includes understanding the system architecture and data flows, identifying trust boundaries, identifying "
                    "potential threat actors and their goals, identifying potential attack vectors, assessing the likelihood and impact of each threat, "
                    "and prioritizing threats for mitigation. "
                    "Threat models should document all identified threats, potential impacts, and planned or implemented mitigations. Threat models should be "
                    "reviewed and updated throughout the development lifecycle as the application evolves."
                ),
                "keywords": [
                    "threat modeling", "STRIDE", "PASTA", "data flow diagram", "trust boundary",
                    "threat actor", "attack vector", "mitigation", "risk assessment", "security design"
                ],
            },
            "secure_requirements": {
                "title": "Security Requirements Definition",
                "part": "Development",
                "clause": "Requirement Specification",
                "content": (
                    "Security requirements must be defined early in the development process as part of the overall project requirements. Security requirements "
                    "specify what the system must do to protect against identified threats and to meet applicable security and compliance standards. "
                    "Security requirements should be derived from threat models, security standards (OWASP ASVS, company security policies), and compliance "
                    "requirements (GDPR, HIPAA, PCI-DSS, etc.). Requirements should be specific, measurable, and testable. "
                    "Common security requirements include authentication and authorization controls, encryption of sensitive data, input validation, output encoding, "
                    "secure error handling, logging and monitoring, and security testing. Requirements should address both preventive controls (preventing attacks) "
                    "and detective controls (identifying attacks). "
                    "Security requirements should be documented in the same format as functional requirements and should be tracked through the development "
                    "lifecycle. Requirements should be reviewed and validated to ensure they address identified threats and meet applicable standards."
                ),
                "keywords": [
                    "security requirements", "functional requirements", "non-functional requirements",
                    "requirement specification", "testable requirements", "OWASP ASVS", "compliance requirements",
                    "security controls", "preventive controls", "detective controls"
                ],
            },
            "secure_design": {
                "title": "Secure Architecture and Design",
                "part": "Development",
                "clause": "Architecture Review",
                "content": (
                    "Secure architecture and design involves incorporating security principles and controls into the application's design from the earliest phases. "
                    "Security should not be added as an afterthought but should be integrated throughout the architecture. "
                    "Secure design principles include defense in depth (multiple layers of security controls), least privilege (users have minimum necessary permissions), "
                    "fail securely (default to denying access), separation of concerns (different responsibilities isolated), and security by default. "
                    "Architecture reviews should identify potential security weaknesses, verify that threat model mitigations are incorporated into the design, "
                    "and ensure that security controls are properly integrated. Design documentation should clearly describe security controls and their interactions. "
                    "Common design patterns for security include authentication patterns (centralized authentication), authorization patterns (centralized access control), "
                    "encryption patterns (data protection), and error handling patterns (secure error messages). Architecture should also consider scalability and "
                    "operational security requirements."
                ),
                "keywords": [
                    "secure architecture", "secure design", "design principles", "defense in depth",
                    "least privilege", "fail securely", "separation of concerns", "design pattern",
                    "architecture review", "centralized controls", "layered security"
                ],
            },
            "secure_coding": {
                "title": "Secure Coding Practices",
                "part": "Development",
                "clause": "Code Implementation",
                "content": (
                    "Secure coding practices involve applying security principles during code implementation. Developers should be trained in common vulnerabilities "
                    "and how to avoid them. Secure coding includes input validation, output encoding, proper use of cryptography, secure error handling, and secure "
                    "use of APIs and libraries. "
                    "Common secure coding practices include validating all input on the server side using allowlists, encoding output appropriately for the context, "
                    "using parameterized queries to prevent SQL injection, properly handling errors without exposing sensitive information, using industry-standard "
                    "libraries for cryptography rather than custom implementations, and regularly keeping dependencies up to date. "
                    "Code should be reviewed for common vulnerabilities including injection attacks, cross-site scripting, broken authentication, broken access control, "
                    "insecure deserialization, and others. Developers should use static code analysis tools to identify potential vulnerabilities during development. "
                    "Security code reviews should be performed to ensure that code implements security requirements and follows secure coding standards."
                ),
                "keywords": [
                    "secure coding", "code review", "input validation", "output encoding", "cryptography",
                    "error handling", "parameterized queries", "SQL injection", "static analysis",
                    "SAST", "code inspection", "vulnerability patterns"
                ],
            },
            "security_testing": {
                "title": "Security Testing and Quality Assurance",
                "part": "Development",
                "clause": "Testing in Development",
                "content": (
                    "Security testing should be integrated into the development lifecycle and should include both automated and manual testing. Security testing "
                    "verifies that security requirements are implemented correctly and that the application is resistant to known attacks. "
                    "Static application security testing (SAST) tools analyze source code for vulnerabilities without executing the code. SAST tools can identify "
                    "many common vulnerabilities early in development. "
                    "Dynamic application security testing (DAST) tools test a running application by sending requests and analyzing responses. DAST tools simulate "
                    "real-world attacks and can identify runtime vulnerabilities. "
                    "Manual security testing includes penetration testing, code review, and security design review. Manual testing can identify vulnerabilities that "
                    "automated tools miss and can validate business logic security. "
                    "Security testing should cover all identified threats from threat modeling, all security requirements, and all security controls. Test results "
                    "should be documented and tracked to ensure that identified vulnerabilities are resolved before release."
                ),
                "keywords": [
                    "security testing", "SAST", "DAST", "penetration testing", "code review",
                    "manual testing", "automated testing", "vulnerability scanning", "security assessment",
                    "test coverage", "test automation", "threat-based testing"
                ],
            },
            "cicd_security": {
                "title": "Security in CI/CD Pipelines",
                "part": "Development",
                "clause": "Pipeline Integration",
                "content": (
                    "Continuous Integration/Continuous Deployment (CI/CD) pipelines can be leveraged to integrate security testing into the development process. "
                    "Security tools should be integrated into CI/CD pipelines to automatically test each code commit for vulnerabilities. "
                    "CI/CD security practices include running static analysis (SAST) on each commit, running dynamic analysis (DAST) on each build, scanning "
                    "dependencies for known vulnerabilities, running security-focused unit tests, and performing security-focused code reviews. "
                    "Automated security gating should be implemented to prevent deployment of code with known vulnerabilities or that doesn't meet security requirements. "
                    "Build pipelines should verify code provenance and integrity to prevent malicious code injection. "
                    "Security testing results should be tracked and visibility provided to developers so that vulnerabilities are addressed promptly. "
                    "CI/CD infrastructure itself must be secured with proper access controls, audit logging, and integrity verification to prevent pipeline tampering."
                ),
                "keywords": [
                    "CI/CD security", "continuous integration", "continuous deployment", "pipeline",
                    "SAST in pipeline", "DAST in pipeline", "dependency scanning", "security gating",
                    "code integrity", "pipeline security", "automated testing", "security metrics"
                ],
            },
            "dependency_management": {
                "title": "Dependency and Component Management",
                "part": "Development",
                "clause": "Supply Chain Security",
                "content": (
                    "Dependency and component management involves maintaining visibility into all third-party components used in the application and ensuring "
                    "they remain secure and up to date. Many modern applications rely on numerous dependencies, each of which introduces potential security risks. "
                    "Software Composition Analysis (SCA) tools should be used to identify all components and their versions, detect known vulnerabilities, and "
                    "recommend updates. Dependency management should be automated where possible to ensure updates are applied consistently. "
                    "All dependencies should be from trusted sources and should be scanned for malware before being used. Transitive dependencies (dependencies "
                    "of dependencies) should also be managed and scanned. "
                    "A process should exist to evaluate new dependencies before adding them to the project, considering security, maintenance status, license, "
                    "and community support. Unused dependencies should be removed. "
                    "Dependency updates should be prioritized based on severity of security vulnerabilities and should be tested before deployment. "
                    "Dependency verification should include cryptographic verification where available."
                ),
                "keywords": [
                    "dependency management", "SCA", "software composition analysis", "vulnerable components",
                    "component inventory", "transitive dependencies", "dependency update", "SBOM",
                    "supply chain security", "component licensing"
                ],
            },
            "security_training": {
                "title": "Developer Security Training",
                "part": "Development",
                "clause": "Team Competency",
                "content": (
                    "All developers should receive security training covering secure coding practices, common vulnerabilities, and how to use security tools. "
                    "Security training should cover the OWASP Top 10, OWASP API Security Top 10, and other common vulnerabilities relevant to the organization. "
                    "Training should include practical exercises and code examples so developers can understand vulnerabilities and how to prevent them. "
                    "Security training should be ongoing as new vulnerabilities and attack techniques are discovered regularly. "
                    "Beyond general security training, developers should be trained on security tools used in the development process including static analysis tools, "
                    "dependency scanning tools, and how to interpret and fix security findings. "
                    "Security awareness training should cover secure development practices, secure handling of credentials and sensitive data, and incident response procedures. "
                    "Specialized training should be provided for security-critical roles such as architects and code reviewers."
                ),
                "keywords": [
                    "security training", "developer training", "secure coding training", "OWASP training",
                    "vulnerability awareness", "security awareness", "tool training", "security competency"
                ],
            },
            "incident_response": {
                "title": "Incident Response and Vulnerability Management",
                "part": "Development",
                "clause": "Incident Handling",
                "content": (
                    "Incident response and vulnerability management processes should be in place to address security vulnerabilities and breaches when they occur. "
                    "A process should exist to receive vulnerability reports, assess severity, and prioritize fixes. "
                    "Vulnerability disclosure policies should define how external security researchers can report vulnerabilities to the organization. "
                    "Identified vulnerabilities should be tracked through resolution and verification. Critical vulnerabilities should be patched and deployed quickly. "
                    "Incident response procedures should define roles, responsibilities, communication paths, and response steps for security incidents. "
                    "Post-incident reviews should analyze what happened, what controls failed, and how to prevent similar incidents in the future. "
                    "Vulnerability trending should be tracked to identify patterns and systemic issues. "
                    "Organizations should participate in vulnerability disclosure programs and maintain responsible disclosure practices."
                ),
                "keywords": [
                    "incident response", "vulnerability management", "vulnerability reporting",
                    "incident handling", "post-incident review", "patch management", "responsible disclosure",
                    "vulnerability tracking", "severity assessment", "remediation"
                ],
            },
        },
    },
}
