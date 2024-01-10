import random
def handle_responses(message) -> str:
    rumourlist = []
    p_message = message.lower()
    p_message = p_message.replace('<@1193176493430423635> ', '')

    if p_message == 'Help':
        return 'Hey there, if you have a new rumour please @ me and include #TransferRumour, if you want a summary then please use #TransferSummary'
    
    if p_message == 'Rumour Summary':
        return 'Rumours are:'
    
    
        