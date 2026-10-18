import re

with open('frontend/SeniorFriendlyGeminiUI.tsx', 'r') as f:
    content = f.read()

select_match = re.search(r'<select[^>]*>', content)
if select_match:
    print(select_match.group(0))
