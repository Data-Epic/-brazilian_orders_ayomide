import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.api import app
#docker 
#brazil_order_ayomide-api-deployment .