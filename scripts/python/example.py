# Example Python userscript for PyTorn

def on_page_load(context):
    """Function called when a page loads.
    
    Args:
        context: The script execution context with helper methods.
    """
    # Get the current URL
    url = context.get_url()
    
    # Only run on the items.php page
    if 'items.php' not in url:
        return
    
    # Log a message
    context.log('Example script running on items page')
    
    # Add a simple button to the page
    button_html = '<button id="pytorn-example-button" class="torn-btn">Quick Actions</button>'
    context.insert_html('.content-title', 'afterend', button_html)
    
    # Add a click handler
    context.add_event_listener('#pytorn-example-button', 'click', on_button_click)

def on_button_click(context, event):
    """Handle button click event.
    
    Args:
        context: The script execution context.
        event: The event data.
    """
    # Show a simple dialog with item counts
    item_counts = get_item_counts(context)
    
    message = 'Item Summary:\n'
    for category, count in item_counts.items():
        message += f"- {category}: {count}\n"
    
    context.show_dialog('Item Summary', message)

def get_item_counts(context):
    """Get counts of items by category.
    
    Args:
        context: The script execution context.
        
    Returns:
        dict: Mapping of category names to item counts.
    """
    # This is a simplified example - in reality we would use
    # context.query_selector_all() to find elements and count them
    
    # Placeholder implementation
    return {
        'Weapons': context.count_elements('.items-cont[data-category="1"] .items-item:not(.empty)'),
        'Armor': context.count_elements('.items-cont[data-category="2"] .items-item:not(.empty)'),
        'Temporary': context.count_elements('.items-cont[data-category="3"] .items-item:not(.empty)'),
        'Medical': context.count_elements('.items-cont[data-category="4"] .items-item:not(.empty)'),
        'Drugs': context.count_elements('.items-cont[data-category="5"] .items-item:not(.empty)'),
        'Energy Drinks': context.count_elements('.items-cont[data-category="6"] .items-item:not(.empty)'),
        'Alcohol': context.count_elements('.items-cont[data-category="7"] .items-item:not(.empty)'),
        'Candy': context.count_elements('.items-cont[data-category="8"] .items-item:not(.empty)'),
        'Book': context.count_elements('.items-cont[data-category="10"] .items-item:not(.empty)'),
        'Collectible': context.count_elements('.items-cont[data-category="11"] .items-item:not(.empty)'),
        'Enhancer': context.count_elements('.items-cont[data-category="12"] .items-item:not(.empty)'),
        'Special': context.count_elements('.items-cont[data-category="13"] .items-item:not(.empty)'),
        'Supply Pack': context.count_elements('.items-cont[data-category="14"] .items-item:not(.empty)'),
        'Booster': context.count_elements('.items-cont[data-category="15"] .items-item:not(.empty)'),
        'Other': context.count_elements('.items-cont[data-category="16"] .items-item:not(.empty)'),
    }

# Register the main entry point
register_handler('page_load', on_page_load)