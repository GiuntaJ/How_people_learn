import ipywidgets as widgets
from IPython.display import display, Image, clear_output


question6_explanation = """To be able to understand what happened we need to decompose the movement into 3 phases:
<ol>
	<li> <u>Before the shock</u>: the puck is sliding on the horizontal surface at a constant velocity  <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msub>
    <mrow>
      <mover>
        <mi>V</mi>
        <mo stretchy="false">&#x2192;</mo>
      </mover>
    </mrow>
    <mi>o</mi>
  </msub>
</math>  with no acceleration </li>
	<li> <u>During the shock</u>: The energy of the kick is entirely transferred to the puck in a form of a velocity <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mrow>
    <mover>
      <mi>V</mi>
      <mo stretchy="false">&#x2192;</mo>
    </mover>
  </mrow>
</math>, it receives an instantaneous vertical upwards acceleration </li>
	<li> <u>After the shock</u>: The puck stops accelerating from the shock in the upward direction and since the velocity of the push is only vertical and upwards (thus perpendicular to the initial velocity <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msub>
    <mrow>
      <mover>
        <mi>V</mi>
        <mo stretchy="false">&#x2192;</mo>
      </mover>
    </mrow>
    <mi>o</mi>
  </msub>
</math>  its new velocity is thus the sum of <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msub>
    <mrow>
      <mover>
        <mi>V</mi>
        <mo stretchy="false">&#x2192;</mo>
      </mover>
    </mrow>
    <mi>o</mi>
  </msub>
</math>  and <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mrow>
    <mover>
      <mi>V</mi>
      <mo stretchy="false">&#x2192;</mo>
    </mover>
  </mrow>
</math></li>
</ol>
<b>Why it’s not D</b> : This case assumes that the puck went into a circular motion which is not true because the latter needs a continuous acceleration towards a center point that continuously pulls the puck. 
Since the puck is not attached to anything this movement is not possible  """

question7_explanation="""The speeds <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msub>
    <mi>V</mi>
    <mi>o</mi>
  </msub>
</math>
and <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>V</mi>
</math> are both the norms of the corresponding velocity vectors <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msub>
    <mrow>
      <mover>
        <mi>V</mi>
        <mo stretchy="false">&#x2192;</mo>
      </mover>
    </mrow>
    <mi>o</mi>
  </msub>
</math>
and <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mrow>
    <mover>
      <mi>V</mi>
      <mo stretchy="false">&#x2192;</mo>
    </mover>
  </mrow>
</math>

<br/>

The new speed is thus the norm <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mo stretchy="false">|</mo>
  <mrow>
    <mo stretchy="false">|</mo>
  </mrow>
  <msub>
    <mrow>
      <mover>
        <mi>V</mi>
        <mo stretchy="false">&#x2192;</mo>
      </mover>
    </mrow>
    <mi>o</mi>
  </msub>
  <mo>+</mo>
  <mrow>
    <mover>
      <mi>V</mi>
      <mo stretchy="false">&#x2192;</mo>
    </mover>
  </mrow>
  <mrow>
    <mo stretchy="false">|</mo>
  </mrow>
  <mo stretchy="false">|</mo>
</math>
and because of the fact that both of the velocities are either entirely vertical or entirely horizontal it's computed using this formula : <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msqrt>
    <msubsup>
      <mi>V</mi>
      <mi>o</mi>
      <mn>2</mn>
    </msubsup>
    <mo>+</mo>
    <msup>
      <mi>V</mi>
      <mn>2</mn>
    </msup>
  </msqrt>
</math>
<br/>You can then easily verify that only the last property holds """



def create_multipleChoice_widget(options, correct_answer, explanation, explanation_gif):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        layout={'width': 'max-content'},
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

def MCQQuestion1():
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
    q4_solution_gif = "Gifs/GifProblem4.gif"
    q4 = create_multipleChoice_widget(q4_options, q4_answer, q4_explanation, q4_solution_gif)
    display(q4)
    
def MCQQuestion2():
    q18_options = ["A", "B", "C", "D", "E"]
    q18_answer = "B"
    q18_explanation = "If the elevator is moving with <b>constant velocity</b>, the <b>net force must be zero (no acceleration)</b>. In order for the net force on the elevator to be zero, the upward and downward <b>forces must cancel</b> exactly."
    q18_solution_gif = "Gifs/GifProblem18.gif"
    q18 = create_multipleChoice_widget(q18_options, q18_answer, q18_explanation, q18_solution_gif)
    display(q18)

def MCQQuestion3():
    q22_options = ["1 only", "1 and 2", "1, 2 and 3", "1 and 3", "2 and 3"]
    q22_answer = "1 and 3"
    q22_explanation = "The <i>hit</i> force is applied only for a short period during the <i>hit</i> and it gives the ball an <b>initial velocity</b>. Once the ball is <b>in flight</b>, the only forces acting on it are the <b>gravity</b>, which <b>accelerates</b> the ball <b>downwards</b>, and <b>air resistance</b>, which <b>decelerates</b> the ball."
    q22_solution_gif = "Gifs/p22.gif"
    q22 = create_multipleChoice_widget(q22_options, q22_answer, q22_explanation, q22_solution_gif)
    display(q22)

def MCQQuestion4():
    q23_options = ["A", "B", "C", "D"]
    q23_answer = "D"
    q23_explanation = "As soon as the bowling ball leaves the plane, the <b>horizontal velocity is the same as the one of the plane</b> and the <b>vertical velocity is zero</b>. From that point onwards, the only forces acting on it are the <b>gravity</b> and the <b>air resistance</b>. The trajectory is therefore a <b>parabola</b>. The ball falling out of the plane is equivalent to throwing the ball with an initial horizontal velocity."
    q23_solution_gif = "Gifs/p23.gif"
    q23 = create_multipleChoice_widget(q23_options, q23_answer, q23_explanation, q23_solution_gif)
    display(q23)

def MCQQuestion5():
    q28_options = ["If the force applied to the box is doubled, the constant speed of the box will increase to 8.0 m/s.", \
        "The amount of force applied to move the box at a constant speed must be more than its weight.", \
        "The amount of force applied to move the box at a constant speed must be equal to the amount of the frictional forces that resist its motion.", \
        "The amount of force applied to move the box at a constant speed must be more than the amount of the frictional forces that resist its motion.", \
        'There is a force being applied to the box to make it move but the external forces such as friction are not "real" forces, they just resist motion.']
    q28_answer = "The amount of force applied to move the box at a constant speed must be equal to the amount of the frictional forces that resist its motion."
    q28_explanation = "The box going at <b>constant speed</b>, means that the <b>acceleration is zero</b> and from the <b>second law of Newton</b>, it follows that the <b>sum of forces is also zero</b>."
    q28_solution_gif = "Gifs/p28.png"
    q28 = create_multipleChoice_widget(q28_options, q28_answer, q28_explanation, q28_solution_gif)
    display(q28)

def MCQQuestion6():
    q6_options = ["A", "B", "C", "D", "E"]
    q6_answer = "B"
    q6_explanation = question6_explanation
    
    q6_solution_gif = "Gifs/GifProblem6.gif"
    q6 = create_multipleChoice_widget(q6_options, q6_answer, q6_explanation, q6_solution_gif)
    display(q6)

def MCQQuestion7():
    q7_options = ['Equal to the speed “Vo” it had before it received the “kick”.', \
        'Equal to the speed “V” it acquires from the “kick”, and independent of the speed “Vo”.', \
        'Equal to the arithmetic sum of speeds “Vo” and “V”.', \
        'Smaller than either of speeds “Vo” or “V”.', \
        'Greater than either of speeds “Vo” or “V”, but smaller than the arithmetic sum of these two speeds.']
    q7_answer = 'Greater than either of speeds “Vo” or “V”, but smaller than the arithmetic sum of these two speeds.'
    q7_explanation = question7_explanation
    q7_solution_gif = "Gifs/p7.png"
    q7 = create_multipleChoice_widget(q7_options, q7_answer, q7_explanation, q7_solution_gif)
    display(q7)

def MCQQuestion8():
    q24_options = ["A", "B", "C", "D", "E"]
    q24_answer = "E"
    q24_explanation = """To be able to understand what happened we need to decompose the movement into 3 phases :
    <ol>
<li><u>From a to b</u>: The rocket is moving at constant speed with no force acting on it</li>
<li><u>At b</u>: The engine of the rocket started providing an upward vertical acceleration perpendicular to the original speed </li>
<li><u>Fom b to c</u>: The rocket kept accelerating upwards and in the same time kept sliding constantly and horizontally in the right direction which explains </li></ol>

<b>Why it’s not D </b> : This case assumes that the rocket started accelerating a few moments after turning on its engine which wrong because the thrust has an immediate effect on the rocket"""
    q24_solution_gif = "Gifs/p8.gif"
    q24 = create_multipleChoice_widget(q24_options, q24_answer, q24_explanation, q24_solution_gif)
    display(q24)

def MCQQuestion9():
    q26_options = ["A", "B", "C", "D", "E"]
    q26_answer = "B"
    q26_explanation = """
    To be able to understand what happened we need to see what happened at point C :
    <li>
    The engine got shut down, the force of the thrust is removed and thus the rocket stopped accelerating upwards, but keeps the upward velocity gained so far. 
    Since the rocket didn't accelerate along the horizontal axis, it keeps its initial horizontal velocity.
    At the end the rocket has two constant velocities, one vertical and one horizontal. if we sum up those two, we get a velocity going towards the upright corner which explains the trajectory B 
    </li>

    """
    q26_solution_gif = "Gifs/p9.gif"
    q26 = create_multipleChoice_widget(q26_options, q26_answer, q26_explanation, q26_solution_gif)
    display(q26)
