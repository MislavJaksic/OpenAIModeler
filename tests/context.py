import os
import sys

# Adds "openai_modeler" to sys.path
# Now you can do import with "from openai_modeler.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "openai_modeler"))
)
