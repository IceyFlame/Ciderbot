import re
from bs4 import BeautifulSoup

def parse_aircraft_data(html_content, nation):
    """Parse aircraft data from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    aircraft_list = []
    
    # Find all aircraft items
    aircraft_items = soup.find_all('div', class_='wt-tree_item')
    
    for item in aircraft_items:
        try:
            # Extract aircraft name
            name_span = item.find('span', class_=False)  # Span without class
            if not name_span:
                continue
                
            name = name_span.get_text(strip=True)
            
            # Extract BR (battle rating)
            br_span = item.find('span', class_='br')
            if br_span:
                br_text = br_span.get_text(strip=True)
                br = float(br_text)
            else:
                br = 0.0
                
            # Check if premium
            is_premium = 'wt-tree_item--prem' in item.get('class', [])
            
            # Determine aircraft type based on name patterns
            aircraft_type = determine_aircraft_type(name)
            
            aircraft_data = {
                'name': name,
                'br': br,
                'type': aircraft_type,
                'nation': nation,
                'premium': is_premium,
                'unit_id': item.get('data-unit-id', '')
            }
            
            aircraft_list.append(aircraft_data)
            
        except Exception as e:
            print(f"Error parsing aircraft: {e}")
            continue
            
    return aircraft_list

def determine_aircraft_type(name):
    """Determine aircraft type based on name patterns"""
    name_lower = name.lower()
    
    # Fighter patterns
    fighter_patterns = ['p-', 'f-', 'mig-', 'yak-', 'i-', 'la-', 'spitfire', 'bf', 'fw', 'zero', 'a6m']
    # Bomber patterns  
    bomber_patterns = ['b-', 'il-', 'pe-', 'tu-', 'sb', 'db', 'yer', 'lancaster']
    # Attack/Strike patterns
    attack_patterns = ['a-', 'su-', 'il-2', 'ad-', 'am-', 'sbd', 'tbf']
    # Jet patterns
    jet_patterns = ['f-8', 'f-10', 'mig-15', 'mig-17', 'mig-21', 'f-86', 'f-4', 'f-14', 'f-15', 'f-16', 'su-27']
    
    if any(pattern in name_lower for pattern in jet_patterns):
        return 'jet'
    elif any(pattern in name_lower for pattern in fighter_patterns):
        return 'fighter'
    elif any(pattern in name_lower for pattern in bomber_patterns):
        return 'bomber'
    elif any(pattern in name_lower for pattern in attack_patterns):
        return 'attack'
    else:
        return 'other'

def save_as_python_file(aircraft_list, filename):
    """Save aircraft data as a Python file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Aircraft data extracted from War Thunder tech tree\n")
        f.write("# Generated automatically from HTML data\n\n")
        f.write("aircraft_data = [\n")
        
        for aircraft in aircraft_list:
            f.write(f"    {aircraft!r},\n")
        
        f.write("]\n\n")
        f.write("def get_aircraft_by_br(min_br=0, max_br=12.0):\n")
        f.write("    \"\"\"Filter aircraft by battle rating range\"\"\"\n")
        f.write("    return [ac for ac in aircraft_data if min_br <= ac['br'] <= max_br]\n\n")
        f.write("def get_aircraft_by_type(aircraft_type):\n")
        f.write("    \"\"\"Filter aircraft by type\"\"\"\n")
        f.write("    return [ac for ac in aircraft_data if ac['type'] == aircraft_type]\n\n")
        f.write("def get_premium_aircraft():\n")
        f.write("    \"\"\"Get all premium aircraft\"\"\"\n")
        f.write("    return [ac for ac in aircraft_data if ac['premium']]\n")

# Main execution
if __name__ == "__main__":
    # Read the HTML files
    with open('usatree.txt', 'r', encoding='utf-8') as f:
        us_html = f.read()
        
    with open('germanytree.txt', 'r', encoding='utf-8') as f:
        germany_html = f.read()
    
    # Parse aircraft data
    us_aircraft = parse_aircraft_data(us_html, 'USA')
    germany_aircraft = parse_aircraft_data(germany_html, 'germany')
    
    # Save as Python files
    save_as_python_file(us_aircraft, 'us_aircraft.py')
    save_as_python_file(germany_aircraft, 'germany_aircraft.py')
    
    print(f"Parsed {len(us_aircraft)} US aircraft")
    print(f"Parsed {len(germany_aircraft)} germany aircraft")
    print("Files saved as 'us_aircraft.py' and 'germany_aircraft.py'")