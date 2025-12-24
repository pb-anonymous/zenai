import requests # type: ignore
import json
import re
import ast

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

SYSTEM_PROMPT = """
You are Zen, a helpful personal AI assistant.

You MUST respond ONLY in valid JSON format.
NO markdown. NO explanations outside JSON.

Your response MUST always be:
{
  "actions": [
    {"type": "action_type", "field1": "value1", ...}
  ]
}

Allowed action types:
1. open_application { "type": "open_application", "name": "app_name" }
2. open_website { "type": "open_website", "url": "url" }
3. write_file { "type": "write_file", "file_name": "name.ext", "content": "full_code_here" }
4. create_ppt { "type": "create_ppt", "title": "title", "slides": [{"title": "s1", "content": "c1"}] }
5. respond { "type": "respond", "message": "your_message" }

CRITICAL RULES:
- When user says "open [app_name]": Use open_application, NOT open_website
  Examples: "open whatsapp" -> open_application, "open spotify" -> open_application
- When user explicitly says "open website" or "search web": Use open_website
- For coding requests: Use write_file with COMPLETE, working code (no truncation)
- For knowledge questions: Use respond (don't open websites unless explicitly asked)
- Always respond with valid JSON only - no extra text before or after JSON
- If unsure, use respond action

Important: Desktop apps take priority over websites. If user says "open Spotify", they want the Spotify app, not the website.

Examples:
{"actions": [{"type": "respond", "message": "Hello! How can I help?"}]}
{"actions": [{"type": "open_application", "name": "notepad"}]}
{"actions": [{"type": "open_application", "name": "whatsapp"}]}
{"actions": [{"type": "open_application", "name": "spotify"}]}
{"actions": [{"type": "write_file", "file_name": "test.py", "content": "print('hello')"}]}
"""

def ask_ollama(user_text):
    prompt = SYSTEM_PROMPT + "\nUser request: " + user_text

    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120
        )
        raw = response.json().get("response", "")
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return {
            "actions": [{
                "type": "respond",
                "message": "I couldn't connect to Ollama. Make sure it's running."
            }]
        }

    print(f"Raw Ollama response: {raw}")

    # Try to extract and parse JSON
    # First, try to find valid JSON as-is
    start_idx = raw.find('{')
    if start_idx == -1:
        return {
            "actions": [{
                "type": "respond",
                "message": f"No JSON found in response"
            }]
        }
    
    # Find closing brace or bracket - search from end backwards
    end_idx = -1
    for end_search in range(len(raw) - 1, start_idx, -1):
        if raw[end_search] in ('}', ']'):
            end_idx = end_search + 1
            break
    
    if end_idx == -1:
        return {
            "actions": [{
                "type": "respond",
                "message": "Could not find JSON end marker"
            }]
        }
    
    # Extract potential JSON
    json_str = raw[start_idx:end_idx]
    
    # First attempt: parse as-is
    try:
        result = json.loads(json_str)
        if "actions" in result and isinstance(result["actions"], list):
            return result
    except json.JSONDecodeError as e:
        print(f"Initial parse failed: {e}")
        pass
    
    # Second attempt: fix newlines in strings
    try:
        fixed_json = ""
        in_string = False
        escape_next = False
        i = 0
        
        while i < len(json_str):
            char = json_str[i]
            
            if escape_next:
                fixed_json += char
                escape_next = False
                i += 1
                continue
            
            if char == '\\':
                fixed_json += char
                escape_next = True
                i += 1
                continue
            
            if char == '"':
                fixed_json += char
                in_string = not in_string
                i += 1
                continue
            
            # Escape unescaped newlines inside strings
            if in_string and char == '\n':
                fixed_json += '\\n'
                i += 1
                continue
            
            fixed_json += char
            i += 1
        
        print(f"Attempting parse with newline fixes...")
        result = json.loads(fixed_json)
        if "actions" in result and isinstance(result["actions"], list):
            return result
    except json.JSONDecodeError as e:
        print(f"Parse with newline fix failed: {e}")
        pass
    
    # Third attempt: try to extract just the actions array
    try:
        actions_start = json_str.find('"actions"')
        if actions_start != -1:
            # Find the opening bracket of the actions array
            bracket_start = json_str.find('[', actions_start)
            if bracket_start != -1:
                # Find matching closing bracket
                bracket_count = 0
                bracket_end = -1
                in_str = False
                esc = False
                
                for i in range(bracket_start, len(json_str)):
                    ch = json_str[i]
                    if esc:
                        esc = False
                        continue
                    if ch == '\\':
                        esc = True
                        continue
                    if ch == '"':
                        in_str = not in_str
                    if not in_str:
                        if ch == '[':
                            bracket_count += 1
                        elif ch == ']':
                            bracket_count -= 1
                            if bracket_count == 0:
                                bracket_end = i + 1
                                break
                
                if bracket_end != -1:
                    # Extract and fix the actions array
                    actions_str = json_str[bracket_start:bracket_end]
                    
                    # Fix newlines in the actions array
                    fixed_actions = ""
                    in_string = False
                    escape_next = False
                    
                    for char in actions_str:
                        if escape_next:
                            fixed_actions += char
                            escape_next = False
                            continue
                        if char == '\\':
                            fixed_actions += char
                            escape_next = True
                            continue
                        if char == '"':
                            fixed_actions += char
                            in_string = not in_string
                            continue
                        if in_string and char == '\n':
                            fixed_actions += '\\n'
                            continue
                        fixed_actions += char
                    
                    # Wrap in a valid object and parse
                    wrapped = '{"actions": ' + fixed_actions + '}'
                    print(f"Trying extracted actions: {wrapped[:200]}...")
                    result = json.loads(wrapped)
                    if "actions" in result and isinstance(result["actions"], list):
                        return result
    except Exception as e:
        print(f"Extraction attempt failed: {e}")
        pass
    
    print(f"All parsing attempts failed")
    return {
        "actions": [{
            "type": "respond",
            "message": "Couldn't parse response. Please try again."
        }]
    }
