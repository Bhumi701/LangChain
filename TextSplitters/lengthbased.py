from langchain_text_splitters import CharacterTextSplitter

text = """
Complications
Flying Carrousel
A flying carrousel is a complex watch mechanism that counters gravity’s effect on timekeeping. Unlike a tourbillon, it uses two gear trains—one for the escapement and one for carriage rotation. "Flying" refers to the lack of an upper bridge, giving it a floating look.
Flyback Chronograph
A Flyback Chronograph allows the user to reset and restart the chronograph function with a single press of a button, without needing to first stop it. This feature is particularly useful for timing consecutive events quickly and efficiently.
Secured movement
A secured movement is a watchmaking innovation designed to protect delicate mechanisms and ensure lasting precision. By preventing accidental damage when setting the watch, it enhances reliability over time. At Blancpain, secured movements are a hallmark of our craftsmanship.
Minute Repeater
The minute repeater is a watch mechanism that chimes the time on demand. By activating a pusher or slide, the watch strikes gongs to indicate the hours, quarters, and minutes, offering a precise acoustic reading of time. Blancpain uses cathedral gongs; their extended length optimizes sound diffusion and richness, creating a deeper and more harmonious tone.
"""
splitter = CharacterTextSplitter(
  chunk_size=100,
  chunk_overlap=0,
  separator=''
)

result = splitter.split_text(text)

print(result)