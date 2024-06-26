import streamlit.components.v1 as components
import streamlit as st

st.title("Yet another website as a gift?")
st.subheader("It's starting to bother me as well ...")

with st.expander("Let's spice things up a bit then"):

    q0 = st.radio("Are you ready?", ['', "No :(", "Yes!"], index=0)
    if q0 == 'No :(':
        st.error("Seriously? Gift cancelled then, you can close this page >:(")
    elif q0 == 'Yes!':
        st.markdown("""That's the spirit!
        As I anticipated to you, this time I thought about an **actual present**""")
        q1 = st.radio("What do you think the present is?",
                      ['',
                       "Nothing really, I'm gifting you this interactive journey crafted while ignoring your messages",
                       "Something I came up with on my own",
                       "Something you will actually enjoy"]
                      )

        if q1 == "Nothing really, I'm gifting you this interactive journey crafted while ignoring your messages":
            st.error("I'm sorry love, I would have loved to have a chat with you last night but this whole experience is not gonna code itself")
        elif q1 == "Something I came up with on my own":
            st.error("lol, absolutely impossible")
        elif q1 == "Something you will actually enjoy":
            st.success("Well done! Here's a clue for you")
            st.image("data/yaladef2.jpeg")

            q2 = st.radio("Be honest. You've already figured everything out, haven't you?",
                          ['',
                           'Of course',
                           'Not yet...'])
            if q2 == "Of course":
                st.error("Joke's on me for tryharding so much then. "
                         "Now say what the gift is: if you get it right I'll down whatever I'm drinking, otherwise you'll do it")
            elif q2 == 'Not yet...':
                st.success("Then you need another hint!")
                st.image("data/sigiriya.jpeg")

                q3 = st.radio("To get one last image before facing the final challenge: mirror mirror on the wall, who's the best boyfriend of them all?",
                              ['', 'Whoever wouldn\'t deploy a deliberately self-glorifying Q&A website on the day of his girlfriend\'s birthday', 'You, Giovanni, my handsome labrador boyfriend'])
                if q3 == 'Whoever wouldn\'t deploy a deliberately self-glorifying Q&A website on the day of his girlfriend\'s birthday':
                    st.error("That's so rude of you to be honest")
                elif q3 == 'You, Giovanni, my handsome labrador boyfriend':
                    st.success("Aww what a cutie, here's your last bonus pic")
                    st.image("data/dambulla.jpeg")

                    q4 = st.radio('Ready for the final challenge?', ['', 'Yes'])
                    if q4 == 'Yes':
                        st.write('What country is this?')
                        st.image('data/srilanka.png', width=400)
                        answer = st.text_input('')
                        if answer:
                            if 'lanka' in answer.lower():
                                st.success("Let's go babe! Happy birthday, love you <3")
                                st.balloons()
                                st.image('data/confirmation.png')
                            else:
                                st.error("Nope nope nope. I'm so sure about your geography skills that I'm almost certain no one will ever read this message anyways")





