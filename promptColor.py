def get_and_render_colors(input):
    return f'''
    You are a color palette generating assistant that respons to text prompts for color pallettes.
    You should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description of a color palette into a list of colors: The Mediterranean Sea
    A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

    Q:Convert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]

    Desired Format: a JSON array of hexadecimal color codes
    Q: Convert the following verbal description of a color pallete into a list of colors: {input}
    A:
    '''
    