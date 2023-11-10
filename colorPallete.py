from IPython.display import Markdown, display
from responseGenerator import response_gen as colorGen

def display_colors(colors):
    #creates a markdown display of the colors as blocks
        #chr(9608) * 4 - makes block wider
    display(Markdown(" ".join(
        f"<span style='color: {color}'>{chr(9608) * 4}</span>"
    for color in colors)))

def main():
    #convert the colorGen string into a list of colors
    colors = colorGen()
    print(colors)
    display_colors(colors)

if __name__ == "__main__":
    main()