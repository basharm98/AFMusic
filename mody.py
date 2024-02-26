import os


class Mody(object):
    ELHYBA = os.environ.get("ELHYBA", "")

    API_ID = int(os.environ.get("API_ID", 20036317))

    API_HASH = os.environ.get("API_HASH", "986cb4ba434870a62fe96da3b5f6d411")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 5145609515))
