from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool
def update_employee_location(employee_name: str, new_location: str):
    """
    Mock function to simulate updating an employee's work location in a backend system.
    
    Args:
        employee_name (str): The employee's name
        new_location (str): The new work location
    
    Returns:
        dict: Response simulating a backend API response
    """
    # Simulate successful backend update
    return {
        "success": True,
        "message": f"Successfully updated location for {employee_name}",
        "data": {
            "employee_name": employee_name,
            "new_location": new_location,
            "updated_at": datetime.now().isoformat() + "Z"  # Current timestamp
        },
        "status_code": 200
    }