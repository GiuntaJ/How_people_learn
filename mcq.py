import ipywidgets as widgets
from IPython.display import display, Image, clear_output

def create_multipleChoice_widget(options, correct_answer, explanation, explanation_gif):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            answer = widgets.Button(
                    description="Right answer. Good job!",
                    disabled=True,
                    button_style='success',
                    layout=widgets.Layout(height='auto', width='auto'))
        else:
            answer = widgets.Button(
                    description="Wrong answer.",
                    disabled=True,
                    button_style='danger',
                    layout=widgets.Layout(height='auto', width='auto'))
        with feedback_out:
            clear_output()
            display_explanation(answer, explanation, explanation_gif)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([alternativ, check, feedback_out])

def display_explanation(answer, explanation, explanation_gif):
    expl = widgets.HTML(
        value=explanation,
        placeholder='',
        description= '')
    file = open(explanation_gif, "rb")
    image = file.read()
    gif = widgets.Image(
        value=image,
        format='gif',
        height=400)
    output = widgets.AppLayout(header=answer,
          left_sidebar=expl,
          center=None,
          right_sidebar=gif,
          footer=None)
    display(output)

def firstMCQQuestion():
    q4_options = ["A", "B", "C", "D"]
    q4_answer = "B"
    q4_explanation = "<b>Ball in circular motion</b>: the string applies the <b>centripetal force</b> " +\
                "to the ball, causing it to move in a <b>circular path.</b> " + \
                "The string pulls the ball <b>toward the center of the circle</b> "+ \
                "while the ball pulls <b>outward on the string</b> and hence "+ \
                "<b>on your hand</b> in accordance with <b>Newton's third law " + \
                "of action and reaction.</b> When the <b>centripetal force is discontinued,</b> "+ \
                "in this case when the string breaks, <b>the object moves in the direction " + \
                "of the velocity at that instant</b>. This direction is <b>tangential</b> " + \
                "to the circle at that point."
    q4_solution_gif = "Gifs/solution.gif"
    q4 = create_multipleChoice_widget(q4_options, q4_answer, q4_explanation, q4_solution_gif)
    display(q4)