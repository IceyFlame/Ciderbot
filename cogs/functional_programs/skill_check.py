import discord
from discord import app_commands
from discord.ext import commands
from cogs.game_data.skill_data import speed_skills, acceleration_skills, stamina_skills, debuff_skills, other_skills
from cogs.game_data.tierlist_data_CM import cm_explanations
from cogs.game_data.tierlist_data_TT import tt_explanations

# Combine all skills into one dictionary for searching
all_skills = {}
all_skills.update(speed_skills)
all_skills.update(acceleration_skills)
all_skills.update(stamina_skills)
all_skills.update(debuff_skills)
all_skills.update(other_skills)

# Category mapping for display
skill_categories = {
    "Speed": speed_skills,
    "Acceleration": acceleration_skills,
    "Recovery": stamina_skills,
    "Debuff": debuff_skills,
    "Other": other_skills
}

class SkillCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_recommendation(self, rating):
        rating_map = {
            "⍟": "🔥 **MUST HAVE** (Absolutely necessary)",
            "◎": "✅ **Yes** (Top priority)",
            "◯": "✅ **Yes** (Good skill)", 
            "▲": "⚠️ **Maybe** (Situationaly good)",
            "△": "⚠️ **Maybe** (Only buy with leftover SP)",
            "✕": "❌ **No** (Not recommended)"
        }
        return rating_map.get(rating, "❓ **Unknown**")

    def find_skill_category(self, skill_name):
        """Find which category a skill belongs to"""
        for category, skills in skill_categories.items():
            if skill_name in skills:
                return category
        return "Unknown"

    @app_commands.command(name="skillcheck", description="Check if a skill is good for Team Trials or Champions Meet")
    @app_commands.describe(
        skill_name="The name of the skill to check", 
        usage="TT for Team Trials or CM for Champions Meet"
    )
    async def skillcheck(self, interaction: discord.Interaction, skill_name: str, usage: str):
        usage = usage.upper()
        skill_name = skill_name.strip()

        # Find the skill (case-insensitive search)
        found_skill = None
        for skill_key in all_skills.keys():
            if skill_name.lower() in skill_key.lower():
                found_skill = skill_key
                break

        if not found_skill:
            await interaction.response.send_message(
                f"❌ Skill '{skill_name}' not found in the database.\n"
                f"*Try using a partial name or check your spelling.*"
            )
            return

        # Get the rating and category
        tt_rating, cm_rating = all_skills[found_skill]
        category = self.find_skill_category(found_skill)

        if usage == "TT":
            rating = tt_rating
            mode_name = "Team Trials"
        elif usage == "CM":
            rating = cm_rating
            mode_name = "Champions Meet"
        else:
            await interaction.response.send_message(
                "❌ Please specify 'TT' for Team Trials or 'CM' for Champions Meet."
            )
            return

        recommendation = self.get_recommendation(rating)

        # Create embed
        embed = discord.Embed(
            title=f"Skill Check: {found_skill}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Category", value=category, inline=True)
        embed.add_field(name="Mode", value=mode_name, inline=True)
        embed.add_field(name="Rating", value=f"`{rating}`", inline=True)
        embed.add_field(name="Recommendation", value=recommendation, inline=False)

        # Add rating guide as a field inside the embed
        embed.add_field(
            name="Rating Guide",
            value="⍟ = Must have\n◎ = Top tier\n◯ = Good\n▲/△ = Situational\n✕ = Bad",
            inline=False
        )

        embed.set_footer(text="Skillcheck bot by Ciderneko")

        await interaction.response.send_message(embed=embed)

    @skillcheck.autocomplete('skill_name')
    async def skill_autocomplete(self, interaction: discord.Interaction, current: str):
        current = current.lower()
        matches = [
            app_commands.Choice(name=skill, value=skill)
            for skill in all_skills.keys()
            if current in skill.lower()
        ][:25]
        return matches
    
    @app_commands.command(name="tierlist", description="Get detailed explanation for why a skill is rated the way it is")
    @app_commands.describe(
        skill_name="The name of the skill to check",
        usage="TT for Team Trials or CM for Champions Meet"
    )
    async def tierlist(self, interaction: discord.Interaction, skill_name: str, usage: str):
        usage = usage.upper()
        skill_name = skill_name.strip()

        # Find the skill (case-insensitive search)
        found_skill = None
        for skill_key in all_skills.keys():
            if skill_name.lower() in skill_key.lower():
                found_skill = skill_key
                break

        if not found_skill:
            await interaction.response.send_message(
                f"❌ Skill '{skill_name}' not found in the database.\n"
                f"*Try using a partial name or check your spelling.*"
            )
            return

        # Get the rating and explanation
        tt_rating, cm_rating = all_skills[found_skill]
        category = self.find_skill_category(found_skill)
        
        if usage == "TT":
            rating = tt_rating
            mode_name = "Team Trials"
            explanation = self.get_tier_explanation(found_skill, "TT")
        elif usage == "CM":
            rating = cm_rating
            mode_name = "Champions Meet"
            explanation = self.get_tier_explanation(found_skill, "CM")
        else:
            await interaction.response.send_message(
                "❌ Please specify 'TT' for Team Trials or 'CM' for Champions Meet."
            )
            return

        # Create embed
        embed = discord.Embed(
            title=f"Tierlist Analysis: {found_skill}",
            color=discord.Color.gold()
        )
        embed.add_field(name="Category", value=category, inline=True)
        embed.add_field(name="Mode", value=mode_name, inline=True)
        embed.add_field(name="Rating", value=f"`{rating}`", inline=True)
        embed.add_field(name="Why?", value=explanation, inline=False)

        # Add rating guide
        embed.add_field(
            name="Rating Guide",
            value="⍟ = Must have\n◎ = Top tier\n◯ = Good\n▲/△ = Situational\n✕ = Bad",
            inline=False
        )

        embed.set_footer(text="Tierlist analysis by Ciderneko")

        await interaction.response.send_message(embed=embed)

    def get_tier_explanation(self, skill_name, mode):
        """Get the explanation for why a skill is rated the way it is for specific mode"""
        try:
            if mode == "TT":
                return tt_explanations.get(skill_name, "No detailed explanation available for Team Trials.")
            elif mode == "CM":
                return cm_explanations.get(skill_name, "No detailed explanation available for Champions Meet.")
        except ImportError:
            return "Tierlist data not loaded yet."
    @tierlist.autocomplete('skill_name')
    async def tierlist_autocomplete(self, interaction: discord.Interaction, current: str):
        current = current.lower()
        matches = [
            app_commands.Choice(name=skill, value=skill)
            for skill in all_skills.keys()
            if current in skill.lower()
        ][:25]
        return matches

async def setup(bot):
    await bot.add_cog(SkillCheck(bot))