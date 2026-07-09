import json, sys

with open('kbprocess/education_knowledge_base.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for entry in data:
    doc = entry['payload'].get('document', '')
    lines = doc.split('\n')
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if '$' in stripped or '\\frac' in stripped or '\\longrightarrow' in stripped or '\\xrightarrow' in stripped:
            sys.stdout.buffer.write(f"{count+1}. {stripped}\n\n".encode('utf-8'))
            count += 1
            if count >= 100:
                break
    if count >= 100:
        break

sys.stdout.buffer.write(f"\n--- Printed {count} formula lines ---\n".encode('utf-8'))
