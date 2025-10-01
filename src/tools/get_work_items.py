import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool
def get_manager_work_items(manager_id: str = None) -> List[Dict[str, Any]]:
    """
    Mock function to retrieve work items for a manager from a backend system.
    
    Args:
        manager_id (str, optional): Manager's unique identifier
    
    Returns:
        List[Dict[str, Any]]: List of work items requiring manager attention
    """
    
    # Sample work item types and templates
    work_item_templates = [
        {
            "type": "pay_adjustment",
            "title": "Pay Adjustment Request",
            "base_description": "requests a salary adjustment",
            "departments": ["Engineering", "Sales", "Marketing", "HR", "Finance"]
        },
        {
            "type": "employee_relocation",
            "title": "Employee Relocation Request", 
            "base_description": "has requested relocation assistance",
            "departments": ["Engineering", "Sales", "Marketing", "Operations"]
        },
        {
            "type": "it_device_approval",
            "title": "IT Device Approval",
            "base_description": "requires approval for new equipment",
            "departments": ["Engineering", "Design", "Marketing", "Sales"]
        },
        {
            "type": "vacation_approval",
            "title": "Vacation Request",
            "base_description": "has submitted a vacation request",
            "departments": ["Engineering", "Sales", "Marketing", "HR", "Finance", "Operations"]
        },
        {
            "type": "training_approval",
            "title": "Training Budget Approval",
            "base_description": "requests approval for professional training",
            "departments": ["Engineering", "Sales", "Marketing", "HR"]
        },
        {
            "type": "team_expansion",
            "title": "Team Expansion Request",
            "base_description": "has requested to hire additional team members",
            "departments": ["Engineering", "Sales", "Marketing", "Operations"]
        },
        {
            "type": "expense_approval",
            "title": "Expense Report Approval",
            "base_description": "submitted expense report for approval",
            "departments": ["Sales", "Marketing", "Engineering", "Operations"]
        }
    ]
    
    # Sample employee names
    employee_names = [
        "Alex Johnson", "Sarah Chen", "Michael Rodriguez", "Emily Davis", 
        "David Wilson", "Jessica Martinez", "Ryan Thompson", "Amanda Lee",
        "Kevin Brown", "Lisa Garcia", "Daniel Kim", "Rachel White",
        "James Taylor", "Maria Lopez", "Christopher Moore", "Ashley Clark"
    ]
    
    # Generate work items
    work_items = []
    
    # Always ensure pay adjustment and relocation requests appear for the same user
    guaranteed_employee = random.choice(employee_names)
    employee_names.remove(guaranteed_employee)  # Remove from available pool
    
    # Find pay adjustment and relocation templates
    pay_adjustment_template = next(t for t in work_item_templates if t["type"] == "pay_adjustment")
    relocation_template = next(t for t in work_item_templates if t["type"] == "employee_relocation")
    
    # Generate guaranteed work items for the same employee
    guaranteed_templates = [pay_adjustment_template, relocation_template]
    
    for i, template in enumerate(guaranteed_templates):
        employee = guaranteed_employee
        
        # Generate submission date (within last 30 days)
        days_ago = random.randint(0, 30)
        submitted_date = datetime.now() - timedelta(days=days_ago)
        
        # Create base work item
        work_item = {
            "id": f"WI-{1000 + len(work_items)}",
            "title": template["title"],
            "employee_name": employee,
            "date_submitted": submitted_date.strftime("%Y-%m-%d"),
            "days_pending": days_ago,
            "description": f"{employee} {template['base_description']}"
        }
        
        work_items.append(work_item)
    
    # Generate remaining random work items
    limit = 5
    remaining_slots = limit - 2  # We already have 2 guaranteed items
    actual_remaining = min(remaining_slots, len(employee_names))
    
    for i in range(actual_remaining):
        template = random.choice(work_item_templates)
        employee = random.choice(employee_names)
        employee_names.remove(employee)  # Avoid duplicates
        
        # Generate submission date (within last 30 days)
        days_ago = random.randint(0, 30)
        submitted_date = datetime.now() - timedelta(days=days_ago)
        
        # Create base work item
        work_item = {
            "id": f"WI-{1000 + len(work_items)}",
            "title": template["title"],
            "employee_name": employee,
            "date_submitted": submitted_date.strftime("%Y-%m-%d"),
            "days_pending": days_ago,
            "description": f"{employee} {template['base_description']}"
        }
        
        work_items.append(work_item)
    
    return work_items