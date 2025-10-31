# tanks_data.py
"""
War Thunder Vehicle Database
Structure for each vehicle:
{'name': str, 'br': float, 'type': str, 'nation': str, 'premium': bool}
Vehicle types: light_tank, medium_tank, heavy_tank, tank_destroyer, spaa
"""

# USA Vehicles
# USA Vehicles
usa_vehicles = [
    # Rank I - Researchable
    {'name': 'M2A4', 'br': 1.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M2', 'br': 1.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'LVT(A)(1)', 'br': 1.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M13 MGMC', 'br': 1.7, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M2A2', 'br': 1.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M3 Stuart', 'br': 2.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M22', 'br': 2.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M15 CGMC', 'br': 1.7, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M8 HMC', 'br': 1.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M3A1 Stuart', 'br': 2.3, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M3 GMC', 'br': 1.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    
    # Rank I - Premium
    {'name': 'M2A4 (1st Arm.Div.)', 'br': 1.0, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    {'name': '○LVT(A)(1)', 'br': 1.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'LVT(A)(4)', 'br': 1.3, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M8 LAC', 'br': 1.0, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M3A1 (USMC)', 'br': 2.3, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    
    # Rank II - Researchable
    {'name': 'M5A1', 'br': 2.7, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M3 Lee', 'br': 2.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M16 MGMC', 'br': 2.7, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M4A3 (105)', 'br': 3.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M24', 'br': 3.7, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4A1', 'br': 3.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4', 'br': 3.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4A2', 'br': 4.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T77E1', 'br': 4.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M10 GMC', 'br': 3.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    
    # Rank II - Premium
    {'name': '▃Stuart VI (5th CAD)', 'br': 2.7, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    {'name': '▃LVT(A)(4) (ZIS-2)', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': '▃Grant I', 'br': 2.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M5A1 TD', 'br': 2.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M4A5', 'br': 3.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M8A1 GMC', 'br': 2.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'M24 (TL)', 'br': 3.7, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T18E2', 'br': 3.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'M4', 'br': 3.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    
    # Rank III - Researchable
    {'name': 'M18 GMC', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M4A1 (76) W', 'br': 5.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M6A1', 'br': 5.0, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T1E1', 'br': 5.3, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M19A1', 'br': 4.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M42', 'br': 4.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M44', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M4A2 (76) W', 'br': 5.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4A3 (76) W', 'br': 5.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4A3E2', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M55', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'T1E1 (90)', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M36 GMC', 'br': 5.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M36B2', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    
    # Rank III - Premium
    {'name': 'T14', 'br': 4.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': True},
    {'name': 'Calliope', 'br': 4.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'Cobra King', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': True},
    {'name': 'T55E1', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'Sherman (Hell)', 'br': 5.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'Hellcat (Hell)', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': '▃Skink (Hell)', 'br': 5.3, 'type': 'spaa', 'nation': 'usa', 'premium': True},
    {'name': 'T86', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'M18 "Black Cat"', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    
    # Rank IV - Researchable
    {'name': 'M41A1', 'br': 6.3, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4/T26', 'br': 6.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T25', 'br': 6.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M4A3E2 (76) W', 'br': 6.3, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': '▃Skink', 'br': 5.3, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M109A1', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'T92', 'br': 7.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M26', 'br': 6.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T26E5', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T26E1-1', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M56', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M46', 'br': 7.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T34', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M50', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    
    # Rank IV - Premium
    {'name': 'Super Hellcat', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'T28', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'T20', 'br': 6.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M551(76)', 'br': 7.0, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M26 T99', 'br': 6.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'T30', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M26E1', 'br': 6.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M6A2E1', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M46 "Tiger"', 'br': 7.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'T29', 'br': 7.0, 'type': 'heavy_tank', 'nation': 'usa', 'premium': True},
    
    # Rank V - Researchable
    {'name': 'M551', 'br': 8.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M47', 'br': 7.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M48A1', 'br': 7.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T32', 'br': 7.3, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T32E1', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M163', 'br': 7.3, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'T95', 'br': 7.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M60', 'br': 8.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M103', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'usa', 'premium': False},
    
    # Rank V - Premium
    {'name': 'M728 CEV', 'br': 7.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'T114', 'br': 7.7, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'T54E2', 'br': 7.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': '▃Magach 3 (ERA)', 'br': 8.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'T54E1', 'br': 8.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'T58', 'br': 8.3, 'type': 'heavy_tank', 'nation': 'usa', 'premium': True},
    
    # Rank VI - Researchable
    {'name': 'XM800T', 'br': 8.7, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M60A1 (AOS)', 'br': 8.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M60A1 RISE (P)', 'br': 8.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'T95E1', 'br': 8.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'XM246', 'br': 8.3, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M60A2', 'br': 8.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M3 Bradley', 'br': 8.3, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M60A3 TTS', 'br': 9.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'XM803', 'br': 9.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'MBT-70', 'br': 9.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M247', 'br': 9.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'Stingray', 'br': 9.3, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'Imp.Chaparral', 'br': 9.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    
    # Rank VI - Premium/Squadron
    {'name': 'M901', 'br': 8.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'EFV', 'br': 9.3, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'XM1 (Chrysler)', 'br': 9.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': '▃Merkava Mk.1', 'br': 9.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'XM1 (GM)', 'br': 9.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': '▃Merkava Mk.2B', 'br': 9.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'XM8', 'br': 9.7, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    
    # Rank VII - Researchable
    {'name': 'M3A3 Bradley', 'br': 10.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': '120S', 'br': 10.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M1 Abrams', 'br': 10.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'LAV-AD', 'br': 10.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M1128', 'br': 10.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'HSTV-L', 'br': 12.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M1A1 HC', 'br': 12.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M1A1', 'br': 11.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'IPM1', 'br': 11.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'XM975', 'br': 10.0, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    
    # Rank VII - Premium/Squadron
    {'name': 'M1128 Wolfpack', 'br': 10.3, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': True},
    {'name': 'CCVL', 'br': 10.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M1 KVT', 'br': 10.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'M60 AMBT', 'br': 10.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': '␙M1A1', 'br': 11.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'LOSAT', 'br': 10.0, 'type': 'tank_destroyer', 'nation': 'usa', 'premium': False},
    {'name': 'M1A1 AIM', 'br': 12.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'AGS', 'br': 12.0, 'type': 'light_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M1A1 Click-Bait', 'br': 12.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': '▃Merkava Mk.3D', 'br': 11.3, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': '◍M1A1 HC', 'br': 12.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': True},
    {'name': 'RDF/LT', 'br': 12.0, 'type': 'light_tank', 'nation': 'usa', 'premium': True},
    
    # Rank VIII - Researchable
    {'name': 'M1A2 Abrams', 'br': 12.0, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'M1A2 SEP', 'br': 12.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'ADATS', 'br': 11.7, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'M1A2 SEP V2', 'br': 12.7, 'type': 'medium_tank', 'nation': 'usa', 'premium': False},
    {'name': 'CLAWS (TADS)', 'br': 12.3, 'type': 'spaa', 'nation': 'usa', 'premium': False},
    {'name': 'CLAWS (TEL)', 'br': 12.3, 'type': 'spaa', 'nation': 'usa', 'premium': False},
]

# Germany Vehicles
# Germany Vehicles
germany_vehicles = [
    # Rank I - Researchable
    {'name': 'Garford-Beute', 'br': 1.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Beutepanzer IV', 'br': 1.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'A7V', 'br': 1.0, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Flakpanzer I', 'br': 1.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Flakpanzer 38', 'br': 1.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': '15cm sIG 33 B Sfl', 'br': 1.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.221 (s.Pz.B.41)', 'br': 1.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.35(t)', 'br': 1.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III E', 'br': 1.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III B', 'br': 1.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV C', 'br': 1.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.222', 'br': 2.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Panzerjäger I', 'br': 1.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.251/9', 'br': 1.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.38(t) A', 'br': 1.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III F', 'br': 1.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.II C', 'br': 1.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.II F', 'br': 1.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz. 6/2', 'br': 2.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Marder III', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'StuG III A', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.38(t) F', 'br': 2.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.38(t) n.A.', 'br': 2.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III J', 'br': 2.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV E', 'br': 2.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV F1', 'br': 2.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    
    # Rank I - Premium
    {'name': 'Pz.II C TD', 'br': 1.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.251/10', 'br': 1.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Pz.II C (DAK)', 'br': 1.3, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Sd.Kfz.234/1', 'br': 2.0, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Nb.Fz.', 'br': 1.3, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Sd.Kfz.234/3', 'br': 2.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Sd.Kfz. 140/1', 'br': 2.0, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Pz.Sp.Wg.P204(f) KwK 38', 'br': 2.0, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    
    # Rank II - Researchable
    {'name': 'Pz.Sp.Wg.P204(f) KwK 39/1', 'br': 2.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III J1', 'br': 2.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV F2', 'br': 3.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV G', 'br': 3.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.251/21', 'br': 3.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Marder III H', 'br': 3.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'StuH 42 G', 'br': 3.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'StuG III F', 'br': 3.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.234/2', 'br': 3.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III L', 'br': 3.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.III M', 'br': 3.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV H', 'br': 3.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Pz.IV J', 'br': 3.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'StuG III G', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Dicker Max', 'br': 3.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Sturer Emil', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    
    # Rank II - Premium
    {'name': '15 cm Pz.W.42', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Pz.Sfl.Ic', 'br': 2.7, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Pz.III J1 TD', 'br': 2.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Sd.Kfz.251/22', 'br': 3.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Pz.III N', 'br': 3.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Sd.Kfz.234/2 TD', 'br': 3.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    
    # Rank III - Researchable
    {'name': '8,8 cm Flak 37 Sfl.', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'M44', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Tiger H1', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'VK 3002 (M)', 'br': 5.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Ostwind', 'br': 3.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Wirbelwind', 'br': 3.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': '◄M55', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Nashorn', 'br': 5.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Waffenträger', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Tiger E', 'br': 6.0, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Panther D', 'br': 5.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Ostwind II', 'br': 5.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Jagdpanzer IV', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Jagdpanzer 38(t)', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Panzer IV/70(V)', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    
    # Rank III - Premium
    {'name': '▀KW II 754 (r)', 'br': 3.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': '▀M4 748 (a)', 'br': 4.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Pz.Bef.Wg.IV J', 'br': 3.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': '▀KV-IB', 'br': 4.3, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': '▀Pz.Kpfw. Churchill', 'br': 4.0, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Sd.Kfz.234/4', 'br': 4.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': '▀T 34 747 (r)', 'br': 4.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': 'VK 45.01 (P)', 'br': 5.3, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Brummbär', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'VFW', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Panzer IV/70(A)', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Tiger Ost', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Tiger West', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Ostwind Ost', 'br': 5.3, 'type': 'spaa', 'nation': 'germany', 'premium': True},
    {'name': '▀KW I C 756 (r)', 'br': 5.0, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': '␠Tiger', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    
    # Rank IV - Researchable
    {'name': 'M109G', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Tiger II (Nr.1-50)', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Panther A', 'br': 6.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Panther G', 'br': 6.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Panther F', 'br': 6.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Zerstörer 45', 'br': 6.0, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Jagdpanther G1', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'JPz 4-5', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'leKPz M41', 'br': 6.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Tiger II', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Kugelblitz', 'br': 6.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Ferdinand', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Jagdtiger', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    
    # Rank IV - Premium
    {'name': 'Pz.Bef.Wg.VI P', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Ersatz M10', 'br': 6.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': '38 cm Sturmmörser', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Flakpanzer 341', 'br': 7.0, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Bfw. Jagdpanther G1', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'SPz 12-3 LGS', 'br': 7.0, 'type': 'spaa', 'nation': 'germany', 'premium': True},
    {'name': 'Elefant', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': True},
    {'name': 'Tiger II (Sla.16)', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Panther II', 'br': 7.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Tiger II (10.5 cm Kw.K)', 'br': 7.0, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Ru 251', 'br': 7.3, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    
    # Rank V - Researchable
    {'name': 'Marder A1-', 'br': 7.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'SPz BMP-1', 'br': 8.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'M48A2 C', 'br': 7.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard I', 'br': 8.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Wiesel 1A4', 'br': 7.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'PzH 2000', 'br': 7.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Marder 1A3', 'br': 8.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'DF105', 'br': 8.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Luchs A2', 'br': 7.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Raketenautomat', 'br': 8.0, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'RakJPz 2', 'br': 8.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    
    # Rank V - Premium
    {'name': 'mKPz M47 G', 'br': 7.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': 'E-100', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'CLOVIS', 'br': 8.0, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Maus', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Turm III', 'br': 8.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    
    # Rank VI - Researchable
    {'name': 'TAM', 'br': 9.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'JaPz.K A2', 'br': 8.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'M48A2 G A2', 'br': 8.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard A1A1', 'br': 9.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 1A5', 'br': 9.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Gepard', 'br': 8.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'RakJPz 2 (HOT)', 'br': 8.3, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'Begleitpanzer 57', 'br': 9.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'KPz-70', 'br': 9.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'M48 Super', 'br': 9.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': '◊T-72M1', 'br': 9.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    
    # Rank VI - Premium
    {'name': 'TAM 2IP', 'br': 9.3, 'type': 'light_tank', 'nation': 'germany', 'premium': True},
    {'name': 'VT1-2', 'br': 8.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard A1A1 (L/44)', 'br': 9.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Class 3 (P)', 'br': 9.0, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'C2A1', 'br': 9.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    
    # Rank VII - Researchable
    {'name': 'Radkampfwagen 90', 'br': 10.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'TAM 2C', 'br': 10.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2K', 'br': 10.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2A4', 'br': 10.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Ozelot', 'br': 9.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Gepard 1A2', 'br': 9.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Wiesel 1A2', 'br': 9.7, 'type': 'tank_destroyer', 'nation': 'germany', 'premium': False},
    {'name': 'PUMA', 'br': 10.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'PUMA VJTF', 'br': 11.0, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'FlaRakPz 1', 'br': 10.0, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': '◊Osa-AK', 'br': 10.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': '◊Strela-10M', 'br': 10.3, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    
    # Rank VII - Premium
    {'name': 'Boxer MGS', 'br': 10.3, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2AV', 'br': 10.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Vilkas', 'br': 10.7, 'type': 'light_tank', 'nation': 'germany', 'premium': False},
    {'name': 'PT-16/T14 mod.', 'br': 11.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2A4M', 'br': 12.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': 'Leopard 2 (PzBtl 123)', 'br': 10.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': '◍Leopard 2A4M', 'br': 12.0, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    
    # Rank VIII - Researchable
    {'name': 'Leopard 2A5', 'br': 12.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2A6', 'br': 12.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'FlaRakRad', 'br': 11.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2 PSO', 'br': 12.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    {'name': 'IRIS-T SLM (TADS)', 'br': 12.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'IRIS-T SLM (TEL)', 'br': 12.7, 'type': 'spaa', 'nation': 'germany', 'premium': False},
    {'name': 'Leopard 2A7V', 'br': 12.7, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
    
    # Rank VIII - Premium/Squadron
    {'name': 'Leopard 2PL', 'br': 12.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': True},
    {'name': '␙Leopard 2A5', 'br': 12.3, 'type': 'medium_tank', 'nation': 'germany', 'premium': False},
]

# USSR Vehicles
ussr_vehicles = [
    # Rank I
    {'name': 'BT-5', 'br': 1.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-26', 'br': 1.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-26-4', 'br': 1.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Garford', 'br': 1.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'GAZ-AAA (4M)', 'br': 1.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'BT-7', 'br': 1.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-28 (1938)', 'br': 1.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-60', 'br': 1.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-5-1', 'br': 1.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'GAZ-AAA (DShK)', 'br': 1.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'BT-7M', 'br': 2.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-28', 'br': 1.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-70', 'br': 2.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-76M', 'br': 2.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},

    # Rank I Premium
    {'name': 'T-26 (1st Gv.T.Br.)', 'br': 1.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-26E', 'br': 1.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'BT-7 TD', 'br': 1.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'RBT-5', 'br': 1.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-35', 'br': 1.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'BA-11', 'br': 1.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'SU-57', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'BM-8-24', 'br': 1.3, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': '▂T-III', 'br': 2.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},

    # Rank II
    {'name': 'T-50', 'br': 2.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-28E', 'br': 2.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-80', 'br': 2.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'ZiS-30', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-57B', 'br': 2.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'GAZ-MM (72-K)', 'br': 2.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-34 (1940)', 'br': 3.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-34 (1941)', 'br': 4.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'KV-1 (L-11)', 'br': 3.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'KV-2 (1939)', 'br': 3.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-122', 'br': 2.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'BTR-152A', 'br': 2.7, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'ZiS-43', 'br': 3.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-34 (1942)', 'br': 4.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-34E STZ', 'br': 4.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'KV-1S', 'br': 4.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'YaG-10 (29-K)', 'br': 3.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'ZiS-12 (94-KM)', 'br': 3.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'ZSU-37', 'br': 3.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},

    # Rank II Premium
    {'name': 'ZUT-37', 'br': 2.3, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': 'SU-76M (5th Gv.Kav.Corps)', 'br': 2.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'T-126', 'br': 3.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'SU-76D', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34 (Prototype)', 'br': 3.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': '▂M3 Medium', 'br': 2.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'BT-7A (F-32)', 'br': 4.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'BM-13N', 'br': 2.7, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': 'SMK', 'br': 3.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': '▂MK-II "Matilda"', 'br': 3.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34 (1st Gv.T.Br.)', 'br': 4.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': '▂МК-IX "Valentine"', 'br': 3.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34E', 'br': 4.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'SU-85A', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},

    # Rank III
    {'name': 'T-34-57', 'br': 4.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'KV-1 (ZiS-5)', 'br': 4.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'KV-85', 'br': 5.0, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'ASU-57', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-152', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-85', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ISU-152', 'br': 4.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'BTR-152D', 'br': 4.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-34-85 (D-5T)', 'br': 5.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IS-1', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'PT-76B', 'br': 5.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-85M', 'br': 5.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ISU-122', 'br': 5.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},

    # Rank III Premium
    {'name': 'BM-31-12', 'br': 4.0, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': 'KV-2 (1940)', 'br': 3.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34-57 (1943)', 'br': 4.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'KV-7 (U-13)', 'br': 4.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'IS-1 (45)', 'br': 5.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34-85 (45)', 'br': 5.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'Hanomag (45)', 'br': 4.0, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': 'KV-1E', 'br': 4.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': '▂M4A2', 'br': 5.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'SU-100Y', 'br': 4.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': '▂Phòng không T-34', 'br': 5.0, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': 'KV-2 (ZiS-6)', 'br': 5.0, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34-85 "Partisan"', 'br': 5.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},

    # Rank IV
    {'name': 'T-34-85', 'br': 5.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IS-2', 'br': 6.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'ASU-85', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ISU-122S', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-100', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'BTR-ZD', 'br': 6.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-44', 'br': 6.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IS-2 (1944)', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IS-2 No.321', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-100P', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': '2S1', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': '2S3M', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'M53/59', 'br': 6.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},

    # Rank IV Premium
    {'name': 'KV-122', 'br': 5.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'KV-220', 'br': 6.0, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34-85E', 'br': 5.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': '▂T-V', 'br': 6.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'SU-122P', 'br': 5.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'T-44 (FM)', 'br': 6.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-44-122', 'br': 6.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'IS-2 "Revenge"', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-34-100', 'br': 6.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'Object 248', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': '▂Type 62', 'br': 6.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},

    # Rank V
    {'name': 'T-44-100', 'br': 7.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IS-3', 'br': 7.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'BTR-80A', 'br': 7.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'SU-122-54', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'Object 268', 'br': 7.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ZSU-57-2', 'br': 7.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-54 (1947)', 'br': 7.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-54 (1949)', 'br': 8.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-54 (1951)', 'br': 8.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IS-4M', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'BMP-1', 'br': 8.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Object 906', 'br': 8.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': '2S19M1', 'br': 7.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ZSU-23-4M2', 'br': 7.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'ZSU-37-2', 'br': 7.7, 'type': 'spaa', 'nation': 'ussr', 'premium': False},

    # Rank V Premium
    {'name': 'IS-6', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': '2S19M2', 'br': 7.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'Object 120', 'br': 8.0, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': True},
    {'name': 'T-10A', 'br': 7.7, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'TO-55', 'br': 8.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'PT-76-57', 'br': 8.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},

    # Rank VI
    {'name': 'T-55A', 'br': 8.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-62', 'br': 8.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-10M', 'br': 8.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'BMP-2', 'br': 8.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Object 685', 'br': 8.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'IT-1', 'br': 8.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ZSU-23-4V', 'br': 8.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-55AMD-1', 'br': 9.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-62M-1', 'br': 9.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Object 435', 'br': 9.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'BMP-3', 'br': 9.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': '2S25', 'br': 9.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Shturm-S', 'br': 8.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'ZSU-23-4M4', 'br': 9.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-72A', 'br': 9.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-64A (1971)', 'br': 9.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-64B', 'br': 9.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'BMD-4M2', 'br': 9.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Object 775', 'br': 9.3, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},

    # Rank VI Premium
    {'name': 'Object 140', 'br': 8.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'IS-7', 'br': 8.3, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-55AM-1', 'br': 9.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'Object 279', 'br': 9.0, 'type': 'heavy_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'BMD-4', 'br': 9.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'BMD-4M', 'br': 9.7, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},

    # Rank VII
    {'name': 'T-72B', 'br': 10.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-72B (1989)', 'br': 10.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-80B', 'br': 10.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': '2S25M', 'br': 10.0, 'type': 'light_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Khrizantema-S', 'br': 9.7, 'type': 'tank_destroyer', 'nation': 'ussr', 'premium': False},
    {'name': 'Osa-AKM', 'br': 10.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'Т-90А', 'br': 11.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-80U', 'br': 11.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Strela-10M2', 'br': 10.3, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-72B3', 'br': 11.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': '2S6', 'br': 10.7, 'type': 'spaa', 'nation': 'ussr', 'premium': False},

    # Rank VII Premium
    {'name': 'BMP-2M', 'br': 10.3, 'type': 'light_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'Object 292', 'br': 10.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': '2S38', 'br': 10.3, 'type': 'spaa', 'nation': 'ussr', 'premium': True},
    {'name': 'T-72M2 Moderna', 'br': 10.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-72AV (TURMS-T)', 'br': 10.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': '␙T-80U', 'br': 11.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-80UD', 'br': 10.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-80UM2', 'br': 11.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'Т-80U-Е1', 'br': 12.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': 'T-80UK', 'br': 11.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},
    {'name': '◍Т-80U-Е1', 'br': 12.0, 'type': 'medium_tank', 'nation': 'ussr', 'premium': True},

    # Rank VIII
    {'name': 'T-72B3A', 'br': 12.3, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'T-80BVM', 'br': 12.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': 'Pantsir-S1', 'br': 12.0, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': 'T-90M', 'br': 12.7, 'type': 'medium_tank', 'nation': 'ussr', 'premium': False},
    {'name': '9K317M "BUK-M3" (TADS)', 'br': 12.7, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
    {'name': '9K317M "BUK-M3" (TELAR)', 'br': 12.7, 'type': 'spaa', 'nation': 'ussr', 'premium': False},
]

# Great Britain Vehicles
britain_vehicles = [
    {'name': 'Cromwell I', 'br': 3.7, 'type': 'light_tank', 'nation': 'britain', 'premium': False}
]

# Japan Vehicles
japan_vehicles = [
    {'name': 'Type 75 SPH', 'br': 6.7, 'type': 'tank_destroyer', 'nation': 'japan', 'premium': False}
]

# China Vehicles
china_vehicles = [
    {'name': '🇨🇳M8 LAC', 'br': 1.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳T-26', 'br': 1.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳Sd.Kfz.222', 'br': 1.3, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M8 HMC', 'br': 1.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳Chi-Ha', 'br': 1.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳SU-76M', 'br': 2.0, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M3A3 Stuart', 'br': 2.7, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M5A1', 'br': 2.7, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳Chi-Ha Kai', 'br': 2.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'CCKW 353 (M45)', 'br': 2.3, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'LVT(A)(4) (ZiS-2)', 'br': 2.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M24', 'br': 3.7, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M4A4', 'br': 3.7, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M10 GMC', 'br': 3.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'Object 211', 'br': 5.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳PT-76', 'br': 5.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳T-34 (1943)', 'br': 4.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M4A1 (75) W', 'br': 4.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M42', 'br': 4.0, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M55', 'br': 4.0, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳Т-34-85 (S-53)', 'br': 5.7, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'T-34-85 Gai', 'br': 5.7, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'Phòng không T-34', 'br': 5.0, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳ISU-152', 'br': 4.7, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M36 GMC', 'br': 5.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳ISU-122', 'br': 5.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M18 GMC', 'br': 6.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳IS-2', 'br': 6.3, 'type': 'heavy_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳IS-2 (1944)', 'br': 6.7, 'type': 'heavy_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZSD63/PG87', 'br': 5.7, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳SU-100', 'br': 6.0, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'Type 63', 'br': 6.3, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'Type 62', 'br': 6.7, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZSL92', 'br': 6.3, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'PLZ83', 'br': 6.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'ZTS63', 'br': 7.7, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZBD86', 'br': 8.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M48A1', 'br': 7.7, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'WZ305', 'br': 8.0, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'PLZ05', 'br': 7.7, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'Type 59', 'br': 8.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'Type 69', 'br': 8.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M113A1 (TOW)', 'br': 8.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'M41D', 'br': 8.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ59D1', 'br': 8.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'PGZ09', 'br': 9.0, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'CM25', 'br': 8.7, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'PTZ89', 'br': 9.0, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': '🇨🇳M60A3 TTS', 'br': 9.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ88B', 'br': 9.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ88A', 'br': 9.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'PTL02', 'br': 9.0, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'AFT09', 'br': 9.0, 'type': 'tank_destroyer', 'nation': 'china', 'premium': False},
    {'name': 'CM11', 'br': 9.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ96', 'br': 9.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'MBT-2000', 'br': 11.7, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ96A', 'br': 10.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'PGZ04A', 'br': 9.3, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'ZLT11', 'br': 9.7, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'VT4', 'br': 12.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ99-II', 'br': 11.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ99-III', 'br': 11.0, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'Antelope', 'br': 10.3, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'ZBD04A', 'br': 10.0, 'type': 'light_tank', 'nation': 'china', 'premium': False},
    {'name': 'WZ1001(E) LCT', 'br': 12.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'ZTZ99A', 'br': 12.3, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'Tor-M1', 'br': 11.3, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'HQ17', 'br': 11.7, 'type': 'spaa', 'nation': 'china', 'premium': False},
    {'name': 'VT4A1', 'br': 12.7, 'type': 'medium_tank', 'nation': 'china', 'premium': False},
    {'name': 'CS/SA5', 'br': 12.0, 'type': 'spaa', 'nation': 'china', 'premium': False},
    #premium vehicles
    {'name': 'T-26 No.531', 'br': 1.0, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': '🇨🇳M3A3 (1st PTG)', 'br': 2.7, 'type': 'light_tank', 'nation': 'china', 'premium': True},
    {'name': '🇨🇳M4A4 (1st PTG)', 'br': 3.7, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': '🇨🇳M41A3', 'br': 5.7, 'type': 'light_tank', 'nation': 'china', 'premium': True},
    {'name': 'M64', 'br': 6.0, 'type': 'light_tank', 'nation': 'china', 'premium': True},
    {'name': 'WZ141-1', 'br': 6.7, 'type': 'light_tank', 'nation': 'china', 'premium': True},
    {'name': 'T-34-85 No.215', 'br': 5.7, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'IS-2 No.402', 'br': 6.3, 'type': 'heavy_tank', 'nation': 'china', 'premium': True},
    {'name': 'ZTZ59A', 'br': 8.0, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'PLZ83-130', 'br': 7.3, 'type': 'tank_destroyer', 'nation': 'china', 'premium': True},
    {'name': 'Type 69-IIa', 'br': 8.3, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'Object 122MT "MC"', 'br': 8.7, 'type': 'medium_tank', 'nation': 'china', 'premium': True}, 
    {'name': 'Т-62 №545', 'br': 8.7, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'WMA301', 'br': 9.0, 'type': 'light_tank', 'nation': 'china', 'premium': True},
    {'name': 'T-69 II G', 'br': 9.0, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'ZTZ96A (P)', 'br': 10.3, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'T-80UD/DU1', 'br': 10.7, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'QN506', 'br': 10.0, 'type': 'light_tank', 'nation': 'china', 'premium': True},
    {'name': 'Al-Khalid-I', 'br': 11.7, 'type': 'medium_tank', 'nation': 'china', 'premium': True},
    {'name': 'VT5', 'br': 11.7, 'type': 'light_tank', 'nation': 'china', 'premium': True},
]

# Italy Vehicles
italy_vehicles = [
    {'name': 'M16/43', 'br': 1.7, 'type': 'medium_tank', 'nation': 'italy', 'premium': False}
]

# France Vehicles
france_vehicles = [
    {'name': 'AMX-13', 'br': 6.7, 'type': 'light_tank', 'nation': 'france', 'premium': False}
]

# Sweden Vehicles
sweden_vehicles = [
    {'name': 'Strv 122', 'br': 11.7, 'type': 'medium_tank', 'nation': 'sweden', 'premium': False}
]

# Israel Vehicles
israel_vehicles = [
    {'name': 'Merkava Mk.1', 'br': 9.0, 'type': 'medium_tank', 'nation': 'israel', 'premium': False}
]

