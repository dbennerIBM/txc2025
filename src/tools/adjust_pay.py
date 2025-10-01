from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool
def update_employee_pay(employee_name: str, yearly_salary: int):
    """
    Mock function to simulate updating an employee's yearly salary in a backend system.
    
    Args:
        employee_name (str): The employee's name
        yearly_salary (float): The new yearly salary amount in dollars
    
    Returns:
        dict: Response simulating a backend API response
    """
    # Simulate successful backend update
    return {
        "message": f"Successfully updated salary for {employee_name}",
        "data": {
            "employee_name": employee_name,
            "new_salary": yearly_salary,
            "updated_at": datetime.now().isoformat() + "Z"  # Current timestamp
        }
    }