from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool
import random

@tool
def update_work_items(employee_name: str, work_item_id: str, status: str, notes: str = ""):
    """
    Mock function to simulate updating work items in a backend system.

    Args:
        employee_name (str): The employee responsible for the work item
        work_item_id (str): The unique identifier of the work item
        status (str): The new status of the work item (e.g., "In Progress", "Completed", "On Hold")
        notes (str, optional): Additional notes or comments for the update

    Returns:
        dict: Response simulating a backend API response
    """
    # Simulated fake update success/failure
    success = random.choice([True, True, False])  # more likely to succeed than fail

    return {
        "message": (
            f"Successfully updated work item {work_item_id} for {employee_name}"
            if success else f"Failed to update work item {work_item_id}"
        ),
        "data": {
            "employee_name": employee_name,
            "work_item_id": work_item_id,
            "new_status": status,
            "notes": notes,
            "success": success,
            "updated_at": datetime.now().isoformat() + "Z"
        }
    }
