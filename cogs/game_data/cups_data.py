class CM_Cup:
    def __init__(self, name, course, distance, track_type, condition, season, weather):
        self.name = name
        self.course = course
        self.distance = distance
        self.track_type = track_type
        self.condition = condition
        self.season = season
        self.weather = weather
    def get_formatted_info(self):
        """Returns the cup information in the formatted string"""
        return f"{self.course}\n{self.distance}\n{self.track_type}\n{self.condition} — {self.season} — {self.weather}"

# Champions Meet database
CM_DATABASE = {
    "Taurus": CM_Cup(
        name="Taurus Cup",
        course="Tokyo — Turf",
        distance="2400 m — Medium",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Firm",
        season="Spring",
        weather="Sunny"
    ),
    "Gemini": CM_Cup(
        name="Gemini Cup",
        course="Kyoto — Turf",
        distance="3200 m — Long",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Spring",
        weather="Sunny"
    ),
    "Cancer": CM_Cup(
        name="Cancer Cup",
        course="Tokyo — Turf",
        distance="1600 m — Mile",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Good",
        season="Summer",
        weather="Sunny"
    ),
    "Leo": CM_Cup(
        name="Leo Cup",
        course="Hanshin — Turf",
        distance="2200 m — Medium",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Summer",
        weather="Sunny"
    ),
    "Virgo": CM_Cup(
        name="Virgo Cup",
        course="Hanshin — Turf",
        distance="1600 m — Mile",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Autumn",
        weather="Sunny"
    ),
    "Libra": CM_Cup(
        name="Libra Cup",
        course="Kyoto — Turf",
        distance="3000 m — Long",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Autumn",
        weather="Sunny"
    ),
    "Scorpio": CM_Cup(
        name="Scorpio Cup",
        course="Tokyo — Turf",
        distance="2000 m — Medium",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Soft",
        season="Autumn",
        weather="Rain"
    ),
    "Sagittarius": CM_Cup(
        name="Sagittarius Cup",
        course="Nakayama — Turf",
        distance="2500 m — Long",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Winter",
        weather="Sunny"
    ),
    "Capricorn": CM_Cup(
        name="Capricorn Cup",
        course="Chukyo — Turf",
        distance="1200 m — Short",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Soft",
        season="Winter",
        weather="Snow"
    ),
    "Aquarius": CM_Cup(
        name="Aquarius Cup",
        course="Tokyo — Dirt",
        distance="1600 m — Mile",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Firm",
        season="Winter",
        weather="Sunny"
    ),
    "Pisces": CM_Cup(
        name="Pisces Cup",
        course="Hanshin — Turf",
        distance="3200 m — Long",
        track_type="Clockwise (RIGHT-handed)",
        condition="Heavy",
        season="Spring",
        weather="Rain"
    ),
    "Aries": CM_Cup(
        name="Aries Cup",
        course="Nakayama — Turf",
        distance="2000 m — Medium",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Spring",
        weather="Sunny"
    ),
    "MILE": CM_Cup(
        name="MILE",
        course="Tokyo — Turf",
        distance="1600 m — Mile",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Heavy",
        season="Spring",
        weather="Rain"
    ),
    "DIRT": CM_Cup(
        name="DIRT",
        course="Funabashi — Dirt",
        distance="1600 m — Mile",
        track_type="Counterclockwise (LEFT-handed)",
        condition="Firm",
        season="Summer",
        weather="Sunny"
    ),
    "CLASSIC": CM_Cup(
        name="CLASSIC",
        course="Longchamp — Turf",
        distance="2400 m — Medium",
        track_type="Clockwise (RIGHT-handed)",
        condition="Soft",
        season="Autumn",
        weather="Rain"
    ),
    "LONG": CM_Cup(
        name="LONG",
        course="Nakayama — Turf",
        distance="2500 m — Long",
        track_type="Clockwise (RIGHT-handed)",
        condition="Soft",
        season="Winter",
        weather="Snow"
    ),
    "SPRINT": CM_Cup(
        name="SPRINT",
        course="Hanshin — Turf",
        distance="1400 m — Short",
        track_type="Clockwise (RIGHT-handed)",
        condition="Good",
        season="Winter",
        weather="Cloudy"
    ),
    "MILE": CM_Cup(
        name="MILE",
        course="Hanshin — Turf",
        distance="1600 m — Mile",
        track_type="Clockwise (RIGHT-handed)",
        condition="Firm",
        season="Spring",
        weather="Sunny"
    )
}

# Set the next upcoming cup
NEXT_CUP = "Virgo"