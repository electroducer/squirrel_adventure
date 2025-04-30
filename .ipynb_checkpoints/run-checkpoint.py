import streamlit as st

st.title("Your Adventure Game")

def start():
    name = st.text_input("What is your character's name?")
    st.write("Hello, ", name, "!")
    st.write(f"One day, {name} was walking through the forest. She saw a squirrel.")
    answer = st.text_input("""Did she:
                      1. Scream and run away
                      2. Try to pet the squirrel
                      3. Ignore it
                    """)
    if answer == "1":
        st.write("She ran away and screamed. AHHHHHHHHH!!!!")
        st.write("After that she was so scared that she couldn't continue the adventure.")
        st.write("========!!!THE END!!!========")
    elif answer == "2" or answer == "3":
        if answer == "2":
            st.write(f'{name} tried to pet the squirrel. But then the squirrel bit her.')
        else:
            st.write(f'{name} ignored the squirrel but the squirrel wanted attention so he bit her.')
        bite(name)

def bite(name):
    st.write("OUCH!!!!")
    answer = st.text_input("""What did she do next?
                      1. Run back home
                      2. Chase after the squirrel
                      3. Try to bite the squirrel back
                      4. Keep ignoring the squirrel
                   """)
    if answer == "1":
        st.write(f'{name} ran back home and never came back to that forest.')
        st.write("========!!!THE END!!!========") 
    elif answer == "2":
        fork(name)
    elif answer == "3":
        st.write(f'{name} tried to bite the squirrel back and succeeded.')
        st.write(f'But there is squirrel fur in her mouth and {name} accidentally swallows it.')
        st.write(f'{name} gets a rash and goes back home.')
        st.write("========!!!THE END!!!========")
    elif answer == "4":
        st.write(f'{name} keeps ignoring the squirrel and the squirrel keeps biting to get attention')
        st.write(f'But {name} keeps ignoring until she gets home with bite marks everywhere.')
        st.write("========!!!THE END!!!========")
def fork(name):
    st.write(f'{name} chased the squirrel who led her to a fork in the road.')
    answer = st.text_input("""Which way did she go?
                      1.Right
                      2.Left
                      3.Go back the way she came
                    """)
    if answer == "3":
        st.write(f'{name} went back the way she came which led her to her home.')
        st.write(f' When {name} got in her house she made a cup of tea and got a piece pie.')
        st.write("========!!!THE END!!!========")
    elif answer == "1":
        right(name)
    elif answer == "2":
        left(name)
def right(name):
    st.write(f'{name} went right and found the squirrel so she started to chase it again which led her to a parliament of animals.')
    st.write(f'But the rule of the parliament is that no human is allowed in the place that the animals meet.')
    answer = st.text_input("""What did she do?
                      1.Admit that you disrespected the rule and that you get a punishment
                      2.Blame the squirrel for leading her here
                    """)
    if answer == "1":
        st.write(f'As soon as {name} admited all the animals of the parlament chased her back home.')
        st.write("========!!!THE END!!!========")
    elif answer == "2":
        st.write(f'Right when {name} started blaming the squirrel all the animals in the parlament got mad and attacked her.')
        st.write(f'So that night {name} did not sleep in her bed instead {name} slept in the hospital bed.')
        st.write("========!!!THE END!!!========")
def left(name):
    st.write(f'{name} went left and found the squirrel so she started to chase it again.')
    st.write("After chasing the squirrel for a long time it finally came to a stop in front of a witch's house and ran away.")
    answer = st.text_input("""What did she do?
                      1.Go in to the house
                      2.Go back home 
                    """)
    if answer == "1":
       st.write(f'{name} went in the house and accidentally hit a shelf and the shelf collapsed.') 
       st.write(f'At that instant a witch suddenly appeared with a angry face and cast a spell on {name} and then she became a frog.')
       st.write("========!!!THE END!!!========")
    elif answer == "2":
       st.write(f'{name} went back home and started to write her adventure into a book.')
       st.write("========!!!THE END!!!========")               


start()