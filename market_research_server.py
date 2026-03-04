import os
import dotenv

def get_port():
    return int(os.environ.get('PORT', 5000))

# Other existing code that uses the port should call `get_port()` instead of using 5000 directly.