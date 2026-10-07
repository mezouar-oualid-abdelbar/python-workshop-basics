def bind_lists(keys,values):
	if len(keys) != len(values):
		return "Error: Lists must have the same length."
	return dict(zip(keys,values))
