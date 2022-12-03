import uuid


def generate_randome_app_name() -> str:
    """_summary_
        Generate randome name for name of app 

    Returns:
        app_name: return uuid4 
    """
    return uuid.uuid4().__str__()
