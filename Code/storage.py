buffer = []

def add_pothole(event):
    buffer.append(event)

def get_buffer():
    return buffer

def clear_buffer():
    buffer.clear()
