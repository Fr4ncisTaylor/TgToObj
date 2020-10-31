def match_with_text(arg, msg):
	if arg in msg:return msg[arg]
	else:return None

def match_with_class(arg, msg, classe):
	if arg in msg:return classe(msg[arg])
	else:return None