import re

with open('frontend/NEXUS_LEGACY_APP.tsx', 'r') as f:
    content = f.read()

# Inject CSS
css_injection = """
          .bento-btn:hover, .bento-btn:focus-visible { transform: scale(1.02) translateY(-10px) !important; }
          .studio-btn:hover, .studio-btn:focus-visible { transform: scale(1.05) !important; }
          .end-session-btn:hover, .end-session-btn:focus-visible { background-color: #ef4444 !important; }
          /* World-Class Ken Burns Animation for Documentaries */"""
content = content.replace('          /* World-Class Ken Burns Animation for Documentaries */', css_injection)

# Studio Button 1
content = re.sub(
    r'(<button\s+onClick=\{\(\) => handleSelectTheme\("NAT_GEO"\)\}\s+aria-label="Select Heritage Studio".*?)\s+onMouseOver=\{[^\}]+\}\s+onMouseOut=\{[^\}]+\}\s+onFocus=\{[^\}]+\}\s+onBlur=\{[^\}]+\}',
    r'\1\n          className="studio-btn"',
    content, flags=re.DOTALL
)

# Studio Button 2
content = re.sub(
    r'(<button\s+onClick=\{\(\) => handleSelectTheme\("AEROSPACE"\)\}\s+aria-label="Select Aerospace Studio".*?)\s+onMouseOver=\{[^\}]+\}\s+onMouseOut=\{[^\}]+\}\s+onFocus=\{[^\}]+\}\s+onBlur=\{[^\}]+\}',
    r'\1\n          className="studio-btn"',
    content, flags=re.DOTALL
)

# End Session Button
content = re.sub(
    r'(<button\s+onClick=\{\(\) => setIsVoiceOnlyMode\(false\)\}.*?)\s+onMouseOver=\{[^\}]+\}\s+onMouseOut=\{[^\}]+\}',
    r'\1\n        className="end-session-btn"',
    content, flags=re.DOTALL
)

# Bento Button
content = re.sub(
    r'(<button key=\{asset\.id\} aria-label=\{`Play \$\{asset\.title\}`\} style=\{\{[^>]+?width: "100%",\s+height: "100%"\s+\}\})\s+onMouseOver=\{[^\}]+\}\s+onMouseOut=\{[^\}]+\}\s+onFocus=\{[^\}]+\}\s+onBlur=\{[^\}]+\}',
    r'\1\n          className="bento-btn"',
    content, flags=re.DOTALL
)

with open('frontend/NEXUS_LEGACY_APP.tsx', 'w') as f:
    f.write(content)
