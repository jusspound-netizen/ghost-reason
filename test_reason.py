from ghost_reason import ReasonTracer
import time

tracer = ReasonTracer()

tracer.log("prompt", "Check the Jira ticket SAM1-1 and create a folder on the desktop.")
time.sleep(0.1)
tracer.log("thought", "I need to first get the ticket details, then create the folder.")
time.sleep(0.1)
tracer.log("tool_call", 'get_jira_ticket({"ticket_id": "SAM1-1"})')
time.sleep(0.1)
tracer.log("tool_result", '{"key": "SAM1-1", "summary": "Implement stress management techniques"}')
time.sleep(0.1)
tracer.log("thought", "Now I have the ticket. I will create the folder on the desktop.")
time.sleep(0.1)
tracer.log("tool_call", 'create_folder({"path": "C:\\\\Users\\\\User\\\\Desktop\\\\test_agent"})')
time.sleep(0.1)
tracer.log("tool_result", "Folder created.")

print("Reasoning steps logged.")
